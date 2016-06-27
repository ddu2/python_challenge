#!/usr/bin/env python

import string

str1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

table = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
print str1.translate(table)

str2 = ''
for cha in str1:
    if cha == 'y':
        str2 = str2 + 'a' 
    elif cha == 'z':
        str2 = str2 + 'b' 
    elif cha.islower():
        str2 = str2 + chr(ord(cha)+2)
    else:
        str2 = str2 + cha 
print str2
