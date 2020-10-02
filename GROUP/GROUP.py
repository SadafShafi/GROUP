from multipledispatch import dispatch 
class Group():

    def __init__(self,List,pointer,switch_list = None):
        self.pointer = pointer
        self.List = List
        self.switch_list = switch_list
        self.steps = 1
    
    def __rmul__(self,num):
        self.steps = num
        return self
     
    @dispatch()   
    def switch(self):
        __ind = self.List.index(self.pointer)
        self.List,self.switch_list = self.switch_list,self.List
        self.pointer = self.List[__ind]
        return self.List[__ind]
        
    @dispatch(int)   
    def switch(self,point):
        self.pointer = point
        __ind = self.List.index(self.pointer)
        self.List,self.switch_list = self.switch_list,self.List
        self.pointer = self.List[__ind]
        return self.List[__ind] 
    
    @dispatch(float)   
    def switch(self,point):
        self.pointer = point
        __ind = self.List.index(self.pointer)
        self.List,self.switch_list = self.switch_list,self.List
        self.pointer = self.List[__ind]
        return self.List[__ind] 
    
    @dispatch(str)   
    def switch(self,point):
        self.pointer = point
        __ind = self.List.index(self.pointer)
        self.List,self.switch_list = self.switch_list,self.List
        self.pointer = self.List[__ind]
        return self.List[__ind] 
    
    @dispatch(complex)   
    def switch(self,point):
        self.pointer = point
        __ind = self.List.index(self.pointer)
        self.List,self.switch_list = self.switch_list,self.List
        self.pointer = self.List[__ind]
        return self.List[__ind] 
    
    @dispatch(bool)   
    def switch(self,point):
        self.pointer = point
        __ind = self.List.index(self.pointer)
        self.List,self.switch_list = self.switch_list,self.List
        self.pointer = self.List[__ind]
        return self.List[__ind] 
    
    @dispatch(list)   
    def switch(self,point):
        self.pointer = point
        __ind = self.List.index(self.pointer)
        self.List,self.switch_list = self.switch_list,self.List
        self.pointer = self.List[__ind]
        return self.List[__ind] 

    @dispatch() 
    def step(self):
        __ind = self.List.index(self.pointer)
        __ind += self.steps
        __ind = __ind%len(self.List) 
        self.steps=1
        self.pointer = self.List[__ind]
        return self.List[__ind]
    
    @dispatch(int) 
    def step(self,point):
        self.pointer = point
        __ind = self.List.index(self.pointer)
        __ind += self.steps
        __ind = __ind%len(self.List)
        self.steps=1
        return self.List[__ind]
    
    @dispatch(float) 
    def step(self,point):
        self.pointer = point
        __ind = self.List.index(self.pointer)
        __ind += self.steps
        __ind = __ind%len(self.List)
        self.steps=1
        return self.List[__ind]
    
    @dispatch(str) 
    def step(self,point):
        self.pointer = point
        __ind = self.List.index(self.pointer)
        __ind += self.steps
        __ind = __ind%len(self.List)
        self.steps=1
        return self.List[__ind]
    
    @dispatch(complex) 
    def step(self,point):
        self.pointer = point
        __ind = self.List.index(self.pointer)
        __ind += self.steps
        __ind = __ind%len(self.List)
        self.steps=1
        return self.List[__ind]
    
    @dispatch(bool) 
    def step(self,point):
        self.pointer = point
        __ind = self.List.index(self.pointer)
        __ind += self.steps
        __ind = __ind%len(self.List)
        self.steps=1
        return self.List[__ind]
    
    @dispatch(list) 
    def step(self,point):
        self.pointer = point
        __ind = self.List.index(self.pointer)
        __ind += self.steps
        __ind = __ind%len(self.List)
        self.steps=1
        return self.List[__ind]
    