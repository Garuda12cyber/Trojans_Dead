import os,sys,time,requests
#Clean screen
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
os.system("clear")
os.system("open-url   https://youtube.com/channel/UC2ItJzPgWyihgREWErfr65g ")
logo = BB+"""
                      ..-------.`                      
                `--::-..........-:::--`                
             .-:-.`     ````````    `.-:-.             
           -:-`      ````````````       .-:-           
         -/.      ````           ````      -/.         
       `/-     `.`      `` ```       `.      :/`       
      `+.     ..         -.--         `.`     .+`      
     `o`     .`   `     `:.+.      `    ..     `+      
     +.     .`   `````  `///`      ``    .`     -/     
     o./`:/`-    ````````./o-```` ```     - -:`-/o     
    -: +`+/.`    ````...//+o//:.`````     -  +`/:+.    
    :-   ``.`     ```.`-o////+/-`````     -  ` ``/-    
    ./     `.      ``-`.+/+m+o:-.``       -      +`    
     o      -       `-`.://ss+---`       `.      o     
     ::     `.     ````...-:---..``     `-      /-     
      /-     `.     `.```./--..--`     `.      :/      
       /:     `.`   `````.:...```     ..      ::       
        -/.     ````````  ``````    ```     ./-        
         `::.      `````     ```````      .::`         
.''''''''''`-:-`       `````````       `-:-````````````
.`            .-:.```   ````````  ```::-.             `
 ..`              `.--:::::-:::::--.`              `.``
   ..`                                          `..`   
     ..```````````````````````````````````````..`     
     
    ______             _
   /_  __/________    (_)___ _____  _____
    / / / ___/ __ \  / / __ `/ __ \/ ___/
   / / / /  / /_/ / / / /_/ / / / (__  )
  /_/ /_/   \____/_/ /\__,_/_/ /_/____/
"""+G+"""FRANS-O,CONER"""+R+"""   /___/"""
     

def run(x):
	for n in x+"\n":
		sys.stdout.write(n)
		sys.stdout.flush()
		time.sleep(0.1)
def main():
	os.system('clear')
	print logo
	print
	no = raw_input(Y+"["+GL+"Masukin nomor Target"+YY+"]["+GL+"?"+YY+"]>> "+G)
	run(GL+"[!] Lagi di proses bro mohon ber sabar ...")
	run(BB+"[!] Gagal di proses mohon maaf ...")
	run(GG+"[!] Author   : Garuda12cyber ...")
        run(YY+"[!] github   : https://github.com/Garuda12cyber ...")
        run(WW+"[!] Youtube  : Garuda12cyber ...")
	run(RR+"[!] Jangan disalah gunankan script Trojan_Dead ini ...")
	run(CC+"[!] Dan Jangan lupa like,share dan subscirbe Garuda12cyber ...")
	run(B+"[!] Kembali di proses bro mohon ber sabar ...")
	run(Y+"[!] sukses di proses bro  ...")
	run(Y+"[!] sukses  ...")
	time.sleep(4)
	if no < 5:
		print R+"[!] Target Not Found"
		sys.exit()
	elif '62' in no or '+62' in no or '08' in no:
		print C+"["+W+"Lokasi"+Y+"]: "+W+"Indonesia"
		time.sleep(4)
		serang(no)
	else:
		print R+"[!] Tool Not Support "+no
		print G+"[!] Tool Support Indonesian Number"
		sys.exit()

def serang(no):
	os.system('clear')
	print logo
	print
	run(GL+"[!] Trojans_Dead ATTACK  ....")
	time.sleep(2)
	while True:
		try:
			print RR+"sukses mengirim Trojans_Dead kepada: "+YY+no
		except:
			pass

if __name__ == '__main__':
	try:
		main()
	except requests.exceptions.ConnectionError:
		print R+"[x] No Connection"
		sys.exit()
