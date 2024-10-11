# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    feedback__form = request.form.get('feedback__form')
    text = request.form.get('text')
    gmail =  request.form.get('email')

    with open ('text.txt', 'a', encoding= 'utf-8') as serhan:
        if gmail == gmail and text == text:

            serhan.write(f'{gmail}\n')
            serhan.write(f'{text}\n') 
            serhan.write("-----------------------------\n")

        
        


    
    



    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html = button_html,button_db=button_db)



if __name__ == "__main__":
    app.run(debug=True)
