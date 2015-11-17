import string #This line defines string so as to be able to get rid of punctuation.
import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "manqnohyphen.txt"
print "Much Ado about Nothing statistics"
handle = open(name)

text = handle.read()
print ''
print 'There are', len(text), 'characters in the text.' #prints the number of characters in the text
lexis = text.split()
print ''
print 'There are', len(lexis), 'words in the text.'

handle = open(name)

counts = dict()
for line in handle:
	line = line.rstrip()
	line = line.translate(None, string.punctuation) #This line gets rid of punctuation.
	words = line.split()
	for word in words:
		wrd = word.lower()
		counts[wrd] = counts.get(wrd,0) + 1
#print counts



lst = list()
for lexicon,occurrence in counts.items():
	lst.append((occurrence, lexicon))
	
print 'The least frequently used words are:'
lst.sort()
for occurrence, lexicon in lst[:]:
	if occurrence == 1:
		print lexicon, occurrence

print 'The most frequently used words are:'	
lst.sort(reverse=True)

for occurrence, lexicon in lst[:30]:
	print lexicon, occurrence


handle = open("manqnohyphen.txt")

print "Compound words divided with a hyphen:"
lineno = 0
compoundno = 0
for line in handle:
	line = line.rstrip()
	lineno = lineno + 1
	cp = re.findall("\S+-\S+", line)
	if len(cp) > 0 :
		compoundno = compoundno + 1
		print cp
print "There are", lineno, "lines in the play."	
print "The number of lines in which compounds divided with hyphen appear are", compoundno, "."
relfre = float(compoundno) / lineno
print "The relative frequency of the lines in which there are hyphenated compounds is:", relfre, "."

handle = open("manqnohyphen.txt")
text = handle.read()
lexis = text.split()
print ''
print 'There are', len(lexis), 'words in the text.'
relfrewords = 56.0 / len(lexis)
print relfrewords
