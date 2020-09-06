from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.contrib import messages

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	my_form = CarForm()
	if request.method == "POST":
		my_form = CarForm(request.POST, request.FILES)
		if my_form.is_valid():
			my_form.save()
			messages.info(request, 'Added successfully')
			return redirect('car-list')
	
	context = {
        "form": my_form
    }
	return render(request, 'create.html', context)


def car_update(request, car_id):
	my_obj = Car.objects.get(id=car_id)
	my_form = CarForm(instance=my_obj)
	if request.method == "POST":
		my_form = CarForm(request.POST, request.FILES, instance=my_obj)
		if my_form.is_valid():
			my_form.save()
			messages.info(request, 'updated successfully')
			return redirect('car-list')
	context = {
        "form": my_form,
        "car":my_obj,
    }
	return render(request, 'update.html', context)


def car_delete(request, car_id):
	#Complete Me
	Car.objects.get(id=car_id).delete()
	messages.info(request, 'Deleted successfully')
	return redirect('car-list')