from flask import Flask, render_template, jsonify
app = Flask(__name__)
@app.route('/')
def hello_world():
 return render_template('home.html',jobs=JOBS)

JOBS =[
  {
    'id':1,
    'title' : 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 25,00,000'
  },
  {
      'id':2,
     'title':'Associate Software Engineer',
     'location': 'Pune, Maharashtra',
      'salary': 'Rs. 7,00,000'
  },
  {
    'id':3,
    'title': 'QA Engineer',
    'location': 'Hyderabad, India',
      'salary': 'Rs. 7,00,000'
  },
  {
    'id':4,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  }
]
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)