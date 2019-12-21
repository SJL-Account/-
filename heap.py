class maxHeap:
    
    def __init__(self,k):
        
        self.k=k
        self.heap_list=[]
        
    
    def _get_len(self):
        return len(self.heap_list)
    
    def _get_keys(self):
        return set(self.heap_list)
    
    def insert(self,num):
        
        self.heap_list.append(num)
        self._upload(self._get_len()-1)
        
    def remove_max(self):
        
        self.swap(0,self._get_len()-1)
        self.heap_list=self.heap_list[:-1]
        #交换队尾元素和num
        self._download()
     
    def top(self):
        
        return self.heap_list[0]
    
    def pop(self):
        
        top=self.top()
        
        self.remove_max()
        
        return top
    
    def _left(self,i):
        
        return i*2+1
    
    def _right(self,i):
        
        return i*2+2
    
    def _is_left(self,i):
        
        return i%2==1
    
    def _is_right(self,i):
        
        return i%2==0
    
    def _has_left(self,i):
        
        return self._left(i)<self._get_len()
    def _has_right(self,i):
        
        return self._right(i)<self._get_len()
    
    def _parent(self,i):
        
        return (i-1)//2
    
    def get_k(self):
        
        return self.heap_list
    
    
    def _upload(self,i):

        parent_index=self._parent(i)
        
        #从最后一个节点回溯和其parent节点进行比较
        parent_index=self._parent(i)
        #r如果当前num没有到顶点，并且当前num小于parent,交换num和parent的值，启动递归上浮
        if i>0 and self.heap_list[i]>self.heap_list[parent_index]:
            self.swap(i,parent_index)
            self._upload(parent_index)

    def _download(self):
        
        #次数走下沉
        
        mid=self._get_len()//2
        
        for i in range(mid):
            
            if self._has_left(i):
                
                max_node=self._left(i)
                
            if  self._has_right(i):
                
                max_node=self._right(i) if self.heap_list[self._right(i)]>self.heap_list[max_node] else max_node
                
            if self.heap_list[i]<self.heap_list[max_node]:
                
                self.swap(i,max_node)
          
    
    def swap(self,i,j):
        
        self.heap_list[i],self.heap_list[j]=self.heap_list[j],self.heap_list[i]
    
    def sort(self):
        
        self.adjust(self._get_len()-1)
    
    def adjust(self,n):
        
        #print (self.heap_list)
        
        #排序走上浮
        if n==0:
            return 
        
        mid=n//2
        
        for i in range(mid)[::-1]:
            
            if self._has_left(i):
                
                max_node=self._left(i)
                
            if  self._has_right(i):
                
                max_node=self._right(i) if self.heap_list[self._right(i)]>self.heap_list[max_node] else max_node
                
            if self.heap_list[i]<self.heap_list[max_node]:
                
                self.swap(i,max_node)
            
        
        self.swap(0,n)
        
        self.adjust(n-1)
        
        #建堆
        #顶点和尾部互换
        #切割尾点
        
        #再建堆
        #再互换
        #再切割
        
        #直到待排数组为一个元素

class minHeap:
    
    def __init__(self,k):
        
        self.k=k
        self.heap_list=[]
        
    
    def _get_len(self):
        return len(self.heap_list)
    
    def _get_keys(self):
        return set(self.heap_list)
    
    def insert(self,num):
        
        self.heap_list.append(num)
        self._upload(self._get_len()-1)
        
    def remove_min(self):
        
        self.swap(0,self._get_len()-1)
        self.heap_list=self.heap_list[:-1]
        #交换队尾元素和num
        self._download()
     
    def top(self):
        
        return self.heap_list[0]
    
    def pop(self):
        
        top=self.top()
        
        self.remove_max()
        
        return top
    
    def _left(self,i):
        
        return i*2+1
    
    def _right(self,i):
        
        return i*2+2
    
    def _is_left(self,i):
        
        return i%2==1
    
    def _is_right(self,i):
        
        return i%2==0
    
    def _has_left(self,i):
        
        return self._left(i)<self._get_len()
    def _has_right(self,i):
        
        return self._right(i)<self._get_len()
    
    def _parent(self,i):
        
        return (i-1)//2
    
    def get_k(self):
        
        return self.heap_list
    
    
    def _upload(self,i):

        parent_index=self._parent(i)
        
        #从最后一个节点回溯和其parent节点进行比较
        parent_index=self._parent(i)
        #r如果当前num没有到顶点，并且当前num大于parent,交换num和parent的值，启动递归上浮
        if i>0 and self.heap_list[i]<self.heap_list[parent_index]:
            self.swap(i,parent_index)
            self._upload(parent_index)

    def _download(self):
        
        #下降
        
        mid=self._get_len()//2
        
        for i in range(mid):
            
            if self._has_left(i):
                
                min_node=self._left(i)
                
            if  self._has_right(i):
                
                min_node=self._right(i) if self.heap_list[self._right(i)]<self.heap_list[min_node] else min_node
                
            if self.heap_list[i]>self.heap_list[min_node]:
                
                self.swap(i,min_node)
          
    
    def swap(self,i,j):
        
        self.heap_list[i],self.heap_list[j]=self.heap_list[j],self.heap_list[i]
    
    def sort(self):
        
        self.adjust(self._get_len()-1)
    
    def adjust(self,n):
        
        #print (self.heap_list)
        
        #排序走上浮
        if n==0:
            return 
        
        mid=n//2
        
        for i in range(mid)[::-1]:
                  
            if self._has_left(i):
                
                min_node=self._left(i)
                
            if  self._has_right(i):
                
                min_node=self._right(i) if self.heap_list[self._right(i)]<self.heap_list[min_node] else min_node
                
            if self.heap_list[i]>self.heap_list[min_node]:
                
                self.swap(i,min_node)
          
        
        self.swap(0,n)
        
        self.adjust(n-1)
        
        #建堆
        #顶点和尾部互换
        #切割尾点
        
        #再建堆
        #再互换
        #再切割
        
        #直到待排数组为一个元素
heap=minHeap(5)
heap.insert(3)
heap.insert(4)
heap.insert(1)
heap.insert(3)
heap.insert(2)
heap.heap_list

def top_k(heap):
    for i in range(1000000):
        if i > heap.top():
            heap.heap_list[0]=i
            heap._download()  
