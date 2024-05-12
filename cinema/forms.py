from django import forms
from .models import Review,Score,ScoreStar


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ("text",)


class RatingForm(forms.ModelForm):

    star = forms.ModelChoiceField(
        queryset= ScoreStar.objects.all(),
        widget= forms.RadioSelect(),
        empty_label=None
    )
    
    class Meta:
        model = Score
        fields = ("film","user","star")



    