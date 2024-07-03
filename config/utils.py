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
                "요청하신 페이지를 찾을 수 없습니다.",
            )
        elif isinstance(exc, ValidationError):
            response = handle_exception(
                response, status.HTTP_400_BAD_REQUEST, "요청이 유효하지 않습니다."
            )
        elif isinstance(exc, MethodNotAllowed):
            response = handle_exception(
                response,
                status.HTTP_405_METHOD_NOT_ALLOWED,
                "허용되지 않은 메소드입니다.",
            )
        elif isinstance(exc, (NotAuthenticated, AuthenticationFailed)):
            response = handle_exception(
                response, status.HTTP_401_UNAUTHORIZED, "인증되지 않은 요청입니다."
            )
        elif isinstance(exc, PermissionDenied):
            response = handle_exception(
                response, status.HTTP_403_FORBIDDEN, "권한이 없는 요청입니다."
            )
        elif isinstance(exc, NotAcceptable):
            response = handle_exception(
                response,
                status.HTTP_406_NOT_ACCEPTABLE,
                "요청하신 형식을 지원하지 않습니다.",
            )
        elif isinstance(exc, UnsupportedMediaType):
            response = handle_exception(
                response,
                status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                "지원하지 않는 미디어 타입입니다.",
            )
        elif isinstance(exc, Throttled):
            response = handle_exception(
                response,
                status.HTTP_429_TOO_MANY_REQUESTS,
                "요청 횟수가 제한을 초과하였습니다.",
            )
        elif isinstance(exc, APIException):
            response = handle_exception(
                response, response.status_code, "API 예외가 발생하였습니다."
            )
        else:
            response = handle_generic_error()

    else:
        response = handle_generic_error()
    return response


def handle_exception(response, status_code, message):
    response.data = {
        "success": False,
        "message": message,
        "detail": response.data,
    }
    response.status_code = status_code
    return response


# 기타 서버 예외
def handle_generic_error():
    return Response(
        {
            "success": False,
            "message": "서버 내부 오류가 발생하였습니다. 서버 관리자에게 문의하세요.",
            "detail": "Internal server error",
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


################ API 응답을 일관된 형식으로 반환하는 유틸리티 클래스 ################


class APIResponse:
    @staticmethod
    def success(
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
            "success": True,
        }
        if message is not None:
            response_data["message"] = message

        if data is not None:
            response_data["data"] = data

        if access_token is not None and refresh_token is not None:
            response_data["token"] = {
                "access": access_token,
                "refresh": refresh_token,
            }

        return Response(response_data, status=status)

    @staticmethod
    def error(message, detail, status=None):
        """
        에러 응답을 반환하는 메소드
        """
        response_data = {
            "success": False,
            "message": message,
            "detail": detail,
        }
        return Response(response_data, status=status)
