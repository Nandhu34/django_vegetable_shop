from django import forms 



class login_form(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'username','id':'username','name':'username'}))
    password = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'password','id':'password','name':'password'}))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    mobile_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password'}))
    confirm_password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'id': 'confirm_password'}))

    # Add eye buttons for password fields
    password.widget.attrs['autocomplete'] = 'new-password'  # Disable autocomplete
    confirm_password.widget.attrs['autocomplete'] = 'new-password'  # Disable autocomplete

    # JavaScript code to toggle password visibility
    password.widget.attrs['onchange'] = 'togglePasswordVisibility("password")'
    confirm_password.widget.attrs['onchange'] = 'togglePasswordVisibility("confirm_password")'