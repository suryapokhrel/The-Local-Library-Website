from django.db import models
from django.urls import reverse
import uuid # Required for unique book instances
# Create your models here.

# class MyModelName(models.Model):
#     # fields
#     my_filed_name = models.models.CharField(max_length=50, help_text='Enter field documentation')
    
#     # metadata
#     class Meta:
#         ordering = ["-my_field_name"]
       
#     #  method
#     def get_absolute_url(self):
#         return reverse("model_detail_view", args=[str(self.id)])
    
#     def __str__(self):
#         return self.my_filed_name
        
    
# record = MyModelName(my_filed_name="Instance #!")
# record.save()

# print(record.id)
# print(record.my_filed_name)


class Genre(models.Model):
    """Model reperesenting a book genre"""
    
    name = models.CharField(max_length=200, unique=True, 
                            help_text="Enter a book genre (e.g.Science fiction, french Poetry etc.)")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('genre_detail', args=[str(self.id)])
    

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)"""
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)
    
    summary = models.TextField(max_length=1000, help_text="Enter a brief desription of the book")
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    

    
class BookInstance(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.PROTECT, null=True)

    # author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)

    # ... (rest of the fields)

    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    
    class Meta:
        ordering = ['due_back']
        
    def __str__(self):
        return  f'{self.id} ({self.book.title})'    
    
    
class Author(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    
