from django.db import models


class SomethingElse(models.Model):

    a = models.CharField(max_length=255)


class Something(models.Model):

    relation1 = models.ForeignKey(SomethingElse, blank=True, null=True, on_delete=models.CASCADE)

    date1 = models.DateField(null=True, blank=True)
    date2 = models.DateField(null=True, blank=True)

    bool1 = models.BooleanField(default=True)
    bool2 = models.NullBooleanField()
    bool3 = models.BooleanField(default=False)

    int1 = models.IntegerField(null=True, blank=True)
    int2 = models.IntegerField(null=True, blank=True)
    int3 = models.IntegerField(null=True, blank=True)

    datetime1 = models.DateTimeField(auto_now=True, null=True)
