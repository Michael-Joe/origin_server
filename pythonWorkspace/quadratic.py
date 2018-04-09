# -*- coding:utf-8 -*-

import math

def quadratic(a,b,c):
	if not isinstance(a,(int,float)):
		return TypeError('Bad operand type')
	if not isinstance(b,(int,float)):
		return TypeError('Bad operand type')
	if not isinstance(c,(int,float)):
		return TypeError('Bad operand type')
	if (b*b-4*a*c) < 0:
		print("方程无解")
	else:
		x1 = (-b-math.sqrt(b*b - 4*a*c )) / (2 * a)
		x2 = (-b+math.sqrt(b*b - 4*a*c )) / (2 * a)
		return x1,x2

print(quadratic(2,3,1))

print(quadratic(1,3,-4))
