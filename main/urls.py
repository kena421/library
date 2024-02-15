from django.urls import path
from main.views.home import index, checkout, return_book, check_overdue


urlpatterns = [
    path('', index),
    path('checkout', checkout),
    path('return', return_book),
    path('overdue', check_overdue)
]