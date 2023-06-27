from bs4 import BeautifulSoup

def prompt(notebook_file_name):
  with open(notebook_file_name+".slides.html", mode = "r", encoding = "utf-8") as file:
    html_content = file.read()
  soup = BeautifulSoup(html_content, 'html.parser')

  # Find the specified text
  reveal_div = soup.find('div', class_='slides')

  user_html_gpt_box = '''<div id="prompt-container" style="position: absolute; top: 0; right: 0; z-index: 9999; width: 300px; background-image: linear-gradient(to bottom, #89CFF0, #FFFFFF); border: 1px solid #ccc; border-radius: 0 0 0 5px; box-shadow: 0 0 5px rgba(0, 0, 0, 0.2); transition: height 0.3s ease;">
    <div id="prompt-content" style="padding: 10px">
      <textarea id="prompt-textarea" style="width: 100%; height: 100px; resize: none; margin-bottom: 10px; transition: height 0.3s ease; minimized {height: 20px}" rows="4" placeholder="Enter your prompt..."></textarea>
      <button id="submit-button", style="display: block; width: 95%; padding: 10px; background-color: #9370db; border: none; border-radius: 5px;cursor: pointer; color: #ffff00;">In doubt?</button>
    </div>
  </div>'''
  html_gpt_box = BeautifulSoup(user_html_gpt_box, 'html.parser')
  reveal_div.insert_before(html_gpt_box)
  
  script_tag_AI = soup.new_tag('script', **{"class":"script_tag_AI"})
  script_tag_AI.string ='''const promptContainer = document.getElementById('prompt-container');
    const promptTextarea = document.getElementById('prompt-textarea');
    const submitButton = document.getElementById('submit-button');

    submitButton.addEventListener('click', () => {
      const promptText = promptTextarea.value;
      // Send the prompt text to your backend or process it using JavaScript
      // and display the response as desired
      const response = 'Response from GPT: ' + promptText;
      alert(response);
    });

    promptContainer.addEventListener('click', () => {
      promptContainer.style.height = promptContainer.classList.contains('minimized') ? 'auto' : '40px';
      promptContainer.classList.toggle('minimized');
      promptTextarea.style.height = promptTextarea.classList.contains('minimized') ? 'auto' : '20px';
      promptTextarea.classList.toggle('minimized');
      submitButton.classList.toggle('hidden');
      submitButton.style.display = promptContainer.classList.contains('minimized') ? 'none' : 'block';
    });
    '''
    
  search_result = soup.new_tag('script', **{"class":"search_result"})
  search_result.string ='''const promptContainer = document.getElementById('prompt-container');
    const promptTextarea = document.getElementById('prompt-textarea');
    const submitButton = document.getElementById('submit-button');

    submitButton.addEventListener('click', () => {
      const promptText = promptTextarea.value;
      var replacedInput = promptText.replace(/ /g, '%20');
      var generatedURL = 'https://www.perplexity.ai/search?q=' + replacedInput;
      window.open(generatedURL, 'PopupWindow', 'width=500,height=400');
      // Send the prompt text to your backend or process it using JavaScript
      // and display the response as desired
    });

    promptContainer.addEventListener('click', () => {
      promptContainer.style.height = promptContainer.classList.contains('minimized') ? 'auto' : '40px';
      promptContainer.classList.toggle('minimized');
      promptTextarea.style.height = promptTextarea.classList.contains('minimized') ? 'auto' : '20px';
      promptTextarea.classList.toggle('minimized');
      submitButton.classList.toggle('hidden');
      submitButton.style.display = promptContainer.classList.contains('minimized') ? 'none' : 'block';
    });'''
    
    
    
  reveal_div = soup.find('div', class_='slides')
  reveal_div.insert_after(script_tag_AI)
  reveal_div.insert_after(search_result)
  
  


  # Get the new HTML content
  _html = str(soup)

  with open(notebook_file_name+'.slides.html', 'w') as file:
      file.write(_html)