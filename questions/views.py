# views.py
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from config.enum.error_code import ErrorCode
from config.enum.success_code import SuccessCode
from config.utils import APIResponse
from .models import Question
from .serializers import QuestionSerializer
from openai import OpenAI

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)
engine = "gpt-4o-mini"

class QuestionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Question.objects.filter(user=request.user)
        serializer = QuestionSerializer(questions, many=True)
        return APIResponse.success(
            data=serializer.data,
            message=SuccessCode.SUCCESS_002.message,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save(user=request.user)  # user를 추가하여 저장

            response = gpt4o_mini_openAI_api(engine, question.question_text)

            question.answer_text = response
            
            question.save()
            return APIResponse.success(
                data=QuestionSerializer(question).data,
                message=SuccessCode.SUCCESS_001.message,
                status=status.HTTP_201_CREATED
            )
        return APIResponse.error(
            code=ErrorCode.COMMON_001.code,
            message=ErrorCode.COMMON_001.message,
            status=status.HTTP_400_BAD_REQUEST
        )

class QuestionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Question.objects.get(pk=pk, user=user)
        except Question.DoesNotExist:
            return APIResponse.error(
            code=ErrorCode.QUESTION_001.code,
            message=ErrorCode.QUESTION_001.message,
            status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, pk):
        question = self.get_object(pk, request.user)
        serializer = QuestionSerializer(question)
        return APIResponse.success(
            data=serializer.data,
            message=SuccessCode.SUCCESS_002.message,
            status=status.HTTP_200_OK
        )

    def delete(self, request, pk):
        question = self.get_object(pk, request.user)
        question.delete()
        return APIResponse.success(
            data={},
            message=SuccessCode.SUCCESS_004.message,
            status=status.HTTP_200_OK
        )
    

# 그냥 gpt4
def gpt4o_mini_openAI_api(engine, question_text):
    completion = client.chat.completions.create(
        model=engine,
        #max_tokens=500,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a highly renowned and intelligent medical doctor with extensive knowledge in diagnosing and treating a wide range of medical conditions. "
                    "Your expertise allows you to accurately diagnose illnesses based on symptoms provided, and you can suggest effective treatments and preventive measures. "
                    "Please provide a thorough diagnosis, possible treatments, and preventive advice for the given symptoms. Respond in Korean."
                ),
            },
            {
                "role": "user",
                "content": question_text,
            },
        ],
        temperature=0.1,
    )
    answer_text = completion.choices[0].message.content
    return answer_text;