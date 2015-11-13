from django.db import models
from django.contrib import admin
class Author(models.Model):
    AuthorID=models.CharField(max_length=20,primary_key=True)
    Name=models.CharField(max_length=20)
    Age=models.CharField(max_length=3)
    Country=models.CharField(max_length=20)
    def __unicode__(self):
        return self.AuthorID
class Book(models.Model):
    ISBN=models.CharField(max_length=150,primary_key=True)
    Title=models.CharField(max_length=150)
    AuthorID=models.ForeignKey(Author)
    Publisher=models.CharField(max_length=150)
    PublishDate=models.DateField()
    Price=models.CharField(max_length=10)
    def __unicode__(self):
        return self.Title
admin.site.register(Author)
admin.site.register(Book)       
