from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm


def home(request):
    return render(request, 'home.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return HttpResponseRedirect('')  # Redirect to a thank-you page
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})


