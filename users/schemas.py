from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from . import serializers

tag = ["Users API"]

register_schema = swagger_auto_schema(
    tags=tag,
    operation_summary="유저 회원가입",
    operation_description="새로운 사용자를 등록하고 JWT 토큰을 반환합니다.",
    request_body=serializers.PrivateUserSerializer,
    responses={
        200: openapi.Response(
            description="Register successful",
            examples={
                "application/json": {
                    "user": "PrivateUserSerializer data",
                    "message": "Register successful",
                    "token": {
                        "access": "access_token",
                        "refresh": "refresh_token",
                    },
                }
            },
        ),
        400: "Bad Request",
    },
)

change_password_schema = swagger_auto_schema(
    tags=tag,
    operation_summary="사용자 비밀번호 변경",
    operation_description="인증된 사용자가 자신의 비밀번호를 변경할 수 있도록 허용합니다.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "old_password": openapi.Schema(
                type=openapi.TYPE_STRING, description="Old password"
            ),
            "new_password": openapi.Schema(
                type=openapi.TYPE_STRING, description="New password"
            ),
        },
    ),
    responses={200: "Password change success", 400: "Bad Request"},
)

log_in_schema = swagger_auto_schema(
    tags=tag,
    operation_summary="로그인",
    operation_description="사용자에 로그인하고 JWT 토큰을 반환합니다.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "username": openapi.Schema(
                type=openapi.TYPE_STRING, description="Username"
            ),
            "password": openapi.Schema(
                type=openapi.TYPE_STRING, description="Password"
            ),
        },
    ),
    responses={200: "Login successful", 401: "Unauthorized"},
)

log_out_schema = swagger_auto_schema(
    tags=tag,
    operation_summary="로그아웃",
    operation_description="쿠키에 저장된 JWT 토큰을 삭제하여 사용자를 로그아웃합니다.",
    responses={202: "Logout successful"},
)


public_user_schema = swagger_auto_schema(
    tags=tag,
    operation_summary="공개 사용자 정보 얻기",
    operation_description="사용자 이름으로 사용자의 공개 정보를 검색합니다.",
    manual_parameters=[
        openapi.Parameter(
            "username",
            openapi.IN_PATH,
            description="Username of the user",
            type=openapi.TYPE_STRING,
        )
    ],
    responses={200: serializers.TinyUserSerializer, 404: "User Not Found"},
)

personal_profile_schema_get = swagger_auto_schema(
    tags=tag,
    operation_summary="개인 프로필 정보 얻기",
    operation_description="인증된 사용자의 개인 프로필 정보를 검색합니다.",
    responses={200: serializers.PrivateUserSerializer},
)

personal_profile_schema_put = swagger_auto_schema(
    tags=tag,
    operation_summary="개인 프로필 정보 수정",
    operation_description="인증된 사용자의 개인 프로필 정보를 수정합니다.",
    request_body=serializers.PrivateUserSerializer,
    responses={200: serializers.PrivateUserSerializer},
)

token_refresh_schema = swagger_auto_schema(
    tags=tag,
    operation_summary="토큰 갱신",
    operation_description="Refresh Token을 사용하여 Access Token을 갱신합니다.",
    responses={
        200: openapi.Response(description="Token Refreshed Successfully"),
        401: "Invalid or Expired Token",
    },
)
