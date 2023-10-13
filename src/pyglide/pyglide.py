import os
import subprocess
import shutil
import pkg_resources
import pyglide.text2audio as text2audio
import pyglide.revealjs_template as revealjs_template
import pyglide.slideEdit as slideEdit
import pyglide.prompt as prom

class Gen:
    def __init__(self,index):
        self.index = index
        self.pyglide()
    
    def pyglide(self,audio=True,aI_assistant=True):
        _index=self.index
        if os.path.isfile(_index+".ipynb"):
            if audio:
                text2audio.text2audio(_index+".ipynb")
            revealjs_template.convert('nbconvert')
            subprocess.run(["jupyter", "nbconvert", _index+".ipynb", "--to", "slides"])
            if aI_assistant:
                prom.prompt(_index)
            slideEdit._ess(_index)
            examples_dir=os.getcwd()
            if not os.path.exists(os.path.join(os.getcwd(), 'output')):
                os.makedirs(os.path.join(os.getcwd(), 'output'))
            self.houesekeeping(_index,examples_dir)
        elif _index=="original_example":
            examples_dir=Showcase(_index).get_file()
            if audio:
                text2audio.text2audio(examples_dir + "/original_example.ipynb")
            revealjs_template.convert('nbconvert')
            subprocess.run(["jupyter", "nbconvert", examples_dir+"/original_example.ipynb", "--to", "slides"])
            if aI_assistant:
                prom.prompt(_index)
            slideEdit._ess("original_example")
            self.houesekeeping(_index,examples_dir)
        else:
            print("\n")
            print(f"\"{_index}.ipynb\" not found!")
            print("*********************************************")
            print("Make sure you have the notebook and try again!")
            print("*********************************************")
    
    def houesekeeping(self, index,examples_dir):
        self.examples_dir=examples_dir
        source_file = os.path.join(examples_dir, index+'_pyglide.html')
        destination_folder = "./output"
        _files = os.listdir(destination_folder)
        for f in _files:
            item=os.path.join(destination_folder, f)
            print(item)
            if os.path.isfile(item):
                os.remove(item)
            elif os.path.isdir(item):
                shutil.rmtree(item)
                
        os.remove(index+".slides.html")
        shutil.move(source_file, destination_folder)
        if self.index=="original_example":
            shutil.move("original_example.ipynb",destination_folder)
        shutil.move(os.path.join(examples_dir, 'slides_audios'), destination_folder)
            
            
class Showcase:
    def __init__(self, index):
        self._name = index
    def get_file(self):
        examples_dir = pkg_resources.resource_filename('pyglide', 'example/original_example.ipynb')
        if not os.path.exists(os.path.join(os.getcwd(), 'output')):
            os.makedirs(os.path.join(os.getcwd(), 'output'))
        shutil.copy(examples_dir, os.getcwd())
        self.examples_dir = os.getcwd()
        return str(self.examples_dir)