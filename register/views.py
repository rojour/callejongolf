from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Player
from .forms import PlayerForm


def players_list(request):
    players = Player.objects.filter(created_date__lte=timezone.now()).order_by('last_name')
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
    
