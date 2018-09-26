import os, sys, argparse, statistics as stds, random as rm

FILE_NOTATION = "_timegen.txt"
file_divider = "/"
if sys.platform != "linux":
	file_divider = "\\"

class RandomTimeGen(object):
	"""docstring for RandomTimeGen"""
	def __init__(self, amount, min_l, max_l, msec_min, msec_max, file_name, main_path):
		self.amount = amount
		self.min_l = min_l
		self.max_l = max_l
		self.msec_min = msec_min
		self.msec_max = msec_max
		self.file_name = file_name
		self.main_path = main_path


	def time_gen(self):
		""" returns a file with random numbers depending of the values provided. """
		result = []
		item_indexer = ""
		for element in range(self.amount):
			second = str(rm.randrange(self.min_l,self.max_l))
			microsecond = str(rm.randrange(self.msec_min,self.msec_max))
			item_indexer = second +'.'+microsecond
			result.append(item_indexer)
		else:
			file = open("%s%s%s"%(self.main_path,file_divider,self.file_name+FILE_NOTATION),"w")
			for item in result:
				file.write(item+'\n')
			else:
				file.close()
				return print("COMPLETED")

	def data_verifier(self,data):
		#  returns bool whether it's good to be calculated or not
		for char in data:
			if '-' in char or "=" in char:
				return False
		else:
			return True
		
	def time_calculator(self):
		# returns amount of values, average, min and max of the values
		carpet = os.listdir(self.main_path)
		final = []
		for file in carpet:
			data = open("%s%s%s"%(self.main_path,file_divider,file),"r+").read().split("\n")
			if not self.data_verifier(data):
				return print("The time in this file has been already calculated.")
			data = [float(x) for x in data if not x.isspace() and x is not "\n" and x ]
			min_amount = str(min(data))+" segundos"
			max_amount = str(max(data))+" segundos"
			total = len(data)
			mean = str(stds.mean(data))+" segundos"
			fill_d= {"Total entradas":total,
			"Valor Promedio":mean,"Valor min":min_amount,"Valor max":max_amount}
			with open("%s%s%s"%(self.main_path,file_divider,file),"a+") as file_opened:
				file_opened.write("\n --------- Results --------\n")
				for key in fill_d.keys():
					file_opened.write("%s = %s \n"%(key,fill_d[key]))
				else:
					file_opened.close()

			final.append(fill_d)
		else:
			return print(final)

def getting_time_gen():
	parser = argparse.ArgumentParser()
	parser.add_argument("option", choices=["time_generate","calculate_time","full_generate"],\
	 help="time_generate: just generates time files \n \
	 calculate_time: just calculates times files in existing files\ full_generate: generates time files\
	  and calculates statistical values.")
	parser.add_argument("amount",help="the amount of numbers you need",type=int)
	parser.add_argument('min_l',help="min amount of seconds",type=int)
	parser.add_argument('max_l',help="max amount of seconds",type=int)
	parser.add_argument('msec_min',help="min amount of microseconds",type=int)
	parser.add_argument('msec_max',help="max amount of microseconds",type=int)
	parser.add_argument('filedst',help="name and path of the file to write the time",type=str)
	parser.add_argument('main_path', help="main directory to read time files",type=str)
	parsed = parser.parse_args()
	time_generator = RandomTimeGen(parsed.amount, parsed.min_l, parsed.max_l, parsed.msec_min, \
		parsed.msec_max, parsed.filedst, parsed.main_path)
	if parsed.option == "time_generate":
		time_generator.time_gen()
	
	elif parsed.option == "calculate_time":
		time_generator.time_calculator()

	elif parsed.option == "full_generate":
		time_generator.time_gen()
		time_generator.time_calculator()

def main():
	getting_time_gen() 
	pass

if __name__ == '__main__':
	main()



