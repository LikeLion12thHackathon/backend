from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import (
    APIException,
    AuthenticationFailed,
    NotAuthenticated,
    PermissionDenied,
    NotFound,
    MethodNotAllowed,
    NotAcceptable,
    UnsupportedMediaType,
    Throttled,
    ValidationError,
)

from config.enum.error_code import ErrorCode
from config.enum.success_code import SuccessCode

################# 클라이언트 에러 응답 ################


def custom_exception_handler(exc, context):
    # DRF의 기본 예외 처리기를 호출
    response = exception_handler(exc, context)

    if response is not None:
        # 예외 유형에 따라 처리
        if isinstance(exc, NotFound):
            response = handle_exception(
                response,
                status.HTTP_404_NOT_FOUND,
                ErrorCode.COMMON_004.code,
                ErrorCode.COMMON_004.message,
            )
        elif isinstance(exc, ValidationError):
            response = handle_exception(
                response, 
                status.HTTP_400_BAD_REQUEST, 
                ErrorCode.COMMON_001.code,
                ErrorCode.COMMON_001.message
            )
        elif isinstance(exc, MethodNotAllowed):
            response = handle_exception(
                response,
                status.HTTP_405_METHOD_NOT_ALLOWED,
                ErrorCode.COMMON_005.code,
                ErrorCode.COMMON_005.message,
            )
        elif isinstance(exc, (NotAuthenticated, AuthenticationFailed)):
            response = handle_exception(
                response, 
                status.HTTP_401_UNAUTHORIZED, 
                ErrorCode.COMMON_002.code,
                ErrorCode.COMMON_002.message
            )
        elif isinstance(exc, PermissionDenied):
            response = handle_exception(
                response, 
                status.HTTP_403_FORBIDDEN, 
                ErrorCode.COMMON_003.code,
                ErrorCode.COMMON_003.message
            )
        elif isinstance(exc, NotAcceptable):
            response = handle_exception(
                response,
                status.HTTP_406_NOT_ACCEPTABLE,
                ErrorCode.COMMON_006.code,
                ErrorCode.COMMON_006.message,
            )
        elif isinstance(exc, UnsupportedMediaType):
            response = handle_exception(
                response,
                status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                ErrorCode.COMMON_007.code,
                ErrorCode.COMMON_007.message,
            )
        elif isinstance(exc, Throttled):
            response = handle_exception(
                response,
                status.HTTP_429_TOO_MANY_REQUESTS,
                ErrorCode.COMMON_008.code,
                ErrorCode.COMMON_008.message,
            )
        elif isinstance(exc, APIException):
            response = handle_exception(
                response, 
                response.status_code, 
                ErrorCode.COMMON_004.code,
                ErrorCode.COMMON_004.message
            )
        else:
            response = handle_generic_error()
    else:
        response = handle_generic_error()
    return response


def handle_exception(response, status_code, code, message):
    response.data = {
        "successFlag": False,
        "code": code,
        "message": message,
        "length": 0,
        "data": None,
    }
    response.status_code = status_code
    return response


# 기타 서버 예외
def handle_generic_error():
    return Response(
        {
            "successFlag": False,
            "code": ErrorCode.COMMON_004.code,
            "message": ErrorCode.COMMON_004.message,
            "length": 0,
            "data": None,
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


################ API 응답을 일관된 형식으로 반환하는 유틸리티 클래스 ################


class APIResponse:
    @staticmethod
    def success(
        code=None,
        data=None,
        access_token=None,
        refresh_token=None,
        message=None,
        status=None,
    ):
        """
        성공적인 응답을 반환하는 메소드
        """
        response_data = {
            "successFlag": True,
            "code": code or SuccessCode.SUCCESS_002.code,
            "message": message or SuccessCode.SUCCESS_002.message,
            "length": 0 if data is None else 1,
            "data": data if data else {
                "grantType": "Bearer",
                "accessToken": access_token,
                "refreshToken": refresh_token,
            } if access_token or refresh_token else None,
        }
        return Response(response_data, status=status)

    @staticmethod
    def error(code, message, status=None):
        """
        에러 응답을 반환하는 메소드
        """
        response_data = {
            "successFlag": False,
            "code": code,
            "message": message,
            "length": 0,
            "data": None,
        }
        return Response(response_data, status=status)