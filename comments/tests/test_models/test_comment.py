from django.test import TestCase
from model_mommy import mommy
from comments.models import Comment as CommentModel


class CommentModelTestCase(TestCase):

    def setUp(self):
        self.model = CommentModel

    def test_create(self):
        comment = mommy.make(CommentModel)
        self.assertIsInstance(comment, CommentModel)
