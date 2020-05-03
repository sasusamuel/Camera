from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#step2
@app.route('/about')
def about_us():
    return render_template('about_us.html')

@app.route('servic')
def abouservice():
    return render_template('service.html')

#step3
@app.route('/contact_us')
def foo(name):
    return render_template('contact_us.html')



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')
