from Music_app.my_app.forms import CreateProfileForm, CreateAlbumForm
from Music_app.my_app.models import Profile, Album
from django.shortcuts import render, redirect


# Create your views here.


def home_page(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
        context = {'form': form}
        return render(request, 'home-no-profile.html', context)
    form = CreateProfileForm()
    context = {'form': form}
    return render(request, 'home-no-profile.html', context)


def add_album(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = CreateAlbumForm()
        context = {'form': form, 'profile': profile}
        return render(request, 'add-album.html', context)
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
        context = {'form': form, 'profile': profile}
        return render(request, 'add-album.html', context)


def album_details(request, album_id):
    album = Album.objects.get(id=album_id)
    context = {'album': album}
    return render(request, 'album-details.html', context)


def edit_album(request, album_id):
    pass


def delete_album(request, album_id):
    pass


def profile_details(request):
    profile = Profile.objects.first()
    albums = len(Album.objects.all())
    context = {'profile': profile, 'albums': albums}
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    if request.method == 'POST':
        profile = Profile.objects.first()
        profile.delete()
        Album.objects.all().delete()
        return redirect('home-page')
    return render(request, 'profile-delete.html')
