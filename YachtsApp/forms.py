from django import forms

class BookingForm(forms.Form):
    yacht_id = forms.IntegerField()
    booking_start = forms.DateField()
    booking_end = forms.DateField()
    customer_name = forms.CharField()
    customer_surname = forms.CharField()
    customer_phone = forms.CharField()
    customer_email = forms.CharField()