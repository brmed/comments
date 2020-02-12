from comments.domain.comment import Comment
from django.contrib.auth.models import User
from comments.domain import Item


class CommentMapper:

    def map(self, instance, app_label=None, model=None):
        domain_author = self._map_user(instance.author)
        item = self._map_item(instance.content_object, app_label, model)
        return Comment(
            item,
            instance.message,
            domain_author,
            instance.created_at,
            id=instance.id,
        )

    def _map_user(self, instance):
        return User(
            username = instance.username,
            email = instance.email,
            first_name = instance.first_name,
            last_name = instance.last_name,
            id = instance.id,
        )

    def _map_item(self, instance, app_label, model):
        return Item.from_object(instance, app_label, model)
