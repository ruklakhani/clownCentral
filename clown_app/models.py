from django.db import models
from django_currentuser.db.models import CurrentUserField
from string import ascii_letters, digits
from django.urls import reverse
from django.utils.text import slugify
from random import choice


# Create your models here.
class Post(models.Model):
    slug = models.CharField(max_length=15, blank=True, editable=False)
    title = models.CharField(max_length=100, help_text="Post Title")
    description = models.TextField(help_text="Description")
    time_published = models.DateTimeField(auto_now_add=True)
    posted_by = CurrentUserField()

    def get_absolute_url(self):
        path_components = {'slug': self.slug}
        return reverse('show_post', kwargs=path_components)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(''.join(choice(ascii_letters + digits) for _ in range(4))+' '+self.title)

        return super(Post, self).save(*args, **kwargs)