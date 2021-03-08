from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.form.get('button_1'):
        uploaded_file = request.files['file']
        target = request.form.get('target')

        if target == "folder_1":
            if uploaded_file.filename in os.listdir(target):
                os.remove(target + "/" + uploaded_file.filename)
                print("Exiting same filename in current dictionary, but deleted")
 
            if uploaded_file.filename != '':
                uploaded_file.save(target + "/" + uploaded_file.filename)

        elif target == "folder_2":
            if uploaded_file.filename in os.listdir(target):
                os.remove(target + "/" + uploaded_file.filename)
                print("Exiting same filename in current dictionary, but deleted")
                
            if uploaded_file.filename != '':
                uploaded_file.save(target + "/" + uploaded_file.filename)
        return redirect(url_for('index'))

    if request.form.get('button_2'):
        target = request.form.get('target2')

        if request.form.get('button_2') and target == "folder_1":
            name = os.listdir(target)

        elif request.form.get('button_2') and target == "folder_2":
            name = os.listdir(target)

        # print(name)

        return("<p>" + "</p><p>".join(name) + "</p>")


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host = '0.0.0.0', port = 80)

