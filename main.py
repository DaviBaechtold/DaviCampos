import time

class Stack:
    def __init__(self):
        self.__stack = [] 
        self.cont = 0
        self.capacity = 10
  
    def push(self, str):
        self.cont += 1
        self.__stack.insert(0,str)
        
    def pop(self):
        self.__stack.pop()

    def empty(self):
        if self.__stack is None:
            print("Pilha Vazia")
        elif len(self.__stack) == 10:
              print("Pilha Cheia")
        else:
            print("Pilha não esta vazia ou cheia")

    def lenght(self):
        return len(self.__stack)

    def capacit(self):
        print(self.capacity - len(self.__stack))

    def TimeSum(self):
        start = time.time()
        sum(self.__stack)
        end = time.time()
        print("Total de somas: ",sum(self.__stack))
        print("Tempo: ", end - start, "segundos")
        
class Fist_InOut:
    def __init__(self):
        self.__io = [] #io -> In Out
        self.cont = 0
        self.capacity = 10
    
    def push(self, str):
        self.cont += 1
        self.__io.append(str)
    
    def pop(self):
        self.__io.pop()

    def empty(self):
        if self.__io is None:
            print("Lista Vazia")
        elif len(self.__io) == 10:
           print("Lista Cheia")
        else:
            print ("Linha nao esta cheia ou vazia")
            
    def lenght(self):
        return len(self.__io)

    def capacit(self):
        print("the capacity is: ", self.capacity -len(self.__io))

    def TimeSum(self):
        start = time.time()
        sum(self.__io)
        end = time.time()
        print("Sum: ", sum(self.__io))
        print("Run time:" ,end - start, "second")

def main():

    list = Fist_InOut()
    pilha = Stack()
    i= 0
    for i in range(10):
        list.push(i)
        pilha.push(i)

    print("*****1 a 1.000.000****")
    pilha.pop()
    pilha.TimeSum()
    print("++++1.000.000 a 1++++")
    list.pop()
    list.TimeSum()

if __name__ == "__main__":
    main()