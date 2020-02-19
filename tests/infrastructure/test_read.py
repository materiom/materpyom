import logging

from materpyom.read import materiom_get_one_item, materiom_search

logging.basicConfig(level=logging.DEBUG)


class TestMateriomCordra:
    def test_get_one_item(self):
        """Test to read one item"""

        item = materiom_get_one_item("c68b8b25ca641689d33c")

        assert len(item) != 0

    def test_materiom_search(self):
        """Test to search function"""

        items = materiom_search("heated")

        assert len(items['results']) != 0
