from GamesPlay.Games.forms import ProfileForm, GameForm, GameDeleteForm, ProfileEditForm
from GamesPlay.Games.models import Profile, Game
from django.shortcuts import render, redirect


def find_profile():
    try:
        profile = Profile.objects.get()
        return profile
    except Profile.DoesNotExist:
        return None


def home_page(request):
    profile = find_profile()
    if profile:
        context = {
            'profile': profile,
            'games': Game.objects.all(),
        }
        return render(request, 'home-page.html', context)
    else:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')

        form = ProfileForm()
        context = {
            'form': form
        }
        return render(request, 'home-page.html', context)


def dashboard(request):
    profile = find_profile()
    if profile:
        games = Game.objects.all()
        context = {
            'profile': profile,
            'games': games,
        }
        return render(request, 'dashboard.html', context)
    return redirect('home page')


def game_create(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')
    form = GameForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'create-game.html', context)


def game_details(request, game_id):
    game = Game.objects.get(id=game_id)
    form = GameForm(initial=Game.__dict__)
    context = {'game': game,
               'form': form,
               }
    return render(request, 'details-game.html', context)


def game_edit(request, game_id):
    game = Game.objects.get(id=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

        context = {'form': form}
        return render(request, 'edit-game.html', context)

    context = {'form': GameForm(initial=game.__dict__)}
    return render(request, 'edit-game.html', context)


def game_delete(request, game_id):
    game = Game.objects.get(id=game_id)
    if request.method == 'POST':
        game.delete()
        return redirect('dashboard page')
    form = GameDeleteForm(instance=game)
    profile = find_profile()
    context = {'form': form, 'profile': profile}
    return render(request, 'delete-game.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileForm()
        context = {
            'form': form,
        }
        return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.get()
    games = Game.objects.all()
    total_games = len(Game.objects.all())

    try:
        rating = sum(game.rating for game in games) / total_games
    except ZeroDivisionError:
        rating = 0.0
    context = {'profile': profile, 'total_games': total_games, 'rating': rating}
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = Profile.objects.get()
    form = ProfileEditForm(initial=profile.__dict__)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile page')
        context = {'form': form}
        return render(request, 'edit-profile.html', context)
    context = {'form': form}
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.get()
    games = Game.objects.all()
    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('home page')
    return render(request, 'delete-profile.html')
