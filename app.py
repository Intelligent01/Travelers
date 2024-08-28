from flask import Flask,render_template,url_for
import os
app = Flask(__name__)


# PicPath=os.path.join('static','pics','data','img')
# img=os.path.join(PicPath,"hello.txt")
# print(img)
@app.route('/')
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(port=8000,debug=True)