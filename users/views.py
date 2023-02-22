from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .forms import CustomUserCreationForm


# class Register(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('register_done')
#     template_name = 'registration/register.html'
#
#
# def register_done(request):
#
#     return render(request, 'registration/register_done.html')
