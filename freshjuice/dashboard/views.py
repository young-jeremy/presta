from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def colors(request):
    template_name='dashboard/utilities-color.html'
    return render(request, template_name)


def borders(request):
    template_name='dashboard/utilities-border.html'
    return render(request, template_name)


def animations(request):
    template_name='dashboard/utilities-animation.html'
    return render(request, template_name)


def all_alerts(request):
    template_name='dashboard/all_alerts'
    return render(request, template_name)


def other(request):
    template_name='dashboard/utilities-other.html'
    return render(request, template_name)


def blank(request):
    template_name = 'dashboard/blank.html'
    return render(request, template_name)


def messages(request):
    template_name ='dashboard/messages.html'
    return render(request, template_name)


def buttons(request):
    template_name='dashboard/buttons.html'
    return render(request, template_name)


def cards(request):
    template_name='dashboard/cards.html'
    return render(request, template_name)

@login_required
def dashboard(request):
    template_name = 'dashboard/index.html'
    return render(request, template_name)

def forgot_password(request):
    template_name = 'dashboard/forgot-password.html'
    return render(request, template_name)


def charts(request):
    template_name = 'dashboard/charts.html'
    return render(request, template_name)

def tables(request):
    template_name = 'dashboard/tables.html'
    return render(request, template_name)

def register(request):
    template_name = 'dashboard/register.html'
    return render(request, template_name)


def index(request):
    template_name = 'dashboard/base_dashboard.html'
    return render(request, template_name)


def login(request):
    template_name = 'dashboard/login.html'
    return render(request, template_name)


def utilities_animation(request):
    template_name = 'dashboard/utilities-animation.html'
    return render(request, template_name)


def utilities_border(request):
    template_name = 'dashboard/utilities-border.html'
    return render(request, template_name)


def utilities_color(request):
    template_name = 'dashboard/utilities-color.html'
    return render(request, template_name)


def utilities_other(request):
    template_name = 'dashboard/utilities-other.html'
    return render(request, template_name)


def error_404(request):
    template_name = 'dashboard/404.html'
    return render(request, template_name)


