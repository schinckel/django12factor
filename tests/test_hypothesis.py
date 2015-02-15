import dj_database_url
import django12factor
import hypothesis
import unittest

from .env import (
    debugenv,
)


class TestHypotheses(unittest.TestCase):
    def test_database_parsing(self):
        @hypothesis.given(str)
        def hypo(database_url):
            def dj12db(u):
                with debugenv(DATABASE_URL=u):
                    return django12factor._database()
            self.assertEquals(dj12db(database_url), dj_database_url.parse(database_url))

        hypo()
