from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class BookView(APIView):
    def get(self,request):
        pass
    
    def post(self,request):
        # create
        pass

    def put(self,request):
        #renew
        pass
    
    def delete(self,request):
        pass

class GetBookByIdView(APIView):
    def get(self,request):
        pass
    

class BookFromCsvView(APIView):
    def post(self,request):
        # create
        pass


class BookBulkView(APIView):
    def post(self,request):
        pass


class GetBookByFilter(APIView):
    # usar filtros, aprnder isso nas rotas
    pass 

class AuthorView(APIView):
    def get(self,request):
        pass
    
    def post(self,request):
        # create
        pass

    def put(self,request):
        #renew
        pass
    
    def delete(self,request):
        pass
 
class GetAuthorById(APIView):
    def get(self,request):
        pass 

class GenreView(APIView):
    def get(self,request):
        pass
    
    def post(self,request):
        # create
        pass

    def put(self,request):
        #renew
        pass
    
    def delete(self,request):
        pass
 
class GetGenreById(APIView):
    def get(self,request):
        pass 

class PublisherView(APIView):
    def get(self,request):
        pass
    
    def post(self,request):
        # create
        pass

    def put(self,request):
        #renew
        pass
    
    def delete(self,request):
        pass
 
class GetPublisherById(APIView):
    def get(self,request):
        pass 

