from rich import *
from rich.highlighter import Highlighter
from random import *
from pystyle import Colors,Write
import ctypes
import os
from colorama import Back,Fore
from rich.console import Console

console = Console()


while True:
 os.system('cmd /c "cls"')
 ctypes.windll.kernel32.SetConsoleTitleW("HAZARD-Free Copy 1.2-Help")
 print("   ")
 print("                                                           v 1.2 ")
 print("                                              [green]██╗  ██╗███████╗██╗     ██████╗ [/green]                            [yellow]For[/yellow] [green]My[/green] [red]People[/red]")
 print("                                              [green]██║  ██║██╔════╝██║     ██╔══██╗[/green]")
 print("[green]created by:[/green] [yellow]HaZaRd#4058[/yellow][white]                       ███████║██[yellow]███╗  ██║    [/yellow] ██████╔╝")
 print("                                              ██╔══██║██[yellow]╔══╝  ██║ [/yellow]    ██╔═══╝ ")
 print("                                              [red]██║  ██║███████╗███████╗██║     [/red]")
 print("                                              [red]╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     [/red]")
 print("   ")
 class RainbowHighlighter(Highlighter):
     def highlight(self, text):  
         for index in range(len(text)):
             text.stylize(f"color({randint(12, 255)})", index, index + 1)


 rainbow = RainbowHighlighter()
 print(rainbow("                                                      IRAN ON TOP!"))


 Write.Print("**free exit: ALT + F4**", Colors.blue_to_cyan, interval=0.02)

 print()
 console.print("Which option do you want more information about? Select it\n", style="red on white")
 Write.Print("------------------------------------------------------------------------------------------------------------------------\n", Colors.blue, interval=0.009)
 print("║[blue]01[/blue]║ : Copy Router Pass                                    ║[blue]09[/blue]║ : free all copy")
 print("║[blue]02[/blue]║ : Google Pass Copy                                    ")
 print("║[blue]03[/blue]║ : Google History Copy                                  ")
 print("║[blue]04[/blue]║ : Copy Time & Loc                                      ")
 print("║[blue]05[/blue]║ : Windows Copy Information                                ")
 print("║[blue]06[/blue]║ : Ipconfig Copy                                 ")
 print("║[blue]07[/blue]║ : Make TxT File For Save                     ")
 print("║[blue]08[/blue]║ : Connect To Wifi                                  ")
 choice=input("--->")

 if choice == "1":
    print("""
Steal all Wi-Fi passwords!
When a person connects to the wireless internet on his PC
All router information is recorded in the network card!
So there is definitely a way to find it and use it :)
[green]Just enter the number 1 ([/green]║[blue]01[/blue]║ : Copy Router Pass[green]) and wait until you find all the Wi-Fis of the victim's system already connected to it[/green].
[cyan]Then you can press the number 1([/cyan]║[red]01[/red]║ : Save[cyan]) to save it in a text file.[/cyan]
[cyan]And to return to the menu number 2([/cyan]║[red]02[/red]║ : Back to Menu[cyan]).[/cyan]
[cyan]Press the number 3([/cyan]║[red]03[/red]║ : Exit[cyan]) to exit.[/cyan]
""")
    try:
       input("Press a key to return to the menu...")
    except:
       pass
 elif choice == "2":
    print("""
Perhaps, when you are creating a new account in Google Chrome, you will see a message asking you: Do you want to save the information?
Well, after pressing the yes button, your information will be saved in a separate file
But this file is encrypted!
But don't worry because we can crack that file and give you all the passwords
[green]Just press number 2 ([/green]║[blue]02[/blue]║ : Google Pass Copy[green])and wait for the result:)[/green]
[red]Note:[/red] This feature is not yet available on all systems[red]:([/red]    
""")
    try:
       input("Press a key to return to the menu...")
    except:
       pass
 elif choice == "3":
    print("""
Get all the victim searches on Google! Even [black on yellow]por*hub[/black on yellow] [magenta]XD[/magenta]
When you enter the search section in Google Chrome, you can see all your recent searches. So these are definitely stored somewhere!
[green]You can access all the recent searches of your target by pressing button 3 ([/green]║[blue]03[/blue]║ : Google History Copy[green]) in our tool :)[/green]
[red]Note:[/red] This mode is not yet applicable on all devices [red]:(  [/red]  
""")
    try:
       input("Press a key to return to the menu...")
    except:
       pass
 elif choice == "4":
    print("""
logger?
[green]Just by pressing the number 4([/green]║[blue]04[/blue]║ : Copy Time & Loc[green]), you can copy the time, IP and country of the victim's system.[/green]
[red]Note:[/red] This work requires internet! 
To save information in a text file number 1(║[red]01[/red]║ : Save)
Back to menu number 2(║[red]02[/red]║ : Back to Menu")
To exit the program number 3(║[red]03[/red]║ : Exit)   
""")
    try:
       input("Press a key to return to the menu...")
    except:
       pass
 elif choice == "5":
    print("""
Get all the information about the new victim system!
You need a lot of time to get a lot of information from the system
And this method is not recommended for theft because it is very slow and the police will quickly arrest you!
But in this tool, we have put all the commands one after the other to increase the speed of your work.
[green]Just press 5([/green]║[blue]05[/blue]║ : Windows Copy Information[green]) and the tool will automatically start copying your data.[/green]
To save information in a text file number 1(║[red]01[/red]║ : Save)
Back to menu number 2(║[red]02[/red]║ : Back to Menu")
To exit the program number 3(║[red]03[/red]║ : Exit)
""")
    try:
       input("Press a key to return to the menu...")
    except:
       pass
 elif choice == "6":
   print("""
Well, my friend? What do you think? The most important rule of hackers? Hide IP
But this tool helps to easily copy the victim's IP system :)
[green]Press the number 6([/green]║[blue]06[/blue]║ : Ipconfig Copyp[green]) and wait for the result of the tool.[/green]
To save that number 1(║[red]01[/red]║ : Save)
To return to the menu number 2(║[red]02[/red]║ : Back to Menu")
And to remove the number 3(║[red]03[/red]║ : Exit)
""")
   try:
       input("Press a key to return to the menu...")
   except:
       pass
 elif choice == "7":
    print("""
In some versions of Python, there are bugs in saving and creating files
And we chose this option for people who use these versions
[green]Press number 7([/green]║[blue]07[/blue]║ : Make TxT File For Save[green])[green]   
""")
    try:
       input("Press a key to return to the menu...")
    except:
       pass
 elif choice == "8":
    print("""
Having internet everywhere is one of our basic needs
And we should always think about this!
Well, you can use the information of the victim's system to connect to Wi-Fi whose information is stored in the system
[green]Just press the number 8([/green]║[blue]08[/blue]║ : Connect To Wifi [green]) and then enter the wifi name or ssid in the wifi name field.[/green]
""")
    try:
       input("Press a key to return to the menu...")
    except:
       pass
 elif choice == "9":
    print("""
Hey carefree man:| Have you ever copied the information one by one????? why are you so weird
[green]Just press the number 9([/green]║[blue]09[/blue]║ : free all copy[green]) and copy all information ([/green][yellow]Time & Loc[/yellow], [red]Router Pass[/red], [blue]Windows Information[/blue], [magenta]Ipconfig Copy[/magenta]).
""")
    try:
       input("Press a key to return to the menu...")
    except:
       pass
 else:
    print("[red]The command is not defined[/red]")