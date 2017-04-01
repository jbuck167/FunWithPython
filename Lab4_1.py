# Lab 4-1
# iterate_comments.py Edited by Josh Buck
# Detect the presence of one of the table entries for a precomputed MD5 Hash Table which has the values:
# 0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee
# Partially from http://www.openrce.org/articles/full_view/11
found = False
count = 0
# For each of the segments
for seg in Segments():
    # For each of the defined elements
    for head in Heads(seg, SegEnd(seg)):
        if isData(GetFlags(head)):
            mnem = hex(head)
            if mnem == 0xd76aa478 or mnem == 0xe8c7b756 or mnem == 0x242070db or mnem == 0xc1bdceee :
                count = count + 1
            if FindBinary(min,SEARCH_DOWN,'D76AA478') <= MaxEA():
                count = count + 1
            if FindBinary(min,SEARCH_DOWN,'E8C7B756') <= MaxEA():
                count = count + 1
            if FindBinary(min,SEARCH_DOWN,'242070DB') <= MaxEA():
                count = count + 1
            if FindBinary(min,SEARCH_DOWN,'C1BDCEEE') <= MaxEA():
                count = count + 1




print count, " MD5 Constants present"
