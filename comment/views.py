import requests
import random

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CommentSerializer


class CommentsView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            comment = serializer.data

            # Simulate error request
            rand = random.randint(0, 10)
            if rand < 5:
                try:
                    r = requests.post(f"http://127.0.0.1:8001/api/posts/{comment['post_id']}/comments",
                                      data={"text": comment['text']})
                except Exception as error:
                    print(error)
                    pass

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
