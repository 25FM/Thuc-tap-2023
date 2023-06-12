from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)

# config database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@127.0.0.1/mytestdb'

# config migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    priority = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'completed': self.completed,
            'priority': self.priority,
            'date_created': self.date_created
        }
     
        
with app.app_context():
    db.create_all()


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission and task creation
        title = request.form['title']
        content = request.form['content']
        priority = request.form['priority']
        date_created = datetime.utcnow()

        # Create a new task
        new_task = Todo(title=title, content=content, priority=priority, date_created=date_created)
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')  # Redirect to the main page after task creation
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

        
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        complete = 0
        priority = request.form['priority']
        date_created = datetime.utcnow()
        new_task = Todo(title=title, content=content, complete = complete, priority=priority, date_created = date_created)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        return render_template('add.html')
    
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting your task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.content = request.form['content']
        task.priority = request.form['priority']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)


if __name__ == '__main__':
    app.run(debug=True)