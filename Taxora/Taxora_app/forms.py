from django import forms

class SignUpForm(forms.Form):
    ROLE_CHOICES = [
        ('SME', 'Small Business Owner'),
        ('CA', 'Chartered Accountant'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'hidden'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'your@email.com', 'class': 'w-full p-3 border rounded-xl'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Create a strong password', 'class': 'w-full p-3 border rounded-xl'}))

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300',
        'placeholder': 'your@email.com'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300',
        'placeholder': 'Enter your password'
    }))

