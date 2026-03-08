# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

###
class Author(models.Model):
    author_id = models.IntegerField(db_column='AUTHOR_ID', primary_key=True)  # Field name made lowercase.
    author_fname = models.CharField(db_column='AUTHOR_FNAME', max_length=15, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    author_lname = models.CharField(db_column='AUTHOR_LNAME', max_length=15, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    author_bod = models.DateField(db_column='AUTHOR_BOD')  # Field name made lowercase.
    isbn = models.ForeignKey('Book', models.DO_NOTHING, db_column='ISBN')  # Field name made lowercase.
    DisplayFields = ['author_id', 'author_fname', 'author_lname', 'author_bod']
    SearchableFields = ['author_id', 'author_fname', 'author_lname', 'author_bod']

    class Meta:
        managed = False
        db_table = 'AUTHOR'
###
class Authorbookassociation(models.Model):
    author = models.OneToOneField(Author, models.DO_NOTHING, db_column='AUTHOR_ID', primary_key=True)  # Field name made lowercase. The composite primary key (AUTHOR_ID, ISBN) found, that is not supported. The first column is LOCATED
    isbn = models.ForeignKey('Book', models.DO_NOTHING, db_column='ISBN')  # Field name made lowercase.
    DisplayFields = ['author', 'isbn']

    class Meta:
        managed = False
        db_table = 'AUTHORBOOKASSOCIATION'
        unique_together = (('author', 'isbn'),)

###
class AvailabilityStatus(models.Model):
    status_id = models.IntegerField(db_column='STATUS_ID', primary_key=True)  # Field name made lowercase.
    statuss = models.CharField(db_column='STATUSS', max_length=15, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    DisplayFields = ['status_id', 'statuss']

    class Meta:
        managed = False
        db_table = 'AVAILABILITY_STATUS'
###
class Book(models.Model):
    isbn = models.IntegerField(db_column='ISBN', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    edition = models.ForeignKey('BookEdition', models.DO_NOTHING, db_column='EDITION_ID')  # Field name made lowercase.
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='LANGUAGE_ID')  # Field name made lowercase.
    availability_status = models.ForeignKey(AvailabilityStatus, models.DO_NOTHING, db_column='AVAILABILITY_STATUS_ID')  # Field name made lowercase.
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='PUBLISHER_ID')  # Field name made lowercase.
    genre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='GENRE_ID')  # Field name made lowercase.
    review = models.ForeignKey('Review', models.DO_NOTHING, db_column='REVIEW_ID')  # Field name made lowercase.
    DisplayFields = ['isbn', 'title', 'edition', 'language', 'availability_status', 'publisher', 'genre', 'review']
    SearchableFields = ['isbn', 'title', 'edition', 'language', 'availability_status', 'publisher', 'genre', 'review']

    class Meta:
        managed = False
        db_table = 'BOOK'

###
class Bookgenreassociation(models.Model):
    isbn = models.OneToOneField(Book, models.DO_NOTHING, db_column='ISBN', primary_key=True)  # Field name made lowercase. The composite primary key (ISBN, GENRE_ID) found, that is not supported. The first column is selected.
    genre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='GENRE_ID')  # Field name made lowercase.
    DisplayFields = ['isbn', 'genre']

    class Meta:
        managed = False
        db_table = 'BOOKGENREASSOCIATION'
        unique_together = (('isbn', 'genre'),)
