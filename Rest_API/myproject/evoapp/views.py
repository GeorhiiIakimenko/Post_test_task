from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Post, PostAnalytics
from django.contrib.auth.models import User
from .serializers import UserSerializer, PostSerializer
from django.db.models import Count
from django.http import JsonResponse
from django.db.models.functions import TruncDate
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.response import Response
from .forms import DateRangeForm
from django.shortcuts import render
from django.db.models import Max
from .models import UserActivity


def home(request):
    return render(request, 'home.html')


class LikeAnalyticsView(APIView):
    def get(self, request):
        # Parse the date_from and date_to parameters from the URL using your form
        form = DateRangeForm(request.GET)
        if form.is_valid():
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']
        else:
            date_from = None
            date_to = None

        # Create a base query for aggregating likes
        likes_query = (Post.objects
                       .annotate(date=TruncDate('created_at'))
                       .values('date')
                       .annotate(total_likes=Count('likes__id')))

        # Apply date filters if provided
        if date_from:
            likes_query = likes_query.filter(date__gte=date_from)
        if date_to:
            likes_query = likes_query.filter(date__lte=date_to)

        # Execute the query and get the results
        likes_by_day = likes_query.order_by('date')

        # Format the results
        results = [{'date': item['date'], 'total_likes': item['total_likes']} for item in likes_by_day]

        # Return the result as JSON
        return Response({'analytics': results})


# ViewSet for User model.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSet for Post model with additional actions for liking and unliking a post.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        post.likes.add(user)
        PostAnalytics.objects.create(post=post, date=timezone.now().date(), likes_count=post.likes.count())
        return JsonResponse({'message': 'Liked'})

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        post.likes.remove(user)
        return JsonResponse({'message': 'Unliked'})


class LastRequestAnalytics(APIView):
    def get(self, request):
        user_activity = UserActivity.objects.values('user__username').annotate(
            last_request=Max('last_activity'),
            last_login=Max('user__last_login')
        )
        results = [{'username': item['user__username'], 'last_request': item['last_request'], 'last_login': item['last_login']} for item in user_activity]
        return JsonResponse({'user_activity': results})


