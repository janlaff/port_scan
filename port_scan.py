#!/usr/bin/python3

from socket import *
import sys

def scan_host(host, port, r_code = 1):
	try:
		s = socket(AF_INET, SOCK_STREAM)
		code = s.connect((host, port))

		if code == 0:
			r_code = 0

		s.close()
	except Exception:
		pass

	return r_code

host = ""
max_port = 5000
min_port = 1

try:
	host = input("[*] Enter target host address: ")
	hostip = gethostbyname(host)
	print("[*] Starting port scan on " + hostip)

	for port in range(min_port, max_port):
		try:
			response = scan_host(host, port)
			
			if response == 0:
				print("[*] Port %d open" % port)
		except Exception:
			print("[*] Finished scan with errors")
			sys.exit(1)
	print("[*] Finished scan")
except KeyboardInterrupt:
	print("\n\n[*] User requested an interrupt")
	print("[*] Application shutting down")
	sys.exit(0)
