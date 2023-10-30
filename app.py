# from flask import Flask
# import datetime
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return f"<h1>Hello, Flask on Azure Web App!</h1><hr/>Current clock time is: {datetime.datetime.utcnow()}"

# if __name__ == '__main__':
#    app.run()

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# CSV file configuration
csv_file = 'tasks.csv'

def create_csv():
    pd.DataFrame(columns=['id', 'description', 'done']).to_csv(csv_file, index=False)

@app.route('/')
def index():
    create_csv()  # Create the CSV file if it doesn't exist
    tasks = pd.read_csv(csv_file)
    return render_template('index.html', tasks=tasks.values)

@app.route('/add_task', methods=['POST'])
def add_task():
    description = request.form['description']
    tasks = pd.read_csv(csv_file)
    new_task = pd.DataFrame({'description': [description], 'done': [0]})
    tasks = tasks.append(new_task, ignore_index=True)
    tasks.to_csv(csv_file, index=False)
    return redirect(url_for('index'))

@app.route('/toggle_task/<int:task_id>')
def toggle_task(task_id):
    tasks = pd.read_csv(csv_file)
    if task_id in tasks['id'].values:
        task = tasks.loc[tasks['id'] == task_id]
        tasks.at[task.index[0], 'done'] = int(not task['done'])
        tasks.to_csv(csv_file, index=False)
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    tasks = pd.read_csv(csv_file)
    if task_id in tasks['id'].values:
        tasks = tasks[tasks['id'] != task_id]
        tasks.to_csv(csv_file, index=False)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
