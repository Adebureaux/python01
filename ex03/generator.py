from random import randint

def shuffle(words):
	length = len(words)
	for i in range(length):
		j = randint(i, length - 1)
		words[i], words[j] = words[j], words[i]
	return words

def unique(words):
	new_words = []
	[new_words.append(word) for word in words if not word in new_words]
	return new_words

def ordered(words):
	return sorted(words)

def generator(text, sep=" ", option=None):
	'''Splits the text according to sep value and yield the substrings.
	option precise if a action is performed to the substrings before it is yielded.
	'''
	if not isinstance(text, str) or not isinstance(sep, str) or not len(sep) or (not option in ["shuffle", "unique", "ordered", None]):
		raise TypeError("argument error")
	text = text.split(sep)
	if option == "shuffle":
		text = shuffle(text)
	elif option == "unique":
		text = unique(text)
	elif option == "ordered":
		text = ordered(text)
	for word in text:
		yield word

if __name__ == "__main__":
	for word in generator("Le Lorem Ipsum est simplement du faux texte.", " ", "shuffle"):
		print(word)