from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User
from . import serializers
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from config.utils import APIResponse


from .schemas import (
    register_schema,
    change_password_schema,
    log_in_schema,
    log_out_schema,
    personal_profile_schema_get,
    personal_profile_schema_put,
    token_refresh_schema,
    public_user_schema,
)


class Register(APIView):
    @register_schema
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ValidationError("비밀번호가 필요합니다.")

        serializer = serializers.PrivateUserSerializer(data=request.data)
        if serializer.is_valid(
            raise_exception=True
        ):  # raise_exception 옵션을 True로 설정, raise_exception 옵션을 사용하면, 시리얼라이저의 유효성 검사가 실패할 때 ValidationError 예외가 자동으로 발생
            user = serializer.save()
            user.set_password(password)
            user.save()

            # JWT 토큰 생성
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)

            # 응답에 JWT 토큰 추가 및 쿠키에 저장
            res = APIResponse.success(
                data=serializer.data,
                access_token=access_token,
                refresh_token=refresh_token,
                message="회원가입에 성공하였습니다.",
                status=status.HTTP_201_CREATED,
            )
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    @change_password_schema
    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise ValidationError("이전 비밀번호와 새 비밀번호가 필요합니다.")
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return APIResponse.success(message="비밀번호가 변경되었습니다.")
        else:
            raise ValidationError("이전 비밀번호가 올바르지 않습니다.")


class LogIn(APIView):
    @log_in_schema
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ValidationError("사용자 이름과 비밀번호가 필요합니다.")

        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is not None:
            serializer = serializers.PrivateUserSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)

            res = APIResponse.success(
                data=serializer.data,
                access_token=access_token,
                refresh_token=refresh_token,
                message="로그인에 성공하였습니다.",
                status=status.HTTP_200_OK,
            )

            # 선택적으로, JWT 토큰을 쿠키에 저장할 수도 있습니다.
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)

            return res
        else:
            raise AuthenticationFailed("사용자 이름 또는 비밀번호가 올바르지 않습니다.")


class LogOut(APIView):
    permission_classes = [IsAuthenticated]

    @log_out_schema
    def post(self, request):
        # 쿠키에 저장된 토큰 삭제 => 로그아웃 처리
        response = APIResponse.success(message="로그아웃에 성공하였습니다.")
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response


class PublicUser(APIView):
    @public_user_schema
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound("사용자가 존재하지 않습니다.")
        serializer = serializers.TinyUserSerializer(user)
        return APIResponse.success(
            data=serializer.data,
            message="사용자 정보를 조회하였습니다.",
            status=status.HTTP_200_OK,
        )


class PersonalProfile(APIView):
    permission_classes = [IsAuthenticated]

    @personal_profile_schema_get
    def get(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user)
        return APIResponse.success(
            data=serializer.data,
            message="사용자 정보를 조회하였습니다.",
            status=status.HTTP_200_OK,
        )

    @personal_profile_schema_put
    def put(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            serializer = serializers.PrivateUserSerializer(user)
            return APIResponse.success(
                data=serializer.data,
                message="사용자 정보를 수정하였습니다.",
                status=status.HTTP_200_OK,
            )


class TokenRefreshAPIView(TokenRefreshView):
    @token_refresh_schema
    def post(self, request, *args, **kwargs):
        try:
            # Refresh Token을 사용하여 Access Token 갱신
            response = super().post(request, *args, **kwargs)
            return response
        except TokenError as e:
            raise InvalidToken(e.args[0])
