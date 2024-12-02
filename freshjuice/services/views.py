from django.shortcuts import render


def services(request):
    template_name ='services/services.html'
    return render(request, template_name)


def small_business(request):
    template_name='services/index.html'
    return render(request, template_name)


def services_card(request):
    template_name='services/services_card.html'
    return render(request, template_name)