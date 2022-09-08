from django.test import SimpleTestCase
from app_logic.helpers import is_open


# class TestConnector(SimpleTestCase):
#     def test_access_denied(self):
#         pass


# class TestDivision(SimpleTestCase):
#     def test_access_denied(self):
#         pass


class TestIsOpen(SimpleTestCase):
    def test_access_denied(self):
        self.assertTrue(is_open(9)) # проверяет True для одного переданного агрумента