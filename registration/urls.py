from django.urls import path
from . import views

urlpatterns = [
    path('', views.records, name='records'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('editstudent/<id>', views.editstudent, name='editstudent'),
    path('updatestudent/<id>', views.updatestudent, name='updatestudent'),
    path('deletestudent/<id>', views.deletestudent, name='deletestudent'),


]