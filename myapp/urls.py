from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.register, name='register'),  # Set the register page as the default route
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),  # Optional: keep a route for the index page
    path('service-details/', views.service_details, name='service-details'),
    path('starter-page/', views.starter_page, name='starter-page'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('myservice/', views.myservice, name='myservice'),
    path('appointment/', views.make_appointment, name='make_appointment'),
    path('contact/', views.contact, name='contact'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),

]
