from django.db import models

from common.models import CommonModel
from users.models import User

# Create your models here.
class Question(CommonModel):
    question_text = models.TextField()
    answer_text = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='questions')

    def __str__(self):
        return self.question_text