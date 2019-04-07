from bottle import request,route,template, Bottle, run

app = Bottle()

@app.route('/myip')
def show_ip():
    ip = request.environ.get("REMOTE_ADDR")
    return template("Your IO is: {{ip}}",ip=ip)

run(app,host='localhost',port=29192)