import sched
import time
from sample.site_checker import DCGBChecker, DCSevenVChecker


class WebEye(object):

    dc_checker = DCGBChecker()
    seven_v = DCSevenVChecker()
    scheduler = sched.scheduler(time.time, time.sleep)

    @classmethod
    def _get_time_str(cls):
        t = time.localtime()
        return time.strftime("%H:%M:%S", t)

    @classmethod
    def _reader(cls):
        print('CHECKED AT: ', cls._get_time_str())
        cls.dc_checker.print_content()
        print('===')
        cls.seven_v.print_content()
        print('===')

    @classmethod
    def reader(cls, secs):
        cls._reader()
        cls.scheduler.enter(secs, 1, cls.reader, (secs,))

    @classmethod
    def continuous_reader(cls, secs=5):
        cls.scheduler.enter(0, 1, cls.reader, (secs,))
        cls.scheduler.run()
