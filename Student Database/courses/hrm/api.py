from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


# class UserAuthentication(ObtainAuthToken):
#     def post(self,request,*args,**kwargs):
#         serializer = self.serializer_class(data=request.data,context={'request':request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer._validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response(token.key)

class UserList(APIView):

    def get(self,request):
        model = Users.objects.all()
        serializer = UsersSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        #model = Users.objects.all()
        #model = Users.objects.get(some_attribue = something)
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(APIView):

    def get_user(self,course_id):
        try:
            model = Users.objects.get(id=course_id)
            return model
        except Users.DoesNotExist:
            return 

    def get(self,request,course_id):
        if not self.get_user(course_id):
            return Response(f'User with {course_id} is Not Found in Database',status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(self.get_user(course_id))
        return Response(serializer.data)

    def put(self,request,course_id):
        #model = Users.objects.all()
        #model = Users.objects.get(some_attribue = something)
        if not self.get_user(course_id):
            return Response(f'User with {course_id} is Not Found in Database',status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(self.get_user(course_id),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,course_id):
        if not self.get_user(course_id):
            return Response(f'User with {course_id} is Not Found in Database',status=status.HTTP_404_NOT_FOUND)
        model=self.get_user(course_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

