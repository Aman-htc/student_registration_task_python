
import json
def load(path):
    with open(path,'r') as file:
        return json.load(file)
        


def active_student(path):
    data=load(path)
    for s in data:
        for key,value in s.items():
            if value ==True:
                print(json.dumps(s,indent=4))
                
    