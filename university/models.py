from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from utils.validators import first_name_validation, last_name_validation, phone_validation


class Question(models.Model):
    text = models.CharField(max_length=1000)

    def __str__(self):
        return "{}".format(self.text)


class Choice(models.Model):
    text = models.CharField(max_length=255, default="Write a choice plz")
    choices = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")

    def __str__(self):
        return "{}...".format(self.text[:10])


class Answer(models.Model):
    text = models.CharField(max_length=255, default="Write an answer plz")
    answers = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return "{}...".format(self.text[:10])


class Quiz(models.Model):
    title = models.CharField(max_length=255, default="Name this quiz plz")
    questions = models.ManyToManyField(Question, related_name="questions")

    def __str__(self):
        return "{}".format(self.title)


class Person(models.Model):
    first_name = models.CharField(max_length=200, validators=[first_name_validation])
    last_name = models.CharField(max_length=200, validators=[last_name_validation])
    email = models.EmailField(null=True)
    phone_number = models.CharField(validators=[phone_validation], max_length=17, blank=True)

    class Meta:
        abstract = True

class Student(Person):
    avg_mark = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)
    quizzes = models.ManyToManyField(Quiz)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Teacher(Person):
    subject = models.CharField(max_length=1000)
    quizzes = models.ForeignKey(Quiz, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Class(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name="teacher")
    students = models.ManyToManyField(Student, related_name="students")
    title = models.CharField(max_length=255, default="Name this class plz")

    def __str__(self):
        return "{}...".format(self.title[:10])








