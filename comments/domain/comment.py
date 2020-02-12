from django.utils import timezone


class Comment:

    def __init__(self, item, message, author, timestamp, id=None):
        self.item = item
        self.message = message
        self.author = author
        self.timestamp = timestamp
        self.id = id

    @classmethod
    def from_object(cls, instance, app_label=None, model=None):
        from comments.mappers import CommentMapper
        mapper = CommentMapper()
        return mapper.map(instance, app_label, model)

    @classmethod
    def create_for(cls, item, author, message, app_label, model):
        from comments.mappers import CommentMapper
        mapper = CommentMapper()
        item = mapper._map_item(item, app_label, model)
        timestamp = timezone.now()
        return cls(item, message, author, timestamp)
