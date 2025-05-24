from django.urls import path
from .views import home_page, header, footer, contact_us_page, login_page, register_page, logout_page

app_name = 'shop'
urlpatterns = [
    path('', home_page, name='home'),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('contact_us', contact_us_page, name='contact_us'),
    path('login', login_page, name='login'),
    path('logout', logout_page, name='logout'),
    path('register', register_page, name='register'),
]
