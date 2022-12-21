from flask import Flask, request, render_template, jsonify
from chatbot import main

app = Flask(__name__)
app.config['secret_key'] = ''


@app.route('/', methods=['GET', 'POST'])
def bot():
    if request.method == 'POST':
        inc_msg = request.form.get('msg')
        response = main(inc_msg)
        return jsonify(response)

    return render_template('index.html')
    

if __name__=='__main__':
    app.run(debug=True)