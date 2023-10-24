from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Post model that defines a blog post or any related content.
class Post(models.Model):
    name = models.CharField(max_length=150, default='Default name')  # Name or title of the post.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_posts')  # User who created the post.
    content = models.TextField()  # Actual content or body of the post.
    likes = models.ManyToManyField(User, related_name='liked_posts')  # Users who liked this post.
    created_at = models.DateTimeField(default=timezone.now)  # Date and time when the post was created.

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


# Model to track analytics of each post.
class PostAnalytics(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_analytics')  # The post being tracked.
    date = models.DateField()  # Specific date of tracking.
    likes_count = models.PositiveIntegerField()  # Count of likes on that specific date.
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time when the record was created.

    class Meta:
        unique_together = ('post', 'date')

    def __str__(self):
        return f"Analytics for {self.post.name} on {self.date}"


# Model to track the last activity of each user.
class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # User being tracked.
    last_activity = models.DateTimeField(auto_now=True)  # Date and time of the last activity.

    def __str__(self):
        return f"{self.user.username} - {self.last_activity}"






