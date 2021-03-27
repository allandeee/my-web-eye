
class SiteChecker(object):

    def __init__(self, url):
        self.url = url

    def get_latest_content(self):
        raise NotImplementedError
