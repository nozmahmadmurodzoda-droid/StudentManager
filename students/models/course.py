
from django.db import models


class Course(models.Model):
    name = models.CharField("NAME:", max_length=100)
    description = models.TextField("DESCRIPTION:")

    teacher = models.ForeignKey(
        "Teacher",
        on_delete=models.CASCADE,
        verbose_name="TEACHER:"
    )

    class Meta:
        verbose_name = "COURSE"
        verbose_name_plural = "COURSES"

    def __str__(self):
        return self.name
