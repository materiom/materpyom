from materpyom.utils import MateriomCordra


def materiom_get_one_item(item_string: str):
    """
    Function to get the item using the item string
    :param item_string:
    :return: json object
    """

    m = MateriomCordra()
    return m.get_one_item(item_string=item_string)


def materiom_search(search_string: str):
    """
    Function to search things
    :param search_string: string to search with
    :return:
    """

    m = MateriomCordra()
    return m.search_objects(search_string)

# add more read functions here
# TODO PD 2020-02-19