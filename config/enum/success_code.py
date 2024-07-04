from enum import Enum

class SuccessCode(Enum):
        # Success Codes
    SUCCESS_001 = ("SUCCESS-001", "생성 성공")
    SUCCESS_002 = ("SUCCESS-002", "조회 성공")
    SUCCESS_003 = ("SUCCESS-003", "수정 성공")
    SUCCESS_004 = ("SUCCESS-004", "삭제 성공")
    SUCCESS_005 = ("SUCCESS-005", "회원가입 성공")
    SUCCESS_006 = ("SUCCESS-006", "로그인 성공")
    SUCCESS_007 = ("SUCCESS-007", "JWT 재발급 성공")
    SUCCESS_008 = ("SUCCESS-008", "로그아웃 성공")

    def __init__(self, code, message):
        self.code = code
        self.message = message