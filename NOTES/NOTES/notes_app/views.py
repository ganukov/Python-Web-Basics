from NOTES.notes_app.forms import ProfileForm, NoteForm, NoteDeleteForm
from NOTES.notes_app.models import Profile, Note
from django.shortcuts import render, redirect


def find_profile():
    try:
        profile = Profile.objects.get()
        return profile
    except Profile.DoesNotExist:
        return None


def home_page(request):
    profile = find_profile()
    form = ProfileForm()
    if not profile:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')
            context = {'form': form}
            return render(request, 'home-no-profile.html', context)

        context = {'form': form}
        return render(request, 'home-no-profile.html', context)
    context = {'notes': Note.objects.all(), 'profile': profile}
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    profile = Profile.objects.first()
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {'form': form, 'profile': profile}
        return render(request, 'note-create.html', context)
    context = {'form': form, 'profile': profile}
    return render(request, 'note-create.html', context)


def edit_note(request, note_id):
    note = Note.objects.get(id=note_id)
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {'form': form, 'profile': profile}
        return render(request, 'note-edit.html', context)
    context = {'form': NoteForm(initial=note.__dict__), 'profile': profile}
    return render(request, 'note-edit.html', context)


def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    profile = Profile.objects.first()
    if request.method == 'POST':
        note.delete()
        return redirect('home page')
    form = NoteDeleteForm(instance=note)
    context = {'form': form, 'profile': profile}
    return render(request, 'note-delete.html', context)


def details_note(request, note_id):
    note = Note.objects.get(id=note_id)
    profile = Profile.objects.first()
    context = {'note': note, 'profile': profile}
    return render(request, 'note-details.html', context)


def profile_page(request):
    profile = Profile.objects.first()
    all_notes = len(Note.objects.all())
    if request.method == 'POST':
        profile.delete()
        Note.objects.all().delete()
        return redirect('home page')
    context = {'profile': profile, 'all_notes': all_notes}
    return render(request, 'profile.html', context)


def delete_button(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        profile.delete()
        Note.objects.all().delete()
        return redirect('home page')
