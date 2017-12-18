

print('I can tell your secret number!!! Just I need only two information. Startpoint and Endpoint. So tell me -')

startpoint = int(input('What is your Startpoint: '))
endpoint = int(input('What is your Endpoint: '))

print('Now Game is on!!!')

ans = int((startpoint + endpoint)/2.0)

while abs(ans - endpoint) >= 0.01:
	print('Is this your secret number ' + str(ans) + '?')
	res = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

	if res == 'h':
		endpoint = ans
	elif res == 'l':
		startpoint = ans
	elif res == 'c':
		break
	else:
		print('Sorry, I did not understand your input.')

	ans = int((startpoint + endpoint)/2.0)

print('Game over. Your secret number was: ' + str(ans))
