
from django import forms
from .models import Session, Expert


class SessionUpdate(forms.ModelForm):

    class Meta:
        model = Session
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        experts = Expert.objects.all()
        friendly_names = [(expert.id, expert.get_friendly_name()) for expert in experts]

        self.fields['expert'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
