def test(x):
	return 6*x
def my_map(func, *iterables):
	for x in range(*iterables):
		yield func(x)
		
do_test = my_map(test,6)
print(next(do_test))
print(next(do_test))
print(list(do_test))
