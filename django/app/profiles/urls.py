from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
#    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]