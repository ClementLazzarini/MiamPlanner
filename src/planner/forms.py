from django import forms


class GeneratePlanForm(forms.Form):
    tags = forms.MultipleChoiceField(
        choices=[
            ('rapide', 'Rapide'),
            ('vegetarien', 'Végétarien'),
            ('vegan', 'Vegan'),
            ('sans_gluten', 'Sans gluten'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Tags de recettes",
    )

    # Cases à cocher pour activer/désactiver la génération de suggestion pour chaque repas
    MONDAY_LUNCH    = forms.BooleanField(required=False, initial=True, label="Lundi Midi")
    MONDAY_DINNER   = forms.BooleanField(required=False, initial=True, label="Lundi Soir")
    TUESDAY_LUNCH   = forms.BooleanField(required=False, initial=True, label="Mardi Midi")
    TUESDAY_DINNER  = forms.BooleanField(required=False, initial=True, label="Mardi Soir")
    WEDNESDAY_LUNCH = forms.BooleanField(required=False, initial=True, label="Mercredi Midi")
    WEDNESDAY_DINNER= forms.BooleanField(required=False, initial=True, label="Mercredi Soir")
    THURSDAY_LUNCH  = forms.BooleanField(required=False, initial=True, label="Jeudi Midi")
    THURSDAY_DINNER = forms.BooleanField(required=False, initial=True, label="Jeudi Soir")
    FRIDAY_LUNCH    = forms.BooleanField(required=False, initial=True, label="Vendredi Midi")
    FRIDAY_DINNER   = forms.BooleanField(required=False, initial=True, label="Vendredi Soir")
    SATURDAY_LUNCH  = forms.BooleanField(required=False, initial=True, label="Samedi Midi")
    SATURDAY_DINNER = forms.BooleanField(required=False, initial=True, label="Samedi Soir")
    SUNDAY_LUNCH    = forms.BooleanField(required=False, initial=True, label="Dimanche Midi")
    SUNDAY_DINNER   = forms.BooleanField(required=False, initial=True, label="Dimanche Soir")
