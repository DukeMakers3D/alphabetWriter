from threading import Timer

#Repeated Timer is a threading timer that runs a function every n seconds
class RepeatedTimer(object):
    def __init__(self,interval,function):
        self.timer = None
        self.interval = interval
        self.function = function
        self.is_running = False
        self.start()
        
    def start(self):
        if not self.is_running:
            self.is_running = True
            self.timer = Timer(self.interval,self.run)
            self.timer.start()
    
    def run(self):
        self.is_running = False
        self.function()
        self.start()
    
    def stop(self):
        self.timer.stop()
        self.is_running = False
    
    
    