import os

def Scanner_Ping(): 
    url = input("Insira a Url do site: ")
    os.system(f"ping -c 8 {url}")

Scanner_Ping()
