import unittest
import uuid

from backend.src.models import ShortenedUrl
from .test_setup import UrlRepositorySQLiteTestSetup


class TestUrlRepositorySQLite(UrlRepositorySQLiteTestSetup):
    def test_save_returns_instance_of_ShortenedUrl(self):
        shortened_url: ShortenedUrl = self.repository.save(self.original_url, self.url_code)
        self.assertIsInstance(shortened_url, ShortenedUrl)

    def test_save_shortened_url_return_object_has_uuid_property_that_is_instance_of_UUID(self):
        shortened_url: ShortenedUrl = self.repository.save(self.original_url, self.url_code)
        self.assertIsInstance(shortened_url.uuid, uuid.UUID)

    def test_save_returns_instance_of_ShortenedUrl_that_matches_data(self):
        shortened_url: ShortenedUrl = self.repository.save(self.original_url, self.url_code)
        self.assertEqual(str(shortened_url.original_url), self.original_url)
        self.assertEqual(shortened_url.url_code, self.url_code)

    def test_save_is_persistent(self):
        shortened_url: ShortenedUrl = self.repository.save(self.original_url, self.url_code)
        urls = self.repository.get_all()
        self.assertTrue(shortened_url in urls)

    def test_save_doesnt_duplicate_entries_with_the_same_original_url(self):
        self.repository.save(self.original_url, self.url_code)
        self.repository.save(self.original_url, self.url_code + "123")
        urls = self.repository.get_all()
        self.assertTrue(len(urls) == 1)


if __name__ == '__main__':
    unittest.main()