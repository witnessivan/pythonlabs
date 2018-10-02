class listItem(object):
    def __init__(self, value = None, next = None):
        self.value = value
        self.firstly = False
 
    def makeFirst(self):
        self.firstly = True
 
    def setNext(self, next):
        self.next = next

   
        

lst = []
input_num = int(input("Введите число элементов: "))
for i in range(input_num):
    lst.append(listItem(input()))
    if i == 0:
        lst[i].makeFirst();
    if i > 0:
        lst[i-1].setNext(lst[i])
    if i == input_num-1:
        lst[i].setNext(lst[0])
        
    
 for k in range(input_num):
       print("Сслыка на следующий элемент " + str(lst[k].value) + "->" + str(lst[k].next.value))
        

        

