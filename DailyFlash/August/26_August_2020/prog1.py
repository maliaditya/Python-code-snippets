import psutil 
print("Process Name".ljust(30), "Id" )
print()

for proc in psutil.process_iter():
    try:
        process_name = proc.name()
        process_id = proc.pid
        print(process_name.ljust(30), process_id )
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass