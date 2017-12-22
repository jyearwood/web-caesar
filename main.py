from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG']= True

form = """
<!DOCTYPE html>
<html> 
    <head>
        <style type="text/css">
            form{{
                background-color: #eee;
                padding:20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body> 
        <form action"/" method="POST">
        <div>
        <label for="rot">Rotate By: </label>
        <input type="text" name="rot" value="0" />
        <div>
        <textarea name="text">{0}</textarea>
        <input type="submit" value="Rotate" />
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    empty_message = ""
    return form.format(empty_message)


@app.route("/", methods=['POST'])
def encrypt():
    text = request.form["text"]
    rot = request.form["rot"]
    rot = int(rot)
    encrypted_text = rotate_string(text, rot)

    return form.format(encrypted_text)

app.run()