from django.db import models
from django.urls import reverse # < here
from django.utils.text import slugify # < here
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model): # < here
    title = models.CharField(max_length=255,
                             default='',
                             blank=True)
    body = models.TextField(default='',
                            blank=True)

    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    
    slug = models.SlugField(max_length=255,
                            default='',
                            blank=True,
                            unique=True)

    image = models.ImageField(upload_to='images/',default='C:\\Users\\User\\Desktop\\Capture.jpg')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail',
                       args=[str(self.slug)])

class Comment (models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)