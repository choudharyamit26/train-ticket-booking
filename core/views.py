from django.http import JsonResponse
import random
import string
from .models import Train, Ticket
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Ticket, Train
from django.contrib import messages


def get_pnr(train_number):
    random_string = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=6))
    pnr = f"{train_number}-{random_string}"
    return pnr


def pnr_status(request, pnr):
    booking = Ticket.objects.get(pnr=pnr)
    return render(request, 'pnr_status.html', {'booking': booking})


def cancel_booking(request, booking_id):
    try:
        booking = Ticket.objects.get(id=booking_id)

        if booking.status == 'Cancelled':
            message = 'Ticket has already been cancelled.'
            return JsonResponse({'success': False, 'message': message})

        # Perform cancellation logic here

        # Set the booking status to "Cancelled"
        booking.status = 'Cancelled'
        booking.save()

        message = 'Ticket has been successfully cancelled.'
        return JsonResponse({'success': True, 'message': message})

    except Ticket.DoesNotExist:
        message = 'Ticket not found.'
        return JsonResponse({'success': False, 'message': message})


def train_search(request):
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        trains = Train.objects.filter(source=source, destination=destination)
        return render(request, 'train_search_results.html', {'trains': trains})
    return render(request, 'train_search.html')


def book_ticket(request, train_number):
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        journey_date = request.POST.get('journey_date')
        journey_time = request.POST.get('journey_time')
        pnr = get_pnr(train_number=train_number)
        if Ticket.objects.filter(train_number=train_number, source=source, destination=destination, journey_date=journey_date).exists():
            messages.error(
                request, 'A ticket is already booked for the same train on the same date and time.')
            return redirect('core:train_search')

        ticket = Ticket.objects.create(
            user=request.user,
            train_number=train_number,
            source=source,
            destination=destination,
            journey_date=journey_date,
            journey_time=journey_time,
            pnr=pnr,
            status="Confirmed"
        )

        return redirect('core:ticket_confirmation', ticket_id=ticket.id)
    train = Train.objects.get(train_number=train_number)
    return render(request, 'booking.html', {'train': train, 'source': train.source, 'destination': train.destination})


def ticket_confirmation(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket_confirmation.html', {'ticket': ticket})


def my_bookings(request):
    # Retrieve all the booked tickets
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'tickets': tickets})
