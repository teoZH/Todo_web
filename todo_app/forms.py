from django import forms


def clean_bot_catcher(bot_catcher):
    if len(bot_catcher) > 0:
        raise forms.ValidationError('Gotcha BOT')
    return bot_catcher


class TodoInput(forms.Form):
    title = forms.CharField(label='Title', max_length=20, min_length=6)
    description = forms.CharField(widget=forms.Textarea())
    bot_catcher = forms.CharField(widget=forms.HiddenInput(), required=False, validators=[clean_bot_catcher])
