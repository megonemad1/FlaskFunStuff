from flask import Flask,render_template,request

app= Flask(__name__)



@app.route('/', methods=['GET','POST'])
def Home():	
	Msg =None
	optid=None
	option_list=[{'optid':"Dynamic1"},{'optid':"Dynamic2"}]
	if (request.method=='POST'):
		Msg=request.form['username']
		print('lvl1')
		
		print (request.form['options'])
		if request.form['options'] == 'Select':
			print("lvl2")
			optid = o.optid
			resp = 'You chose: ', optid
            


	return render_template('Word.html',Msg=Msg,option_list=option_list,optid=optid)

if __name__=="__main__":	
	app.debug=True
	app.run(host='0.0.0.0')