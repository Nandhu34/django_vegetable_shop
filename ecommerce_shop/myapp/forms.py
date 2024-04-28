from django import forms 



class login_form(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'username','id':'username','name':'username'}))
    password = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'password','id':'password','name':'password'}))