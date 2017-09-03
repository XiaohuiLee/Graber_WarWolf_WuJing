# coding:utf8

import random
import string

def bidGenerator():
    bid = "".join(random.sample(string.ascii_letters + string.digits, 11))
    cookies = {
        'Cookie' : 'bid=%s; ps=y; ue="aukuno@126.com"; dbcl2="65548707:dmtiAByXcfI"'%bid
    }
    print cookies
for i in xrange(0,5):
    bidGenerator()