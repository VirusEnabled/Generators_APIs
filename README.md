# Generators_APIs
This directory contains a set of scripts for generating different resources as described below
<li>
PwdDicGenerator
</li>
<li>
RandomTimeGenerator
</li>
<li>
CsvGenerator
</li>
<li>
SqlScriptGenerator
</li>


## PwdDicGenerator
This is a scrpit for generataing random-secured passwords with the given parameters.
This program is console based and it will return a file with the specified amount of passwords.

It takes the following positional arguments:
* gtype: {w,n,a,s-w,s-n,s-a} 
	* w: for just words 
	* n: for numbers 
	* a: for alphanumeric
	* s-w: for scale with just words 
	* s-n: for scale with just numbers 
	* s-a: for scale with alphanumeric including symbols
* file_name :name of the file to be generated
* file_path :path to store the file
* pwd_amount: amount of passwords to be generated
* ending_length: full lenght of the password.
