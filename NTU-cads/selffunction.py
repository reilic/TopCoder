def RemoveSpecialChars(s):

	string = s

	return ''.join(e for e in s if e.isalnum())