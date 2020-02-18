import logging
import pytest


from materpyom.utils import MateriomCordra

logging.basicConfig(level=logging.DEBUG)


class TestUtils:
    """
    Test utils functions
    """
    def test_check_credentials(self):
        """Test check credentials"""

        m = MateriomCordra()

        item = m.check_credentials()

        print(item)

        assert item["active"]

    def test_false_check_credentials(self):
        """Test fake credentials"""

        m = MateriomCordra()
        m.user = 'FAKE'

        with pytest.raises(Exception):
            m.check_credentials()

