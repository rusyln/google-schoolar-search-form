from django import forms

class SearchForm(forms.Form):
    person_to_search = forms.CharField(label='Person to Search', max_length=100)
