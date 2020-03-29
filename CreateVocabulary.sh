#!/bin/bash
rm  Vocabulary

for file in  ./documents/*.product 
do	
	cat $file   >> Vocabulary 
	echo >> Vocabulary
done
