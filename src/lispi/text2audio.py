import json
from gtts import gTTS
import random
import string
import os 

    
def text2audio(example_file_path):
    source  = string.digits + string.ascii_letters

    language = 'en'
    with open(example_file_path, mode = "r", encoding = "utf-8") as f:
        nb = json.loads(f.read())
         
        for cell in nb['cells']:
            if cell['metadata']:
                
                if cell['metadata']['slideshow']['slide_type'] == 'slide' or cell['metadata']['slideshow']['slide_type'] == 'subslide':
                    mp3name = ''.join([char for char in cell['source'][0] if char in source])
                    
                if cell['metadata']['slideshow']['slide_type'] == 'notes':
                    loc = nb['cells'].index(cell)
                    
                    notes = ' '.join(cell['source'])

                    obj = gTTS(text = notes, lang = language, slow = False)
                
                    cell_id = ''.join(random.sample(source, 50))
                    path = os.path.join(os.path.dirname(example_file_path), 'slides_audios')
                    os.makedirs(path, exist_ok = True)
                    obj.save('{}/{}.mp3'.format(path, mp3name))
                    
                # insert as a fragment
                    cell_description = {'cell_type': 'markdown', 'id': cell_id, 
                                    'metadata': {'slideshow': {'slide_type': 'fragment'}, 'tags': []}}
                    cell_description['source'] = ['<audio controls src=' + '"slides_audios/{}.mp3"'.format(mp3name) + '>']

                    nb['cells'].insert(loc + 1, cell_description)
                        
    with open(example_file_path, mode = "w") as f:
        f.write(json.dumps(nb))