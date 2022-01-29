from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return "$ Welcome to Flask Applicaiom...!"

@app.route("/PFSD")
def myname():
    return"MEGHA VAMSI KIRAN"

@app.route('/emp/<int:emp1>')
def show_emp(emp1):
    return 'EMP ID Number %d' %emp1

@app.route('/erp/<float:emp1>')
def show_erp(emp1):
    return 'ERP ID Number %f' %emp1

if __name__=="__main__":
    app.run()