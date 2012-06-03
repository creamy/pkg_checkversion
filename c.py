# c.py
# June 2012
# check package version with available on FreeBSD.org site
# Waitman Gobble <waitman@waitman.net>
# San Jose, California USA
#
# NO WARRANTIES
#
# NOTE: check URL below to match your architecture / os version / mirror
#

import HTMLParser
import urllib2
import re
import subprocess


req = urllib2.Request("http://ftp.freebsd.org/pub/FreeBSD/ports/amd64/packages/All/")
res = urllib2.urlopen(req)
htc = res.read()
tbz = re.findall(r'href=[\'"]?([^\'" >]+)', htc)
vers = {}
for t in tbz:
	t = t.replace('.tbz','')
	t = t.replace('%2c',',')
	l = t.split('-')
	vx = l.pop()
	rt = '-'.join(l)
	vers[rt] = vx

p = subprocess.Popen(['pkg_info'], stdout=subprocess.PIPE).communicate()[0]
ln = p.split("\n")
for l in ln:
	t = l.split(' ')
	c = t[0]
	n = c.split('-')
	nx = n.pop()
	rt = '-'.join(n)
	if rt!='':
		if vers[rt]!=nx:
			print rt,"\t",nx,"\t",vers[rt]

