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
    _ = '\n\n'.join([u'CMD示例:{0}\n简介:{1}'.format(i['command'],i['summary']) for i in rst])
    return _

if __name__ == "__main__":
    kw = sys.argv[1]
    print  translate.en2zh(search(kw))
