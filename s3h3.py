# Mehdi Najmi- Thursday 14-18
# Geometric calculation base on given shape
def geometric_calculation(length,width,request,shape):
	if request=='area' and shape=='rectangle':
		print(' area is equal to:', float(length)*float(width))
	elif request=='space' and shape=='rectangle':
		print(' space is equal to:', (float((length)+float(width))*2))
	elif request=='area' and shape=='square':
		print(' area is equal to:' ,float(length)*float(width))
	elif request=='space' and shape=='square':
		print(' area is equal to:' ,float(length)*4)
	elif request=='area' and shape=='diamond':
		print(' area is equal to:',(float(length)*float(width))/2)
	elif request=='space' and shape=='diamond':
		print(' area is equal to:', float(length)*4)
