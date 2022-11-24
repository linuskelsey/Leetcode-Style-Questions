def split_string(s):
	substrings=[]
	L=len(s)
	for i in range(L):
		if s:
			k=0
			substr=''
			try:
				while s[0] == s[k]:
					substr+=s[k]
					k+=1
			except IndexError:
				substrings.append(s)
			s=s[k:]
			substrings.append(substr)
	return substrings[:-1]

print(split_string('aaabbaabbbcca'))