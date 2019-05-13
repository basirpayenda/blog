from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(blank=True, unique=True)
    image = models.ImageField(default='default.jpg',
                              upload_to='posts/%Y/%m/%d')
    created_at = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={'title_slug': self.slug})

    def get_update_url(self):
        return reverse('blog:blog_update', kwargs={'title_slug': self.slug})

    def get_delete_url(self):
        return reverse('blog:blog_delete', kwargs={'title_slug': self.slug})
