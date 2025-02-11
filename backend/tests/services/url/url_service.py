from unittest.mock import MagicMock, create_autospec
import unittest
import uuid

from backend.src.repository.url_repository_sqlite import UrlRepositorySQLite
from backend.src.services.code_generator import RandomCodeGeneratorService
from backend.src.services.url import UrlService
from backend.src.models import ShortenedUrl


class TestUrlService(unittest.TestCase):
    def setUp(self):
        self._setup_constants()
        self._setup_mocks()

        self.service = UrlService(
            repository=self.repository,
            code_generator=self.code_generator,
            get_code_length=self.get_code_length,
        )

    def _setup_constants(self):
        self.original_url = "https://www.google.com/"
        self.url_code = "abc123"
        self.code_length = 5

    def _setup_mocks(self):
        self.code_generator = create_autospec(RandomCodeGeneratorService)
        self.code_generator.generate = MagicMock(return_value=self.url_code)

        self.repository = create_autospec(UrlRepositorySQLite)
        self.repository.save.side_effect = lambda original_url, url_code: ShortenedUrl(
            uuid=uuid.uuid4(),
            original_url=original_url,
            url_code=url_code,
        )

        self.get_code_length = MagicMock(return_value=self.code_length)

    def test_save_generates_code_using_get_code_length(self):
        self.service.save(self.original_url)
        self.get_code_length.assert_called_once()
        self.code_generator.generate.assert_called_once_with(self.code_length)

    def test_save_saves_on_the_repository(self):
        self.service.save(self.original_url)
        self.repository.save.assert_called_once_with(self.original_url, self.url_code)

    def test_save_returns_instance_of_ShortenedUrl(self):
        shortened_url = self.service.save(self.original_url)
        self.assertIsInstance(shortened_url, ShortenedUrl)