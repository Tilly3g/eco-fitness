
from django import forms
from .models import Session, Expert, SessionTypes


class SessionUpdate(forms.ModelForm):

    class Meta:
        model = Session
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        experts = Expert.objects.all()
        session_types = SessionTypes.objects.all()
        friendly_names = [(expert.id, expert.get_friendly_name()) for expert in experts]
        session_names = [(sesh.id, sesh.name) for sesh in session_types]

        self.fields['Expert'].choices = friendly_names
        self.fields['name'].choices = session_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
