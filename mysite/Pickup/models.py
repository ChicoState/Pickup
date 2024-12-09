from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_text = models.CharField(max_length=255)
    post_title = models.CharField(max_length=255)
    post_date = models.DateTimeField(("date posted"),auto_now_add=True)
    post_loc = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rsvp_list = models.ManyToManyField(User, related_name='rsvp')
    date_time = models.DateTimeField()  

    class Meta:
        db_table = "post"

class Tag(models.Model):
    tag_name = models.CharField(max_length=255)
    tagged_posts = models.ManyToManyField(Post, related_name="post_tags")
    class Meta:
        db_table = "tag"