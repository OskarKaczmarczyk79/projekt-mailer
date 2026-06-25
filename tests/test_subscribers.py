import pytest

from mailer.subscribers import SubscriberManager


class TestSubscriberManager:

    @pytest.fixture
    def manager(self) -> SubscriberManager:
        return SubscriberManager()

    def test_add_and_list_subscribers(self, manager: SubscriberManager) -> None:
        assert manager.add_subscriber("user@example.com", "User") is True
        assert manager.add_subscriber("user@example.com") is False
        subscribers = manager.list_subscribers()
        assert subscribers == [{"email": "user@example.com", "name": "User"}]

    def test_remove_subscriber(self, manager: SubscriberManager) -> None:
        manager.add_subscriber("test@example.com")
        assert manager.remove_subscriber("test@example.com") is True
        assert manager.remove_subscriber("test@example.com") is False

    def test_get_subscriber(self, manager: SubscriberManager) -> None:
        manager.add_subscriber("hello@domain.com", "Hello")
        subscriber = manager.get_subscriber("hello@domain.com")
        assert subscriber == {"email": "hello@domain.com", "name": "Hello"}
        assert manager.get_subscriber("missing@domain.com") is None

    def test_add_invalid_email_raises(self, manager: SubscriberManager) -> None:
        with pytest.raises(ValueError):
            manager.add_subscriber("invalid-email")
