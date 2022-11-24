def split_string(s):
	substrings=[]
	L=len(s)
	for i in range(L):
		k=0
		substr=''
		try:
			while s[i] == s[i+k]:
				substr += s[i+k]
				k+=1
			substrings.append(substr)
		except IndexError:
			substrings.append(s[i:])
		i+=k
	return substrings

print(split_string('aaabbaabbbcc'))
Lol 