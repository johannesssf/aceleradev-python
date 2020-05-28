import requests

from requests.exceptions import RequestException


def get_temperature(lat, lng):
    """Given a latiture and longiture, return the location temperature
    in celsius degrees.

    Arguments:
        lat {float} -- A valid latitude is between -90 to +90
        lng {float} -- A valid longitude is between -180 to +180

    Raises:
        RequestException: If some requests problem
        ConnectionError: If some network problem

    Returns:
        int -- Location temperature (C°) or None otherwise
    """
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)

    try:
        reponse = requests.get(url)
    except RequestException as ex:
        print(f"ERROR: requests, {type(ex)}")
        raise ex
    except ConnectionError as ex:
        print(f"ERROR: network, {type(ex)}")
        raise ex

    data = reponse.json()
    temperature = data.get('currently', {}).get('temperature')

    if temperature is None:
        return

    return int((temperature - 32) * 5.0 / 9.0)
