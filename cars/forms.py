from django import forms

class CarFilterForm(forms.Form):
    GEAR_CHOICES = (
        ("Robot", "Robot"),
        ("Automatic", "Automatic"),
        ("Manual", "Manual"),
        ("", "None")
    )

    model = forms.CharField(label="model", required=False)
    min_year = forms.IntegerField(label="year from", required=False)
    max_year = forms.IntegerField(label="year to", required=False)
    gear = forms.ChoiceField(choices=GEAR_CHOICES, required=False)


class CarFullFilter(forms.Form):
    search = forms.CharField(label="search", required=False, max_length=255)