import os
from bs4 import BeautifulSoup
current_working_directory = os.getcwd()
file_names = os.listdir('.')

def _ess(notebook_file_name):

  def get_html(html_file_name):
      with open(html_file_name, mode = "r", encoding = "utf-8") as file:
          html_content = file.read()
          return html_content


  soup = BeautifulSoup(get_html(notebook_file_name+".slides.html"), 'html.parser')

  # Find the specified text
  target_text = "Practice time!"
  target_element = soup.find(string=lambda text: text and target_text in text)

  user_html = '''
  <div class="bm_insert">
    <div>
      <textarea class="solution" type="text" id="txt" placeholder="write here"
        style="height: 200px; width: 600px;"></textarea>
    </div>

    <div class="submit"
      style="display: flex; flex-direction: row; align-items: center; margin-left: 200px;">
      <form>
          <button class="Run_btn" id="run" type="button" onclick="py_scr()" style="cursor: pointer;
                  background-color: yellow; border-radius: 5px; height: 50px; font-size: 28px; margin-left: 20px;">
          Run?
          </button>
          <button class="submit_button" id="code" type="button" onclick="codeFunction()" style="cursor: pointer;
                  background-color: rgb(77, 191, 11); border-radius: 5px; height: 50px; font-size: 28px; margin-left: 20px;">
          Submit now!
          </button>
      </form>
    </div>
    <div class="user_input">
      <p id="user_answer" style="color: #00e676;"> Final answer will be copied here</p>
    </div>
  </div>'''

  script_tag_pyScript = soup.new_tag('script')
  script_tag_pyScript.string ="""function py_scr() {\n  var newWindow = window.open("", "newWindow", "width=400, height=200");\n  const parser= new DOMParser();\n  var test=\'<html><head><title>PyScript</title></head><body><div id=""><p id="user_answer"></p><p id="py_script_tag"></p></div><div id="compiled_results"></div></body></html>\';\n  const parsedDocument= parser.parseFromString(test,"text/html");\n  newWindow.document.body=parsedDocument.body;\n  var script = newWindow.document.createElement(\'script\');\n  script.defer=true;\n  script.src = \'https://pyscript.net/latest/pyscript.js\';\n  newWindow.document.head.appendChild(script);\n  var initial_text = document.getElementById("txt").value;\n  localStorage.setItem("user_text", initial_text);\n  var script = newWindow.document.createElement(\'script\');\n  script.id="u_user"\n  newWindow.document.body.appendChild(script);\n  var initial_text2 = \'<py-config class="pyscript_env" style="display: none;">\\n\' +\n                       \'packages = ["numpy", "matplotlib"]\\n\' +\n                       \'terminal = false</py-config>\'\n  var user_script2= \'<py-script output="compiled_results">\\n\' +\n                    \'from js import user_script\\n\' +\n                    \'input=user_script\\n\' +\n                    \'def py_run(*args):\\n\' +\n                    \' exec(input)\\n\' +\n                    \'py_run()\\n</py-script>\'\n  var submittied_text_to_PyScrip=\'user_script= localStorage.getItem("user_text")\';\n  newWindow.document.getElementById("user_answer").innerHTML=initial_text2;\n  newWindow.document.getElementById("py_script_tag").innerHTML=user_script2;\n  newWindow.document.getElementById("u_user").innerHTML=submittied_text_to_PyScrip;\n  localStorage.setItem("user_text", initial_text);\n  // window.open("index6_test.html", "_blank");\n  return false;\n}"""

  script_tag_Code = soup.new_tag('script')
  script_tag_Code.string ="""
  function codeFunction() {
    let writtenCode = document.getElementById("txt").value;
    writtenCode = writtenCode.replace(/\\n\\r?/g, '<br />');
    document.getElementById("user_answer").innerHTML = writtenCode;
  }
  """

  if target_element:
      # Get the parent <p> tag
      p_tag = target_element.find_parent("p")

      # Create a new BeautifulSoup object to parse the user-defined HTML
      user_soup = BeautifulSoup(user_html, 'html.parser')

      # Get the root element of the user-defined HTML
      user_div = user_soup.find()

      # Insert the user-defined <div> after the <p> tag
      p_tag.insert_after(script_tag_Code)
      p_tag.insert_after(script_tag_pyScript)
      p_tag.insert_after(user_div)


  # Get the new HTML content
  _html = str(soup)

  with open(notebook_file_name+'_lispi.html', 'w') as file:
      file.write(_html)