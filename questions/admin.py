from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'answer_text', 'user', 'created_at', 'updated_at')
    search_fields = ('question_text', 'answer_text', 'user__username')
    list_filter = ('created_at', 'updated_at', 'user')
    ordering = ('-created_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('user')

admin.site.register(Question, QuestionAdmin)
