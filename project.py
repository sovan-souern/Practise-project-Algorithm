# import socket
# import platform
# import shutil

# def get_system():
#     return platform.system()


# def get_ip_address():
#     hostname = socket.gethostname()
#     ip_address = socket.gethostbyname(hostname)
#     return ip_address

# def get_divice_name():
#     return platform.node()

# def get_processor():
#     return platform.processor()


# def get_window_version():
#     return platform.version()


# def get_system_type():
#     return platform.architecture()



# def check_disk_usage():
#     system = platform.system()


#     path = "/" if system != "Windows" else "C:\\"
#     total, used, free = shutil.disk_usage(path)

#     total_gb = total / (1024 ** 3)
#     used_gb = used / (1024 ** 3)
#     free_gb = free / (1024 ** 3)

#     return total_gb, used_gb, free_gb, system

# total_gb, used_gb, free_gb, system = check_disk_usage()


# print("System:", get_system())
# print("Total: {:.2f} GB".format(total_gb))
# print("Used: {:.2f} GB".format(used_gb))
# print("Free: {:.2f} GB".format(free_gb))

# print("IP Address:", get_ip_address())
# print("Divice Name:", get_divice_name())
# print("Processor:", get_processor())
# print("Window Version:", get_window_version())
# print("System Type:", get_system_type())



# shutdown and restart computer
import os
import tkinter as tk

Mywindow = tk.Tk()
Mywindow.title("Shutdown pc")
Mywindow.geometry("500x500")
frame = tk.Frame(Mywindow, width=500, height=500)
frame.pack()
def shutdown_computer():
    os.system("shutdown /s /t 1") 

def restart_computer():
    os.system("shutdown /r /t 1")
    


Button_shutdown = tk.Button(frame, text="Shutdown", font=("Arail",10), command=shutdown_computer, bg="red",fg="white")
Button_shutdown.place(x=100,y=100, width=100, height=50)

Button_restart = tk.Button(frame, text="Restart", font=("Arail",10), command=restart_computer, bg="green",fg="white")
Button_restart.place(x=300,y=100, width=100, height=50)


Mywindow.mainloop()
