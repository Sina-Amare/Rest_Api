from rest_framework.views import APIView
from rest_framework.views import Response

class HelloApiView(APIView):
    
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
        