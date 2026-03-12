from django import forms
from app.core.models import Theme


class ThemeCreateForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = [
            "name",
            "comment",
            "is_active",
            "date_from",
            "date_to",
            "points",
            "check_points",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите название..."}
            ),
            "comment": forms.Textarea(
                attrs={"rows": 4, "class": "form-control", "placeholder": "Описание..."}
            ),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "date_from": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "date_to": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "points": forms.NumberInput(
                attrs={"class": "form-control", "readonly": True}
            ),
            "check_points": forms.NumberInput(attrs={"class": "form-control"}),
        }


class ThemeUpdateForm(ThemeCreateForm):
    author_info = forms.CharField(
        label="Автор темы",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "disabled": True}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            user = self.instance.user
            self.fields["author_info"].initial = user.get_full_name() or user.username

        self.order_fields(["author_info"] + self.Meta.fields)
