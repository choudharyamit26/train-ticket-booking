from django import forms

class BookingForm(forms.Form):
    train_number = forms.CharField()
    source = forms.CharField()
    destination = forms.CharField()
    journey_date = forms.DateField()
    pnr = forms.CharField()