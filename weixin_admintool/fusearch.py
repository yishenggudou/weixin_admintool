#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright 2011 timger
#    +Author timger
#    +Gtalk&Email yishenggudou@gmail.com
#    +Msn yishenggudou@msn.cn
#    +Weibo @timger http://t.sina.com/zhanghaibo
#    +twitter @yishenggudou http://twitter.com/yishenggudou
#    Licensed under the MIT License, Version 2.0 (the "License");
import commands
from translate import translate
import sys
from api import API
translate = translate()


def search(keyword):
    a = API(keyword)
    rst = a.load()
    _ = u'\n\n'.join([u'CMD example:{0}\ninfo:{1}'.format(i['command'],i['summary']) for i in rst[:10]])
    print _
    return _.encode('utf-8')

if __name__ == "__main__":
    kw = sys.argv[1]
    print search(kw)
    #print  translate.en2zh(search(kw))
