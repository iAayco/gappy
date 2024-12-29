coder = 'Aayco'
version = 1.0
github = '@iAayco'

from os import system
try:
    #We Will Use Requests Module In This Code
    from requests import get
    from requests import post
except ImportError:
    #Install Requests Module If Not Installed (Or You Can Just Install It By Yourself It's Not That Hard!!)
    system('pip install requests')    

#This Class Will Contain Module The Functions
class Proxy:
    #Function To Generate Proxies From User Inputed Protocol ex(generate_proxies('https'))
    def generate_proxies(protocol):
        try:
            #The Proxyscrape Api
            url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={protocol}&timeout=10000&country=all&ssl=all&anonymity=all"
            #Get Proxies From Api
            proxies = get(url).text.split('\n')
            #Return Generated Proxies
            return proxies
        except Exception as e:
            #Error Handling
            print(e)
    
    def check_proxy(proxy):
        try:
            #Test The Proxy By Send Request To Any Website Using It ex(response = 200 (work))
            response = post("https://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=5)
            #Check If Response Code Is 200 Or Not
            if response.status_code == 200:
                #Return True If Work
                return True
            else:
                #Return False If Not Work
                return False
        except Exception as e:
            #I Told You Before It's Error Handling
            print(e)
    
    def generate_check(protocol):
        try:
            #The Proxyscrape Api
            url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={protocol}&timeout=10000&country=all&ssl=all&anonymity=all"
            #Get Proxies From Api
            proxies = get(url).text.split('\n')
            #Get Every Proxy From Proxies List
            for proxy in proxies:
                try:
                    #Test Every Proxy We Get From Api
                    response = post("https://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=5)
                    #Check If Response Code Is 200 Or Not
                    if response.status_code == 200:
                        #Return Worked Proxy
                        return proxy
                    else:
                        #Pass If Response Code Is Not 200 ex(401,403,404,etc)
                        pass
                except Exception as e:
                    #How Many Times Should I Told You It's Error Handling!!
                    print(e)
        except Exception as e:
            print(e)
    
    def help():
        #Print Simple Info About Module Functions
        print(f'Module Version Is {version}\ngenerate_proxies -> Generate Proxies\ncheck_proxy -> Check Proxy\ngenerate_check -> Generate Proxies And Check It\nhelp -> Print Help Message\ninfo -> Print Module Info')
    
    def info():
        #Print Simple Info About Module Coder (Me:3)
        print('Coder Is {}\nModule Version {}\nGithub Username {}').format(coder,version,github)
