from django import forms


class DateRangeForm(forms.Form):
    date_from = forms.DateField(label='Begin date')
    date_to = forms.DateField(label='End date')
