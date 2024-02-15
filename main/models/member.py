from django.db import models
from main.models.base import BaseModel

class Member(BaseModel):
    name = models.CharField(max_length=50)
    