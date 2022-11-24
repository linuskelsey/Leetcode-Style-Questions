def remove_threes(s):

	def remove_first_three(s):
		for i in range(len(s)-2):
			if s[i] == s[i+1] and s[i] == s[i+2]:
				s = s[:i] + s[i+3:]
				break
		return s

	threes = True
	while threes:
		if s == remove_first_three(s):
			threes = False
		else:
			s = remove_first_three(s)

	return s