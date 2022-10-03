from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.
class Tags(models.Model):
    title = models.CharField(max_length=100)
    descr = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    POST_STATUS = (
        ('D', 'draft'),
        ('P', 'published')
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='cover_images/', default='cover_images/default.png')
    content = FroalaField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    descr = models.TextField()
    # tags = models.ManyToManyField(Tags)
    status = models.CharField(max_length=1, choices=POST_STATUS)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='comments')
    comment = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(help_text="your email would not be published")
    body = models.TextField()

    def __str__(self):
        return f"{self.email}-{self.post}"

    class Meta:
        ordering = ['-created']