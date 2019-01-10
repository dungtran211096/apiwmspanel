from django.db import models

# Create your models here.


class server (models.Model):
    filter = None
    objects = None
    name = models.CharField(max_length=100, default="")
    name_server = models.CharField(max_length=100, default="")

    @property
    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'server'
        verbose_name_plural = 'servers'


class server_id (models.Model):
    object = None
    filter = None
    objects = None
    server_id = models.CharField(max_length=100, default="")

    @property
    def __str__(self):
        return self.server_id

    class Meta:

        verbose_name = 'server'
        verbose_name_plural = 'servers'


class stream (models.Model):
    filter = None
    objects = None
    id_stream = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100, default="")
    bandwidth = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="")
    input = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name


class re_publish (models.Model):
    objects = None
    id_rule = models.CharField(max_length=100, default="")
    src_strm = models.CharField(max_length=100, default="")
    re_start = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

