#!/bin/bash
rm DocumentList
for file in  ./documents/*.product
	do
	   echo $file  | cut -c 13-18 >> DocumentList   
	   cat $file | tr "\n" " " >> DocumentList
	   echo >> DocumentList
done;
