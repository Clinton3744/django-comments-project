from django import forms
from commandapp.models import Details

class DetailsForm(forms.ModelForm):

    class Meta:

        model=Details
        
        fields='__all__'