import os
from bs4 import BeautifulSoup, Comment
current_working_directory = os.getcwd()
file_names = os.listdir('.')

def _ess(notebook_file_name):
  def get_html(html_file_name):
      with open(html_file_name, mode = "r", encoding = "utf-8") as file:
          html_content = file.read()
          return html_content
  soup = BeautifulSoup(get_html(notebook_file_name+".slides.html"), 'html.parser')
  # Find the specified text in the HTML content
  def codePage(soup):
    target_code = soup.find_all(string=lambda text: isinstance(text, Comment) and "Course_Code" in text)
    target_text = soup.find_all(string=lambda text: isinstance(text, Comment) and "Course_Text" in text)
    field_nu_txt=0
    field_nu_code=0
    if target_code:
      for i in target_code:
        user_html = '''
        <div class="bm_insert">
          <div>
            <textarea class="solution" type="text" id="txt_%s" placeholder="write here"></textarea>
          </div>

          <div class="submit"
            style="display: flex; flex-direction: row; align-items: center; margin-left: 200px;">
            <form>
                <button class="button_run" id="run" type="button" onclick="py_scr(%s)">
                Execute?
                </button>
                <button class="button_submit" id="code" type="button" onclick="codeFunction(%s,y='Course_Code')">
                Submit!
                </button>
            </form>
          </div>
          <div class="user_input">
            <p id="user_answer_%s_Course_Code" style="color: #00e676;"> Final answer will be copied here</p>
          </div>
        </div>''' % (field_nu_code,field_nu_code,field_nu_code,field_nu_code)
        
        field_nu_code+=1
        
        # Get the parent tag
        p_tag = i.find_parent()

        # Create a new BeautifulSoup object to parse the user-defined HTML
        user_soup = BeautifulSoup(user_html, 'html.parser')

        # Get the root element of the user-defined HTML
        user_div = user_soup.find()

        # Insert the user-defined <div> after the <p> tag
        p_tag.insert_after(user_div)
        
    
    if target_text:
      for ii in target_text:
        user_html = '''
          <div class="bm_insert">
            <div>
              <textarea class="solution" type="text" id="txt_%s_Text" placeholder="write here"></textarea>
            </div>

            <div class="submit"
              style="display: flex; flex-direction: row; align-items: center; margin-left: 200px;">
                  <button class="button_submit" id="code" type="button" onclick="codeFunction(%s,y='Course_Text')">
                  Submit!
                  </button>
            </div>
            <div class="user_input%s">
              <p id="user_answer_%s_Course_Text" style="color: #00e676;"> Final answer will be copied here</p>
            </div>
          </div>''' % (field_nu_txt,field_nu_txt,field_nu_txt,field_nu_txt)
        field_nu_txt+=1
        # Get the parent tag
        p_tag = ii.find_parent()

        # Create a new BeautifulSoup object to parse the user-defined HTML
        user_soup = BeautifulSoup(user_html, 'html.parser')

        # Get the root element of the user-defined HTML
        user_div = user_soup.find()

        # Insert the user-defined <div> after the <p> tag
        p_tag.insert_after(user_div)
    
    reveal_div = soup.find('div', class_='slides') 
    body_tag = soup.find('body')  
    script_tag_text = soup.new_tag('script')
    script_tag_text.string ="""
    function codeFunction(x,y) {
      if (y == "Course_Code"){
      let writtenCode = document.getElementById("txt_"+x).value;
      writtenCode = writtenCode.replace(/\\n\\r?/g, '<br />');
      document.getElementById("user_answer_"+x+"_Course_Code").innerHTML = writtenCode;
      }
      else if (y == "Course_Text"){
      let writtenCode = document.getElementById("txt_"+x+"_Text").value;
      writtenCode = writtenCode.replace(/\\n\\r?/g, '<br />');
      document.getElementById("user_answer_"+x+"_Course_Text").innerHTML = writtenCode;
      }
      
    }
    """
    script_tag_pyScript = soup.new_tag('script')
    script_tag_pyScript.string ="""function py_scr(x) {\n  var newWindow = window.open("", "newWindow", "width=400, height=200");\n  const parser= new DOMParser();\n  var test=\'<html><head><title>PyScript</title></head><body><div id=""><p id="user_answer"></p><p id="py_script_tag"></p></div><div id="compiled_results"></div></body></html>\';\n  const parsedDocument= parser.parseFromString(test,"text/html");\n  newWindow.document.body=parsedDocument.body;\n  var script = newWindow.document.createElement(\'script\');\n  script.defer=true;\n  script.src = \'https://pyscript.net/latest/pyscript.js\';\n  newWindow.document.head.appendChild(script);\n  var initial_text = document.getElementById("txt_"+x).value;\n  localStorage.setItem("user_text_${x}", initial_text);\n  var script = newWindow.document.createElement(\'script\');\n  script.id="u_user"\n  newWindow.document.body.appendChild(script);\n  var initial_text2 = \'<py-config class="pyscript_env" style="display: none;">\\n\' +\n                       \'packages = ["numpy", "matplotlib"]\\n\' +\n                       \'terminal = false</py-config>\'\n  var user_script2= \'<py-script output="compiled_results">\\n\' +\n                    \'from js import user_script\\n\' +\n                    \'input=user_script\\n\' +\n                    \'def py_run(*args):\\n\' +\n                    \' exec(input)\\n\' +\n                    \'py_run()\\n</py-script>\'\n  var submittied_text_to_PyScrip=\'user_script= localStorage.getItem("user_text_${x}")\';\n  newWindow.document.getElementById("user_answer").innerHTML=initial_text2;\n  newWindow.document.getElementById("py_script_tag").innerHTML=user_script2;\n  newWindow.document.getElementById("u_user").innerHTML=submittied_text_to_PyScrip;\n  localStorage.setItem("user_text_${x}", initial_text);\n  // window.open("index6_test.html", "_blank");\n  return false;\n}"""
    
    button_style = soup.new_tag('style')
    button_style.string ="""
    textarea {
      width: 600px;
      height: 200px;
      padding: 10px;
      margin-bottom: 20px;
    }
    
.button-container {
      position: absolute;
      bottom: -40px;
      left: 50%;
      transform: translateX(-50%);
    }
    
    button {
      padding: 15px 30px;
      border: none;
      border-radius: 5px;
      font-size: 18px;
      transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
    }
    
    button:hover {
      background-color: #fff;
      color: #007bff;
    }

    .button_submit {
      background-color: green;
      color: #fff;
      margin-right: 10px;
    }

    .button_run {
      background-color: orange;
      color: #fff;
      margin-left: 10px;
    }"""
    
    
    reveal_div.insert_after(script_tag_text)
    reveal_div.insert_after(script_tag_pyScript)
    body_tag.insert_before(button_style)
    
    return soup
        
  _html = str(codePage(soup))
  with open(notebook_file_name+'_pyglide.html', 'w') as file:
      file.write(_html)