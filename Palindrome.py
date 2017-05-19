s = "kek"
s = s.lower()
rev_s = reversed(s)

if list(s) == list(rev_s):
	print("It is palindrome")
else:
	print("It is not palindrome")