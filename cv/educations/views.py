from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Education

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['name', 'pages']

def education_list(request, template_name='educations/education_list.html'):
    education = Education.objects.all()
    data = {}
    data['object_list'] = education
    return render(request, template_name, data)

def education_create(request, template_name='educations/education_form.html'):
    form = EducationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('educations:education_list')
    return render(request, template_name, {'form':form})

def education_update(request, pk, template_name='educations/education_form.html'):
    education= get_object_or_404(Education, pk=pk)
    form = EducationForm(request.POST or None, instance=education)
    if form.is_valid():
        form.save()
        return redirect('educations:education_list')
    return render(request, template_name, {'form':form})

def education_delete(request, pk, template_name='educations/education_confirm_delete.html'):
    education= get_object_or_404(Education, pk=pk)    
    if request.method=='POST':
        education.delete()
        return redirect('educations:education_list')
    return render(request, template_name, {'object':education})
