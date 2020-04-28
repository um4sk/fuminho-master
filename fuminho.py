import os
import socket
import sys
import time
os.system('apt install curl -y')
os.system('apt install figlet -y')
os.system('cls||clear')
print "########################################################################"
os.system('figlet fuminho.py')
print ""
print "coded by > um4sk"
print "########################################################################"
print ""
print "      [  MENU  ]      "
print ""
print "      [ 1 ] whois"
print "      [ 2 ] header check"
print "      [ 3 ] Port Scan"
print "      [ 4 ] Subdomains check"
print "      [ 0 ] Quit"
print ""
op1 = int(input('> '))
if op1 == 1:
	os.system('cls||clear')
	print "##########################"
	print "#!         WHOIS        !#"
	print "##########################"
	print ""
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	url = raw_input('alvo: ')
	host = "200.160.2.3"
	port = 43
	s.connect((host, port))
	
	s.send(url+"\r\n")
	
	resposta = s.recv(1024)
	print "###########! CONSULTA WHOIS !################"
	print ""
	print resposta
	print ""
	print "#############################################"
if op1 == 2:
	os.system('cls||clear')
	print "##########################"
        print "#!     HEADER CHECK     !#"
        print "##########################"
        print ""
	url = raw_input('alvo: ')
	print "#############################################"
	print ""
	os.system('curl --head {}'.format(url))
	print ""
	print "#############################################"
	exit()
if op1 == 3:
	os.system('cls||clear')
	print "##########################"
        print "#!       PORT SCAN      !#"
        print "##########################"
        print ""
	url = raw_input('alvo: ')
	porta = int(input('Digite uma porta: '))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.5)
	try:
		s.connect((url, porta))
		s.send('fuminho.py\r\n')
		resposta = s.recv(100)
		print(">> PORTA: [ "+str(porta)+" ] ABERTA!")
	except:
		print(">> PORTA: [ "+str(porta)+" ] FECHADA!")
	finally:
		s.close
		exit()
if op1 == 4:
	os.system('cls||clear')
	print "##########################"
        print "#!   SUBDOMAINS CHECK   !#"
        print "##########################"
        print ""
	url = raw_input('alvo: ')
	print ""
	print "#############! SUB DOMAINS !#################"
	print ""
	os.system('dig {} +noall +answer'.format(url))
	print ""
	print "#############################################"
	exit()
