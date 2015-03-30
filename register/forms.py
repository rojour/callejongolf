from django import forms

from .models import Player, Sponsor

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'shirt', 'email', 'phone', 'comments',)
        
        
class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ('cont_first_name', 'cont_last_name', 'cont_email', 'cont_phone', 'cont_comments', 'sponsor_name', 'sponsor_type',)