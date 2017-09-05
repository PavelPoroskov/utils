# -*- coding: utf-8 -*-

# strWord = "yoyo"

# strWordForLen = strWord[0]
# iIn = 0

# for Letter in strWord:
#     if Letter != strWordForLen[iIn]:
#         strWordForLen = strWordForLen + Letter
#         iIn += 1

#     print(strWordForLen, Letter, iIn )


strWord = "̈ɪwu:f"

#strWord = "[̈ɪhəup]"
# ('[', 91, u'[')
# ('\xcc', 204, u'\xcc')
# ('\x88', 136, u'\x88')
# ('\xc9', 201, u'\xc9')
# ('\xaa', 170, u'\xaa')
# ('h', 104, u'h')
# ('\xc9', 201, u'\xc9')
# ('\x99', 153, u'\x99')
# ('u', 117, u'u')
# ('p', 112, u'p')
# (']', 93, u']')


strWord = u'[̈ɪhəup]'
# (u'[', 91, u'[')
# (u'\u0308', 776, u'\u0308') # Combining Diaeresis
# (u'\u026a', 618, u'\u026a') # Latin Letter Small Capital I
# (u'h', 104, u'h')
# (u'\u0259', 601, u'\u0259') # Latin Small Letter Schwa
# (u'u', 117, u'u')
# (u'p', 112, u'p')
# (u']', 93, u']')

for Letter in strWord:
#    print( Letter, ord(Letter), unichr(ord(Letter)) )
#    print( Letter, ord(Letter), unicode(Letter) )
    print( Letter, ord(Letter) )
