import time 
import random

print("-" * 70)
print("Magic 8 Ball")
print()

question = input("What is your question? ")
print()
time.sleep(0.8)
print("...thinking...")
print()
time.sleep(0.8)
print("...thinking...")
print()
time.sleep(0.8)
print("...thinking...")
print()

choice = random.randint(1,4)

if choice == 1:
	print("What ever feels right buddy")
elif choice == 2:
	print("Go for it!!!!")
elif choice == 3:
	print("I wouldn't do that if I were you")
else:
	print("Yeah...No")
