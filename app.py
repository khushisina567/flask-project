from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['aabha']
        email = request.form['aabhapandey11d@gmail.com']
        message = request.form['urgent']
        # Here you would typically save this data or send an email
        return f"Thank you {name}! Your message has been received."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)