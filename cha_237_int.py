#[2015-10-14] Challenge #236[Intermediate] Fibonacci-ish Sequence
fn= int(input("Enter a number: "))


def get_fib_seq(fn):
	fib_seq = [0,1]
	while  fib_seq[-1] < fn:
		fib_seq.append(fib_seq[-1]+fib_seq[-2])
	return fib_seq

fib_seq = get_fib_seq(fn)

f1 = 1
for n in fib_seq[1:]:
	if fn%n == 0:
		f1 = fn/n
print [x*f1 for x in fib_seq if x*f1 <=fn]

