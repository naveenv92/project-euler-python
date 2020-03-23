### Problem 25
###---------------------------------------------------------------------------------------
### Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
### Hence the first 12 terms will be:
### F1 = 1
### F2 = 1
### F3 = 2
### F4 = 3
### F5 = 5
### F6 = 8
### F7 = 13
### F8 = 21
### F9 = 34
### F10 = 55
### F11 = 89
### F12 = 144
### The 12th term, F12, is the first term to contain three digits.
### What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

### Solution

f = 1
f_prev = 1

currentIndex = 2

while True:
	currentIndex += 1
	f_temp = f
	f = f + f_prev
	f_prev = f_temp

	if len(str(f)) == 1000:
		break

print("First Fibonacci term with 1000 digits: " + str(currentIndex))