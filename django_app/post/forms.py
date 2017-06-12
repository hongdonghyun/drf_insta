from django import forms

class PostCreateForm(forms.Form):
    photo = forms.ImageField()
    created_date = forms.DateTimeField(required=False)
    text = forms.CharField(max_length=500)
