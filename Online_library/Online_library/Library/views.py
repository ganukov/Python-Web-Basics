from Online_library.Library.forms import ProfileForm, BookForm, ProfileDeleteForm
from Online_library.Library.models import Profile, Book
from django.shortcuts import render, redirect


def find_profile():
    try:
        profile = Profile.objects.get()
        return profile
    except Profile.DoesNotExist:
        return None


def home_page(request):
    profile = find_profile()
    if not profile:
        form = ProfileForm()
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')
            context = {'form': form}
            return render(request, 'home-no-profile.html', context)
        context = {'form': form}
        return render(request, 'home-no-profile.html', context)
    else:
        books = Book.objects.all()
        context = {'profile': profile, 'books': books}
        return render(request, 'home-with-profile.html', context)


def add_book(request):
    profile = Profile.objects.first()
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {'form': form, 'profile': profile}
        return render(request, 'add-book.html', context)
    context = {'form': form, 'profile': profile}
    return render(request, 'add-book.html', context)


def edit_book(request, book_id):
    profile = Profile.objects.get()
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {'form': form, 'profile': profile}
        return render(request, 'edit-book.html', context)
    context = {'form': BookForm(initial=book.__dict__), 'profile': profile}
    return render(request, 'edit-book.html', context)


def delete_book(request, book_id):
    if request.method == 'GET':
        book = Book.objects.get(id=book_id)
        book.delete()
        return redirect('home page')


def details_book(request, book_id):
    profile = Profile.objects.get()
    book = Book.objects.get(id=book_id)
    context = {'book': book, 'profile': profile}
    return render(request, 'book-details.html', context)


def profile_details(request):
    profile = Profile.objects.get()
    context = {'profile': profile}
    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = Profile.objects.get()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {'form': form, 'profile': profile}
        return render(request, 'edit-profile.html', context)
    context = {'form': ProfileForm(initial=profile.__dict__),
               'profile': profile}
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.get()
    if request.method == 'POST':
        profile.delete()
        return redirect('home page')
    form = ProfileDeleteForm(instance=profile)
    context = {'form': form, 'profile': profile}
    return render(request, 'delete-profile.html', context)
