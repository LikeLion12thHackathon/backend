from enum import Enum

class ErrorCode(Enum):
    # Common Errors
    COMMON_001 = ("COMMON-001", "입력 값이 잘못되었습니다.")
    COMMON_002 = ("COMMON-002", "허용되지 않은 메서드입니다.")
    COMMON_003 = ("COMMON-003", "엔티티를 찾을 수 없습니다.")
    COMMON_004 = ("COMMON-004", "서버 내부 오류.")
    COMMON_005 = ("COMMON-005", "유형 값이 잘못되었습니다.")
    COMMON_006 = ("COMMON-006", "접근이 거부되었습니다.")
    COMMON_007 = ("COMMON-007", "이미지 업로드에 실패했습니다.")
    COMMON_008 = ("COMMON-008", "요청이 중복되었습니다.")
    COMMON_009 = ("COMMON-009", "잘못된 요청입니다.")
    COMMON_010 = ("COMMON-010", "필수 필드가 없습니다.")
    COMMON_011 = ("COMMON-011", "데이터를 검색하지 못했습니다.")
    COMMON_012 = ("COMMON-012", "널 포인터 예외.")
    COMMON_013 = ("COMMON-013", "잘못된 인수 예외.")
    COMMON_014 = ("COMMON-014", "메서드 인수 유효성 검사 실패 예외.")
    COMMON_015 = ("COMMON-015", "핸들러를 찾을 수 없는 예외.")
    COMMON_016 = ("COMMON-016", "접근 거부 예외.")
    COMMON_017 = ("COMMON-017", "HTTP 메시지를 읽을 수 없는 예외.")

    # User Errors
    USER_001 = ("PUSER-001", "없는 유저 입니다.")
    USER_002 = ("PUSER-002", "비밀번호가 틀렸습니다.")

    # JWT Errors
    INVALID_TOKEN = ("INVALID_TOKEN", "유효하지 않은 JWT 토큰.")
    EXPIRED_TOKEN = ("EXPIRED_TOKEN", "만료된 JWT 토큰.")
    MALFORMED_JWT = ("MALFORMED_JWT", "형식이 잘못된 JWT 예외.")
    UNSUPPORTED_JWT = ("UNSUPPORTED_JWT", "지원되지 않는 JWT 토큰.")
    ILLEGAL_ARGUMENT_JWT = ("ILLEGAL_ARGUMENT_JWT", "JWT Claims 문자열 부적절.")
    REFRESH_INVALID = ("REFRESH_INVALID", "유효하지 않은 REFRESH 토큰.")


    def __init__(self, code, message):
        self.code = code
        self.message = message
