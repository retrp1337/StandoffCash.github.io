from flask import Flask, render_template, request, redirect

app = Flask(__name__)





@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/standoff')
def standoff():
    return render_template('game.html')


@app.route('/pay/QWHVNQOVSAJJVQIGD')
def pay1():
    return render_template('payQWHVNQOVSAJJVQIGD.html')

@app.route('/pay/EFBNIBSDBVFIWBEGB')
def pay2():
    return render_template('payEFBNIBSDBVFIWBEGB.html')

@app.route('/pay/WSDFIHBIWBEVIPUBWPIEBG')
def pay3():
    return render_template('payWSDFIHBIWBEVIPUBWPIEBG.html')

@app.route('/pay/SFOWREGBIJNWNEOGBNPWD')
def pay4():
    return render_template('paySFOWREGBIJNWNEOGBNPWD.html')

@app.route('/pay/SFBJNOISDBVGHWEVJWNB')
def pay5():
    return render_template('paySFBJNOISDBVGHWEVJWNB.html')

@app.route('/pay/EFBJNWOJEVNOWBNPFIUBWBEY')
def pay6():
    return render_template('payEFBJNWOJEVNOWBNPFIUBWBEY.html')





if __name__ == "__main__":
    app.run(debug=True)
