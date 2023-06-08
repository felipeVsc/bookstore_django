from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class UsersView(APIView):
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

    

class LibAdminView(APIView):
    def get(self,request):
        pass
    
    def post(self,request):
        # create
        pass

    def delete(self,request):
        pass

class BorrowBookView(APIView):
    #Renew vai ser um PUT
    # Return vai ser um delete
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

