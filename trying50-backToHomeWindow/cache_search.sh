#!/bin/bash
# Cache Search

pkgname="" 	#packageName= empty string


# $1 is a special variable, This variable corresponds to the arguments with which a script was invoked.
# namely, $1 holds the keyword which the user typed to search for.
if [ "$1" == "" ]; then   # if user don't enter a keyword to search, but click the search button..
	echo "package name missing"
else
	pkgname=$1  #user types a valid string. Now variable pkgname hold the keyword to be searched.
	#apt-cache search pkgname command is run in terminal, results are saved into cache_list.txt
	apt-cache search $pkgname > cache_list.txt
fi
