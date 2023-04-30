from django import forms

class MyForm(forms.Form):
    my_choices = (
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    )
    my_dropdown = forms.ChoiceField(choices=my_choices, widget=forms.Select(attrs={'class': 'dropdown-menu'}))
