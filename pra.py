#secret code
#Caesar Ciphar Program
message = 'Hello to everybody from the Hamalayan nation of Nepal.'
key = 10
mode = 'encript'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'

store = ''

for code in message:
	if code in SYMBOLS:
		index = SYMBOLS.find(code)

		if mode == 'encript':
			convertedIndex = index + key
		elif mode == 'decript':
			convertedIndex = index - key

		if convertedIndex >= len(SYMBOLS):
			convertedIndex = convertedIndex - len(SYMBOLS)

		elif convertedIndex < 0:
			convertedIndex = convertedIndex + len(SYMBOLS)

		store = store + SYMBOLS[convertedIndex]

	else:
		store = store + code


print(store)

