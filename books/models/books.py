from django.db import models

class Books(models.Model):
    clientname = models.CharField("NAME:", max_length = 100)
    adress = models.CharField("ADRESS:", max_length = 100)
    clientPhone = models.IntegerField("TELL:")


    class Meta:
        verbose_name = "BOOKS"
        verbose_name_plural = "BOOKS"

    def __str__(self):
        return self.clientname    