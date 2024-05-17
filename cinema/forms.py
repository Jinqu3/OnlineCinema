from django import forms
from .models import Review,ScoreStar


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ("text",)


class RatingForm(forms.Form):
    star = forms.ModelChoiceField(
        queryset=ScoreStar.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None
    )


class FavoriteForm(forms.Form):
    pass

class ViewedForm(forms.Form):
    pass
