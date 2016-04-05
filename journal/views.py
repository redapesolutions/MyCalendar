from django.shortcuts import render, get_object_or_404, redirect
from .forms import PlansForm, UpdateForm
from .models import Plans
from django.contrib import messages

def welcomeview(request):
	return render(request, "journal/Home.html")

def journalview(request):
	form = PlansForm(request.POST or None)
	allplans = Plans.objects.all().order_by("date")
	context = {"plan_list":allplans}
	return render(request, "journal/Alldays.html", context)
	
def detailview(request, pk):
	oneplan = get_object_or_404(Plans, pk=pk)
	context = {"plan":oneplan}
	return render(request, "journal/Details.html", context)

def createview(request):
	form = PlansForm(request.POST or None)
	context = {
		"title": "Make a new plan",
		"form": form,
	}
	if form.is_valid():
		cleaned = form.cleaned_data						#pobiera informacje wpisane do formularza
		if Plans.objects.filter(date=cleaned["date"]):	#filtruje baze odnoszac sie do pola date i porownuje do "date" z formularzza
			messages.success(request, "Plan with this date already exists, You can edit it")
			return redirect("journal:journallist") 
		else:
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, "Plan added!")
		return redirect("journal:journallist") 
	return render(request, "journal/create.html", context)

def deleteview(request, pk):
	oneplan = get_object_or_404(Plans, pk=pk)
	oneplan.delete()
	messages.success(request, "Plan deleted!")
	return redirect("journal:journallist")
				
def updateview(request, pk):
	oneplan = get_object_or_404(Plans, pk=pk)
	form = UpdateForm(request.POST or None, instance = oneplan)
	context = {
		"title": "Update a plan",
		"date": oneplan,
		"form": form,
		"instance": oneplan
	}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Plan eddited!")
		return redirect("journal:journallist") 
	return render(request, "journal/create.html", context)