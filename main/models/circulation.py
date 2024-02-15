from django.db import models
from main.models.base import BaseModel
from main.models.book import Book
from main.models.member import Member

class Circulation(BaseModel):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField()
    returned = models.BooleanField(default=False)