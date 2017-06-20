class eventConverter():
    
    eventsT = ""
    
    events = []
    
    def __init__(self):
        pass
    
    def openFile(self, events):
        self.eventsT = open(events, "r").read()
        
       
    
    def convert(self):
        temp = ""
        var = 0
        x = 0
        
        for val in self.eventsT:
            
            if val != " ":
                temp += val
            else:
                if temp != "":
                    
                    self.events += [temp]
                    
                    temp = ""
                    var += 1
                else:
                    pass
        
        return self.events
        
        
                    
                         
converter = eventConverter()

converter.openFile("events.txt")

output = converter.convert()

finalStr = ""

eventArray = [[] for n in range(0)]
eventList = []
for n in range(int(int(len(output)) / 3)):
    for j in range(3):
        eventList += [output[(3 * n) + j]]
    eventArray.append(eventList)

q = 0
for r in range(len(eventList)):
    if(q == 2):
        var3 = eventList[r]
        finalStr += "{dec: " + var3 + ", ra: " + var2 + ", err: " + var1 + ", type: types.shower},\n"
        q = 0
    elif(q == 1):
        var2 = eventList[r]
        q+= 1
    else:
        var1 = eventList[r]
        q+= 1

    
print(finalStr)
    
    


    

        
