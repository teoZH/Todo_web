from django import forms


class TodoInput(forms.Form):
    title = forms.CharField(label='Title', max_length=20,min_length=6)
    description = forms.CharField(widget=forms.Textarea())
