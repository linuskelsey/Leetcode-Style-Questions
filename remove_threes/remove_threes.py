def remove_threes(s):
	threes = True

	while threes:
		L = len(s)
		for i in range(L):
			if s[i] == s[i+1]:
				if s[i+1] == s[i+2]:
					a = s[i]
					s = s.replace(a, '', 3)
					continue

		threes = False

	return s

print(remove_threes('aaabbaabbbc'))