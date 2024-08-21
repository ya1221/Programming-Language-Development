from PartA import basic

while True:
	text = input('basic > ')
	if text == 'END':
		break
	result, error = basic.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)