from django import forms


class UserForms(forms.Form):
    # name = forms.CharField(label='name', error_messages={'required': 'Error not name'})
    # age = forms.IntegerField(label='age')
    # basket = forms.BooleanField(label='polojit tovar v korzinu', required=False)
    # vyb = forms.NullBooleanField(label='tut vopros')
    story = forms.ChoiceField(
        label='Available categories',
        choices=[
            ('1', 'Ask'),
            ('2', 'Job'),
            ('3', 'Show'),
            ('4', 'New'),
        ],
        help_text='Choose a category'
    )
    required_css_class = 'field'
    error_css_class = 'error'


