import datetime
from django.db import models
from django.contrib.auth.models import Permission

import os
import random


# Create your models here.
class clientsTable(models.Model):
    name    = models.CharField(max_length=200)
    email   = models.EmailField(max_length=200)
    contact_number = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    date    = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.email

class TestDetails(models.Model):
    test_id = models.CharField(max_length=200, unique=True)
    client_id = models.CharField(max_length=200, default=0)
    test_tittle  = models.CharField(max_length=200)
    test_duration = models.CharField(max_length=200)
    date    = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.test_id

class StudentProfile(models.Model):
    name    = models.CharField(max_length=200)
    email   = models.EmailField(max_length=200)
    password= models.CharField(max_length=200, default=None)
    roll_NO = models.CharField(max_length=200, default=None)
    client  = models.CharField(max_length=200, default=None)
    date    = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.email

class Question(models.Model):
    question_id = models.CharField(max_length=200)
    question    = models.CharField(max_length=200)
    option1     = models.CharField(max_length=200)
    option2     = models.CharField(max_length=200)
    option3     = models.CharField(max_length=200)
    option4     = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class studentMark(models.Model):
    student_id = models.CharField(max_length=120, default=0)
    ques_paper_id = models.CharField(max_length=50)
    marks = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    test_title = models.CharField(max_length=50)
    client = models.CharField(max_length=50, default=None)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.email