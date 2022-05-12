from django.urls import path
from .views import loginUser, index


urlpatterns = [
    path('', loginUser, name='login'),
    path('index/', index, name='index'),

]

