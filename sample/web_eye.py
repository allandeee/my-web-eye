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
        self.found = False

    def _get_time_str(self):
        t = time.localtime()
        return time.strftime("%H:%M:%S", t)

    def _reader(self):
        print('CHECKED AT: ', self._get_time_str())
        self.dc_checker.print_content()
        print('===')
        self.seven_v.print_content()
        print('===')

    def reader(self):
        self._reader()
        self.scheduler.enter(self.secs, 1, self.reader)

    def continuous_reader(self):
        self.scheduler.enter(0, 1, self.reader, ())
        self.scheduler.run()

    def _checker(self):
        if not self.found and self.seven_v.get_item_availability().lower() == 'available':
            webbrowser.open(self.seven_v.url, new=2)
            self.found = True

    def checker(self):
        self._checker()
        event = self.scheduler.enter(self.secs, 1, self.checker)
        if self.found:
            self.scheduler.cancel(event)

    def continuous_checker(self):
        self.scheduler.enter(0, 1, self.checker)
        self.scheduler.run()
