from django.db import models


class Experiment(models.Model):

    INBUILT = 0
    PACKAGE = 1

    method = models.IntegerField()
    field_types = models.CharField(max_length=100)
    fields = models.SmallIntegerField()
    count = models.IntegerField()
    batch_size = models.IntegerField()
    time = models.FloatField()
