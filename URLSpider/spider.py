import Debug
import urllib2


class Spider(object):
    """A class to check for hidden web pages."""

    COMMON_WEB_PAGES = ['index.html', 'index.php']

    def __init__(self, baseurl):
        """
        Class ctor, hold ont base url
        :param baseurl: The base url to scan.
        """

        # make sure the base does not end with '/'
        self.__base = baseurl[:-1] if baseurl[-1] == '/' else baseurl

    def scan(self, entries):
        """
        A method to scan the website with the given entries
        in order to determine if entries contain anything.
        :param entries: The paths to scan.
        :return: A list of hidden pages.
        """

        res = []  # will hold valid paths

        print '[*] Scanning website %s...' % self.__base
        for e in entries:
            # create a list of url's to scan

            urls = self.__generate_url(self.__base + e)

            for u in urls:
                url = 'http://' + u
                Debug.debug('Checking path %s' % url)
                if self.__check(url):  # is a valid path
                    res.append(url)
                    Debug.debug('Path is valid')
                else:
                    Debug.debug('Path is invalid')

        return res

    def __generate_url(self, url):
        """
        A method to generate a list of
        URLs from a specific entry
        :param url: The url to use in order to generate.
        :return A list of urls to try.
        """

        if url[-1] == '/':  # need to add our own file names
            return [url + path for path in self.COMMON_WEB_PAGES]
        else:  # already a file
            return [url]

    @staticmethod
    def __check(url):
        """
        A method to check if given url is
        a valid web page.
        :param url: The URL to check.
        :return: Whether input is a valid web page.
        """

        try:
            urllib2.urlopen(url)  # attempt to read webpage

            # TODO: check if 404 is given on page rather than HTTP

            return True
        except:
            return False
