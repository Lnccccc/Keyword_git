from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.
def first(request):
    return render(request,'login.html')


def register(request):
    user_name_list = []
    user_info = User.objects.all()
    for i in user_info:
        user_name_list.append(i.user)
    try:
        request.session['user_id']
        return render(request,'info.html',context={'info':'You have login!'})
    except:

        if request.method == 'POST':
            reg_user_name = request.POST['r_user_name']
            if reg_user_name in user_name_list:
                return render(request,'info.html',context={'info':'the account is exited!'})
            else:
                pass
            reg_password = request.POST['r_password']
            reg_password_2 = request.POST['r_password_2']
            if reg_password != reg_password_2:
                return render(request,'info.html',context={'info':'The password you enter didnt the same!'})
            else:
                reg = User(user=reg_user_name,password=reg_password)
                reg.save()
                return render(request,'login.html')
        else:
            return render(request,'register.html')
def logout(request):
    try:
        del request.session['user_id']
        return render(request, 'login.html')
    except KeyError:
        return render(request,'info.html',context={'info':'you did not login'})


def login(request):
    user_name_list = []
    password_list = []
    if request.method == 'POST':
        sub_user_name = str(request.POST['user_name'])
        sub_password = str(request.POST['password'])
    else:
        return render(request,'login.html')
    user_info = User.objects.all()
    for i in user_info:
        user_name_list.append(i.user)
        password_list.append(i.password)
    user_dict = dict(zip(user_name_list,password_list))
    if sub_user_name in user_name_list:
        if user_dict[sub_user_name] and sub_password == str(user_dict[sub_user_name]):
            request.session['user_id'] = sub_user_name
            return render(request,'detail.html')
        else:
            return render(request,'info.html',context={'info':'PASSWORD WRONG!'})
    else:
        return render(request,'info.html',context={'info':'This account do not register'})



def reset(request):
    pass
