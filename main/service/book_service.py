from main.models.book import Book
from main.models.circulation import Circulation
from main.models.reservation import Reservation
from main.service.reservation_service import ReservationService

from django.db import transaction


class BookService:
    @classmethod
    def return_book(cls, book_id, member_id, date):
        circulated_book = Circulation.objects.select_for_update().filter(book_id=book_id, member_id=member_id, returned=False).first()
        with transaction.atomic():
            if circulated_book:
                circulated_book.returned = True
                book = Book.objects.filter(id=book_id).first()
                assigned = ReservationService.assign_book_if_reserved(book_id, date)
                if not assigned:
                    book.num_copies += 1
                    book.save()
                    
                circulated_book.save()
                return True
            else:
                return False
                
    @classmethod
    def assign_book(cls, book_id, member_id, date):
        return Circulation.objects.create(book_id=book_id, member_id=member_id, date=date)
    
    @classmethod
    def checkout(cls, book_id, member_id, date):
        book = Book.objects.select_for_update().filter(id=book_id, num_copies__gt = 0).first()
        with transaction.atomic():
            book.num_copies -= 1
            book.save()
            if book.num_copies > 0:
                circulation = Circulation.objects.create(book_id=book_id, member_id=member_id, date=date)
                return [True, circulation.id]
            else:
                # do i need to check if reservation already exist ?
                reservation = Reservation.objects.create(book_id=book_id, member_id=member_id, date=date)
                return [False, reservation.id]


            
        