from django.urls import path
from . import views
from .views import EmpList

urlpatterns = [
    path('home/', views.EmpList.as_view(), name='Emp_list'),
    path('Emp/<int:pk>', views.EmpDetail.as_view(), name='Emp_detail'),
    path('create/', views.EmpCreate.as_view(), name='Emp_create'),
    path('update/<int:pk>', views.EmpUpdate.as_view(), name='Emp_edit'),
    path('delete/<int:pk>', views.EmpDelete.as_view(), name='Emp_delete'),
]