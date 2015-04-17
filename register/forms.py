from django import forms


from .models import Player, Sponsor
from django.forms.formsets import formset_factory

SHIRT_CHOICES = (('XS','XS'), ('S','S'), ('M','M'), ('L','L'), ('XL','XL'), ('XXL','XXL'))
GENDER_CHOICES = (('F', 'F'), ('M','M'))

class PlayerForm(forms.ModelForm):
    shirt = forms.ChoiceField(widget=forms.RadioSelect(), choices=SHIRT_CHOICES)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES, label='gender, in case the shirt is not for you')
    class Meta:
        model = Player
        fields = ('first_name', 'last_name',  'email', 'phone', 'comments', 'shirt', 'gender',)
        labels = {
            'first_name': ('First Name'),
            'last_name': ('Last Name'),
            }
        help_text = {
            'cont_phone': ('please use the form ###-###-####'),
            }
        Player.shirt = forms.ChoiceField(widget=forms.RadioSelect(), choices=SHIRT_CHOICES)
        Player.gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES, label='gender, in case the shirt is not for you')
            
        
class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ( 'sponsor_name', 'cont_first_name', 'cont_last_name', 'cont_email', 'cont_phone', 'cont_comments')
        labels = {
            'sponsor_name': ('Company Name'),
            'cont_first_name': ('Contact Person First Name'),
            'cont_last_name': ('Contact Person Last Name'),
            'cont_email': ('email'),
            'cont_phone': ('phone'),
            'cont_comments': ('comments'),
            }
        help_text = {
            'cont_phone': ('please use the form ###-###-####'),
            }


