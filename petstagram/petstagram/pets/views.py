from django.shortcuts import render


def add_pet(request):
    return render(request, template_name='pet-add-page.html')


def show_pet_details(request):
    return render(request, template_name='pet-details-page.html')


def edit_pet(request):
    return render(request, template_name='pet-edit-page.html')


def delete_pet(request):
    return render(request, template_name='pet-details-page.html')
