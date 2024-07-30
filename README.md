# **AI 기반 건강 정보 검색 및 분석 서비스**

## **서비스 이름:** 1분 닥터

**설명:** OpenAi의 API를 활용하여 사용자가 현재 처한 증상을 얘기하면 그에 대한 응급처치 및 건강 정보를 제공 해주는 서비스. 요약하여 사용자의 건강 관련 질문에 답변하는 서비스.

**주요 기능:**

- **건강 정보 검색:** 사용자가 입력한 건강 관련 질문에 대해 GPT API가 신뢰할 수 있는 최신 정보 제공.
- **증상 분석:** 사용자가 입력한 증상을 바탕으로 GPT API가 가능한 원인과 대응 방법 제안.
- **개인 맞춤형 정보:** 사용자의 건강 상태와 관심사에 맞춘 맞춤형 정보 제공.
  
## 개발자 소개

| 이름 | [이민재](https://github.com/mimijae) | [김효림](https://github.com/Kimhyorim123) | [정승환](https://github.com/Seunghwan31) |
| :-: | :-: | :-: | :-: |
| 프로필 | ![이민재](https://avatars.githubusercontent.com/u/95695319?v=4) | ![김효림](https://avatars.githubusercontent.com/u/164029475?v=4) | ![정승환](https://avatars.githubusercontent.com/u/163824668?v=4) |
| 기술 스택 | <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"> <img src="https://www.postgresql.org/media/img/about/press/elephant.png" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.nginx.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/nginx-1.svg" alt="nginx" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/docker.svg" alt="docker" width="40" height="40"/> </a> | <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"> <img src="https://www.postgresql.org/media/img/about/press/elephant.png" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.nginx.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/nginx-1.svg" alt="nginx" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/docker.svg" alt="docker" width="40" height="40"/> </a> | <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"> <img src="https://www.postgresql.org/media/img/about/press/elephant.png" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.nginx.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/nginx-1.svg" alt="nginx" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/docker.svg" alt="docker" width="40" height="40"/> </a> |
| 분류 | 백엔드 | 백엔드 | 백엔드 |
| 역할 | <ul><li>auth관련 JWT 인증인가 구현</li><li>openai api를 활용한 증상 질문에 답변하는 기능 question 구현</li><li>Nginx와 Docker를 사용하여 Django 애플리케이션 배포</li></ul> | <ul><li>auth관련 JWT 인증인가 구현</li><li>openai api를 활용한 증상 질문에 답변하는 기능 question 구현</li><li>Nginx와 Docker를 사용하여 Django 애플리케이션 배포</li></ul> | <ul><li>auth관련 JWT 인증인가 구현</li><li>openai api를 활용한 증상 질문에 답변하는 기능 question 구현</li><li>Nginx와 Docker를 사용하여 Django 애플리케이션 배포</li></ul> |


## 서비스 기능 API Endpoints

| 기능                       | 메소드 | PATH | 분류 |
|-------------------------| --- | --- | --- |
| 회원가입                    | POST | /api/v1/auth/signup | 인증 |
| 로그인                      | POST | /api/v1/auth/signin | 인증 |
| 로그아웃                    | POST | /api/v1/auth/signout | 회원 |
| 비밀번호 변경                | PUT | /api/v1/auth/change-password | 회원 |
| 회원 정보 수정               | PUT | /api/v1/auth/users | 회원 |
| 회원 정보 상세 조회            | GET | /api/v1/auth/users | 회원 |
| JWT 액세스 토큰 리프레시      | POST | /api/v1/auth/token/refresh | 인증 |
| 증상 질문에 대한 대답(정보)    | POST | /api/v1/questions/ | 증상질의 |
| 한 유저가 질문한 것에 대한 정보들 | GET | /api/v1/questions/ | 증상질의 |
| 한 유저가 질문한 것에 대한 상세 정보 | GET | /api/v1/questions/{questionId}/ | 증상질의 |
| 한쌍의 질문과 답변 삭제         | DELETE | /api/v1/questions/{questionId}/ | 증상질의 |


## API 응답 예시

### 성공 응답

```json
{
    "successFlag": true,
    "code": "SUCCESS-002",
    "message": "생성 성공",
    "length": 1,
    "data": {
        "id": 2,
        "question_text": "어제 축구를 하다가 상대방 발에 대 복숭아 뼈를 타박 당했어 너무 아파",
        "answer_text": "복숭아 뼈, 즉 외과적 관절의 부위에 타박상을 입으셨군요. 타박상은 일반적으로 외부의 충격으로 인해 발생하며, 통증, 부기, 멍 등이 동반될 수 있습니다. 다음은 가능한 진단과 치료 방법, 예방 조치입니다.\n\n### 진단\n1. **타박상**: 외부 충격으로 인한 조직 손상.\n2. **염좌**: 인대가 늘어나거나 찢어질 수 있습니다.\n3. **골절**: 심한 경우 뼈가 부러질 수 있습니다. 통증이 극심하고 부기가 심하다면 X-ray 촬영이 필요할 수 있습니다.\n\n### 치료 방법\n1. **RICE 요법**:\n   - **Rest (휴식)**: 부상을 입은 부위를 쉬게 하세요.\n   - **Ice (냉찜질)**: 부위에 얼음찜질을 15-20분씩, 하루에 여러 번 해주세요. 이는 부기를 줄이고 통증을 완화하는 데 도움이 됩니다.\n   - **Compression (압박)**: 탄력 붕대 등을 사용하여 부위를 압박해 주세요. 이는 부기를 줄이는 데 도움이 됩니다.\n   - **Elevation (높이기)**: 부상을 입은 다리를 심장보다 높게 유지하여 부기를 줄이세요.\n\n2. **진통제**: 필요시 이부프로펜이나 아세트아미노펜과 같은 진통제를 복용하여 통증을 완화할 수 있습니다.\n\n3. **물리치료**: 통증이 지속되거나 기능이 제한된다면 물리치료를 고려할 수 있습니다.\n\n### 예방 조치\n1. **적절한 준비 운동**: 운동 전 충분한 스트레칭과 준비 운동을 통해 부상을 예방하세요.\n2. **적절한 장비 착용**: 축구화와 같은 적절한 운동화를 착용하여 발목을 보호하세요.\n3. **운동 기술 향상**: 축구 기술을 향상시켜 부상의 위험을 줄이세요.\n\n부상이 심각하거나 통증이 지속된다면 반드시 전문의와 상담하여 정확한 진단과 치료를 받는 것이 중요합니다. 빠른 회복을 기원합니다!",
        "created_at": "2024-07-29T20:49:28.209134+09:00",
        "updated_at": "2024-07-29T20:49:37.030551+09:00"
    }
}
```

### 실패 응답

```json
{
    "successFlag": false,
    "code": "COMMON-004",
    "message": "서버 내부 오류.",
    "length": 0,
    "data": null
}
```
