from django.shortcuts import render
from .form import Createuser
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def registerPage(request):
    form = Createuser()
    if request.method == 'POST':
        form = Createuser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Вы успешно создали {user}')
            return render(request, 'center.html')
    context = {'form': form}
    return render(request, 'Register.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'center.html')
        else:
            messages.info(request, 'Пароль или логин не правильны')
    return render(request, 'sign_in.html')


def center(request):
    return render(request, 'center.html')
