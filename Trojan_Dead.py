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
os.system("termux-open-url  https://youtube.com/channel/UC5qaTtGpIDZABVOSKwKcYtQ  ")
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
	run(GL+"[!] Lagi di proses bro mohon bersabar ")
	run(GL+"[!] masih di proses bro mohon bersabar ")
	run(BB+"[!] Gagal di proses mohon maaf ")
	run(CC+"[!] Tools ini hanya bisa digunakan di terminal linux ")
	run(YY+"[!] tidak bisa digunakan di termux ")
	run(RR+"[!] Tools ini bisa mengirim trojan sampai 41 negara nomor whatsapp ")
	run(GG+"[!] terserah kalian mau mengirim trojan ke nomor negara yang mana ")
	run(GG+"[!] Author   : Garuda12cyber ")
        run(YY+"[!] github   : https://github.com/Garuda12cyber ")
        run(WW+"[!] Youtube  : Garuda12cyber ")
	run(RR+"[!] Hargailah yang membuat script ini ")
	run(CC+"[!] Dan Jangan lupa like,share dan subscirbe chenel Garuda12cyber ")
	run(B+"[!] Kembali di proses bro mohon ber sabar ")
	run(Y+"[!] sukses di proses bro ")
	run(Y+"[!] sukses ")
	time.sleep(4)
	if no < 5:
		print R+"[!] Target Not Found"
		sys.exit()
	elif '+1' in no or '+7' in no or '+17' in no or '+20' in no or '+212' in no or '+213' in no or '+218' in no or '+30' in no or '+31' in no or '+33' in no or '+34' in no or '+380' in no or '+41' in no or '+44' in no or '+47' in no or '+48' in no or '+49' in no or '+55' in no or '+58' in no or '+60' in no or '+61' in no or '+62' in no or '+63' in no or '+65' in no or '+66' in no or '+81' in no or '+82' in no or '+85' in no or '+86' in no or '+886' in no or '+90' in no or '+91' in no or '+92' in no or '+95' in no or '+962' in no or '+966' in no or '+970' in no or '+971' in no or '+974' in no or '+98' in no or '+972' in no:
		print C+"["+W+"Lokasi"+Y+"]: "+W+"41 code country number"
		time.sleep(4)
		serang(no)
	else:
		print R+"[!] Tool Not Support "+no
		print G+"[!] Tool Support 41 code country Number"
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
