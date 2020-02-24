from django import forms


from apps.operations.models import UserFavourite

class UserFavForm(forms.ModelForm):
    class Meta:
        model=UserFavourite
        fields=["fav_id","fav_type"]