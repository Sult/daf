from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from apps.characters.decorators import valid_character_selected
from apps.characters.models import CharacterApi

import apps.charts.charts as charts


@login_required
@valid_character_selected
def wallet_balance_chart(request, chart_type):
    try:
        character = CharacterApi.objects.get(pk=request.session['charpk'])
    except CharacterApi.DoesNotExist:
        return None
    if not character.api.access_to("WalletJournal"):
        return None

    if chart_type == "monthly_balance":
        #return JsonResponse(charts.monthly_balance(character))
        return JsonResponse(charts.monthly_balance(character))
