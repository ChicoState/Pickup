from django.db import models
from django.contrib.auth.models import User

CAT_CHOICES = (
    ('Choose a Category', 'NULL'),
    ('Sports', 'SPORTS'),
    ('Gaming', 'VIDEO GAMES'),
)

SPORT_CHOICES = (
    ('Basketball', 'BASKETBALL'),
    ('Football', 'FOOTBALL'),
    ('Soccer', 'SOCCER'),
)

class Post(models.Model):
    post_text = models.CharField(max_length=255)
    post_title = models.CharField(max_length=255)
    post_date = models.DateTimeField(("date posted"), auto_now_add=True)
    post_loc = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rsvp_list = models.ManyToManyField(User, related_name='rsvp')
    #catergory = models.CharField(max_length=11, choices=CAT_CHOICES, default='Choose a Category')
    #sports_catergory = models.CharField(max_length=10, choices=SPORT_CHOICES, default='Basketball')

    class Meta:
        db_table = "post"