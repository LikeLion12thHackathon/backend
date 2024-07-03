# DjangoTemplate
django 백엔드 새 프로젝트 개발을 위한 템플릿 레퍼지토리

## Django settings.py 셋팅
Django 서버를 한국시간으로 설정

커스텀 user 등록

환경변수로 개발환경 배포환경 분리
- [.env.dev](.env.dev)
- [.env.dev.db](.env.dev.db)

## DRF 프로젝트를 위해 아래와 같이 초기 라이브러리 셋팅
django = "^5.0.2"
django-cors-headers==4.3.1
djangorestframework==3.14.0
drf-yasg==1.21.7
djangorestframework-simplejwt = "^5.3.1"

## JWT 인증인가 셋팅

## 배포를 위한 nginx , docker 셋팅

### nginx
- [nginx/Dockerfile](nginx/Dockerfile)
- [nginx/nginx.conf](nginx/nginx.conf)
### docker
- [Dockerfile](Dockerfile)
- [docker-compose.yml](docker-compose.yml)
