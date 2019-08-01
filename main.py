import dealssrlink
import os

import sys
def help():
		print ("SSR-script version 1.0.1  ( author:dawn)")
		print("usage: python3 main.py -h  [help]")
		print("usage: python3 main.py -S  [SSRNode]")
		print("usage: python3 main.py -l  [list of ssrNode]")
		print("usage: python3 main.py -r  [run]")
		print("usage: python3 main.py -s  [stop]")
		print("usage: python3 main.py- i  [install SSR]")

def main():

			
	if len(sys.argv)==1:	
		help()
	
	elif len(sys.argv)==2:
		if sys.argv[1] == "-h":
			help()
		if sys.argv[1] == "-S":
			s = input("please enter ssr node : ")
			is_ss = s.find('ss://')
			is_ssr = s.find('ssr://')
			if is_ss != -1:
				ss = s[is_ss:].strip()
				dealssrlink.decode_ss(ss)
			elif is_ssr != -1:
				ssr = s[is_ssr:].strip()
				
				dealssrlink.decode_ssr(ssr)
			else:
				print("ssr node is worse !!!")

		if sys.argv[1] == "-l":
			employee_file = open("config/shadowsocks.json", "r") 
 
			for employee in employee_file.readlines():
				spilted = employee.split('//')  
			print ("-----------------------------")
			print ("|     ssr node              |")
			i=0
			for ipaddresschoose in range(0,len(spilted)):
				i = i+1
				solverange = ipaddresschoose
				ipaddress = spilted[solverange].split('server": \"')
				ipaddress = ipaddress[1].split('",')
				print ("-----------------------------")
				print ("* "+str(i)+ ". "+ipaddress[0] + "        ")
	
			print ("-----------------------------")    
			employee_file.close()
			userchoosenode = employee.split('//')
			while 1:
				choosenodenum = int (input ("please enter a number to choice a ssr node :"))
				testvalue = 0
				
				employee_filebychoice = open("/etc/shadowsocks.json", "w")
				for ipaddresschoose in range(0,len(spilted)):
					ipaddresschoose = ipaddresschoose + 1
					if choosenodenum == ipaddresschoose:    
						employee_filebychoice.write(userchoosenode[choosenodenum-1])
						testvalue = 1;
				if testvalue == 1 :
					print("	choice success ")
					break;
				else :
					print("	Invail value")
			employee_filebychoice.close()


	
		if sys.argv[1] == "-r":
			os.system("bash runandstop.sh 1")
 
		if sys.argv[1] == "-s":
			os.system("bash runandstop.sh 2")
		if sys.argv[1] == "-i":
			os.system("bash init.sh")



main()

