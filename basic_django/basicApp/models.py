from django.db import models

# Create your models here.

class Authors(models.Model):
    def __init__(self, AuthorName, Country, BookName):
        self.AuthorName = AuthorName
        self.Country = Country
        self.BookName = BookName