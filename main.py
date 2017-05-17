#!/usr/bin/env python

import RobotsFileParser
from URLSpider import Spider


base = 'http://www.yahoo.com'

s = Spider(base)
print s.scan(RobotsFileParser.parse(base))
