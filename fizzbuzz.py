def fizz_buzz(arg):
	if not isinstance(arg, int):
		return "Error"

	if arg < 0 :
		return ''

	elif arg % 5 == 0 and arg % 3 == 0:
		return 'FizzBuzz'

	elif arg % 3 == 0:
		return 'Fizz'
		
	elif arg % 5 == 0:
		return 'Buzz'
	
	else :
		return arg