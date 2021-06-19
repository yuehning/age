driving = input('請問你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age < 18:
		print('你違法了!!')
	else:
		print('好, 沒事')
elif driving == '沒有':
	if age < 18:
		print('滿18再去考駕照')	
	else:
		print('路上小心喔')	