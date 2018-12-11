from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    roleId = models.ForeignKey("Role", on_delete=models.SET_NULL, null=True)
    fullname = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    regDate = models.DateTimeField()

class Role(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField((""), max_length=50)

class Paper(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    authorId = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    subjectId = models.ForeignKey("Subject", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    createDate = models.DateTimeField()
    status = models.IntegerField()

class Version(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    paperId = models.ForeignKey("Paper", on_delete=models.CASCADE)
    authorId = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    text = models.TextField()
    status = models.IntegerField()

class File(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    filename = models.CharField(max_length=100)
    size = models.FloatField()
    extension = models.CharField(max_length=10)
    date = models.DateTimeField()

class Settings(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    setType = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    
class Subject(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
