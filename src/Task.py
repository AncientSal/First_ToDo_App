from enum import Enum


class Task:
    '''
    ### Basic Todo object:
    #### Description: 
    information about an Todo:
    - headline like -> do the dishes
    - priority (how important is the task) -> is calculated from deadline and expenditure of time
    - expenditure of time
    - task deadline
    - deactivate task for a certain time

    #### TODO:
    - make it serializable (dump in json file)
    - make every element an object, to have full control of the contents (validating is done inside objects)

    '''
    def __init__(self, config : dict , description) -> None:
        self.header = TaskDescription(config["header"], description)


class TaskDescription:
    '''
    ### Simple container that only contains one string (a description)
    #### Parametrs:
    - the configuration for this element (as json formatted dictionary)
    - the description, this container has to hold (it is validated before it is saved)
    #### Methods:
    - getter method that returns the internal description string
    '''

    def __init__(self,config : dict, descriptiveHeader : str) -> None:
        self.Config = self._checkConfig(config)
        self.internalString = self._checkHeader(descriptiveHeader)

    def get(self):
        return self.internalString

    def _checkConfig(self, config : dict):
        if type(config) != dict:
            raise Exception("config in wrong format!!!!!!!")
        try:
            config["maxHeaderLength"]
            return config
        except:
            raise Exception("maxHeaderLength is not in cofinguration")

    def _checkHeader(self, header : str):
        if type(header) != str:
            raise Exception("the header message needs to be a string but is: " + type(header))
        if len(header) > self.Config["maxHeaderLength"]:
            raise Exception("headline is to long")
        return header
 

class priority(Enum):
    low = 0
    higher = 1
    high = 2
    very_high = 3

    def calculatePriority():
        ''' 
        ### Desc: 
        calculates the priority of an ToDo 
        ### Parameters:
         - deadline 
         - expenditure of time
         - current Time 
        
        ### Returns:
        returns one priority element dependent on the given parameters
        '''
        pass


class complexity(Enum):
    lessThanAHour = 0
    lessThanThreeHours = 1
    lessThanADay = 2
    ## now come elements that are to big for a simple Todo (hint using a nested ToDo to split the big todo in smaller ones) 

    
    
     


    
