from django.contrib import admin
from .models import Post


# Admin settings for the Post model.
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')  # Fields to display in the list view.
    list_filter = ('user', 'created_at')  # Fields to provide filters for.
    search_fields = ('name', 'content')  # Fields to allow searching for.
    date_hierarchy = 'created_at'  # Hierarchical date-based browsing.


admin.site.register(Post, PostAdmin)


