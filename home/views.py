from django.shortcuts import render
from .forms import ContactForm
from django.db import DatabaseError


def home(request):
    success_message = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                success_message = "Your message has been sent successfully!"
            except DatabaseError as e:
                success_message = f"An error occurred: {e}"
            form = ContactForm()
            return render(request, 'home.html', {'form': form, 'success_message': success_message, 'scroll_to': '#contact'})
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form, 'success_message': success_message})