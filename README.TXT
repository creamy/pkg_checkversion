
Python script (tested 2.7.2 /should/ run 2.4-3.x) that compares installed 
version of packages with latest available on FreeBSD.org. If there is a 
newer (different) version available it will output the package info with
current installed version and newer version, download the tbz package file, 
and perform an MD5 checksum verficiation of the file. Output is writted to 
'updates.sh' in the CWD. For each package it prints a pkg_delete line for 
the previous package version, then a pkg_add line for the new version. If 
there is an MD5 checksum mismatch it will report to the updates.sh file. 
In the case of a mismatch it is recommended to unlink the particular package 
file and run the python c.py script again. It will not download package 
files if they already exist in the CWD, so running the script subsequent 
times should go faster.

Note: update URL for your architecture / os version / mirror etc.

Note: DO NOT RUN updates.sh without editing! There are some cases when you 
do not want to delete a package (or install a new one). Before updating your 
system, make sure to get the latest package information by typing in:

# pkg_updating

on your command line. 


See ups.txt and updates.sh for example output.


NOTE:

issues encounter using the updates.sh script
major versions available are not necessarily updates that will work with the
other packages...

1) don't delete gtk20 and replace with gtk30.
(xfce4 depends on lib-gtk-2.0)
2) don't delete gcc46 and replace with gcc48.
(mplayer and ffmpeg depend on gcc46)
3) don't delete docbook.. 
(all the docbook packages are installed by xfce4, there are multiple versions)



 


Waitman Gobble <waitman@waitman.net>
San Jose, California USA
NO WARRANTIES




