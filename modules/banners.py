#!/usr/bin/env python3
from random import choice
from modules.color import print_colored

def print_banner():
    banner1 = """

     █████╗ ██╗   ██╗████████╗ ██████╗ ██████╗ ██╗    ██╗███╗   ██╗    ███████╗██╗   ██╗██╗████████╗███████╗
    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗██║    ██║████╗  ██║    ██╔════╝██║   ██║██║╚══██╔══╝██╔════╝
    ███████║██║   ██║   ██║   ██║   ██║██████╔╝██║ █╗ ██║██╔██╗ ██║    ███████╗██║   ██║██║   ██║   █████╗  
    ██╔══██║██║   ██║   ██║   ██║   ██║██╔═══╝ ██║███╗██║██║╚██╗██║    ╚════██║██║   ██║██║   ██║   ██╔══╝  
    ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║     ╚███╔███╔╝██║ ╚████║    ███████║╚██████╔╝██║   ██║   ███████╗
    ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝    ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝
                                                                                                        
    """

    banner2 = """

        ___           __          ____  _       __ _   __   _____         _  __      
       /   |  __  __ / /_ ____   / __ \| |     / // | / /  / ___/ __  __ (_)/ /_ ___ 
      / /| | / / / // __// __ \ / /_/ /| | /| / //  |/ /   \__ \ / / / // // __// _ \\
     / ___ |/ /_/ // /_ / /_/ // ____/ | |/ |/ // /|  /   ___/ // /_/ // // /_ /  __/
    /_/  |_|\__,_/ \__/ \____//_/      |__/|__//_/ |_/   /____/ \__,_//_/ \__/ \___/ 

    """

    banner3 = """

     ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ██▓███   █     █░███▄    █      ██████  █    ██  ██▓▄▄▄█████▓▓█████ 
    ▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██░  ██▒▓█░ █ ░█░██ ▀█   █    ▒██    ▒  ██  ▓██▒▓██▒▓  ██▒ ▓▒▓█   ▀ 
    ▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██░ ██▓▒▒█░ █ ░█▓██  ▀█ ██▒   ░ ▓██▄   ▓██  ▒██░▒██▒▒ ▓██░ ▒░▒███   
    ░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██▄█▓▒ ▒░█░ █ ░█▓██▒  ▐▌██▒     ▒   ██▒▓▓█  ░██░░██░░ ▓██▓ ░ ▒▓█  ▄ 
     ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██▒ ░  ░░░██▒██▓▒██░   ▓██░   ▒██████▒▒▒▒█████▓ ░██░  ▒██▒ ░ ░▒████▒
     ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ▒▓▒░ ░  ░░ ▓░▒ ▒ ░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▓    ▒ ░░   ░░ ▒░ ░
      ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░▒ ░       ▒ ░ ░ ░ ░░   ░ ▒░   ░ ░▒  ░ ░░░▒░ ░ ░  ▒ ░    ░     ░ ░  ░
      ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░░         ░   ░    ░   ░ ░    ░  ░  ░   ░░░ ░ ░  ▒ ░  ░         ░   
          ░  ░   ░                  ░ ░               ░            ░          ░     ░      ░              ░  ░

    """

    banner4 = """

      @@@@@@  @@@  @@@ @@@@@@@  @@@@@@  @@@@@@@  @@@  @@@  @@@ @@@  @@@       @@@@@@ @@@  @@@ @@@ @@@@@@@ @@@@@@@@
     @@!  @@@ @@!  @@@   @@!   @@!  @@@ @@!  @@@ @@!  @@!  @@! @@!@!@@@      !@@     @@!  @@@ @@!   @@!   @@!     
     @!@!@!@! @!@  !@!   @!!   @!@  !@! @!@@!@!  @!!  !!@  @!@ @!@@!!@!       !@@!!  @!@  !@! !!@   @!!   @!!!:!  
     !!:  !!! !!:  !!!   !!:   !!:  !!! !!:       !:  !!:  !!  !!:  !!!          !:! !!:  !!! !!:   !!:   !!:     
      :   : :  :.:: :     :     : :. :   :         ::.:  :::   ::    :       ::.: :   :.:: :  :      :    : :: :::

    """

    blue = 'blue'
    cyan = 'cyan'
    green = 'green'
    yellow = 'yellow'
    red = 'red'
    bold = 'bold'

    banner = choice([
        banner1,
        banner2,
        banner3,
        banner4
    ])

    color = choice([
        blue,
        cyan,
        yellow,
        red
    ])

    print_colored("\nDeveloped by GamehunterKaan.", bold)
    print_colored("\n------------------------------------------------------------------------------------------------------------------------", bold)
    print_colored(banner, color)
    print_colored("------------------------------------------------------------------------------------------------------------------------\n", bold)
    print_colored("I am not responsible if you are doing something stupid with this tool!\n", bold)