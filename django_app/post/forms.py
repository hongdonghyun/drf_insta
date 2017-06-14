from django import forms


class PostCreateForm(forms.Form):
    photo = forms.ImageField()
    content = forms.CharField(max_length=500,required=False)
    # text = forms.CharField(max_length=500)

class PostModifyForm(forms.Form):
    photo = forms.ImageField()
    content = forms.CharField(max_length=500,required=False)
