import bcrypt
import json
import jwt
import random

from django.core.exceptions import ValidationError
from django.core import validators
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views import View

from posts import models as CONTENT_MODEL
from .models import * 
from westar import customDef
from westar.settings import TOKEN_SECRECTKEY,ALGORITHMS

class UserCreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        data_username = data.get('username', None)
        data_email = data.get('email', None)
        data_password = data.get('password', None)
        data_telephone = data.get('telephone', None)
        try:            
            validators.validate_email(data_email)
            check_user = User.objects.filter(Q(username=data_username)
                                            |Q(email=data_email)
                                            |Q(telephone=data_telephone)).count()    
        except ValidationError:
            return HttpResponse(status = 400)    
        if check_user != 0:
            return HttpResponse(status = 400)
        if data_username != None and data_email != None and data_password != None and data_telephone != None:
            try:
                hash_pw = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
                print(hash_pw)
                hash_pw = hash_pw.decode('utf-8')
                User(
                      username = data['username'],
                      email = data['email'],
                      password = hash_pw,
                      telephone = data['telephone']
                    ).save()
                return HttpResponse(status=201)
            except:
                return HttpResponse(status = 500)
        return HttpResponse(status = 400)


class UserLoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        check_password = data.get('password', None)
        check_username = data.get('username', None)
        check_email = data.get('email', None)
        check_telephone = data.get('telephone', None)
        user_pw = User.objects.filter(
            Q(username=check_username)
            |Q(email=check_email)
            |Q(telephone=check_telephone)
            ).values('password')
        check_bcrypt = bcrypt.checkpw(data['password'].encode('utf-8'),user_pw[0]['password'].encode('utf-8'))
        if check_bcrypt != True:
            return HttpResponse(status = 400)
        if check_bcrypt == True:
            user = User.objects.get(
            Q(username=check_username)
            |Q(email=check_email)
            |Q(telephone=check_telephone))
            try:
                dic_user = {
                             'id': user.id,
                             'username': user.username,
                             'exp': 600000
                            }
                encoded_token = jwt.encode(dic_user, TOKEN_SECRECTKEY, algorithm=ALGORITHMS)
                return JsonResponse({'Authorization':encoded_token.decode("utf-8")}, status = 200)
            except:
                return HttpResponse(status=400)


class User_recommend(View):
    def get(self, request):
        user = customDef.checking_token(request)
        user_id = user.id
        random_users = []
        check_num = []
        while True:
            random_num = int(random.randint(1,15))
            if user_id == random_num:
                continue
            elif str(random_num) in check_num:
                continue
            random_user = list(User.objects.filter(pk=random_num).values('username', 'avartar'))
            if 1 != len(random_user):
                continue            
            check_num += str(random_num)
            random_users += random_user            
            if 3 < len(random_users):
                break
        return JsonResponse({"data":list(random_users)}, status = 200)

