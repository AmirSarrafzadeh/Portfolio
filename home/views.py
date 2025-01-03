from django.shortcuts import render
from .forms import ContactForm


def home(request):
    success_message = None  # Variable to hold the success message
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            success_message = "Your message has been sent successfully!"  # Set the success message
            form = ContactForm()  # Reset the form after successful submission
            return render(request, 'home.html', {'form': form, 'success_message': success_message, 'scroll_to': '#contact'})
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form, 'success_message': success_message})
