import dealssrlink
import os

def main():
	while 1 :	    
		print ("                                         ")
		print ("|---------------------------------------|")
		print ("|        ssr-script                     |")
		print ("|        author:dawn                    |")
		print ("|---------------------------------------|")
		print ("| 1. inputssrlink                       |")
		print ("| 2.choosessrnode                       |")
		print ("| 3.run service                         |")
		print ("| 4.stop service                        |")
		print ("| 5.init  software                      |")
		print ("|---------------------------------------|")
			
		num = int (input("please enter a number(represent quit is zero)  : "))
	
		if num == 1:
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
		elif num == 2:
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


	
		elif num == 3:
			os.system("bash runandstop.sh 1")
 
		elif num == 4:
			os.system("bash runandstop.sh 2")
		elif num == 5:
			os.system("bash init.sh")

		elif num == 0:
			break;

main()

