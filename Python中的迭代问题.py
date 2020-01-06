class Node:
    
    def __init__(self,value):
        self._value=value
        self._children=[]
    def __repr__(self,):
        return 'Node{%s}' % (self._value)
    def add_child(self,node):
        self._children.append(node)
    def __iter__(self,):
        return iter(self._children)
    def depth_first(self,):
        yield self._value
        for c in self:
            yield from c.depth_first()
            
def main():
    
    root =Node(0)
    
    child1=Node(1)
    
    child2=Node(2)
    
    child3=Node(3)
    
    root.add_child(child1)
    
    root.add_child(child2)
    
    child2.add_child(child3)

    for node in root:
        
        print node 
    
    
if __name__=='__main__':
    
    main()
        
