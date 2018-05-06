import logging


logger = logging.getLogger(__name__)


class Chatters:
    def __init__(self):
        self.chatters_list = set()
        self.chatter_points = {}
