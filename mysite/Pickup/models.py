from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
#import PIL
# 
# 
from PIL import Image
 
class Post(models.Model):
    post_text = models.CharField(max_length=255)
    post_title = models.CharField(max_length=255)
    post_date = models.DateTimeField(("date posted"), auto_now_add=True)
    post_loc = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rsvp_list = models.ManyToManyField(User, related_name='rsvp')
    event_time = models.DateTimeField(("event time"), default=timezone.now)  # Defaults to current time
    class Meta:
        db_table = "post"

class Tag(models.Model):
    tag_name = models.CharField(max_length=255)
    tagged_posts = models.ManyToManyField(Post, related_name="post_tags")
    class Meta:
        db_table = "tag"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='avatar.jpg', # default avatar
        upload_to='profile_avatars' # dir to store the image
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)