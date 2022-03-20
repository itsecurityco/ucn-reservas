from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Borrow, Device


def index_view(request):
    return HttpResponseRedirect(reverse("home"))

def login_view(request):

    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        
        return render(request, "webapp/login.html", {
            "message": "Usuario y/o contraseña inválidos."
        })

    return render(request, 'webapp/login.html')


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


@login_required
def home_view(request):
    borrows = request.user.borrows.all()
    title = "Mis Préstamos"
    return render(request, "webapp/home.html", {"title": title, "borrows": borrows})


@login_required
def devices_index(request):
    devices = Device.objects.all()
    title = "Dispositivos"
    return render(request, "webapp/devices.html", {"devices": devices, "title": title})


@login_required
@csrf_exempt
def borrow_post(request):
    if request.method == "POST":
        device_id = request.POST["device_id"]
        device = Device.objects.get(pk=device_id)

        # check if user has previous requests for the same device
        user = request.user
        has_borrow = user.borrows.filter(device=device)
        
        if has_borrow:
            return JsonResponse({
                "msg": "No puede reservar este dispositivo dos veces.", 
                "type": "alert-warning"
            })

        new_borrow = Borrow.objects.create(
            user=user,
            device=device
        )

        if not new_borrow:
            return JsonResponse({
                "msg": "Error al reservar el dispositivo.", 
                "type": "alert-warning"
            })

        # set device as unavailable
        try:
            device.available = False
            device.save()
        except:
            return JsonResponse({
                "msg": "Error al bloquear el dispositivo.", 
                "type": "alert-danger"
            })
        
        return JsonResponse({
            "msg": "Dispositivo reservado correctamente.", 
            "type": "alert-success"
        })

    return HttpResponseRedirect(reverse("home"))
