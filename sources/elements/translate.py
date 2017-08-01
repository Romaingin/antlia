from sources.message import log, ERROR, WARNING, OK

def toArrayOfSizes(arg):
	if arg == "":
		log(ERROR, "The specified values are incorrect")
	array = arg.split(" ")
	if array[0][-1] == "%":
		# Percentage
		type_ = "%"
		values = [float(x[:-1]) / 100.0 for x in array]
	elif array[0][-1] == "x":
		# Pixels
		type_ = "px"
		values = [int(x[:-2]) for x in array]
	else:
		print(arg)
	return values, type_
