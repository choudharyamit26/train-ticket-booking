from django.urls import path

from core.views import book_ticket, pnr_status, cancel_booking, train_search, ticket_confirmation, my_bookings

app_name = 'core'

urlpatterns = [
    path('booking/<str:train_number>/', book_ticket, name='booking'),
    path('pnr/<str:pnr>/', pnr_status, name='pnr_status'),
    path('booking/<int:booking_id>/cancel/',
         cancel_booking, name='cancel_booking'),
    path('train/search/', train_search, name='train_search'),
    path('train/book/<str:train_number>/', book_ticket, name='book_ticket'),
    path('ticket/confirmation/<int:ticket_id>/',
         ticket_confirmation, name='ticket_confirmation'),
    path('my-bookings/', my_bookings, name='my_bookings'),

]
