from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="DjangoTemplate",  # 프로젝트 이름 (예: DjangoTemplate-project)
        default_version="1.0.0",  # 프로젝트 버전(예: 1.0.0)
        description="DjangoTemplate-project API 문서",  # 해당 문서 설명(예: DjangoTemplate-project API 문서)
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="qzqzcaraz00@gmail.com"),  # 부가정보
        license=openapi.License(name="BSD License"),  # 부가정보
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),  # 어드민 페이지 URL
    path("api/v1/users/", include("users.urls")),  # users 앱의 URL
]


# 디버그일때만 swagger 문서가 보이도록 해주는 설정,
# 여기에 urlpath도 작성 가능해서 debug일때만 작동시킬 api도 설정할 수 있음
if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        re_path(
            r"^redoc/$",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
        # 이 아래 부터 우리가 debug일때만 작동시킬 api URL들을 넣습니다.
    ] + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# static 파일을 제공하기 위한 설정
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)

admin.site.site_title = (
    "Site Tile | The Template Admin"  # django 어드민 페이지의 타이틀
)
admin.site.site_header = "The Template Admin"  # django 어드민 페이지의 헤더
admin.site.index_title = (
    "The Template Management"  # django 어드민 페이지의 인덱스 타이틀
)
