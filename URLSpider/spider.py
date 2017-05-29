import Debug
import urllib2


class Spider(object):
    """A class to check for hidden web pages."""

    COMMON_WEB_PAGES = ['index.html', 'index.php', 'index.htm', 'index.asp',
                        'default.html', 'default.htm', 'default.php', 'default.asp',
                        'home.htm', 'home.html', 'home.php', 'home.asp']

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

        valid = []  # will hold valid paths
        suspects = []  # will hold suspected web pages

        print '[*] Scanning website %s...' % self.__base
        for e in entries:
            # create a list of url's to scan

            urls = self.__generate_url(self.__base + e)

            for u in urls:
                url = 'http://' + u
                Debug.debug('Checking path %s' % url)

                code = self.__check(url)
                if  code == 2:  # is a valid path
                    valid.append(url)
                    Debug.debug('Path is valid')
                elif code == 1:
                    suspects.append(url)
                    Debug.debug('Path is suspected to be closed')
                else:
                    Debug.debug('Path is invalid')

        return valid, suspects

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
        :return: 2 -> open, 1 -> suspected, 0 -> closed
        """

        try:
            html = urllib2.urlopen(url).read().lower()  # attempt to read webpage

            if '404' in html and 'not found' in html:
                return 1
            return 2

        except:
            return 0
