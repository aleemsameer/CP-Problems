# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	text = ""
	letters = 'abcdefghijklmnopqrstuvwxyz'
	for m in msg :
		if m not in m.isalpha():
			text += m
		else:
			position = letters.index(m.lower())
			newP = position + shift
			if newp < 0:
				newp +=26
			elif newp > 25:
				newp -= 26
			if m.lower():
				text += letters[newp]
			elif m.isupper():
				text += letters[newp].upper()
	return text 





