from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User

class SignUpForm(UserCreationForm):
   
   # here is the important part.. add a class Meta-
   class Meta:
      model = User #this is the "YourCustomUser" that you imported at the top of the file  
      widgets = {
            'birth_date': forms.DateInput(format=('%d-%m-%Y'), 
                                             attrs={'class':'myDateClass', 
                                            'placeholder':'Select a date', 'type':'date'})
        }

      fields = ('username', 'password1', 'password2', 'birth_date', 'location', 'perfil_photo')

