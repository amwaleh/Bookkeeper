from django import forms


class SearchForm(forms.Form):
    '''
    Handles the search query
    '''
    CHOICES = [('title', 'title'), ('category', 'category')]
    search = forms.CharField(max_length=32)
    filter = forms.ChoiceField(label="Search by", choices=CHOICES)
