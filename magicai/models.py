from django.db import models

from common.helper import make_uuid
from user.models import UserBase


class ResponseData(models.Model):
    id = models.UUIDField(primary_key=True, default=make_uuid)
    quran_res = models.TextField(null=True, blank=True)
    hadeeth_res = models.TextField(null=True, blank=True)
    # Usage
    prompt_tokens = models.IntegerField(null=True, blank=True)
    completion_tokens = models.IntegerField(null=True, blank=True)
    total_tokens = models.IntegerField(null=True, blank=True)
    gpt_model = models.CharField(max_length=255, null=True, blank=True)



class UserPrompt(models.Model):
    id = models.UUIDField(primary_key=True, default=make_uuid)
    user = models.ForeignKey(UserBase, on_delete=models.CASCADE, related_name="user_prompts")
    prompt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    response = models.ForeignKey(ResponseData,  on_delete=models.CASCADE, null=True, blank=True)


