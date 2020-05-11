import json
import jwt

from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View

from account.models import User
from feeds.models import UserFeeds
from .models import Content, Comments, Like, Photo
from westar.settings import TOKEN_SECRECTKEY

# Create your views here.

#class NewContentsView(View):
    

class ContentsView(View):
    def post(self, request):
       data = json.loads(request.body)
       if 'description' not in data:
           data['description'] = ""
       data_description = 'description'
       token = request.headers
       if 'X-Api-Token' not in token:
           return HttpResponse("please login, You are not status Login", status = 401)
       
       token_value = token['X-Api-Token']
       token_value = token_value[1:]
       try:
           user_info = jwt.decode(token_value, TOKEN_SECRECTKEY, algorithms=['HS256'])
           user = User.objects.get(pk=user_info['id']) 
       except:
           return HttpResponse("Your Token is not Normal")
       else:
           try:
               new_photo = Photo(
                   image_file = request.FILES['img_file'] 
                   )
               new_photo.save()
           except:
               return HttpResponse("Can`t save new photo")
           else:
               photo_instance = Photo.objects.filter(id=new_photo.id)
       try:
           new_content = Content(
               user_id = user,
               description = data['description'],
               )
           new_content.save()
           new_content.images.set(photo_instance)
           instanced = Content.objects.filter(Q(user_id=user)&Q(pk=new_content.id))
       except:
           return HttpResponse("Fail Error, Can't Save for New Content")
       else:
           try:
               user_feed = UserFeeds.objects.get(user_id = user)           
               user_feed.content_id.set(instanced)
           except:
               return HttpResponse("Fail Error, Can't Save UserFeed add New Content", status = 400)
           else:
               return HttpResponse("save New Content", status=201)

       return HttpResponse("Do Nothing", status = 400) 

   
class CommetView(View):
    def post(self, request):
        data = json.loads(request.body)
        token = request.headers
        if 'X-Api-Token' not in token:
            return HttpResponse("please login, You are not status Login", status = 401)
        token_value = token['X-Api-Token']
        token_value = token_value[1:]
        try:
            user_info = jwt.decode(token_value, TOKEN_SECRECTKEY, algorithms=['HS256'])
            user = User.objects.get(pk=user_info['id']) 
        except:
            return HttpResponse("Your Token is not Normal")
        else:
            comment_text = data['comment']
            content_id = int(data['content'])
            try:
                content = Content.objects.get(pk=content_id)
            except:
                return HttpResponse("Can't Find this Content")            
            else:
                Comments( 
                    user_id = user,
                    comment = comment_text,
                    content_id = content
                    ).save()
                return HttpResponse("Succes Save new comment", status=201)
        return HttpResponse("Fail Save comment")


class LikeView(View):
    def post(self, request):
        data = json.loads(request.body)
        token = request.headers
        if 'X-Api-Token' not in token:
            return HttpResponse("please login, You are not status Login", status = 401)
        token_value = token['X-Api-Token']
        token_value = token_value[1:]

        try:
            user_info = jwt.decode(token_value, TOKEN_SECRECTKEY, algorithms=['HS256']) 
            user = User.objects.get(pk=user_info['id'])
        except:
            return HttpResponse("Your Token is not Normal")
        else:
            isLike_switch = data['isLike']
            content_id = data['content']

            try:
                content = Content.objects.get(pk=content_id)
            except:
                return HttpResponse("Can't Find this Content")            
            else:

                try:
                    filter_like = Like.objects.filter(Q(user_id=user_info['id'])&Q(content_id=content_id))
                    count_like = filter_like.count()
                except:
                    return HttpResponse("Can't Get Like Obj", status=400)
                else:

                    if count_like == 0:
                        try:
                            Like( 
                                  user_id = user,
                                  isLike = isLike_switch,
                                  content_id = content
                             ).save()                
                        except:
                            return HttpResponse("Cant save Like", status=400)
                        else:
                            return HttpResponse("Succes Save Like", status=201 )

                    else:
                        this_like = Like.objects.get(Q(user_id=user_info['id'])&Q(content_id=content_id))
                        this_like.isLike = isLike_switch
                        this_like.save()
                        return HttpResponse("Succes Like Change", status=200)
        return HttpResponse("Fail Save LIke")

