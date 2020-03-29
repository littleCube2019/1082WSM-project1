#!/bin/bash
[ -z "$1" ] && sh CreateDocumentList.sh  
python makeVec.py
python main.py --query  drill wood sharp