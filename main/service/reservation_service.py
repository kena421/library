from main.models.book import Book
from django.db import transaction
from main.models.reservation import Reservation
from main.models.circulation import Circulation
from datetime import timedelta

class ReservationService:
    @classmethod
    def check_overdue(cls, member_id, date):
        books = []
        fine = 0
        ciculations = Circulation.objects.filter(member_id=member_id, returned=False, date__lt = date)
        for circulation in ciculations:
            books.append(circulation.book_id)
            fine += (date - circulation.date).days * 50
        return [books, fine]
    
    @classmethod
    def popfirst_reserved_member(cls, book_id):
        reservation = Reservation.objects.select_for_update().filter(book_id=book_id).order_by('id').first()
        with transaction.atomic():
            if reservation:
                member_id = reservation.member_id
                reservation.delete()
                return member_id
        return None
    
    @classmethod
    def assign_book_if_reserved(cls, book_id, date):
        from main.service.book_service import BookService
        with transaction.atomic():
            member_id =  cls.popfirst_reserved_member(book_id)
            if member_id:
                BookService.assign_book(book_id, member_id, date)
                return True
            else:
                return False
        
        
                

                
                
                
                
        
        
        