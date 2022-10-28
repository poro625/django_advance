from django.shortcuts import render
from rest_framework.views import APIView
from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework.response import Response
# Create your views here.

class ArticleView(APIView):
    def get(seif, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, )