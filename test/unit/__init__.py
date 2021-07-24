from unittest import TestCase


class DefaultTestBase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        print("\nRunning scenario: ", self.id().rpartition('.')[-1])

    def tearDown(self) -> None:
        print("Finished!\n")
        super().tearDown()
