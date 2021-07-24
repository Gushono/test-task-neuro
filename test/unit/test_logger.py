from configurations import logger
from . import DefaultTestBase


class TestLogger(DefaultTestBase):

    def test_factory_logger(self):
        builded_logger = logger.factory_logger()

        self.assertEqual('test_logger', builded_logger.name)
        self.assertEqual(10, builded_logger.level)

    def test_get_logger(self):
        current_logger = logger.get_logger()

        self.assertEqual('test_logger', current_logger.name)
        self.assertEqual(10, current_logger.level)
