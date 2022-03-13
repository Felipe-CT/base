
from django import forms
from datetime import date
from acceso.models import Usuario

#CIERTA_EDAD = 16

# def calculate_age(born):
#    today = date.today()
#    return (today.year - born.year) - ((today.month, today.day) < (born.month, born.day))

class UsuarioForm(forms.ModelForm):

    confirmar_password = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))

#    def clean_birthday(self):
#        birthday = self.cleaned_data['birthday']
#        edad = calculate_age(birthday)

#        if birthday > date.today():
#            raise forms.ValidationError(
#                    f"solo fechas en pasado."
#                )

#        if edad < CIERTA_EDAD:
#            raise forms.ValidationError(
#                    f"Tienes {edad} años, te esperamos cuando cumplas {CIERTA_EDAD}."
#                )
#        return birthday

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

        if cleaned_data.get('password') != cleaned_data.get('confirmar_password'):
            raise forms.ValidationError(
                    "Las contraseñas no coinciden"
                )

    class Meta:
        model = Usuario
        fields  = ['nombre','alias','email','password', 'birthday']

        labels = {
            'nombre':'Nombre: ',
            'alias':'Alias: ',
            'email':'Correo: ',
            'password':'Password: ',
            'birthday':'Birthday: ',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'alias': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type':'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type':'date', 'max':date.today().strftime('%Y-%m-%d')}),
        }
