from django.shortcuts import render
from django.http import HttpResponse
from app_one.models import User
# Create your views here.

def users(request):
    user_list = User.objects.order_by('last_name')
    user_dict = {'user_records':user_list}
    return render(request, 'app_one/users.html', context=user_dict)

def index(request):
    return HttpResponse('Hi')
