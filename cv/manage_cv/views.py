from django.shortcuts import render
from educations.models import Education


def home(request, template_name='manage_cv/home.html'):
    education = Education.objects.all()
    data = {}
    data['object_list'] = education
    return render(request, template_name, data)