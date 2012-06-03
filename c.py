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
import os.path
import sys

url = "http://ftp.freebsd.org/pub/FreeBSD/ports/amd64/packages/All/"

try:
	os.unlink('CHECKSUM.MD5')
except:
	pass


subprocess.Popen(['wget',url+'CHECKSUM.MD5'], stdout=subprocess.PIPE).communicate()[0]

print "Parsing CHECKSUM.MD5. Might take a minute. Please wait....."

chks = {}
try:
	f = open('CHECKSUM.MD5', 'r')
	for line in f:
		chks[line.strip()] = True
	f.close()
except:
	print "no CHECKSUM.MD5. bail."
	sys.exit()

print " Done."

print "Downloading list of available packages. Might take a minute. Please wait...."


req = urllib2.Request(url)
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

print " Done."

try:
	dun = open('updates.sh','w')
except:
	print "cannot open updates.sh for writing. bail."
	sys.exit()

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
			chkfile = rt+'-'+vers[rt]+'.tbz'
			if (os.path.exists(chkfile)):
				pass
			else:
				subprocess.Popen(['wget',url+rt+'-'+vers[rt]+'.tbz'], stdout=subprocess.PIPE).communicate()[0]
				
			ru = subprocess.Popen(['md5',chkfile], stdout=subprocess.PIPE).communicate()[0]
			dr = ru.split('\n')
			cu = dr[0].strip()

			try:
				if chks[cu]:
					print chkfile," +MD5 CHECK OK"
				else:
					chks[cu]='missing or mismatch check CHECKSUMS.MD5'
					dun.write('#\n')
					dun.write('#'+chkfile+' +MD5 CHECK NOGO.\n')
					dun.write('#'+cu+'\n')
					dun.write('#'+chks[cu]+'\n')
					dun.write('#\n')
			except:
				chks[cu]='missing or mismatch check CHECKSUMS.MD5'
				dun.write('#\n')
				dun.write('#'+chkfile+' +MD5 CHECK NOGO.\n')
				dun.write('#'+cu+'\n')
				dun.write('#'+chks[cu]+'\n')
				dun.write('#\n')
				pass

			dun.write('pkg_delete --force '+rt+'-'+nx+'\n')
			dun.write('pkg_add '+rt+'-'+vers[rt]+'.tbz\n')

dun.close()

