from django import forms


class DateForm(forms.Form):
    date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datepicker-input',
            'data-target': '#datepicker1'
        })
    )
