import unittest

from decorated_registry import (
    Registry, RegistryItem, RegistryError, ConstructorPayloadFactory, DefaultDecorateStrategy
)


class TestDecoratedRegistrySimple(unittest.TestCase):
    def setUp(self):
        self.registry = Registry()

    def test_simple(self):
        @self.registry
        class A:
            pass

        self.assertEqual(
            [
                RegistryItem(
                    payload=None,
                    value=A,
                )
            ],
            self.registry.items,
        )

        self.registry.remove(A)

        self.assertEqual(
            [],
            self.registry.items,
        )

    def test_double(self):
        with self.assertRaisesRegex(RegistryError, 'already registered'):
            @self.registry
            @self.registry
            class A:
                pass


class TestDecoratedRegistryExtended(unittest.TestCase):
    def setUp(self):
        self.registry = Registry(
            payload_factory=ConstructorPayloadFactory(dict),
            decorator_strategy=DefaultDecorateStrategy(
                allow_duplicates=True,
            )
        )

    def test_double_empty(self):
        @self.registry
        @self.registry
        class A:
            pass

        self.assertEqual(
            [
                RegistryItem(
                    payload={},
                    value=A,
                )
            ] * 2,
            self.registry.items
        )

    def test_double(self):
        # the call order will be reversed
        @self.registry(a=1)
        @self.registry(a=2)
        class A:
            pass

        @self.registry(b=1)
        class B:
            pass

        # as here
        self.assertEqual(
            [
                RegistryItem(
                    payload=dict(a=2),
                    value=A,
                ),
                RegistryItem(
                    payload=dict(a=1),
                    value=A,
                ),
                RegistryItem(
                    payload=dict(b=1),
                    value=B,
                ),
            ],
            self.registry.items
        )

        # thus removing the item will remove a=1
        self.registry.remove(A)

        self.assertEqual(
            [
                RegistryItem(
                    payload=dict(a=2),
                    value=A,
                ),
                RegistryItem(
                    payload=dict(b=1),
                    value=B,
                ),
            ],
            self.registry.items
        )
