from flask import Flask, render_template, request
import pandas as pd
from utils2 import identify_cancer, find_drug_name, association_hint, classify_study_type
# from utils2 import find_cancer_name, find_drug_name, association_hint, classify_study_type
from flask import jsonify,make_response,request
import json
app = Flask(__name__)
import time


@app.route('/background_process')
def background_process():
	try:
		#Get data
		df=pd.read_csv('data.csv')
		df=df[0:10]
		file_dict={}
		titles=[]
		abstracts=[]
		cancer_names=[]
		drug_names=[]
		thera_names = []
		study_names = []
		for index,row in df.iterrows():
			print(index)
			title=row['title']
			abstract=row['abstract']
			# cancer_name = "testA"
			# drug_name = "drugA"
			# thera_name = "suggested text"
			# study_name = "vivo"

			cancer_name = identify_cancer(title, abstract)
			cancer_names.append(cancer_name)

			drug_name = find_drug_name(title)
			drug_names.append(drug_name)

			thera_name = association_hint(abstract)
			thera_names.append(thera_name)

			study_name = classify_study_type(abstract)
			study_names.append(study_name)

			titles.append(title)
			abstracts.append(abstract)

			file_dict[title]=abstract


		# lang = request.args.get('proglang', 0, type=str)
		# if lang.lower() == 'python':
		print("python done now")
		return jsonify(result=titles,result2=abstracts, result3=cancer_names, result4=drug_names, result5=thera_names, result6=study_names)
		# else:
		# 	return jsonify(result='Try again.')
	except Exception as e:
		return str(e)



@app.route('/interactive')
def interactive():
	return render_template('form_layout.html')

@app.route('/')
@app.route('/home')
def home():
	suggestion = {"drug": "aspirin", "cancer": "leukemia"}
	return render_template('welcome.html', suggestion=suggestion)

@app.route("/test_data", methods=["POST"])
def create_entry():
	print("GOT THE DATA!")

	req = request.get_json()
	drugname =req['drugname']
	cancername = req['cancername']
	theraname=req['theraname']
	studyname=req['studyname']
	row=[[drugname,cancername,theraname,studyname]]

	orig=pd.read_csv('answers.csv')
	orig=orig[['drug_name', 'cancer_name', 'thera_name', 'study_name']]
	#orig.append({'drug1':drugname, 'drug2':cancername,'drug3':theraname,'drug4':studyname}, ignore_index=True)


	new=pd.DataFrame([[drugname,cancername,theraname,studyname]],columns=['drug_name', 'cancer_name', 'thera_name', 'study_name'])
	
	d=pd.concat([orig,new])
	print(d)

	d.to_csv('answers.csv',index=False)
	# t=time.time()*1000
	# tmp_df.to_csv('submission_'+str(t)+'.csv')
	res = make_response(jsonify({"message": "OK"}), 200)

	return res


 
if __name__ == '__main__':
   app.run(debug = True)