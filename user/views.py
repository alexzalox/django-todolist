from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def user_login(request):
    message='登入'
    # 是否是POST表單
    if request.method=='POST':
        print('POST')
        if request.POST.get('login'):
            # 1.檢查帳號密碼是否為空
            # 2.是否有該使用者
            # 3.匹配密碼進行登入

            print('login')
        elif request.POST.get('register'):
            return redirect('register')
        
    
    return render(request, './user/login.html', {'message':message})

# Create your views here.
def user_register(request):
    # 產生使用者表單
    form =  UserCreationForm()
    message=''
    print(User.objects.all())

    for user in User.objects.all():
        print(user.id, user.username, user.email)

    # 檢查是get or post
    if request.method == 'GET':
        print('GET')
    elif request.method =='POST':
        print('POST')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(password1) <8:
            message='密碼少於8個字元'
        elif password1 != password2:
            message= '兩次密碼不同'
        else:
            if User.objects.filter(username=username).exists():
                message='帳號重複'
            else:
                User.objects.create_user(username=username,password=password1).save()
                message='註冊成功!'




        # 註冊功能
        # 密碼不能少於8個字元
        # 兩次密碼是否相同
        # 使用者名稱不能重複
        # 進行註冊



    return render(request,'./user/register.html',{'form':form, 'message':message,})