from comments.models import Comment as CommentModel
from django.contrib.contenttypes.models import ContentType


class CommentRepository:
    content_types = ContentType

    def __init__(self, model=None):
        self._model = model or CommentModel

    def save(self, comment):
        content_type = self._get_content_type(comment.item)
        self._model.objects.get_or_create(
            content_type_id=content_type.id,
            object_id=comment.item.id,
            author_id=comment.author.id,
            message=comment.message,
            created_at=comment.timestamp,
            id=comment.id,
        )

    def get_for_item(self, item):
        content_type = self._get_content_type(item)
        qs = self._get_queryset()
        return qs.filter(
            content_type=content_type,
            object_id=item.id,
        )

    def _get_queryset(self):
        return self._model.stored.all().order_by('created_at')

    def _get_content_type(self, item):
        return self.content_types.objects.get_by_natural_key(
            app_label=item._meta.app_label,
            model=item._meta.model.lower(),
        )
