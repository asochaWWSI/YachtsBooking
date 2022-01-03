from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('yachts/<int:yacht_id>', views.booking, name="booking"),
]