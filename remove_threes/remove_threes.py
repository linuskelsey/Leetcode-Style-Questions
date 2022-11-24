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

def remove_threes(s):
	strings = split_string(s)
	for string in strings:
		if len(string) >= 3:
			strings.remove(string)
	return ''.join(strings)