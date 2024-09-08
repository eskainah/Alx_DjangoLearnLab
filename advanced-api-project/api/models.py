from django.db import models

# Create your models here.
class Author(models.Model):
    author = models.CharField(max_length= 100)

    def __str__(self):
        return self.author
class Book(models.Model):
    title = models.CharField(max_length= 100)
    author = models.ForeignKey(
        Author,
        on_delete= models.CASCADE
    )
    publication_year = models.DateField()

    def __str__(self):
        return self.title