# importing database and model from app.py
from app import db, Task 

first_task = Task(task_text = 'lets play with flask')
db.session.add(first_task) # how to store in database
db.session.commit()

# lets run task.py it will add task in databse

# how to access the data in database
all_tasks = Task.query.all()
print(all_tasks[0].task_text)
