import random

WORDS=['one','two','three','four','five']

def Random_WORD():
	kword=WORDS[random.randint(0,len(WORDS)-1)]
	rword=list(kword)
	random.shuffle(rword)
	return ''.join(rword),kword #列表轉字串



def guess():
	Guess_word=Random_WORD()
	print(Guess_word[0])
	input_word=input('GUESS THE WORD:')
	while 1:
		if input_word==Guess_word[1]:
			print('Correct!')
			break
		else:input_word=input('Wrong, try again: ')
	return


while 1:
	guess()
	isContinue=input('Continue? (Press any key except "n/N" to continue, press "n/N" to quit): ')
	if isContinue=='n' or isContinue=='N':
		break
