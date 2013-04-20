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
translate = translate()

def search(keyword):
    cmd = "fu -a " + keyword
    t = commands.getstatusoutput(cmd)
    return str(t[1])

if __name__ == "__main__":
    import sys
    kw = sys.argv[1]
    print  translate.en2zh(search(kw))
