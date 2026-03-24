from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Libro
from .forms import LibroForm

def homepage(request):
    return redirect('lista_libri')

def lista_libri(request):
    tutti_i_libri = Libro.objects.all()
    return render(request, 'libri/lista.html', {'libri': tutti_i_libri})

def dettaglio_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libri/dettaglio.html', {'libro': libro})

@login_required
def aggiungi_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('lista_libri')
    else:
        form = LibroForm()

    return render(request, 'libri/form.html', {'form': form, 'azione': 'Aggiungi libro'})

@login_required
def modifica_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
        return redirect('lista_libri')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libri/form.html', {'form': form, 'azione': 'Modifica libro'})

@login_required
def elimina_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libri')
    else:
        return render(request, 'libri/conferma_elimina.html', {'libro': libro})
    



# per cambiamenti sui permessi crud etc guarda commento base.html co le opzioni e leva @login required dalla roba solo admin

# Create your views here.

#NB RICORDA HAI DISATTIVATO IL FORMATTER DI JINJA CHE SI ROMPEVA CO DJANGO

# NB2 cambiare formatter, prettier non va bene