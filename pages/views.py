from django.views.generic import TemplateView
from .models import UserInfoForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class CvPageView(TemplateView):
    template_name = "pages/cv.html"


class AccountPageView(FormView):
    form_class = UserInfoForm
    template_name = "pages/account.html"


def insertUser(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = UserInfoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("pages/account.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserInfoForm()

    return render(request, "pages/account.html", {"form": form})
