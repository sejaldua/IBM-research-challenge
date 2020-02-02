from flask import Flask, render_template, request
import pandas as pd
from flask import jsonify
import json
app = Flask(__name__)

@app.route('/')
def student():
   df=pd.read_csv('data.csv')
   df=df[0:5]
   file_dict={}
   json_data=[]
   for index,row in df.iterrows():
      title=row['title']
      abstract=row['abstract']

      file_dict[title]=abstract

      #json_data.append({ title : abstract})
   # print(file_dict)
   # js=json.dumps(file_dict)

   # print("Javascript:",js)
   data = {'username': 'Pang', 'site': 'stackoverflow.com'}

   return render_template("result.html",result = file_dict)





@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form

      print(result)
      my_dict = {1: 'apple', 2: 'ball'}
      result_1=my_dict


      df=pd.read_csv('data.csv')
      df=df[0:5]
      file_dict={}

      for index,row in df.iterrows():
      	title=row['title']
      	abstract=row['abstract']

      	file_dict[title]=abstract


      return render_template("result.html",result = file_dict)

# @app.route('/abstract')
# def abstract():
# 	return render_template("abstract.html",result = result)




 
if __name__ == '__main__':
   app.run(debug = True)