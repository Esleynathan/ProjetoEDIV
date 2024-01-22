from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import RegisterForm
from django.shortcuts import redirect

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        register_form = RegisterForm()
        return render (request, 'register.html', {'register_form': register_form})
    elif request.method == "POST":
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            # TODO: Redirecionar para Login
            return HttpResponse("Salvo com sucesso!")
        else:
            return render (request, 'register.html', {'register_form': register_form})