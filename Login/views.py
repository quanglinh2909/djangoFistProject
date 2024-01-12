from django.contrib.auth import authenticate
from django.shortcuts import render,HttpResponse
from django.views import View
class IndexClass(View):
    def get(self,request):
        return HttpResponse('<a href="/login">Login</a>')


class LoginClass(View):
    def get(self,request):
        return render(request,'Login/login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        # user = User.objects.create_user(username=username,password=password)
        # user.save()
        #login
        my_user  = authenticate(username=username,password=password)
        if my_user is not None:
            return render(request,'api/view_question.html')
        else:
            return HttpResponse("User Login Failed")

    #delete
    def delete(self,request):
        print(request.POST.get('username'))
        pass