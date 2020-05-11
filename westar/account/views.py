import json
import jwt

from django.db import IntegrityError
from django.db.models import Q
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from django.views import View

from .models import User
from feeds.models import UserFeeds
from westar.settings import TOKEN_SECRECTKEY

# Create your views here.

class UserCreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        data_username = data['username']
        data_email = data['email']
        data_password = data['password']
        data_telephone = data['telephone']
        try:
            User(
                  username = data_username,
                  email = data_email,
                  password = data_password,
                  telephone = data_telephone
                ).save()
                
            new_user_obj = User.objects.get(email = data_email)
            new_user_feed = UserFeeds(user_id = new_user_obj)
            new_user_feed.save()
        except IntegrityError:
            new_user_obj = None
            new_user_feed = None
            username_check = User.objects.filter(username__exact=data_username)
            email_check = User.objects.filter(email__exact=data_email)
            check_count = username_check.count()
            if check_count != 0:
                return JsonResponse({'message':'Already somebody using this username, change username'}, status = 400)
            else: 
                check_count = email_check.count()  
                if check_count != 0:
                    return JsonResponse({'message':'Already somebody using this Email, Please Enter other Email '}, status = 400) 
                else:
                    return JsonResponse({'message':'Already somebody using this PhoneNumber, Can`t use this Numbers'}, status = 400)
        else:
            return HttpResponse("Succes", status = 201)



class UserLoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        check_password = int(data['password'])
        check_username = 'username'
        check_email = 'email'
        check_telephone = 'telephone'
        
        if check_username in data:
            login_username = data['username']
#            login_user = User.objects.filter(username__exact = login_username).values()
            try:
                get_user = User.objects.get(username=login_username)
            except:
                return JsonResponse({'message':'have not this username User'}, status = 400)
            else:
                try:
                    user_password_check = User.objects.get(Q(username=login_username)&Q(password=check_password))
                except:
                    return JsonResponse({'message':'Not correct password'}, status = 403)
                else:                    
                    queryset = User.objects.get(username=login_username)
                    dic_user = {
                            'id': queryset.id,
                            'username': queryset.username,                      
                        }
                    encoded_token = jwt.encode(dic_user, TOKEN_SECRECTKEY, algorithm='HS256')
                    return JsonResponse({'token':str(encoded_token)}, status = 200)

        elif check_email in data:
            login_email = data['email']
            try:
                get_user = User.objects.get(email=login_email)
            except:
                return JsonResponse({'message':'have not this Email User'}, status = 400)
            else:
                try:
                    user_password_check = User.objects.get(Q(email=login_email)&Q(password=check_password))
                except:
                    return JsonResponse({'message':'Not correct password'}, status = 403)
                else:                    
                    queryset = User.objects.get(email=login_email)
                    dic_user = {
                            'id': queryset.id,
                            'username': queryset.username
                        }
                    encoded_token = jwt.encode(dic_user, TOKEN_SECRECTKEY, algorithm='HS256')
                    return JsonResponse({'token':str(encoded_token)}, status = 200)

        elif check_telephone in data:
            login_telephone = data['telephone']
            try:
                get_user = User.objects.get(telephone=login_telephone)
            except:
                return JsonResponse({'message':'have not this telephone User'}, status = 400)
            else:
                try:
                    user_password_check = User.objects.get(Q(telephone=login_telephone)&Q(password=check_password))
                except:
                    return JsonResponse({'message':'Not correct password'}, status = 403)
                else:                    
                    queryset = User.objects.get(telephone=login_telephone)
                    dic_user = {
                            'id': queryset.id,
                            'username': queryset.username                       
                        }
                    encoded_token = jwt.encode(dic_user, TOKEN_SECRECTKEY, algorithm='HS256')
                    return JsonResponse({'token':str(encoded_token)}, status = 200)
        
        return JsonResponse({'message':'Fail Login'}, status = 400)



