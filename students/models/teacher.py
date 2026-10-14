
from django.db import models


class Teacher(models.Model):
    name = models.CharField("NAME:", max_length=100)
    subject = models.CharField("SUBJECT:", max_length=100)
    phone = models.CharField("PHONE:", max_length=20)

    class Meta:
        verbose_name = "TEACHER"
        verbose_name_plural = "TEACHERS"

    def __str__(self):
        return self.name
