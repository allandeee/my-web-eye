import sched
import time
import webbrowser
from sample.site_checker import DCGBChecker, DCSevenVChecker


class WebEye(object):

    def __init__(self, secs=5):
        self.secs = secs
        self.dc_checker = DCGBChecker()
        self.seven_v = DCSevenVChecker()
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def _get_time_str(self):
        t = time.localtime()
        return time.strftime("%H:%M:%S", t)

    def _reader(self):
        print('CHECKED AT: ', self._get_time_str())
        self.dc_checker.print_content()
        print('===')
        self.seven_v.print_content()
        print('===')

    def reader(self, secs):
        self._reader()
        self.scheduler.enter(secs, 1, self.reader, (secs,))

    def continuous_reader(self):
        self.scheduler.enter(0, 1, self.reader, (self.secs,))
        self.scheduler.run()

    @classmethod
    def _checker(cls):
        if cls.seven_v.get_item_availability().lower() == 'sold out':
            webbrowser.open(cls.seven_v.url)

    def checker(cls):
        pass
