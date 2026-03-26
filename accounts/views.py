from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import FormRegistrazione

def registrazione(request):
    if request.method == 'POST':
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            nuovo_utente = form.save()
            login(request, nuovo_utente)
            return redirect('lista_libri')
    else:
        form = FormRegistrazione()
    return render(request, 'accounts/registrazione.html', {'form': form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'accounts/logout.html')