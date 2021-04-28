from django.db import models
from django.forms import ModelForm
import datetime


class UserInfo(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    bd_date = models.DateField(("date of birth"), default=datetime.date.today)
    phone = models.CharField(max_length=18)  # todo validators

    def __str__(self):
        return self.name


class Employer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date_founding = models.DateField(("founding date"), default=datetime.date.today)
    url = models.CharField(max_length=18)  # todo validators

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    employee = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    date_start = models.DateField(
        ("Initial date of employment"), default=datetime.date.today
    )
    date_end = models.DateField(
        ("Finel date of employment"), default=datetime.date.today
    )

    def __str__(self):
        return self.employee.name + " worked at " + self.employer.name


class Institution(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date_founding = models.DateField(("founding date"), default=datetime.date.today)
    url = models.CharField(max_length=18)  # todo validators

    def __str__(self):
        return self.name


class Education(models.Model):
    employee = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.employee.name + " studied at " + self.name


# FORMS


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ["name", "surname", "bd_date", "phone"]
