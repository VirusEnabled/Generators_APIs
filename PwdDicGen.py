import os,random,argparse

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
			 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z', 
			 ]
special_characters = ['_','-','ç','^','·',';',':','<','?','>','\/','|','~',
					'!','@','#','$','-%-','^','&','*','-','+','^',"<",">",
					"=","'","`","(",")"]
upcase_alphabet = [x.upper() for x in alphabet]
numbers = [num for num in range(0,10)]
all_in_one = [alphabet,upcase_alphabet,numbers,special_characters]
just_words = [alphabet,upcase_alphabet]

class PwdFileGenerator(object):
	def __init__(self,file_name,file_path,pwd_amount,ending_len):
		self.file_name  =  file_name
		self.file_path  =  file_path
		self.pwd_amount =  pwd_amount
		self.ending_len =  ending_len

	def all_numbers_gen(self):
		"""
		Returns a file on the given location with 
		the given amount of passwords with the given
		chars per password.
		"""
		number_stopper = 0
		pwd_file = open("%s/%s.txt"%(self.file_path,self.file_name),"a+")
		while number_stopper < self.pwd_amount:
			g_number = ""
			while len(g_number) < self.ending_len:
				ran_num = random.randrange(len(numbers))
				g_number += str(numbers[ran_num])
			else:
				pwd_file.write(g_number+"\n")
			number_stopper += 1
		else:
			print("File %s Generated at %s"%(self.file_name,self.file_path))

	def all_letters_gen(self):

		word_stopper = 0
		pwd_file = open("%s/%s.txt"%(self.file_path,self.file_name),"a+")
		while word_stopper < self.pwd_amount:
			g_word = ""
			while len(g_word) < self.ending_len:
			#for number in range(1,self.ending_len + 1):
				ran_select = just_words[random.randrange(len(just_words))]
				ran_num = random.randrange(len(ran_select))
				g_word += ran_select[ran_num]
			else:
				pwd_file.write(g_word+"\n")
			word_stopper += 1
		else:
			print("File %s Generated at %s"%(self.file_name,self.file_path))

	def prime_gen(self):
		"""
		Returns a file on the given location with 
		the given amount of passwords with the given
		chars per password.
		"""
		stopper = 0
		pwd_file = open("%s/%s.txt"%(self.file_path,self.file_name),"a+")
		while stopper < self.pwd_amount:
			g_word = ""
			while len(g_word) < self.ending_len:
			#for number in range(1,self.ending_len + 1):
				ran_select = all_in_one[random.randrange(len(all_in_one))]
				ran_num = random.randrange(len(ran_select))
				g_word += str(ran_select[ran_num])
			else:
				pwd_file.write(g_word+"\n")
			stopper += 1
		else:
			print("File %s Generated at %s"%(self.file_name,self.file_path))
	
	def scale_a_gen(self):
		"""
		returns a dictionary file
		changing the length of the passwords.
		in the range number provided.
		type ~> provides the type of password to generate
		by deafult the type is ap == alphanumeric (symbols,words and numbers)
		"""
		scale_stopper = 0
		pwd_file = open("%s/%s.txt"%(self.file_path,self.file_name),"a+")
		while scale_stopper < self.pwd_amount:
			#while len(g_word) < self.ending_len:
			for number in range(self.ending_len + 1):
				g_word = ""
				for another in range(number):
					ran_select = all_in_one[random.randrange(len(all_in_one))]
					ran_num = random.randrange(len(ran_select))
					g_word += str(ran_select[ran_num])
				pwd_file.write(g_word+"\n")
				scale_stopper += 1
		else:
			print("File %s Generated at %s"%(self.file_name,self.file_path))

	def scale_number_gen(self):
		"""
		returns a dictionary file
		changing the length of the passwords.
		in the range number provided.
		type ~> provides the type of password to generate
		by deafult the type is ap == alphanumeric (symbols,words and numbers)
		"""
		scale_stopper = 0
		pwd_file = open("%s/%s.txt"%(self.file_path,self.file_name),"a+")
		while scale_stopper < self.pwd_amount:
			#while len(g_word) < self.ending_len:
			for number in range(self.ending_len + 1):
				g_number = ""
				for another in range(number):
					ran_num = random.randrange(len(numbers))
					g_number += str(numbers[ran_num])
				pwd_file.write(g_number+"\n")
				scale_stopper += 1
		else:
			print("File %s Generated at %s"%(self.file_name,self.file_path))

	def scale_word_gen(self):
		"""
		returns a dictionary file
		changing the length of the passwords.
		in the range number provided.
		type ~> provides the type of password to generate
		by deafult the type is ap == alphanumeric (symbols,words and numbers)
		"""
		scale_stopper = 0
		pwd_file = open("%s/%s.txt"%(self.file_path,self.file_name),"a+")
		while scale_stopper < self.pwd_amount:
			#while len(g_word) < self.ending_len:
			for number in range(self.ending_len + 1):
				g_word = ""
				for another in range(number):
					ran_select = just_words[random.randrange(len(just_words))]
					ran_num = random.randrange(len(ran_select))
					g_word += ran_select[ran_num]
				pwd_file.write(g_word+"\n")
				scale_stopper += 1
		else:
			print("File %s Generated at %s"%(self.file_name,self.file_path))

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("gtype",help="""chooses the type of password generated; 
		w: for just words, n for numbers, a for alphanumeric, s-w for scale with just words,
		 s-n for scale with just numbers, s-a for scale with alphanumeric including symbols
		""",choices=["w","n","a","s-w","s-n","s-a"],type=str)
	parser.add_argument("file_name",help="name of the file to be generated")
	parser.add_argument("file_path",help="path to store the file")
	parser.add_argument("pwd_amount",help="amount of passwords to be generated",type=int,default=100)
	parser.add_argument("ending_length",help="full lenght of the password" ,type=int,default=8 )
	p_g = parser.parse_args()
	gen = PwdFileGenerator(p_g.file_name,p_g.file_path,p_g.pwd_amount,p_g.ending_length)
	
	if p_g.gtype == "w":
		gen.all_letters_gen()
	elif p_g.gtype == "n":
		gen.all_numbers_gen()
	elif p_g.gtype == "a":	
		gen.prime_gen()
	elif p_g.gtype == "s-w":
		gen.scale_word_gen()
	elif p_g.gtype == "s-n":
		gen.scale_number_gen()
	elif p_g.gtype == "s-a":
		gen.scale_a_gen()

if __name__ == '__main__':
	main()