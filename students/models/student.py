
from django.db import models


class Student(models.Model):
    name = models.CharField("NAME:", max_length=50)
    age = models.IntegerField("AGE:")
    email = models.EmailField("EMAIL:", max_length=50)
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        verbose_name="COURSE:"
    )

    class Meta:
        verbose_name = "STUDENT"
        verbose_name_plural = "STUDENTS"

    def __str__(self):
        return self.name
