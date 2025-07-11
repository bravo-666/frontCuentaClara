from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        if user:
            login(request, user)
            if request.headers.get('Hx-Request'):
                return HttpResponse('<script>window.location.href="/dashboard/"</script>')
            return redirect('dashboard')
        else:
            form.add_error(None, 'Credenciales inválidas')

    if request.headers.get('Hx-Request'):
        return render(request, 'usuarios/partials/form_login.html', {'form': form})
    
    return render(request, 'usuarios/login.html')
def registro_view(request):
    return HttpResponse("Aquí irá el formulario de registro HTMX")
from django.contrib.auth.models import User
from .forms import RegistroForm

def registro_view(request):
    form = RegistroForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        if request.headers.get('Hx-Request'):
            return HttpResponse('<script>window.location.href="/" </script>')
        return redirect('login')

    if request.headers.get('Hx-Request'):
        return render(request, 'usuarios/partials/form_register.html', {'form': form})

    return render(request, 'usuarios/register.html')
