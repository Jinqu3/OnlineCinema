from django import forms
from .models import Review,Score,ScoreStar,User


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ("text",)



class RatingForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['star']
        widgets = {
            'star': forms.Select(choices=ScoreStar.STARS),
        }


