from django import forms


class PostCreateForm(forms.Form):
    photo = forms.ImageField()
    # text = forms.CharField(max_length=500)

class PostModifyForm(forms.Form):
    photo = forms.ImageField()
