#!/bin/bash
#Author: timger <yishenggudou@gmail.com>
#weibo <http://t.sina.com/zhanghaibo>
#@yishenggudou http://twitter.com/yishenggudou
git pull
python setup.py install
ps aux|grep weixin_admintool_server|grep -v grep|awk '{print $2}'|xargs kill

