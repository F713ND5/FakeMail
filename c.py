# coding:utf8
# coded by: Rizky ID | hekelpro
import os, requests
os.system('clear')
print '\x1b[1;97m'
froE = raw_input('Masukan Email Pengirim : ')
froN = raw_input('Masukan Nama Pengirim  : ')
froT = raw_input('Masukan Email Penerima : ')
froS = raw_input('Masukan Subject/Title  : ')
froM = raw_input('Masukan Pesan Anda     : ')
url = 'https://rajajatuhcinta.000webhostapp.com/email-script.php'
data = {
        'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36',
        'fromEmail':froE,
        'fromName':froN,
        'toEmail':froT,
        'subject':froS,
        'message':froM,
        'sendMailBtn':''
        }
requests.post(url,data,allow_redirects=True)
print 'Berhasil ....'
