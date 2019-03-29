import program

import logging as logger

class SingletonHolder:
    pass

class StatsTracker:
     
    
    sh = SingletonHolder()

    def __init__(self):
        self.stats_buider = ""
        self.named_vals = {}
        logger.info(type(self))

    def record(self, obj):
        self.stats_buider += "%s,"%str(obj)

    def record(self, s_type, obj):
        self.named_vals[s_type] = str(obj)
    
    def print(self):
        for key in self.named_vals.keys():
            record(self.named_vals[key])
        
        logger.critical(self.stats_buider)
        
    @classmethod         
    def getInstance(cls):
        return SingletonHolder.INSTANCE 
    
class SingletonHolder:
    INSTANCE = None       
    def __init__(self):
        INSTANCE = StatsTracker()