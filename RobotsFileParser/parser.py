from urllib2 import urlopen
import Debug


def get(rbt_url):
    """
    A function to make a GET request.
    :param rbt_url: The url to request.
    :return: A list of disallowed options
    """

    Debug.debug('Attempting to parse %s' % rbt_url)

    # if server doesn't exist or no internet
    # connection, will throw URLError.
    # if getting error code from server,
    # will throw HTTPError
    return [line.split(': ')[1].split(' ')[0]  # select the path while ignoring comments
            for line in urlopen(rbt_url).read().split('\n')  # split result into lines
            if line.startswith('Disallow')]  # is a disallow option


def parse(url):
    """
    A function to parse a given url
    containing a robots.txt file. The 
    function will return a list of disallowed
    paths.
    
    :param url: The page to parse
    :return A list of disallowed URL paths.
    """

    # parse url
    rbt_url = 'http://' + url + '/robots.txt'

    # read the url's page

    try:
        return get(rbt_url)
    except:
        rbt_url = 'https://' + url
        return get(rbt_url)
