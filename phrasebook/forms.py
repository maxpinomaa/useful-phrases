from django import forms

from .models import Convcon


class PostForm(forms.ModelForm):


    class Meta:
        model = Convcon
        fields = ('connector','contransl',)