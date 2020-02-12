import mock
from django.test import TestCase
from comments.domain import Comment


class CommentTestCase(TestCase):

    def setUp(self):
        self.domain_class = Comment

    def instantiate(self):
        comment = self.domain_class(
            'item', 'author', 'message', 'timestamp'
        )
        self.assertIsInstance(comment, self.domain_class)
        self.assertEqual(comment.item, 'item')
        self.assertEqual(comment.author, 'author')
        self.assertEqual(comment.message, 'message')
        self.assertEqual(comment.timestamp, 'timestamp')

    def test_instantiate_from_object_instance(self):
        commentmodel_instance = mock.Mock()
        comment = self.domain_class.from_object(commentmodel_instance)
        self.assertIsInstance(comment, self.domain_class)
        self.assertEqual(comment.author.id, commentmodel_instance.author.id)
        self.assertEqual(comment.item.id,
                         commentmodel_instance.content_object.id)
        self.assertEqual(comment.message, commentmodel_instance.message)
        self.assertEqual(comment.timestamp, commentmodel_instance.created_at)
