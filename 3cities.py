f = input()
s = input()
t = input()
fl = len(f)
sl = len(s)
tl = len(t)
if min(fl, sl, tl) == fl:
	print(f)
if min(fl, sl, tl) == sl:
	print(s)
if min(fl, sl, tl) == tl:
	print(t)
if max(fl, sl, tl) == fl:
	print(f)
if max(fl, sl, tl) == sl:
	print(s)
if max(fl, sl, tl) == tl:
	print(t)
