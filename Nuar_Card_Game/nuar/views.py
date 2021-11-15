from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render

from .models import CharacterCard

def index(request):
    character_card_list = CharacterCard.objects.select_related(
        "mane"
    ).prefetch_related(
        "id"
    ).distinct()

    paginator = Paginator(character_card_list, settings.PAGINATION_PAGE_SIZE)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    return render(request, "index.html", {
        "paginator": paginator,
        "page": page,
        "character_card_list": character_card_list,
    }
                  )