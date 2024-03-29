from django.shortcuts import render, redirect
from django.http import HttpResponse
from portal.models import UserAccount

# Create your views here.
def index(request):
    mycontext = {
        "name": "Your name",
        "class": "Senior"
    }
    return render(request, "index.html", context=mycontext)

def login_view(request):
    context = dict()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = UserAccount.objects.get(username = username)
            request.session['username'] = user.username
            if user.password == password:
                return redirect(f'/profile/{username}')
        except:
            context['err_msg'] = "Username/password does not exist."
    return render(request, "login.html", context=context)

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        age = int(request.POST['age'])

        userAcc = UserAccount(username=username, password=password, age=age)
        userAcc.save()
        return redirect('/account/login')
    return render(request, "register.html")

def profile_view(request, username):
    if request.session.get('username', "") != username:
        return HttpResponse("Forbidden", status=403)
    user = UserAccount.objects.get(username=username)
    if len(request.GET) > 0:
        username = request.GET['username']
        password = request.GET['password']
        age = int(request.GET['age'])

        user.username = username
        user.password = password
        user.age = age
        user.save()
    return render(request, "profile.html", context={'user': user})

def delete_account_view(request, username):
    user = UserAccount.objects.get(username=username)
    user.delete()
    return redirect('account/login/')

def logout_view(request):
    request.session.flush()
    return redirect('/account/login')