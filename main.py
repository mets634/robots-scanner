#!/usr/bin/env python

import RobotsFileParser
from URLSpider import Spider
import sys


def main():
    if len(sys.argv) < 2:
        print 'USAGE: ./main.py <SITE TO SCAN>'
        return

    base = sys.argv[1]

    s = Spider(base)
    try:
        print '\n'.join(['[*]FOUND: ' + path
                        for path in s.scan(RobotsFileParser.parse(base))]
                        )
    except Exception, e:
        print '[*]' + str(e)
        print '[*]Unable to find robots.txt file'

    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    main()
