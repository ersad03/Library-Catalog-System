# your_app/admin.py

from django.contrib import admin
from .models import (
    Author, Authorbookassociation, AvailabilityStatus, Book,
    Bookgenreassociation, BookEdition, Fine,
    Genre, Language, Librarian, LibraryBranch, Loan, Member, Publisher,
    Reservation, Review, Shelf
)


###
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = Author.DisplayFields
    search_fields = Author.SearchableFields
###
@admin.register(Authorbookassociation)
class AuthorbookassociationAdmin(admin.ModelAdmin):
    list_display = Authorbookassociation.DisplayFields
###
@admin.register(AvailabilityStatus)
class AvailabilityStatusAdmin(admin.ModelAdmin):
    list_display = AvailabilityStatus.DisplayFields
###
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = Book.DisplayFields
    search_fields = Book.SearchableFields
###
@admin.register(Bookgenreassociation)
class BookgenreassociationAdmin(admin.ModelAdmin):
    list_display = Bookgenreassociation.DisplayFields
###
@admin.register(BookEdition)
class BookEditionAuthorAdmin(admin.ModelAdmin):
    list_display = BookEdition.DisplayFields

###
@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = Fine.DisplayFields
###
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = Genre.DisplayFields
###
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = Language.DisplayFields
###
@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = Librarian.DisplayFields
###
@admin.register(LibraryBranch)
class LibraryBranchAdmin(admin.ModelAdmin):
    list_display = LibraryBranch.DisplayFields
###
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = Loan.DisplayFields
###
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = Member.DisplayFields
###
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = Publisher.DisplayFields
###
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = Reservation.DisplayFields
###
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = Review.DisplayFields
###
@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = Shelf.DisplayFields

