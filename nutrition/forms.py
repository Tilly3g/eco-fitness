from crispy_forms.helper import FormHelper


def __init__(self, *args, **kwargs):
    self.helper = FormHelper()
    Fieldset(
        [...]
        Field('date_start', css_class='input-small', readonly='readonly',
              id="date_start", template='nutrition/nutrition.html'),
        Field('date_end', id='date_end', css_class='input-small',
              readonly='readonly', template='nutrition/nutrition.html'),
    )
