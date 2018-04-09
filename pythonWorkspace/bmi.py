# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5

bmi = weight/(height * height)

print ('bmi:',bmi)

if bmi < 18.5:
	print ('too thin')
elif bmi < 25:
	print ('normal')
elif bmi < 32:
	print ('too fat')
else:
	print ('very fat')
