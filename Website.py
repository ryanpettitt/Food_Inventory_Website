from flask import Flask, render_template, request, flash, redirect, url_for   
import Intentory_manager, os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/ryanpettitt/Desktop/Everything/dev/Food Inv/pics'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        #if request.keys()
        req = request.form.keys()
        for i in req:
            if i == "DELETE":
                Intentory_manager.Remove_item(request.form["DELETE"])
            if i == "EDIT":
                values = Intentory_manager.return_value(int(request.form['EDIT']))
                print(values)
                return render_template("edit.html", values=[values])
            if i == "Index":
                Intentory_manager.edit_item(request.form['Index'], request.form['Food'], request.form['Type'], request.form['QTY'])
        headers, values = Intentory_manager.display_items()
        return render_template("index.html", headers = headers, values = values)
    else:
        headers, values = Intentory_manager.display_items()
        return render_template("index.html", headers = headers, values = values)

@app.route("/Add_Item", methods=['GET', 'POST'])
def Adding():
    if request.method == "POST":
        req = request.form
        Intentory_manager.New_item(req['Food'], req['Type'], req['QTY'])
        return render_template("Add_Itme.html")
    else:
        return render_template("Add_Itme.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/pic', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return home()
    return home()

    
if __name__ == "__main__":
    app.run(host='192.168.1.12', port=4000)