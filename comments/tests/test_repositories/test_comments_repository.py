import mock
from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment as CommentModel
from comments.repositories import CommentRepository


class CommentRepositoryTestCase(TestCase):

    def setUp(self):
        model = mock.Mock()
        self.repo = CommentRepository(model)
        self.repo.content_types = mock.Mock()
        self.comment = mock.Mock()
        self.comment.item = self._get_item()

    def test_instantiate(self):
        self.assertIsInstance(self.repo, CommentRepository)

    @mock.patch.object(CommentRepository, '_get_content_type')
    def test_save_creates_object(self, _get_content_type):
        self.repo.save(self.comment)
        self.repo._model.objects.get_or_create.assert_called_once_with(
            content_type_id=_get_content_type().id,
            created_at=self.comment.timestamp,
            object_id=self.comment.item.id,
            author_id=self.comment.author.id,
            message=self.comment.message,
            id=self.comment.id,
        )

    @mock.patch.object(CommentRepository, '_get_content_type')
    def test_save_calls_get_content_type(self, _get_content_type):
        self.repo.save(self.comment)
        _get_content_type.assert_called_once_with(self.comment.item)

    def test_get_content_type(self):
        self.repo._get_content_type(self.comment.item)
        self.repo.content_types.objects.get_by_natural_key \
            .assert_called_once_with(
                app_label=self.comment.item._meta.app_label,
                model=self.comment.item._meta.model.lower(),
            )

    def test_default_contenttype_model(self):
        repo = CommentRepository()
        self.assertEqual(repo.content_types, ContentType)

    def test_default_comment_model(self):
        repo = CommentRepository()
        self.assertEqual(repo._model, CommentModel)

    def _get_item(self):
        item = mock.Mock()
        item._meta.app_label = 'billing'
        item._meta.model = 'Billing'
        return item
