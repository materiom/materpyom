import logging

from materpyom.read import get_one_item

logging.basicConfig(level=logging.DEBUG)


class TestMateriomCordra:
    def test_get_one_item(self):
        """Test to read one item"""

        item = get_one_item("c68b8b25ca641689d33c")

        assert len(item) != 0
