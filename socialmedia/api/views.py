from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics

from django.shortcuts import get_object_or_404

from .permissions import IsCreatorOrReadOnly
from .serializers import RegisterSerializer, PostSerializer
from .models import Post


class RegisterAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class PostDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsCreatorOrReadOnly,)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_interactions(request, pk, interaction):
    post = get_object_or_404(Post, pk=pk)
    
    if interaction.lower() == 'like':
        if request.user != post.creator:
            if request.user not in post.liked_by.all():
                post.liked_by.add(request.user)
                serializer = PostSerializer(post)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Post already liked'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'A user cannot like its own post'}, status=status.HTTP_400_BAD_REQUEST)
    elif interaction.lower() == 'unlike':
        if request.user in post.liked_by.all():
            post.liked_by.remove(request.user)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Cannot unlike a post that is not liked'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'detail': 'No such interaction'}, status=status.HTTP_400_BAD_REQUEST)
