# NODE CLASS
class node:
    """DEFINING A CLASS TO CREATE SINGLE NODE FOR OUR STACK"""

    #CONSTRUCTOR FUNCTION
    def __init__(self, data):

        self.data = data #PASSING DATA IN NODE GIVEN BY THE USER

        self.next = None #PASSING THE DEFAULT VALUE IN OUR NEXT NODE

class Stack:
    """DEFINING A CLASS TO CREATE STACK"""

    #CONSTRUCTOR
    def __init__(self):
        """DEFINING A CONSTRUCTOR TO INITIALIZE A STACK"""

        self.top = None #INITIALIZING TOP TO NONE

        self.n = 0 #INITIALIZING NO. OF NODES TO 0

    #LEN FUNCTION
    def __len__(self):
        """DEFINING A FUNCTION TO RETURN THE NO. OF NODES IN OUR STACK"""

        return self.n #RETURNING THE NO. OF NODES

    #PUSH FUNCTION
    def push(self, passed_data):
        """DEFINING A FUNCTION TO INSERT VALUE IN OUR STACK"""

        new_node = node(passed_data) #MAKING A NEW NODE AND PASSING OUR DATA

        new_node.next = self.top #CREATING A LINK BETWEEN OLD AND NEW TOP

        self.top = new_node #DEFINING NEW NODE AS OUR TOP

        self.n += 1 #UPDATING THE NO. OF NODES IN OUR STACK

    #POP FUNCTION (LIFO FUNDAMENTAL)
    def pop(self):
        """DEFINING A FUNCTION TO DELETE VALUES FROM TOP"""

        if self.Is_Empty() : #LOGIC IF OUR STACK IS EMPTY

            return "Stack is Empty"

        else : #LOGIC IF STACK IS NOT EMPTY

            popped_data = self.top.data #STORING THE POPPED DATA

            self.top = self.top.next #ASSIGNING TOP TO NEXT NODE

            self.n -= 1 #UPDATING THE NO. OF NODES IN STACK

            return popped_data

    #PEEK FUNCTION
    def peek(self):
        """DEFINING A FUNCTION TO RETURN TOP OF OUR STACK"""

        if self.Is_Empty() : #IF OUR STACK IS EMPTY

            return "Stack is Empty" #RETURNING MSG IF STACK IS NOT EMPTY

        else :

            return self.top.data #RETURNING TOP IF STACK IS NOT EMPTY

    #PRINT FUNCTION
    def __str__(self):
        """DEFINING A DUNDER FUNCTION TO PRINT OUR STACK"""

        result = "" #CREATING A TEMP VARIABLE TO STORE OUR RESULT

        temp_node = self.top #CREATING A TEMPORARY NODE TO VISIT EACH ELEMENT IN OUR STACK

        for i in range(self.n): #DEFINING A LOOP TO UPDATE RESULT WITH EACH ELEMENT IN OUR STACK

            result = result + str(temp_node.data) + ">-" #APPROPRIATE SYNTAX

            temp_node = temp_node.next

        return ("[" + result[:-2] + "]") #RETURNING THE DESIRED RESULT

    #IS_EMPTY FUNCTION
    def Is_Empty(self):
        """DEFINING A FUNCTION TO CHECK IF OUR STACK IS EMPTY"""

        if self.top == None : #DEFINING OUR LOGIC

            return True

        else :

            return False
