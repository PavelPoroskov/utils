import os
import re
from collections import Counter, namedtuple 
from itertools import groupby


#patHtmlTag = re.compile('<(.*?)>')


def genWords( in_fromDir):
	for file in os.listdir( in_fromDir ):
		if file.startswith("chapter") or file.startswith("part") or file.startswith("content") :
	#        print( os.path.join( fromDir, file) )

			html_text = open( os.path.join( in_fromDir, file) ).read()
			text_filtered = re.sub( '<(.*?)>', '', html_text )
	#		listWords = re.split('\W+', text_filtered )

#			print(file)
	#		print(text_filtered)
			for mobj in re.finditer( r'\w+', text_filtered):
	#			print(word)
				yield mobj.group(0)

	#		print(listWords)

#			break

listBlackList = ['the', 'a', 'an']
listBlackList = listBlackList + [ 'and', 'or', 'not' ]
listBlackList = listBlackList + [ 'with', 'of', 'to', 'in' ]


fromDir = '/home/*/xhtml'

data = Counter( genWords(fromDir) )
#print(data)

WordInfo = namedtuple( 'WordInfo', ['word', 'wordcount', 'wordlower', 'wordlowercount' ] )

#for (word, count) in sorted( data, key=lambda i: i[0].lower() ):
data_with_lower = [ (word, count, word.lower()) for word, count in data.items() ]

setWords = { wi[2] for wi in data_with_lower }

data_noplural = []
for word, count, wordlower in data_with_lower:
	flag_add = True
	if wordlower.endswith('s') and 1 < len(wordlower):
		word_nos = wordlower[:-1]
		if word_nos in setWords:
			data_noplural.append( (word, count, word_nos) )
			flag_add = False
		else:
#			if wordlower.endswith('ies') and 3 < len(wordlower):
			if wordlower.endswith('es') and 2 < len(wordlower):
				word_nos = wordlower[:-2]
				if word_nos in setWords:
					data_noplural.append( (word, count, word_nos) )
					flag_add = False
	elif wordlower.endswith('ed') and 2 < len(wordlower):
			word_nos = wordlower[:-2]
			if word_nos in setWords:
				data_noplural.append( (word, count, word_nos) )
				flag_add = False

	if flag_add:
		data_noplural.append( (word, count, wordlower) )


data_sort_lower = sorted( data_noplural, key=lambda wi: wi[2] )

data_lower_uniq = []
data_all = []
for key_lowerword, g in groupby( data_sort_lower, key=lambda wi: wi[2] ):

	lowercount = 0
	for wi in g:
		lowercount = lowercount + wi[1]

#	for wi in g:
#		data_all.append( WordInfo( wi.word, wi.wordcount, wi.wordlower, lowercount ) )

	data_lower_uniq.append( ( key_lowerword, lowercount ) )

#for (word, count) in sorted(data_lower_uniq, key=lambda i: (-i[1], i[0]) ):
#	print(word, count)

for (word, count) in sorted(data_lower_uniq, key=lambda i: i[0] ):
	print(word, count)

#to do
#+) plurals: zombie, zombies --+ zombie

#new
#get one file from console (srt, epub)
#	get list of files from console
#	get .txt file
#get names of heroes (chapter in, first)
#console parameters: 
#	sort: alphabetical/most use
#output: word, frequency, chapter