def editDistance(str1, str2, a , b): 

	if a==0: #if string1 is empty insert characters from string2
		return b 
	if b==0: #if string 2 is empty insert characters from string1
		return a 
	if str1[a-1]==str2[b-1]: 
		return editDistance(str1,str2,a-1,b-1) 
		# conisder all three options if charcters are not the same
	return 1 + min(editDistance(str1, str2, a, b-1), editDistance(str1, str2, a-1, b), editDistance(str1, str2, a-1, b-1)) 
	# 				INSERT							, REMOVE						, REPLACE

# Class Exercise Example 
str1 = "BRAND"
str2 = "RANDOM"
print(editDistance(str1, str2, len(str1), len(str2)))