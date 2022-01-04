from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.urls import reverse

from .models import Booking, Customer, Yacht
from .forms import BookingForm

# Create your views here.
def index(request):
    all_yachts = Yacht.objects.all()
    context = {
        'all_yachts': all_yachts,
    }
    return render(request, 'YachtsApp/index.html', context)

def booking(request, yacht_id):
    yacht = Yacht.objects.get(pk=yacht_id)
    context = {
        'yacht': yacht
    }
    return render(request, 'YachtsApp/booking.html', context)

def make_booking(request: HttpRequest):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            yacht = Yacht.objects.get(pk=form_data['yacht_id'])
            (customer, _) = Customer.objects.get_or_create(email=form_data['customer_email'],
                                                           name=form_data['customer_name'],
                                                           surname=form_data['customer_surname'],
                                                           telephone=form_data['customer_phone'])
            duration = form_data['booking_end'] - form_data['booking_start']
            final_price = duration.days * yacht.price
            new_booking = Booking.objects.create(date_lend=form_data['booking_start'],
                                                 date_return=form_data['booking_end'],
                                                 final_price=final_price,
                                                 customer=customer,
                                                 yachts=yacht)
            new_booking.save()
            return HttpResponseRedirect(reverse('show_booking', args=[new_booking.id]))
        else:
            s = ""
            for i in request.POST.items():
                s += str(i) + "<br/>"
            return HttpResponse(f"nieprawidłowe dane: {s}")
    else:
        return HttpResponse(f"nieprawidłowa metoda: {request.method}")


def show_booking(request: HttpRequest, booking_id: int):
    booking = Booking.objects.get(pk=booking_id)
    context = {
        'booking': booking
    }
    return render(request, 'YachtsApp/show_booking.html', context)