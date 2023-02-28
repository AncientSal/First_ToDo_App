from enum import Enum
from Exceptions import *
from Constants import priorityEnum
from datetime import datetime
import json
import os.path as path

#python 3.11.2
# Manuel Benner


class Task:
    '''
    ### Basic Todo object:
    #### Description: 
    information about an Todo:
    - description -> string that describes

    '''
    
    def __init__(self,  description : str, priority: priorityEnum = None, date : datetime = None) -> None:
        #TODO: add use properties to check if the type is valid and 
        self.description : str = description
        self.priority : priority = priority
        self.date : datetime = date
        self.active : bool = True

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value : str):
        if len(value) < 100: # TODO: get this value from configfile
            self._description = value
        else:
            raise DescriptionException("The length of the description is too long")




    def __repr__(self) -> str:
        return self._dumpInstance()

    def __str__(self) -> str:
        return f"description: {self.description}, priority: {self.priority}, date: {self.date}, active: {self.active}"
 
    #################### serialize and deserialize  #####################

    def DumpAsJson(self, filepath : str) -> None:        
        with open(filepath, mode= "w", encoding= "utf8") as file:
            file.write(json.dumps(self._dumpInstance()))
            print(f"Dumped at: {filepath}")  

    def LoadJson(self, filepath: str) -> None:
        self._LoadDict(self._ReadJson(filepath))
          
    def _ReadJson(self, filepath:str) -> dict:
        with open(filepath, mode= "r",encoding="utf8") as file:
            fileData = file.readline()  
        return json.loads(fileData)

    def _LoadDict(self, dump: dict) -> None:
        self.__init__(
        description = dump["description"],
        priority= priorityEnum(dump["priority"]),
        date = self._deserializeDatetime(dump["date"])
    )        
    
    def _dumpInstance(self) -> dict:
        result = {}
        result["description"] = self.description
        result["priority"] = self.priority
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
    
    @staticmethod
    def _deserializeDatetime(date : dict) -> datetime:

        if not type(date) == dict:
            raise DeserializingException("Date in wrong format")
        
        if len([date]) == 3 :
            return datetime(date["year"], date["month"], date["day"])
        
        elif(len(date) == 5):
            return datetime(date["year"], date["month"], date["day"], date["hour"], date["minute"])
        else :
            raise DeserializingException("Date in unsupported format")



if __name__ == "__main__":
    task = Task("Do Dishes")
    task.DumpAsJson("dump\\task.json")
    print(task)
    


    