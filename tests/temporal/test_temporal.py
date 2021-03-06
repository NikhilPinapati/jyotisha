import logging

from jyotisha.panchangam import temporal

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s {%(filename)s:%(lineno)d}: %(message)s "
)

def test_sanitize_time():
    assert temporal.sanitize_time(2018, 11, 11, 10, 8, 60) == (2018, 11, 11, 10, 9, 00)
    assert temporal.sanitize_time(2018, 12, 31, 23, 60, 00) == (2019, 1, 1, 00, 00, 00)