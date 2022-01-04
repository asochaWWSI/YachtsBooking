from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('yachts/<int:yacht_id>', views.booking, name="booking"),
    path('yachts/make_booking', views.make_booking, name="make_booking"),
    path('yachts/bookings/<int:booking_id>', views.show_booking, name="show_booking")
]