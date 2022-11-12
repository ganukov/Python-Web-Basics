from Car_collection_app.car_app.forms import ProfileForm, CarForm, ProfileEdit
from Car_collection_app.car_app.models import Profile, Car
from django.shortcuts import render, redirect


def find_profile():
    try:
        profile = Profile.objects.get()
        return profile
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = find_profile()
    context = {'profile': profile}
    return render(request, 'index.html')


def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')
        context = {'form': form}
        return render(request, 'profile-create.html', context)
    form = ProfileForm()
    context = {'form': form}
    return render(request, 'profile-create.html', context)


def catalogue(request):
    profile = find_profile()
    if profile:
        cars = Car.objects.all()
        all_cars = len(Car.objects.all())
        context = {'profile': profile, 'cars': cars, 'all_cars': all_cars}
        return render(request, 'catalogue.html', context)
    else:
        return redirect('index page')


def car_create(request):
    profile = find_profile()
    if profile:
        if request.method == 'POST':
            form = CarForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('catalogue page')
            context = {'form': form, 'profile': profile}
            return render(request, 'car-create.html', context)
        form = CarForm()
        context = {'form': form, 'profile': profile}
        return render(request, 'car-create.html', context)
    else:
        return redirect('index page')


def car_details(request, car_id):
    profile = find_profile()
    car = Car.objects.get(id=car_id)
    car_price = f'{car.price:.3f}'
    context = {'car': car, 'profile': profile, 'car_price': car_price}
    return render(request, 'car-details.html', context)


def car_edit(request, car_id):
    profile = find_profile()
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')
        context = {'form': form, 'profile': profile}
        return render(request, 'car-edit.html', context)
    context = {'profile': profile,
               'form': CarForm(initial=car.__dict__)}
    return render(request, 'car-edit.html', context)


def car_delete(request, car_id):
    profile = find_profile()
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('catalogue page')
    form = CarForm(instance=car)
    context = {'form': form, 'profile': profile}
    return render(request, 'car-delete.html', context)


def profile_details(request):
    profile = find_profile()
    if profile:  # making sure it cannot be hardcoded
        total_price = f"{sum([car.price for car in Car.objects.all()]):.3f}"
        context = {'profile': profile, 'total_price': total_price}
        return render(request, 'profile-details.html', context)
    else:
        return redirect('index page')


def profile_edit(request):
    profile = find_profile()
    if profile:  # making sure it cannot be hardcoded
        if request.method == 'POST':
            form = ProfileEdit(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile details page')
            context = {'form': form, 'profile': profile}
            return render(request, 'profile-edit.html', context)
        context = {'form': ProfileEdit(initial=profile.__dict__), 'profile': profile}
        return render(request, 'profile-edit.html', context)
    return redirect('index page')


def profile_delete(request):
    profile = find_profile()
    if profile:  # making sure it cannot be hardcoded
        if request.method == 'POST':
            profile.delete()
            Car.objects.all().delete()
            return redirect('index page')
        context = {'profile': profile}
        return render(request, 'profile-delete.html', context)
    return redirect('index page')
