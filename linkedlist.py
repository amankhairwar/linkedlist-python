class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        pass
    pass
class LinkedList:
    def __init__(self):
        self.head=None
        pass
    def insertBegin(self,data):
        node=Node(data,self.head)
        self.head=node
        pass
    def display(self):
        temp=self.head
        lltr=''
        while temp:
            lltr+=str(temp.data)+'-->'
            temp=temp.next
        print(lltr)
            
    def insertLast(self,data):
        if self.head is None:
            node=Node(data,None)
            self.head=node
            pass
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data,None)
        pass
    def insertList(self,data_list):
        for data in data_list:
            self.insertLast(data)
            pass
        pass
    def insertAfter(self,index,data):
        if index<0 or index>=self.getCount():
            raise Exception('invalid index number')
        temp=self.head
        count=0
        while temp:
            if count==index:
                node=Node(data,temp.next)
                temp.next=node
                break
            temp=temp.next
            count+=1
    def getCount(self):
        count=0
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
        return count
    def removeBegin(self):
        if self.head is not None:
            self.head=self.head.next
            return
    def removeLast(self):  #removing the last node
        if self.head is None:
            print('empty list')
        second_last=self.head  
        while second_last.next.next!=None: #it'll check if thr second last node ka next is Null
            second_last=second_last.next
        second_last.next=None
        return
    def searching(self,target):
        temp=self.head
        while temp is not None and temp.data!=target:
            temp=temp.next
        return temp is not None
    def removeAt(self,index,data):
        if index<0 or index>=self.getCount():
            raise Exception('invlid index')
        if index==self.head:
            self.head=self.head.next
        temp=self.head
        count=0
        while temp.next:
            if index==count-1:
                temp.next=temp.next.next
            count+=1
            temp=temp.next
    def reverse(self):
        temp=self.head
        prev=None
        while temp:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        self.head=prev
if __name__=="__main__":
    l=LinkedList()
    l.insertBegin(10)
    l.insertBegin(20)
    l.insertBegin(30)
    l.insertLast(40)
    l.insertLast(69)
    l.insertBegin(24)
    l.insertAfter(1,200)
    l.removeBegin()
    l.removeLast()
    l.display()
    #l.swapnodes(30,40)
    l.display()
    print(l.getCount())
    print(l.searching(30))
    l.reverse()
    l.display()
    
        
