from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from profiles import serializers
import requests
class HelloApiView(APIView):
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format = None):
        
        an_apiview = [
            "sina",
            "amareh",
            "guilan",
            "university"
        ]

        return Response({
            "massage" : "Hello",
            "an_apiview" : an_apiview
        })
        
    def post(self, request):
        #Create a new Object
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            massage = f'Hello {name}'
            return Response({"massage": massage})
        else:
            return Response(serializer.errors,
                            status= status.HTTP_400_BAD_REQUEST)
    def put(self, request , pk = None):
        name = request.data.get('name')
        return Response({'method': 'PUT'})
    #update the whole object
    
    def patch(self,request , pk = None):
        return Response({'method': 'PATCH'})
    #Update a partial object
    
    def delete(self,request, pk = None):
        return Response({'method': 'DELETE'})
    #Delete