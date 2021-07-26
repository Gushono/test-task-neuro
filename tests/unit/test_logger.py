from configurations import logger
from tests.unit import DefaultTestBase


class TestLogger(DefaultTestBase):

    def test_logger_name(self):
        """
        Test if the logger name is test_logger-> logging.INFO
        """

        builded_logger = logger.factory_logger()
        current_logger = logger.get_logger()

        self.assertEqual('logger_neuro', builded_logger.name)
        self.assertEqual('logger_neuro', current_logger.name)

    def test_logger_level(self):
        """
        Test if the logger level is 10 -> logging.INFO
        """
        builded_logger = logger.factory_logger()
        current_logger = logger.get_logger()

        self.assertEqual(20, builded_logger.level)
        self.assertEqual(20, current_logger.level)
