from urllib2 import urlopen
import Debug

def parse(url):
    """
    A function to parse a given url
    containing a robots.txt file. The 
    function will return a list of disallowed
    paths.
    
    :param url: The page to parse
    :return A list of disallowed URL paths.
    """

    rbt_url = url + '/robots.txt'

    Debug.debug('Attempting to parse %s' % rbt_url)

    # read the url's page

    # if server doesn't exist or no internet
    # connection, will throw URLError.
    # if getting error code from server,
    # will throw HTTPError
    return [line.split(': ')[1].split(' ')[0]  # select the path while ignoring comments
            for line in urlopen(rbt_url).read().split('\n')  # split result into lines
            if line.startswith('Disallow')]  # is a disallow option
