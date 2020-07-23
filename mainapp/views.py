from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import get_template

from mainapp.forms import ContactForm


def index(request):
    return render(request,'mainapp/base.html')


def newsletter(request):
    return render(request,'mainapp/newsletter.html')


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'name'
                , '')
            contact_email = request.POST.get(
                'email'
                , '')
            form_content = request.POST.get('message', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" + '',
            ['youremail@gmail.com'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('contact')

    return render(request, 'mainapp/contact.html', {
        'form': form_class,
    })