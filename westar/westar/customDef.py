import jwt

from django.http import HttpResponse

from account.models import User
from posts import models as CONTENT_MODEL
from .settings import TOKEN_SECRECTKEY, ALGORITHMS

# check token and return user objects
def checking_token(request):
    token = request.headers
    if 'Authorization' not in token:
        return HttpResponse(status = 401)
       
    token_value = token['Authorization']
    try:
        user_info = jwt.decode(token_value, TOKEN_SECRECTKEY, algorithms=ALGORITHMS)
        user = User.objects.get(pk=user_info['id'])
        return user
    except:
        return False

def show_content(content, num):
    content_info = []
    username = []
    content_list = []
    image_url = []
    comment_info = []
    like_count = []
    content_info.append(content)
    comment_count = []

    username += User.objects.filter(pk=content['user']).values('username', 'avartar')
    image_url.append(list(CONTENT_MODEL.Photo.objects.filter(content=num).values('image_file')))
    comment_user_id  = list(CONTENT_MODEL.Comments.objects.filter(content=num).values('user'))
    comment = list(CONTENT_MODEL.Comments.objects.filter(content=num).values('comment', 'user'))
    like_count.append(CONTENT_MODEL.Like.objects.filter(content=num, isLike=True).count())
    comment_count.append(CONTENT_MODEL.Comments.objects.filter(content=num).count())
    if len(comment) != 0:
        for i in range(len(comment_user_id)):
            if i == len(comment_user_id):
                break 
            i -= 1
            user_id_box = comment_user_id[i]['user']
            comment_user = User.objects.filter(pk=user_id_box).values('username', 'avartar')
            comment[i]['user'] = comment_user[0]['username']
            comment[i]['avartar'] = comment_user[0]['avartar']
            comment_info.append(list(comment))
    for i in range(len(content_info)):
        if i == len(content_info):
            break 
        i -= 1
        print(content_info[i])
        content_info[i]['user_name'] = username[i]['username']
        content_info[i]['user_avartar'] = username[i]['avartar']
        if len(comment) != 0: 
            content_info[i]['comment'] = comment_info[i]
            content_info[i]['comment_count'] = comment_count[i]
        content_info[i]['images'] = image_url[i]
        content_info[i]['like'] = like_count[i]
        dicts = {
                 'content': content_info[i],
                        }
        content_list.append(dicts)

    return content_list