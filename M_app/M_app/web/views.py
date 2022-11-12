from M_app.web.forms import AlbumCreateForm, CreateProfile, AlbumDeleteForm, DeleteProfile
from M_app.web.models import Profile, Album
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
            'albums': Album.objects.all(),
        }
        return render(request, 'home-with-profile.html', context)
    else:
        if request.method == 'GET':
            form = CreateProfile()
        else:
            form = CreateProfile(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')
            context = {'form': form}
            return render(request, 'home-no-profile.html', context)
        context = {
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)


def add_album(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form, 'profile': profile
    }
    return render(request, 'add-album.html', context)


def details_album(request, album_id):
    album = Album.objects.get(id=album_id)
    context = {'album': album}
    return render(request, 'album-details.html', context)


def edit_album(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {'form': form}
        return render(request, 'edit-album.html', context)
    context = {'form': AlbumCreateForm(initial=album.__dict__)}
    return render(request, 'edit-album.html', context)


def delete_album(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        album.delete()
        return redirect('home page')
    form = AlbumDeleteForm(instance=album)
    profile = find_profile()
    context = {'form': form, 'profile': profile}
    return render(request, 'delete-album.html', context)


def profile_details(request):
    all_albums = len(Album.objects.all())
    profile = find_profile()
    context = {'profile': profile, 'all_albums': all_albums}
    return render(request, 'profile-details.html', context)


def profile_deletion(request):
    if request.method == 'POST':
        profile = Profile.objects.get()
        profile.delete()
        Album.objects.all().delete()
        return redirect('home page')
    profile = Profile.objects.get()
    form = CreateProfile(initial=profile.__dict__)
    context = {'form': form}
    return render(request, 'profile-delete.html',context)
