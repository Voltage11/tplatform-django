from django import forms


class ThemeCreateForm(forms.Form):
    name = forms.CharField(
        label="Наименование",
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите название..."}
        ),
    )
    comment = forms.CharField(
        label="Описание",
        required=False,
        widget=forms.Textarea(
            attrs={"rows": 4, "class": "form-control", "placeholder": "Описание..."}
        ),
    )
    is_active = forms.BooleanField(
        label="Активна",
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
    date_from = forms.DateField(
        label="Дата начала",
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    date_to = forms.DateField(
        label="Дата окончания",
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    points = forms.IntegerField(
        label="Максимально возможное количество баллов",
        required=False,
        initial=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "type": "number", "disabled": True}
        ),
    )
    check_points = forms.IntegerField(
        label="Количество баллов для зачета",
        required=False,
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "type": "number"}),
    )


class ThemeUpdateForm(forms.Form): ...
