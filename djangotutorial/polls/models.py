import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Operation(models.Model):
    normative_time = models.IntegerField()  # Нормативное время на выполнение операции
    allocated_resources = models.IntegerField()  # Количество выделяемых ресурсов
    resource_availability_coefficient = models.FloatField()  # Коэффициент доступности ресурсов
    labor_productivity_coefficient = models.FloatField()  # Коэффициент производительности труда
    duration_estimate = models.FloatField()  # Оценка длительности

    def str(self):
        return f"Operation {self.id}: Normative Time={self.normative_time}, Allocated Resources={self.allocated_resources}"