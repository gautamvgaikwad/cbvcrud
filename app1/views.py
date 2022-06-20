from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Empdata

class EmpList(ListView): 
    model = Empdata
    template_name = 'app1/Emp_list.html'

class EmpDetail(DetailView): 
    model = Empdata
    template_name = 'app1/Emp_details.html'

class EmpCreate(CreateView): 
    model = Empdata
    fields = ['name','email','designation','contact_no']
    template_name = 'app1/Emp_form.html'
    success_url = '/fa/home'

class EmpUpdate(UpdateView): 
    model = Empdata
    fields = ['name','email','designation','contact_no']
    template_name = 'app1/Emp_form.html'
    success_url = '/fa/home'

class EmpDelete(DeleteView): 
    model = Empdata
    template_name = 'app1/Emp_delete.html'
    success_url = '/fa/home'

