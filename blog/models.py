from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    header_image = CloudinaryField('header-image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateField(auto_now_add=True)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def comment_count(self):
        return self.comments.filter(approved=True).count()

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User, related_name='comment_like', blank=True
        )

    class Meta:
        ordering = ['created_on']
    

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def number_of_likes(self):
        return self.likes.count()


class GalleryImage(models.Model):
    caption = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField('gallery-image', default='placeholder')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="gallery_image"
    )
    created_on = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='gallery_image_like', blank=True)

    class Meta:
        ordering = ['created_on']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.caption)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.caption

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')
