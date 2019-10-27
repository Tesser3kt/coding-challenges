ENCRYPTION_DICT = {
	'a': '0',
	'e': '1',
	'o': '2',
	'u': '3'
}

def _reverse_string(word: str) -> str:
	reversed_word = ''
	for (index, char) in enumerate(word):
	    reversed_word += word[-(index + 1)]
	return reversed_word
	
def encrypt(word: str) -> str:
	reversed_word = _reverse_string(word)
	for char in ENCRYPTION_DICT:
		reversed_word = reversed_word.replace(char, ENCRYPTION_DICT[char])
	return reversed_word + 'aca'

print(encrypt(input()))
