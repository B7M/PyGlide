import os
import pkgutil
import subprocess


def convert(package_name):
    if pkgutil.find_loader(package_name) is None:
        print(f"{package_name} is not installed")
        ask_install = input("Do you want to install it? (y/n): ")
        if ask_install == "y":
            subprocess.run(["pip", "install", package_name])
        else:
            print("Sorry without nbconvert ess can't generate the desired output! \n Exiting...")
            exit()
    
# convert(package_name)