from django.db import models
from django.urls import reverse


class Education(models.Model):
    name = models.CharField(max_length=200)
    grades = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('educations:education_edit', kwargs={'pk': self.pk})