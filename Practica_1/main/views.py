from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from registro import forms
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import UploadedFiles

def index(request):
    return HttpResponse('este es el index')

def home(request):
    return render(request, 'registro/home.html', context=None)

def actualizar_datos(request, nom):
    #definimos contexto para actualizar datos del que ya estaba loggeado
    user = User.objects.get(username=nom)
    conte = {'email': user.email, 'nombre': user.username, 'cui': user.profile.cui}
    return render(request, 'registro/editar_datos.html', context=conte)

def profile(request, nom):
    try:
        user = User.objects.get(username=nom)
        ctx = {'nombre': user.username, 'email': user.email, 'cui': user.profile.cui, 'profesion': user.profile.profesion}
        return render(request, 'registro/profile.html', context=ctx)
    except User.DoesNotExist:
        raise Http404('not found')

def create(request):
    return HttpResponse('este es el create')

def logged_out(request):
    return render(request, 'registration/salir.html', context = None)

def editar(request):
    return HttpResponse('aca deberia ir el formulario para cambiar datos')

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'main/upload.html', context)

def files_list(request):
    files = UploadedFiles.objects.all()
    return render(request, 'main/files_list.html', {'files':files})

def file_uploaded(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'main/files_list.html', {'form':form})
    else:
        form = FileForm
    return render(request, 'main/file_uploaded.html', {'form':form })
