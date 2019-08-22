from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

def loginview(request):
    user = None
    if request.method == "POST":

        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
            return redirect('warga:list_ktp')
        else:
            return redirect('login')
    return render(request, 'login.html')


def logoutView(request):
    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'logout.html')