import json
import jwt

from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views import View

from account.models import User
from .models import Content, Comments, Like, Photo
from westar.settings import TOKEN_SECRECTKEY, ALGORITHMS
from westar import customDef

# Create your views here.

#class NewContentsView(View):
    
class ContentCreateView(View):
    def post(self, request):
       data = json.loads(request.body)
       if 'description' not in data:
           data['description'] = ""
       data_description = data['description']
       data_images = data.get('image_URL', None)
       if data_images == None:
           return HttpResponse(status = 400)
       print(data_images)
       user = customDef.checking_token(request)
       if user == False:
           return HttpResponse(status = 400)
       try:
           this_content = Content(
            user =  user,
            description = data_description
           )
           this_content.save()
           this_images = Photo(
               image_file = data_images
               )
           this_images.save()
           this_content.images.add(this_images)
           return HttpResponse(status = 201)
       except:
           return HttpResponse(status = 500)


class CommetView(View):
    def post(self, request):
        data = json.loads(request.body)
        user = customDef.checking_token(request)
        comment_text = data.get('comment', None)
        content_id = data.get('content', None)
        if comment_text == None or content_id == None:
            return HttpResponse(status = 400)
        try:
            content = Content.objects.get(pk=content_id)
            new_conmment = Comments( 
                        user = user,
                        comment = comment_text,
                        )
            new_conmment.save()
            print(new_conmment)
            content.comment.add(new_conmment)
            return HttpResponse(status = 201)
        except:
            return HttpResponse(status = 500)

class LikeView(View):
    def post(self, request):
        data = json.loads(request.body)
        user = customDef.checking_token(request)
        isLike_switch = data.get('isLike', None)
        content_id = data.get('content', None)
        print(isLike_switch)
        if isLike_switch == None or content_id == None:
            return HttpResponse("here", status = 400)

        count_like = Like.objects.filter(Q(user_id=user.id)&Q(content_id=content_id)).count()

        if count_like == 0:
            try:
                new_like = Like( 
                    user = user,
                    isLike = isLike_switch,
                    content_id = content_id
                    )
                new_like.save()
                content = Content.objects.get(pk=content_id)
                content.like.add(user)
            except:
                return HttpResponse(status = 500)
        try:
            this_like = Like.objects.get(Q(user_id=user.id)&Q(content_id=content_id))
            this_like.isLike = isLike_switch
            this_like.save()
            return HttpResponse(status = 200)
        except:
            return HttpResponse(status = 500)


#인터넷 사이트용 유저FEED, 포스트 조회 기능
class ContentView(View):
    def get(self, request, username):
        user = User.objects.get(username = username)
        contetns = Content.objects.filter(user=user.id).values('user', 'description', 'createdAt', 'id')
        user_contents = []
        for i in range(len(contetns)):
            num = contetns[i]['id']
            user_contents.append(customDef.show_content(contetns[i],num))
        return JsonResponse({"data":list(user_contents)}, status = 200)

