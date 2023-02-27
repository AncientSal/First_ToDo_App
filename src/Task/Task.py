from enum import Enum
from Exceptions import *
from Constants import priorityEnum
from datetime import datetime
import json


class Task:
    '''
    ### Basic Todo object:
    #### Description: 
    information about an Todo:
    - description -> string that describes

    #### TODO:
    - make it serializable (dump in json file)
    - 

    '''
    
    def __init__(self,  description : str, priority: priorityEnum = ..., date : datetime = ...) -> None:
        self.description : str = description
        self.priority : priority
        self.date : datetime = datetime.now()
        self.active : bool = True


        
    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass
    
    def Load(self, dump: dict):
        self.__init__(
            description= dump["description"],
            priority= priorityEnum(dump["priority"]),
            date= 
        )         

    def Dump(self):

        # Todo learn json dump functionality
        return self._dumpInstance()
    
    def _dumpInstance(self) -> dict:
        result = {}
        result["description" : str] = self.description
        result["priority" : int] = self.priority.value 
        result["date"] = self._serializeDatetime()
        result["active"] = self.active
        return result

    def _serializeDatetime(self) -> dict:
        res : dict = {"year" : self.date.year, "month" : self.date.month, "day" : self.date.day} 
        # check weather the datetime contains hour and minute
        if self.date.hour != None and self.date.minute != None:
            res["hour"] = self.date.hour
            res["minute"] = self.date.minute
            return res
        return res

if __name__ == "__main__":
    task = Task("Do Dishes")
    a = task.description.__len__()
    b = priorityEnum.low.value


    