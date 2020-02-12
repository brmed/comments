from collections import namedtuple

Meta = namedtuple('Meta', ['app_label', 'model'])


class Item:

    def __init__(self, id, type, app_label=None, model=None):
        self.id = id
        self.type = type
        self._meta = Meta(app_label=app_label, model=model)

    @classmethod
    def from_object(cls, obj, app_label=None, model=None):
        app_label = app_label or (obj._meta.app_label if hasattr(
            obj, '_meta') else None)
        model = model or (obj._meta.model_name if hasattr(
            obj, '_meta') else None)
        return cls(
            id=obj.id,
            type=model or type(obj),
            app_label=app_label,
            model=model,
        )

    def allows(self, user):
        return True
