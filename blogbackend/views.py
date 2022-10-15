import json

from blogbackend import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from blogbackend.models import Post


# code

class PostList(APIView):
    def get(self,request,*args,**kwargs):
        ret = {'code':200,'msg':'ok'}
        try:
            ret['post'] = serializers.serialize("json", Post.objects.all())
            return JsonResponse(ret)
            # return Response(ret)
        except Exception as e:
            ret['code'] = 500
            ret['msg'] = 'Timeout'
        return JsonResponse(ret)


class PostDetail(APIView):
    def post(self,request,*args,**kwargs):
        ret = {'code':200,'msg':'ok'}
        try:
            id = request.data.get('postId')['postId']
            if not id:
                ret['code'] = 404
                ret['msg'] = 'Post does not exist'
                return JsonResponse(ret)
            ret['post'] = serializers.serialize("json", Post.objects.filter(post_id=id))
            return JsonResponse(ret)
            # return Response(ret)
        except Exception as e:
            ret['code'] = 500
            ret['msg'] = 'Timeout'
        return JsonResponse(ret)