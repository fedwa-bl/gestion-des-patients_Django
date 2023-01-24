from django import forms
class SearchForm(forms.Form):
    mcle=forms.CharField()
    hidden_input=forms.CharField(widget=forms.HiddenInput,initial="Hidden value")