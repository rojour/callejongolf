from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from .models import Player, Sponsor
from .forms import PlayerForm, SponsorForm
from django.forms.formsets import formset_factory
from django.contrib.auth.decorators import login_required

# -- PLAYER VIEWS--
@login_required
def players_list(request):
    players = Player.objects.order_by('last_name', 'sponsor')
    return render(request, 'players/players_list.html', {'players': players})
    
@login_required
def players_pay_status(request):
    players = Player.objects.order_by('pay_status', 'sponsor', 'last_name')
    return render(request, 'players/players_pay_status.html', {'players': players})

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'players/player_detail.html', {'player': player})
    
def player_new(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.author = request.user
            player.save()
            return redirect('register.views.player_detail', pk=player.pk)
    else:
        form = PlayerForm()
    return render(request, 'players/player_edit.html', {'form': form})
    
@login_required
def player_remove(request, pk):
    player = get_object_or_404(Player, pk=pk)
    player.delete()
    return redirect('register.views.players_list')

def player_edit(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save(commit=False)
            player.author = request.user
            player.save()
            return redirect('register.views.player_detail', pk=player.pk)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'players/player_edit.html', {'form': form})
    
    
# -- SPONSOR VIEWS--
def sponsor_list(request):
    sponsors = Sponsor.objects.order_by('sponsor_name')
    return render(request, 'sponsors/sponsor_list.html', {'sponsors': sponsors})

def sponsor_detail(request, pk):
    sponsor = get_object_or_404(Sponsor, pk=pk)
    return render(request, 'sponsors/sponsor_detail.html', {'sponsor': sponsor})

def sponsor_new(request):
    if request.method == "POST":
        form = SponsorForm(request.POST)
        if form.is_valid():
            sponsor = form.save(commit=False)
            sponsor.author = request.user
            sponsor.save()
            return redirect('register.views.sponsor_detail', pk=sponsor.pk)
    else:
        form = SponsorForm()
    return render(request, 'sponsors/sponsor_edit.html', {'form': form})
    
@login_required
def sponsor_remove(request, pk):
    sponsor = get_object_or_404(Sponsor, pk=pk)
    sponsor.delete()
    return redirect('register.views.sponsor_list')

def sponsor_edit(request, pk):
    sponsor = get_object_or_404(Sponsor, pk=pk)
    if request.method == "POST":
        form = SponsorForm(request.POST, instance=sponsor)
        if form.is_valid():
            sponsor = form.save(commit=False)
            sponsor.author = request.user
            sponsor.save()
            return redirect('register.views.sponsor_detail', pk=sponsor.pk)
    else:
        form = SponsorForm(instance=sponsor)
    return render(request, 'sponsors/sponsor_edit.html', {'form': form})

def sponsor_bronze(request):
    if request.method == "POST":
        form = SponsorForm(request.POST)
        if form.is_valid():
            sponsor = form.save(commit=False)
            sponsor.sponsor_type = 'Bronze'
            sponsor.author = request.user
            sponsor.save()
            return redirect('register.views.sponsor_detail', pk=sponsor.pk)
    else:
        form = SponsorForm()
    return render(request, 'sponsors/sponsor_edit.html', {'form': form})

def sponsor_silver(request):
    if request.method == "POST":
        form = SponsorForm(request.POST)
        if form.is_valid():
            sponsor = form.save(commit=False)
            sponsor.sponsor_type = 'Silver'
            sponsor.author = request.user
            sponsor.save()
            return redirect('register.views.sponsor_detail', pk=sponsor.pk)
    else:
        form = SponsorForm()
    return render(request, 'sponsors/sponsor_edit.html', {'form': form})

def sponsor_gold(request):
    PlayerFormSet = formset_factory(PlayerForm, extra=2)
    if request.method == "POST":
        form = SponsorForm(request.POST, request.FILES, prefix='sponsor')
        player_formset = PlayerFormSet(request.POST, request.FILES, prefix='players')
        if form.is_valid() and player_formset.is_valid():
            sponsor = form.save(commit=False)
            sponsor.sponsor_type = 'Gold'
            sponsor.author = request.user
            name = sponsor
            sponsor.save()
            for playerform in player_formset:
                player = playerform.save(commit=False)
                player.sponsor = name
                player.pay_status = 'G sponsor'
                player.author = request.user
                player.save()
            return render(request, 'players/player_detail.html', {'player': player})
    else:
        form = SponsorForm(prefix='sponsor')
        player_formset = PlayerFormSet(prefix='players')
    return render(request, 'sponsors/sponsor_players.html', {'form': form, 'player_formset': player_formset})

def sponsor_platinum(request):
    PlayerFormSet = formset_factory(PlayerForm, extra=4)
    if request.method == "POST":
        form = SponsorForm(request.POST, request.FILES, prefix='sponsor')
        player_formset = PlayerFormSet(request.POST, request.FILES, prefix='players')
        if form.is_valid() and player_formset.is_valid():
            sponsor = form.save(commit=False)
            sponsor.sponsor_type = 'Platinum'
            sponsor.author = request.user
            name = sponsor
            sponsor.save()
            for playerform in player_formset:
                player = playerform.save(commit=False)
                player.sponsor = name
                player.pay_status = 'P sponsor'
                player.author = request.user
                player.save()
            return render(request, 'players/player_detail.html', {'player': player})
    else:
        form = SponsorForm(prefix='sponsor')
        player_formset = PlayerFormSet(prefix='players')
    return render(request, 'sponsors/sponsor_players.html', {'form': form, 'player_formset': player_formset})
