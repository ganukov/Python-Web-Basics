from django.shortcuts import render


def add_photo(request):
    return render(request, template_name='photo-add-page.html')


def edit_photo(request):
    return render(request, template_name='photo-edit-page.html')


def show_photo_details(request):
    return render(request, template_name='photo-details-page.html')
