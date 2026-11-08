from django.core.cache import cache
from django.test import Client, TestCase

from .models import Item


class HealthEndpointTests(TestCase):
    def test_health_returns_ok(self):
        client = Client()
        response = client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})


class ItemModelTests(TestCase):
    def test_create_item(self):
        item = Item.objects.create(name="widget")
        self.assertEqual(str(item), "widget")
        self.assertEqual(Item.objects.count(), 1)


class CacheTests(TestCase):
    def test_redis_cache_roundtrip(self):
        cache.set("ci-key", "ci-value", timeout=30)
        self.assertEqual(cache.get("ci-key"), "ci-value")
