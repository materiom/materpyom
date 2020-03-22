import requests
import logging
import os
import json
from requests.auth import HTTPBasicAuth

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

user = os.environ["MATERIOM_USER"]
password = os.environ["MATERIOM_PASSWORD"]
host = os.environ.get("MATERIOM_HOST", "https://materiom.org")


class MateriomCordra:
    """
    Class object to connect with the materiom database
    """

    def __init__(self):
        self.url_root = host + ":8443"
        self.user = user
        self.pswd = password

    def call_api(self, url: str):
        """
        Call api
        :param url: (string) url string to call
        :return: json object
        """

        logging.debug(f'Calling API to the follow URL {url}')

        # hit and get content from materiom website
        item = requests.get(
            url, verify=False, auth=HTTPBasicAuth(self.user, self.pswd)
        ).content

        # make json object
        try:
            return json.loads(item.decode("utf-8"))
        except:
            raise Exception('Could not return json object')

    def search_objects(self, search_term: str):
        """
        Function to search the database and return all objects
        :param search_term: (string)
        :return:
        """

        logger.debug('Searching objects')

        url = f"{self.url_root}/objects/?query={search_term}"

        return self.call_api(url=url)

    def get_one_item(self, item_string: str):
        """
        Function to get one item
        :param item_string:
        :return: json object
        """

        logger.debug(f'Getting one item {item_string}')

        # make url
        url = f"{self.url_root}/objects/test/{item_string}"

        return self.call_api(url=url)

    def check_credentials(self):
        """
        Function to check credentials
        :return: json object
        """

        logger.debug(f'Checking credentials')

        url = f"{self.url_root}/check-credentials"

        item = self.call_api(url=url)

        return item

    def get_all_objects_by_type(self, object_type: str = "Material"):
        """
        Function to get objects from a certain type
        :item object_type: the type of objects you want to be returned
        :return: json object
        """

        logger.debug(f'Checking credentials')

        url = f'{self.url_root}/objects/?query=type:"{object_type}"'

        items = self.call_api(url=url)

        return items
