from django.contrib import admin
from django.urls import path
from App_1 import views

urlpatterns = [
    path('',views.index),
    path('home',views.index), #if matches blank '' then go to app_1 views file and execute function named as index.
    path('about',views.about),
    path('services',views.services),
    path('contactus',views.contactus),
    path('loginuser',views.loginuser),
    path('logoutuser',views.logoutuser),
    path('createacc',views.createacc),
    path('admin_login',views.admin_login),
    path('admin_main',views.admin_main),
    path('eng',views.engineering),
    path('science',views.science),
    path('agr',views.agriculture),
    path('mng',views.management),
    path('arc',views.architectural),
    path('add_book',views.add_book),
    path('checkout',views.checkout),
    path('return_1',views.return_1),
    path('show_books',views.show_books),
    path('show_books_admin',views.show_books_admin),
    path('remove', views.remove),
    path('delete/<int:book_id>', views.delete, name='delete'),
    path('about_admin', views.about_admin),
    path('cnf_order',views.cnf_order),
    path('search',views.search),
]
