from django import forms
from app.models import Personage

class PersonageForm(forms.ModelForm):
    class Meta:
        model = Personage
        fields = '__all__'
#    name = forms.CharField()
#    clan = forms.
#    message = forms.CharField(widget=forms.Textarea)

#    def set_psw(self):
        # send email using the self.cleaned_data dictionary
#        print(self.psw)