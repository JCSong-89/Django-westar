import jwt

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from .models import UserFeeds
from westar.settings import TOKEN_SECRECTKEY
# Create your views here.

class UserFeedView(View):
    def get(self, request):
        print(request)
        if 'X-Api-Token' in request.headers:
            get_token = request.headers
            token_value = get_token['X-Api-Token']
            token_value = token_value[1:]
            try:
                user_info = jwt.decode(token_value, TOKEN_SECRECTKEY, algorithms=['HS256'] )
            except:
                return HttpResponse("Cant decode token", status = 403)
            else:
                data = UserFeeds.manager(pk=user_info['id'])
                data = {
                        'id' : data.id,
                        'content_id' : [data.content_id],
                        'follwing' : [data.following]
                    }
                print(data)
                return JsonResponse({"user_info":list(data)}, status = 200)
        else:
            return HttpResponse("You not login now, Plz login account")