import os
import subprocess
import jupyter
import shutil
import pkg_resources
import lispi
from lispi import *

def main():
    index = input("Enter the name of the notebook file: \n")
    if os.path.isfile(index+".ipynb"):
        text2audio.text2audio(index+".ipynb")
        revealjs_template.convert('nbconvert')
        subprocess.run(["jupyter", "nbconvert", index+".ipynb", "--to", "slides"])
        slideEdit._ess(index)
    elif index=="original_example":
        class Showcase:
            def __init__(self, index):
                self._name = index
            def get_file(self):
                examples_dir = pkg_resources.resource_filename('lispi', '../../example/original_example.ipynb')
                if not os.path.exists(os.path.join(os.getcwd(), 'output')):
                    os.makedirs(os.path.join(os.getcwd(), 'output'))
                shutil.copy(examples_dir, os.getcwd())
                self.examples_dir = os.getcwd()
                return self.examples_dir
        
        
        examples_dir=Showcase(index).get_file()
        text2audio.text2audio(examples_dir+"/original_example.ipynb")
        revealjs_template.convert('nbconvert')
        subprocess.run(["jupyter", "nbconvert", examples_dir+"/original_example.ipynb", "--to", "slides"])
        slideEdit._ess("original_example")
        source_file = os.path.join(examples_dir, 'original_example_lispi.html')
        destination_folder = "./output"
        _files = os.listdir(destination_folder)
        print(_files)
        for f in _files:
            item=os.path.join(destination_folder, f)
            print(item)
            if os.path.isfile(item):
                os.remove(item)
            elif os.path.isdir(item):
                shutil.rmtree(item)
                
        os.remove("original_example.ipynb")
        os.remove("original_example.slides.html")
        shutil.move(source_file, destination_folder)
        shutil.move(os.path.join(examples_dir, 'slides_audios'), destination_folder)
    else:
        print("\n")
        print(f"\"{index}.ipynb\" not found!")
        print("*********************************************")
        print("Make sure you have the notebook and try again!")
        print("*********************************************")

if __name__ == "__main__":
    main()