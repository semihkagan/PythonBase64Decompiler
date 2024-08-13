# https:#github.com/semihkagan/PythonLogger
# Lütfe#yorum satırlarını silmeyin :/ ❤️
from datetime import datetime
from colorama import Fore, init
import zipfile
import shutil
import os

init(autoreset=True)

def _stack_file(file_path, target_folder):

    if not os.path.isfile(file_path):
        return False

    index = file_path.find('.')
    if index != -1:
        result = file_path[:index]
    else:
        result = file_path 

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_file_path = f"{result}_{timestamp}.zip"
    
    try:
        with zipfile.ZipFile(zip_file_path, 'w') as zipf:
            zipf.write(file_path, os.path.basename(file_path))

        shutil.move(zip_file_path, os.path.join(target_folder, os.path.basename(zip_file_path)))
        os.remove(file_path)

        return True
    except:
        return False

class Logger:
    def __init__(self, stack_mode=False, file_name="log.log",logs_folder="logs"):
        self.file_name = file_name
        self.stack_mode = stack_mode
        self.logs_folder_path = logs_folder
        
        if(self.stack_mode):
            if not os.path.exists(logs_folder):
                os.makedirs(logs_folder)
            _stack_file(file_name,logs_folder)
    
    def log(self, text = "log.log"):
        try:
            with open(self.file_name, "a") as f:
                f.write("[{0}] {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), text))
                print(text)
        except FileNotFoundError:
            print(Fore.RED + "[ERROR/Logger] Log file or path not found!")
        except:
            print(Fore.RED + "[ERROR/Logger] An logger exception occurre")

    def info(self, text= "log.log"):
        try:
            with open(self.file_name, "a") as f:
                f.write("[{0}] {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"),"[INFO] "  + text))
                print(Fore.BLUE + text)
        except FileNotFoundError:
            print(Fore.RED + "[ERROR/Logger] Log file or path not found!")
        except:
            print(Fore.RED + "[ERROR/Logger] An logger exception occurre")
    
    def err(self,text= "log.log",err_type=""):
        try:
            with open(self.file_name, "a") as f:
                if(err_type == "" or err_type == " "):
                    f.write("[{0}] {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"),"[ERROR] "  + text))
                    print(Fore.RED + "[ERROR] " + text)
                else:
                    f.write("[{0}] {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"),"[ERROR/" + err_type + "] "  + text))
                    print(Fore.RED + "[ERROR/" + err_type + "] " + text)
        except FileNotFoundError:
            print(Fore.RED + "[ERROR/Logger] Log file or path not found!")
        except:
            print(Fore.RED + "[ERROR/Logger] An logger exception occurre")

    def warn(self,text= "log.log",warn_type=""):
        try:
            with open(self.file_name, "a") as f:
                if(warn_type == "" or warn_type == " "):
                    f.write("[{0}] {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"),"[WARNING] "  + text))
                    print(Fore.YELLOW + "[WARNING] " + text)
                else:
                    f.write("[{0}] {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"),"[WARNING/" + warn_type + "] "  + text))
                    print(Fore.YELLOW + "[WARNING/" + warn_type + "] " + text)
        except FileNotFoundError:
            print(Fore.RED + "[ERROR/Logger] Log file or path not found!")
        except:
            print(Fore.RED + "[ERROR/Logger] An logger exception occurre")

    def clear(self):
        try:
            files_deleted = False
            for filename in os.listdir(self.logs_folder_path):
                file_path = os.path.join(self.logs_folder_path, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    files_deleted = True
            return files_deleted
        except Exception as e:
            print(Fore.RED + f"[ERROR/Logger] {e}")
            return False
# https://github.com/semihkagan tarafından yazılmıştır.
