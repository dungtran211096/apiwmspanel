from django.db import models

# Create your models here.


class server (models.Model):
    objects = None
    name = models.CharField(max_length=100, default="")
    name_server = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name


class stream (models.Model):
    objects = None
    id_stream = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100, default="")
    bandwidth = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="")
    input = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name