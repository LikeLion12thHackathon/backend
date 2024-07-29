from rest_framework import serializers

from users.serializers import PrivateUserSerializer
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    # user = PrivateUserSerializer(read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'answer_text', 'created_at', 'updated_at']# , 'user'
