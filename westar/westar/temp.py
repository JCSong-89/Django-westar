
#class ContentsView(View):
#    def get(self, request, pk):
#        content = Content.objects.filter(pk=pk).values('comment','description','createdAt','id','user')
#        contetns = customDef.show_content(content, pk)
#        return JsonResponse({"data":contetns}, status = 200)


#class UserFeedView(View):
#    def get(self, request):
#        if 'Authorization' not in request.headers:
#            content_info = []
#            random_num_box = []
#            while  len(content_info) < 3:
#                ramdom_number = int(random.randint(1,15))
#                print(ramdom_number)
#                if ramdom_number in random_num_box:
#                    continue
#                random_num_box.append(ramdom_number)
#                ramdom_content = CONTENT_MODEL.Content.objects.filter(pk=ramdom_number).values
#                ('comment','description','createdAt','id','user') 
#                print(ramdom_content)
#                if 0 != len(ramdom_content):                   
#                    content_info.append( customDef.show_content(ramdom_content, ramdom_number))
#                    
#            return JsonResponse({"data":content_info}, status = 200)
#
#        user = customDef.checking_token(request)
#        content_image = []
#        user_content = CONTENT_MODEL.Content.objects.filter(user=user.id).values('id')
#        
#        for i in range(len(user_content)):
#            if i == len(user_content):
#                break
#
#            content_image.append(CONTENT_MODEL.Photo.objects.filter(content=user_content[i]['id']).first()
#                                 )            
#            user_content[i]['image'] = content_image[i].image_file 
#        
#        user_content_id = user_content.values('id')
#        content_count = user_content.count()
#        follow_count = Follow.objects.filter(follow=user).count()
#        follower_count = Follow.objects.filter(follower=user).count()
#        return JsonResponse({"content":list(user_content),
#                             "content_count":content_count,
#                             "follow_count":follow_count,
#                             "follower_count":follow_count
#                             }, status = 200)       