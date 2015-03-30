from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Player, Sponsor
from .forms import PlayerForm, SponsorForm


def players_list(request):
    players = Player.objects.order_by('group_play')
    return render(request, 'players/players_list.html', {'players': players})
    
    
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
