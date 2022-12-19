from django import forms


class ImageForm(forms.Form):
    image = forms.ImageField(required=True)
    description = forms.CharField(max_length=256, label='What is this image about?')
