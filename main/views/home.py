from django.shortcuts import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponseBadRequest, JsonResponse
from main.models.book import Book
from django.db import transaction
from datetime import datetime
from  main.service.book_service import BookService
from main.service.reservation_service import ReservationService
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return HttpResponse("helo")

# {
#         "eventtype": "checkout",
#         "book_id": 1000,
#         "member_id": 2003,
#         "date": "2023-05-10"
#     },

@csrf_exempt
@require_POST
def checkout(request):
    data = json.loads(request.body)
    member_id = data.get('member_id')
    book_id = data.get('book_id')
    date = data.get('date')
    
    print(data)
    date = datetime.strptime(date, "%Y-%m-%d").date()
    if None in [member_id, book_id, date]:
        return HttpResponseBadRequest('Invalid data')

    checkedout, response_id = BookService.checkout(book_id, member_id, date)
    if checkedout:
        return JsonResponse({ 'message': f'Successfully checked out with circulation: {response_id}'})
    else:
        return JsonResponse({ 'message': f'Book not available, checked out with reservation: {response_id}'})


@csrf_exempt
@require_POST
def return_book(request):
    data = json.loads(request.body)
    member_id = data.get('member_id')
    book_id = data.get('book_id')
    date = data.get('date')

    print(data)
    date = datetime.strptime(date, "%Y-%m-%d").date()
    if None in [member_id, book_id, date]:
        return HttpResponseBadRequest('Invalid data')

    returned = BookService.return_book(book_id, member_id, date)
    if returned:
        return JsonResponse({ 'message': 'Successfully returned'})
    else:
        return JsonResponse({ 'message': 'Unable to return book'})
        
from datetime import timedelta

@require_GET
def check_overdue(request):
    data = json.loads(request.body)
    member_id = data.get('member_id')
    date = data.get('date')
    date = datetime.strptime(date, "%Y-%m-%d").date() - timedelta(days=7)
    if None in [member_id]:
        return HttpResponseBadRequest('Invalid data')
    
    books, fine = ReservationService.check_overdue(member_id, date)
    return JsonResponse({ 'overdue_books': books, 'fine': fine})  

from main.models.circulation import Circulation
