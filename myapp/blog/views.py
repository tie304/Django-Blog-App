import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer, PostSerializer, UserSerializerIn

from .models import Post, User

@csrf_exempt
def post_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def post_detail(request, pk):
    """
    Retrieve, update or delete a post.
    """

    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)

@csrf_exempt
def user(request, pk):
    """
    Creates user on POST
    Returns user on GET

    """
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializerIn(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

@csrf_exempt
def user_like(request, post_key, user_id):

    """
    Checks if user and post exist, if so adds a like from the user to post

    """

    if request.method == "POST":
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return JsonResponse({"message": "User does not exist"}, status=404)

        try:
            post = Post.objects.get(pk=post_key)
        except Post.DoesNotExist:
            return JsonResponse({"message": "Post not found"}, status=404)

        user.likes.add(post)

        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    else:
        return HttpResponse(status=405)










