from .OSOperator import OSOperator
from .OSFilter import OSFilter

class OSPayload:

    def __init__(self):
        self.app_id = None
        self.filters = list()
        self.send_after = None
        self.delayed_option = None
        self.delivery_time_of_day = None
        self.ttl = None
        self.priority = None
        self.included_segments = None
        self.contents = None
        self.headings = None
        self.url = None

    @staticmethod
    def encode_filters(obj):
        if isinstance(obj, OSFilter):
            return obj.__dict__
        elif isinstance(obj, OSOperator):
            return obj.__dict__
        return obj