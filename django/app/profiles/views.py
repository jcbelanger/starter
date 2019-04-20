from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Profile


class IndexView(generic.ListView):
	model = Profile


class DetailView(generic.DetailView):
    model = Profile

