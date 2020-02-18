from materpyom.utils import MateriomCordra


def get_one_item(item_string: str):
    """
    Function to get the item using the item string
    :param item_string:
    :return: json object
    """

    m = MateriomCordra()
    return m.get_one_item(item_string=item_string)


# add more read functions here
# TODO PD 2020-02-18