import requests

headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
}

print("""
        

            ___  ___   _____ 
            |  \/  |  |_   _|
            | .  . |_ __| |  
            | |\/| | '__| |  
            | |  | | |__| |_ 
            \_|  |_/_(_)___/ 
                 
                 

   
	""")
site = input("Enter your coder programmer Address : ")
coder_programmer = eval(input("Enter The number of Viewers : "))
def run():
	url = requests.get(site, headers=headers)
	url.content
	print("["+str(i)+"]" + " coder_programmer View Added")


if __name__ == '__main__':
	for i in range(coder_programmer):
		run()
    
			
			


			

