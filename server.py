from flask import Flask, render_template, session, redirect, request # added render_template!
app = Flask(__name__)
app.secret_key="Magic sauce."                        
    
@app.route('/')                           
def index():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html')  
    
@app.route('/process', methods = ["POST"])                           
def process_page():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect('/result')  

@app.route('/result')                           
def result_page():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('result.html')  






if __name__=="__main__":
    app.run(debug=True)                   





