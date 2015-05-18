from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('template.html', my_string-"Wheeeee!", my_list[0,1,2,3,4,5])

if __name__=="main":
    app.run(debug=True, host="0.0.0.0", port=8080)