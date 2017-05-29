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
        valid, suspects = s.scan(RobotsFileParser.parse(base))
        print '\n'.join(['[*]OPEN: ' + path
                        for path in valid]
                        )
        print '\n'.join(['[*]SUSPECTED (to be closed): ' + path
                         for path in suspects]
                        )
    except Exception, e:
        print '[*]' + str(e)
        print '[*]Unable to find robots.txt file'

    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    main()
