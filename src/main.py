import json
from Task import Task

with open("config.json") as file:
    configuration = json.loads(file.read())
Task(config= configuration["Task"], description= "testToDo")
print(Task(config= configuration["Task"], description= "testToDo"))




