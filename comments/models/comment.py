from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User as UserModel
from .base_model import BaseModel


class Comment(BaseModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    author = models.ForeignKey(UserModel, on_delete=models.PROTECT)
    message = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "{}: {}".format(self.author, self.message)
