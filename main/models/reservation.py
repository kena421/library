from django.db import models
from main.models.base import BaseModel
from main.models.member import Member
from main.models.book import Book

class Reservation(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField()
    