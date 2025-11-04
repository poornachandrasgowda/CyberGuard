from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Routes for different commands
@app.route('/command1')
def command1():
    os.system('x-terminal-emulator -e "bash -c \'cd ~/Documents/rapidscan; python3 rapidscan.py sh4.in;exec bash\'"')
    return "Web Vulnerability Scanner Has Been executed Succesfully"

@app.route('/command2')
def command2():
    os.system('x-terminal-emulator -e "bash -c \'cd ~/Documents/sauron; sudo RUST_LOG=info ./target/release/sauron \--rules ./Yara-rules \--scan \--root ~/Desktop \--ext txt; exec bash\'"')
    return "Malware Scanner Has Been Executed Sucessfully"

@app.route('/command3')
def command3():
    os.system('x-terminal-emulator -e "bash -c \'cd ~/Documents/Hash-Buster; buster -s b3ea2220280ec43c31c7f6723f85904c; exec bash\'"')
    return "Password Cracker Has Been Executed Sucessfully"



if __name__ == '__main__':
    app.run(debug=True)

