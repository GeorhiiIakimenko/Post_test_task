from .models import Post, PostAnalytics
from datetime import date
from celery import shared_task


@shared_task
def collect_post_analytics():
    for post in Post.objects.all():
        # Calculate likes count for today
        likes_count_today = post.likes.count()

        # Create or update the analytics data for today
        analytics, created = PostAnalytics.objects.get_or_create(post=post, date=date.today())
        analytics.likes_count = likes_count_today
        analytics.save()
