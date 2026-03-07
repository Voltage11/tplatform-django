from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db.models import BooleanField, Case, Q, Value, When
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_http_methods

from app.core.forms.theme import ThemeCreateForm
from app.core.models import Theme


@login_required
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["GET"])
def get_theme_list(request):
    """Получение списка тем"""
    now = timezone.now()

    themes = Theme.objects.select_related("user").annotate(
        is_available_db=Case(
            When(
                Q(is_active=True)
                & (Q(date_from__isnull=True) | Q(date_from__lte=now))
                & (Q(date_to__isnull=True) | Q(date_to__gte=now)),
                then=Value(True),
            ),
            default=Value(False),
            output_field=BooleanField(),
        )
    )

    if (active := request.GET.get("is_active")) in ["true", "false"]:
        themes = themes.filter(is_active=(active == "true"))

    if q := request.GET.get("q"):
        themes = themes.filter(name__icontains=q)

    themes = themes.order_by("-created_at")

    # Пагинация: 30 записей на страницу
    paginator = Paginator(themes, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "core/theme/list.html", {"page_obj": page_obj})


@login_required
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["GET", "POST"])
def create_theme(request):
    """Создание темы"""
    if request.method == "POST":
        form = ThemeCreateForm(request.POST)
        if form.is_valid():
            Theme.objects.create(
                name=form.cleaned_data["name"],
                comment=form.cleaned_data["comment"],
                is_active=form.cleaned_data["is_active"],
                date_from=form.cleaned_data["date_from"],
                date_to=form.cleaned_data["date_to"],
                user=request.user,
            )
            return redirect("core:theme_list")
    else:
        form = ThemeCreateForm()

    return render(request, "core/theme/create.html", {"form": form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["GET", "POST"])
def edit_theme(request, pk: int): ...
