def editDistance(str1, str2, a , b): 

	if a==0: 
		return b 
	if b==0: 
		return a 
	if str1[a-1]==str2[b-1]: 
		return editDistance(str1,str2,a-1,b-1) 
	return 1 + min(editDistance(str1, str2, a, b-1), editDistance(str1, str2, a-1, b), editDistance(str1, str2, a-1, b-1)) 
	# 				INSERT							, REMOVE						, REPLACE

str1 = "BRAND"
str2 = "RANDOM"
print(editDistance(str1, str2, len(str1), len(str2)))