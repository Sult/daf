from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .decorators import valid_character_selected
from .forms import FilterJournalForm
from apps.apies.forms import ApiForm
from apps.characters.models import CharacterApi, CharacterJournal


@login_required
def characters(request):
    api_form = ApiForm(request.POST or None, user=request.user)

    if request.POST and api_form.is_valid():
        api_form.save(request.user)
        api_form = ApiForm(user=request.user)

    characters = CharacterApi.objects.filter(api__user=request.user)
    if request.user.groups.filter(
        name="moderator"
    ).exists() or request.user.is_superuser:

        members = CharacterApi.objects.exclude(api__user=request.user)
        return render(
            request,
            "characters/characters.html",
            {
                "api_form": api_form,
                "characters": characters,
                "members": members
            }
        )

    return render(
        request,
        "characters/characters.html",
        {
            "api_form": api_form,
            "characters": characters
        }
    )


@login_required
def select_character(request, pk):
    if request.user.groups.filter(
        name="moderator"
    ).exists() or request.user.is_superuser:
        character = get_object_or_404(CharacterApi, pk=pk)
        request.session['moderator'] = True
    else:
        character = get_object_or_404(
            CharacterApi,
            pk=pk,
            api__user=request.user
        )
        request.session['moderator'] = False
    request.session['charpk'] = character.pk
    request.session['access'] = character.api.access()
    return HttpResponseRedirect(reverse("character_sheet"))


@login_required
@valid_character_selected
def character_sheet(request):
    character = get_object_or_404(CharacterApi, pk=request.session['charpk'])

    sheet, employment = character.character_sheet()
    account = character.api.account_status()
    in_training = character.skill_in_training()

    return render(
        request,
        "characters/character_sheet.html",
        {
            "character": character,
            "employment": employment,
            "in_training": in_training,
            "sheet": sheet,
            "account": account,
        }
    )


@login_required
@valid_character_selected
def character_skills(request):
    character = get_object_or_404(CharacterApi, pk=request.session['charpk'])
    if not character.api.access_to("CharacterSheet"):
        return HttpResponseRedirect(reverse("characters"))
    skills = character.trained_skills()
    queue = character.skill_queue()
    return render(
        request,
        "characters/character_skills.html",
        {
            "character": character,
            "skills": skills,
            "queue": queue,
        }
    )


@login_required
@valid_character_selected
def character_journal(request):
    character = get_object_or_404(CharacterApi, pk=request.session['charpk'])
    if not character.api.access_to("WalletJournal"):
        return HttpResponseRedirect(reverse("characters"))

    all_transactions = character.wallet_journal()
    filter_form = FilterJournalForm(
        request.POST or None, characterapi=character
    )

    paginator = Paginator(
        all_transactions,
        50, request=request
    )
    page = request.GET.get('page', 1)
    try:
        transactions = paginator.page(page)
    except PageNotAnInteger:
        transactions = paginator.page(1)
    except EmptyPage:
        transactions = paginator.page(paginator.num_pages)

    chart_list = CharacterJournal.monthly_balance(character)

    return render(
        request,
        "characters/wallet_journal.html",
        {
            "character": character,
            "transactions": transactions,
            "chart_list": chart_list,
            "filter_form": filter_form,
        }
    )