###
class BookEdition(models.Model):
    edition_id = models.IntegerField(db_column='EDITION_ID', primary_key=True)  # Field name made lowercase.
    edition_name = models.CharField(db_column='EDITION_NAME', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    publication_date = models.DateField(db_column='PUBLICATION_DATE')  # Field name made lowercase.
    formatt = models.CharField(db_column='FORMATT', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    DisplayFields = ['edition_id', 'edition_name', 'publication_date', 'formatt']

    class Meta:
        managed = False
        db_table = 'BOOK_EDITION'
#
# class DatabaseAppAuthor(models.Model):
#     author_id = models.AutoField(primary_key=True)
#     author_fname = models.CharField(max_length=15, db_collation='Latin1_General_CI_AS')
#     author_lname = models.CharField(max_length=15, db_collation='Latin1_General_CI_AS')
#     author_bod = models.DateField()
#     isbn = models.IntegerField()
#     DisplayFields = ['author_id', 'author_fname', 'author_lname', 'author_bod', 'isbn']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_author'
#
#
# class DatabaseAppAuthorbookassociation(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     author_id = models.IntegerField()
#     isbn = models.IntegerField()
#     DisplayFields = ['id', 'author_id', 'isbn']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_authorbookassociation'
#
#
# class DatabaseAppAvailabilitystatus(models.Model):
#     status_id = models.AutoField(primary_key=True)
#     statuss = models.CharField(max_length=15, db_collation='Latin1_General_CI_AS')
#     DisplayFields = ['status_id', 'statuss']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_availabilitystatus'
#
#
#
# class DatabaseAppBook(models.Model):
#     isbn = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS')
#     edition_id = models.IntegerField()
#     language_id = models.IntegerField()
#     availability_status_id = models.IntegerField()
#     publisher_id = models.IntegerField()
#     genre_id = models.IntegerField()
#     review_id = models.IntegerField()
#     DisplayFields = ['isbn', 'title', 'edition_id', 'language_id', 'availability_status_id', 'publisher_id', 'genre_id', 'review_id']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_book'
#
#
# class DatabaseAppBookedition(models.Model):
#     edition_id = models.AutoField(primary_key=True)
#     edition_name = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS')
#     publication_date = models.DateField()
#     formatt = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)
#     DisplayFields = ['edition_id', 'edition_name', 'publication_date', 'formatt']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_bookedition'
#
#
# class DatabaseAppBookgenreassociation(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     isbn = models.IntegerField()
#     genre_id = models.IntegerField()
#     DisplayFields = ['id', 'isbn', 'genre_id']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_bookgenreassociation'
#
#
# class DatabaseAppFine(models.Model):
#     fine_id = models.AutoField(primary_key=True)
#     fine_amount = models.IntegerField()
#     fine_reason = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS')
#     fine_pay_status = models.CharField(max_length=15, db_collation='Latin1_General_CI_AS')
#     member_id = models.IntegerField()
#     DisplayFields = ['fine_id', 'fine_amount', 'fine_reason', 'fine_pay_status', 'member_id']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_fine'
#
#
#
# class DatabaseAppGenre(models.Model):
#     genre_id = models.AutoField(primary_key=True)
#     genre_name = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS')
#     genre_description = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)
#     DisplayFields = ['genre_id', 'genre_name', 'genre_description']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_genre'
#
#
# class DatabaseAppLanguage(models.Model):
#     language_id = models.AutoField(primary_key=True)
#     language_name = models.CharField(max_length=15, db_collation='Latin1_General_CI_AS')
#     DisplayFields = ['language_id', 'language_name']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_language'
#
#
# class DatabaseAppLibrarybranch(models.Model):
#     branch_id = models.AutoField(primary_key=True)
#     branch_name = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS')
#     branch_location = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS')
#     branch_contact = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS')
#     DisplayFields = ['branch_id', 'branch_name', 'branch_location', 'branch_contact']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_librarybranch'
# class DatabaseAppLoan(models.Model):
#     loan_id = models.AutoField(primary_key=True)
#     loan_date = models.DateField()
#     due_date = models.DateField()
#     return_date = models.DateField()
#     fine_amount = models.IntegerField()
#     loan_status = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS')
#     isbn = models.IntegerField()
#     member_id = models.IntegerField()
#     DisplayFields = ['loan_id', 'loan_date', 'due_date', 'return_date', 'fine_amount', 'loan_status', 'isbn', 'member_id']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_loan'
#
#
# class DatabaseAppPublisher(models.Model):
#     publisher_id = models.AutoField(primary_key=True)
#     publisher_name = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS')
#     publisher_contact = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS')
#     publisher_address = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS')
#     DisplayFields = ['publisher_id', 'publisher_name', 'publisher_contact', 'publisher_address']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_publisher'
#
#
# class DatabaseAppReservation(models.Model):
#     reservation_id = models.AutoField(primary_key=True)
#     reservation_date = models.DateField()
#     reservation_status = models.CharField(max_length=15, db_collation='Latin1_General_CI_AS')
#     isbn = models.IntegerField()
#     member_id = models.IntegerField()
#     DisplayFields = ['reservation_id', 'reservation_date', 'reservation_status', 'isbn', 'member_id']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_reservation'
#
#
# class DatabaseAppReview(models.Model):
#     review_id = models.AutoField(primary_key=True)
#     rating = models.CharField(max_length=10, db_collation='Latin1_General_CI_AS')
#     review_date = models.DateField()
#     DisplayFields = ['review_id', 'rating', 'review_date']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_review'
# class DatabaseAppShelf(models.Model):
#     shelf_id = models.AutoField(primary_key=True)
#     shelf_number = models.IntegerField()
#     shelf_capacity = models.IntegerField()
#     shelf_type = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS')
#     isbn = models.IntegerField()
#     branch_id = models.IntegerField()
#     DisplayFields = ['shelf_id', 'shelf_number', 'shelf_capacity', 'shelf_type', 'isbn', 'branch_id']
#
#     class Meta:
#         managed = False
#         db_table = 'DATABASE_APP_shelf'

###
class Fine(models.Model):
    fine_id = models.IntegerField(db_column='FINE_ID', primary_key=True)  # Field name made lowercase.
    fine_amount = models.IntegerField(db_column='FINE_AMOUNT')  # Field name made lowercase.
    fine_reason = models.CharField(db_column='FINE_REASON', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    fine_pay_status = models.CharField(db_column='FINE_PAY_STATUS', max_length=15, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    DisplayFields = ['fine_id', 'fine_amount', 'fine_reason', 'fine_pay_status', 'member']

    class Meta:
        managed = False
        db_table = 'FINE'
###
class Genre(models.Model):
    genre_id = models.IntegerField(db_column='GENRE_ID', primary_key=True)  # Field name made lowercase.
    genre_name = models.CharField(db_column='GENRE_NAME', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    genre_description = models.CharField(db_column='GENRE_DESCRIPTION', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    DisplayFields = ['genre_id', 'genre_name', 'genre_description']

    class Meta:
        managed = False
        db_table = 'GENRE'
###
class Language(models.Model):
    language_id = models.IntegerField(db_column='LANGUAGE_ID', primary_key=True)  # Field name made lowercase.
    language_name = models.CharField(db_column='LANGUAGE_NAME', max_length=15, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    DisplayFields = ['language_id', 'language_name']

    class Meta:
        managed = False
        db_table = 'LANGUAGE_'
###
class Librarian(models.Model):
    librarian_id = models.IntegerField(db_column='LIBRARIAN_ID', primary_key=True)  # Field name made lowercase.
    librarian_fname = models.CharField(db_column='LIBRARIAN_FNAME', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    librarian_lname = models.CharField(db_column='LIBRARIAN_LNAME', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    librarian_contact = models.CharField(db_column='LIBRARIAN_CONTACT', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    branch = models.ForeignKey('LibraryBranch', models.DO_NOTHING, db_column='BRANCH_ID')  # Field name made lowercase.
    DisplayFields = ['librarian_id', 'librarian_fname', 'librarian_lname', 'librarian_contact', 'branch']

    class Meta:
        managed = False
        db_table = 'LIBRARIAN'
###
class LibraryBranch(models.Model):
    branch_id = models.IntegerField(db_column='BRANCH_ID', primary_key=True)  # Field name made lowercase.
    branch_name = models.CharField(db_column='BRANCH_NAME', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    branch_location = models.CharField(db_column='BRANCH_LOCATION', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    branch_contact = models.CharField(db_column='BRANCH_CONTACT', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    DisplayFields = ['branch_id', 'branch_name', 'branch_location', 'branch_contact']

    class Meta:
        managed = False
        db_table = 'LIBRARY_BRANCH'
###
class Loan(models.Model):
    loan_id = models.IntegerField(db_column='LOAN_ID', primary_key=True)  # Field name made lowercase.
    loan_date = models.DateField(db_column='LOAN_DATE')  # Field name made lowercase.
    due_date = models.DateField(db_column='DUE_DATE')  # Field name made lowercase.
    return_date = models.DateField(db_column='RETURN_DATE')  # Field name made lowercase.
    fine_amount = models.IntegerField(db_column='FINE_AMOUNT')  # Field name made lowercase.
    loan_status = models.CharField(db_column='LOAN_STATUS', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    isbn = models.ForeignKey(Book, models.DO_NOTHING, db_column='ISBN')  # Field name made lowercase.
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    DisplayFields = ['loan_id', 'loan_date', 'due_date', 'return_date', 'fine_amount', 'loan_status', 'isbn', 'member']

    class Meta:
        managed = False
        db_table = 'LOAN'
###
class Member(models.Model):
    member_id = models.IntegerField(db_column='MEMBER_ID', primary_key=True)  # Field name made lowercase.
    member_fname = models.CharField(db_column='MEMBER_FNAME', max_length=15, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    member_lname = models.CharField(db_column='MEMBER_LNAME', max_length=15, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    member_contact = models.CharField(db_column='MEMBER_CONTACT', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    member_email = models.CharField(db_column='MEMBER_EMAIL', unique=True, max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    member_address = models.CharField(db_column='MEMBER_ADDRESS', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    membership_status = models.CharField(db_column='MEMBERSHIP_STATUS', max_length=15, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    review = models.ForeignKey('Review', models.DO_NOTHING, db_column='REVIEW_ID')  # Field name made lowercase.
    branch = models.ForeignKey(LibraryBranch, models.DO_NOTHING, db_column='BRANCH_ID')  # Field name made lowercase.
    DisplayFields = ['member_id', 'member_fname', 'member_lname', 'member_contact', 'member_email', 'member_address', 'membership_status', 'review', 'branch']

    class Meta:
        managed = False
        db_table = 'MEMBER_'
###
class Publisher(models.Model):
    publisher_id = models.IntegerField(db_column='PUBLISHER_ID', primary_key=True)  # Field name made lowercase.
    publisher_name = models.CharField(db_column='PUBLISHER_NAME', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    publisher_contact = models.CharField(db_column='PUBLISHER_CONTACT', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    publisher_address = models.CharField(db_column='PUBLISHER_ADDRESS', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    DisplayFields = ['publisher_id', 'publisher_name', 'publisher_contact', 'publisher_address']

    class Meta:
        managed = False
        db_table = 'PUBLISHER'
###
class Reservation(models.Model):
    reservation_id = models.IntegerField(db_column='RESERVATION_ID', primary_key=True)  # Field name made lowercase.
    reservation_date = models.DateField(db_column='RESERVATION_DATE')  # Field name made lowercase.
    reservation_status = models.CharField(db_column='RESERVATION_STATUS', max_length=15, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    isbn = models.ForeignKey(Book, models.DO_NOTHING, db_column='ISBN')  # Field name made lowercase.
    member = models.ForeignKey(Member, models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    DisplayFields = ['reservation_id', 'reservation_date', 'reservation_status', 'isbn', 'member']

    class Meta:
        managed = False
        db_table = 'RESERVATION'
###
class Review(models.Model):
    review_id = models.IntegerField(db_column='REVIEW_ID', primary_key=True)  # Field name made lowercase.
    rating = models.CharField(db_column='RATING', max_length=10, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    review_date = models.DateField(db_column='REVIEW_DATE')  # Field name made lowercase.
    DisplayFields = ['review_id', 'rating', 'review_date']

    class Meta:
        managed = False
        db_table = 'REVIEW'
###
class Shelf(models.Model):
    shelf_id = models.IntegerField(db_column='SHELF_ID', primary_key=True)  # Field name made lowercase.
    shelf_number = models.IntegerField(db_column='SHELF_NUMBER')  # Field name made lowercase.
    shelf_capacity = models.IntegerField(db_column='SHELF_CAPACITY')  # Field name made lowercase.
    shelf_type = models.CharField(db_column='SHELF_TYPE', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    isbn = models.ForeignKey(Book, models.DO_NOTHING, db_column='ISBN')  # Field name made lowercase.
    branch = models.ForeignKey(LibraryBranch, models.DO_NOTHING, db_column='BRANCH_ID')  # Field name made lowercase.
    DisplayFields = ['shelf_id', 'shelf_number', 'shelf_capacity', 'shelf_type', 'isbn', 'branch']

    class Meta:
        managed = False
        db_table = 'SHELF'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Latin1_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Latin1_General_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Latin1_General_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Latin1_General_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Latin1_General_CI_AS')
    email = models.CharField(max_length=254, db_collation='Latin1_General_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Latin1_General_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Latin1_General_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Latin1_General_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS')
    model = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    name = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Latin1_General_CI_AS')
    session_data = models.TextField(db_collation='Latin1_General_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
