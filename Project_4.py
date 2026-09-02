#NODE CLASS
class Node :
    """DEFINING A CLASS TO CREATE A SINGLE NODE FOR OUR QUEUE"""

    def __init__(self, data):
        """CONSTRUCTOR FUNCTION TO ASSIGN DEFAULT VALUES"""

        self.data = data

        self.next = None

#QUEUE CLASS
class Queue :
    """DEFINING A CLASS TO CREATE QUEUE"""

    def __init__(self):
        """DEFINING A CONSTRUCTOR FUNCTION TO ASSIGN DEFAULT VALUES"""

        self.front = None

        self.rear = None

        self.n = 0 

    def len(self):
        """DEFINING A FUNCTION TO RETURN LENGTH OF OUR QUEUE"""

        return self.n

    def enqueue(self, value):
        """DEFINING A FUNCTION TO INSERT DATA FROM REAR (FIFO)"""

        New_Node = Node(value)

        if self.is_empty():

            self.rear = New_Node

            self.front = self.rear

        else :

            self.rear.next = New_Node

            self.rear = self.rear.next

        self.n += 1 

    def dequeue(self):
        """DEFINING A FUNCTION TO DELETE VALUES FROM FRONT (FIFO)"""

        if self.is_empty():

            raise Exception("Can't Dequeue, Queue is Empty")

        else :

            Temp = self.front 

            self.front = self.front.next

            self.n -= 1

        if self.is_empty():

            self.rear = None

        return Temp.data

    def is_empty(self):
        """DEFINING A FUNCTION TO CHECK IF OUR QUEUE IS EMPTY OR NOT"""

        if self.n == 0 :

            return True

        else :

            return False

    def __str__(self):
        """DEFINING A FUNCTION TO PRINT OUR QUEUE"""

        if self.is_empty() :

            return ("[]")

        else :

            result = ""

            temp = self.front

            for i in range(self.n):

                result = result + str(temp.data) + "-"

                temp = temp.next

            return f"[{result[:-1]}]"

    def front_item(self):
        """DEFINING A FUNCTION TO RETURN FRONT ITEM"""

        if self.is_empty():

            raise Exception("Queue is Empty")

        else :

            return self.front.data

    def rear_item(self):
            """DEFINING A FUNCTION TO RETURN REAR ITEM"""
    
            if self.is_empty():
    
                raise Exception("Queue is Empty")
    
            else :
    
                return self.rear.data

        

q = Queue()

print(q.len())
print(q)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.len())
print(q)
print(q.front_item())
print(q.rear_item())
print(q.dequeue())
print(q.len())
print(q)



        




    


