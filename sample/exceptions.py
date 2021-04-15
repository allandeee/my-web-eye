class ItemContentError(Exception):

    def __init__(self, message=None):
        self.message = message or "Issue with item's content"
