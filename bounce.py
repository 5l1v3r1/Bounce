import subprocess
import time

target = raw_input("Enter Target IP/Hostname: ")
response = subprocess.call(["ping", "-c", "1", target])

while (response == 0):
	time.sleep(10)
	print "Bouncing:", target, "Please wait..."
	subprocess.call(["ping", "-c", "1", target])
else:
	print target, "is down."
	time.sleep(0)
