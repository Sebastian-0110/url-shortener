import uuid

from backend.app.exceptions import ShortenedUrlNotFound
from backend.app.models import ShortenedUrl
from .test_setup import UrlRepositorySQLiteTestSetup


class TestUrlRepositorySQLiteGetters(UrlRepositorySQLiteTestSetup):
    def test_get_by_original_url_returns_instance_of_ShortenedUrl_when_url_was_found(self):
        self.repository.save(self.original_url, self.url_code)
        shortened_url: ShortenedUrl = self.repository.get_by_original_url(self.original_url)
        self.assertIsInstance(shortened_url, ShortenedUrl)

    def test_get_by_original_url_raises_ShortenedUrlNotFound_when_url_wasnt_found(self):
        with self.assertRaises(ShortenedUrlNotFound):
            self.repository.get_by_original_url(self.original_url)

    def test_get_by_original_url_returns_the_same_object_as_save(self):
        inserted: ShortenedUrl = self.repository.save(self.original_url, self.url_code)
        requested: ShortenedUrl = self.repository.get_by_original_url(self.original_url)
        self.assertEqual(inserted, requested)


    def test_get_by_url_code_returns_instance_of_ShortenedUrl_when_url_code_was_found(self):
        self.repository.save(self.original_url, self.url_code)
        shortened_url: ShortenedUrl = self.repository.get_by_url_code(self.url_code)
        self.assertIsInstance(shortened_url, ShortenedUrl)

    def test_get_by_url_code_raises_ShortenedUrlNotFound_when_url_wasnt_found(self):
        with self.assertRaises(ShortenedUrlNotFound):
            self.repository.get_by_url_code(self.url_code)

    def test_get_by_url_code_returns_the_same_object_as_save(self):
        inserted: ShortenedUrl = self.repository.save(self.original_url, self.url_code)
        requested: ShortenedUrl = self.repository.get_by_url_code(self.url_code)
        self.assertEqual(inserted, requested)


    def test_get_by_uuid_returns_instance_of_ShortenedUrl_when_uuid_was_found(self):
        inserted_shortened_url: ShortenedUrl = self.repository.save(self.original_url, self.url_code)
        requested_shortened_url: ShortenedUrl = self.repository.get_by_uuid(str(inserted_shortened_url.uuid))
        self.assertIsInstance(requested_shortened_url, ShortenedUrl)

    def test_get_by_uuid_raises_ShortenedUrlNotFound_when_uuid_wasnt_found(self):
        with self.assertRaises(ShortenedUrlNotFound):
            self.repository.get_by_uuid(str(uuid.uuid4()))

    def test_get_by_uuid_returns_the_same_object_as_save(self):
        inserted: ShortenedUrl = self.repository.save(self.original_url, self.url_code)
        requested: ShortenedUrl = self.repository.get_by_uuid(str(inserted.uuid))
        self.assertEqual(inserted, requested)
