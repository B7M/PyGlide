import os
import sys
import subprocess
import argparse
import shutil
import pkg_resources
import lispi.text2audio as text2audio
import lispi.revealjs_template as revealjs_template
import lispi.slideEdit as slideEdit
import lispi

def main():
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('-v','--version', help='Display the version of LISPI', action='version', version=f'LISPI version {lispi.__version__ }')
    parser.add_argument('filename',help='Pass the file name without extension', nargs='?')
    parser.add_argument('-m','--mute', help='Mute the audio', action='store_true')
    parser.add_argument('-i', help='The file name without extension', action='store', dest='input')
    args=parser.parse_args()
    mute=args.mute
        
    if args.input is None and not args.filename:
        parser.print_help()
        sys.exit()
    elif args.filename:
        index=args.filename
    else:
        index = args.input

    
       
    class Showcase:
        def __init__(self, index):
            self._name = index
        def get_file(self):
            examples_dir = pkg_resources.resource_filename('lispi', 'example/original_example.ipynb')
            if not os.path.exists(os.path.join(os.getcwd(), 'output')):
                os.makedirs(os.path.join(os.getcwd(), 'output'))
            shutil.copy(examples_dir, os.getcwd())
            self.examples_dir = os.getcwd()
            return self.examples_dir
    
    def houesekeeping(examples_dir,index,mute):
        source_file = os.path.join(examples_dir,index+'_lispi.html')
        destination_folder = "./output"
        if not mute:
            _files = os.listdir(destination_folder)
            for f in _files:
                item=os.path.join(destination_folder, f)
                print(item)
                if os.path.isfile(item):
                    os.remove(item)
                elif os.path.isdir(item):
                    shutil.rmtree(item)
            shutil.move(os.path.join(examples_dir, 'slides_audios'), destination_folder)
        
        os.remove(index+".slides.html")
        shutil.move(source_file, destination_folder)
        if index=="original_example":
            shutil.move("original_example.ipynb",destination_folder)
        
    if os.path.isfile(index+".ipynb"):
        if not mute:
            text2audio.text2audio(index+".ipynb")
        revealjs_template.convert('nbconvert')
        subprocess.run(["jupyter", "nbconvert", index+".ipynb", "--to", "slides"])
        slideEdit._ess(index)
        examples_dir=os.getcwd()
        if not os.path.exists(os.path.join(os.getcwd(), 'output')):
                os.makedirs(os.path.join(os.getcwd(), 'output'))
        houesekeeping(examples_dir,index,mute)
    elif index=="original_example":
        examples_dir=Showcase(index).get_file()
        if not mute:
            text2audio.text2audio(examples_dir + "/original_example.ipynb")
        revealjs_template.convert('nbconvert')
        subprocess.run(["jupyter", "nbconvert", examples_dir+"/original_example.ipynb", "--to", "slides"])
        slideEdit._ess("original_example")
        houesekeeping(examples_dir,index,mute)
    else:
        print("\n")
        print(f"\"{index}.ipynb\" not found!")
        print("*********************************************")
        print("Make sure you have the notebook and try again!")
        print("*********************************************")

if __name__ == "__main__":
    main()
    