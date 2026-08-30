# NODE CLASS
class node:
    """DEFINING A CLASS TO CREATE SINGLE NODE FOR OUR LL"""

    #CONSTRUCTOR FUNCTION
    def __init__(self, value):

        self.value = value #PASSING VALUE IN NODE GIVEN BY THE USER

        self.next = None #PASSING THE DEFAULT VALUE IN OUR NEXT NODE

class LinkedList:
    """DEFINING A CLASS TO CREATE LL"""

    #CONSTRUCTOR
    def __init__(self):
        """DEFINING A CONSTRUCTOR TO INITIALIZE LL"""

        self.head = None #INITIALIZING HEAD TO NONE

        self.n = 0 #INITIALIZING NO. OF NODES TO 0

    #LEN FUNCTION
    def __len__(self):
        """DEFINING A FUNCTION TO RETURN THE LENGTH OF OUR LL"""

        return self.n #RETURNING THE NO. OF NODES
    
    #INSERT HEAD FUNCTION
    def insert_head(self, data):
        """DEFINING A FUNCTION TO INSERT VALUE FROM HEAD IN OUR LL"""

        new_node = node(data) #MAKING A NEW NODE AND PASSING OUR DATA

        new_node.next = self.head #CREATING A LINK BETWEEN OLD AND NEW HEAD

        self.head = new_node #DEFINING NEW NODE AS OUR HEAD

        self.n += 1 #UPDATING THE NO. OF NODES IN OUR LL

    #APPEND FUNCTION
    def append(self, data):
        """DEFINING A FUNCTION TO ADD NODES FROM LAST """

        if self.head == None : #DEFINING THE LOGIC WHEN OUR LL IS EMPTY

            self.head = node(data)

            self.n += 1

        else :

            new_node = node(data) #MAKING A NEW NODE AND PASSING OUR DATA

            curr = self.head #DEFINING A TEMPORARY VARIABLE FOR OUR LOOP

            while curr.next != None : #DEFINING OUR LOOP TO GO IN THE END 

                curr = curr.next

            curr.next = new_node #MAKING CONNECTION BETWEEN OUR NEW AND OLD TAIL

            self.n += 1 #UPDATING THE NO. OF NODES IN OUR LL

    #INSERT AFTER FUNCTION
    def insert_after(self, after, data):
        """DEFINING A FUNCTION TO INSERT NODES IN BETWEEN OUR LL"""

        new_node = node(data) #MAKING A NEW NODE AND PASSING OUR DATA

        curr = self.head #DEFINING A TEMPORARY VARIABLE FOR OUR LOOP

        while curr != None : #DEFINING OUR LOOP TO GO IN THE DESIRED POSITION

            if curr.value == after : #DEFINING LOGIC TO CHECK IF GIVEN ENTITY IS IN OUR LL

                new_node.next = curr.next #CREATING A NEW LINK 

                curr.next = new_node #UPDATING THE EXISTING LINK

                self.n += 1 #UPDATING THE NO. OF NODES IN OUR LL

                return

            elif curr.next == None : #IF ENTITY NOT IN OUR LL

                print("No such entity exists in LL") #MSG TO PRINT

                return

            curr = curr.next

    #TRAVERSING FUNCTION
    def __getitem__(self, value):
        """DEFINING A DUNDER FUNCTION TO TRAVERSE AND GET SINGLE ITEM FROM OUR LL"""

        if value >= self.n or value < (-self.n): #DEFINING A LOGIC FOR INVALID INDEX

            return("Invalid Index")

        elif value < 0 : #DEFINING A LOGIC FOR NEGATIVE INDEXING

            value += self.n

            return self.__getitem__(value)

        else : #LOGIC FOR NORMAL INDEXING

            temp_node = self.head #CREATING A TEMPORARY NODE

            for i in range(value): #DEFINING A LOOP TO TRAVERSE IN OUR LL

                temp_node = temp_node.next

            return temp_node.value #RETURNING THE DESIRED VALUE

    #PRINT FUNCTION
    def __str__(self):
        """DEFINING A DUNDER FUNCTION TO PRINT OUR LL"""

        result = "" #CREATING A TEMP VARIABLE TO STORE OUR RESULT

        temp_node = self.head #CREATING A TEMPORARY NODE TO VISIT EACH ELEMENT IN OUR LL

        for i in range(self.n): #DEFINING A LOOP TO UPDATE RESULT WITH EACH ELEMENT IN OUR LL

            result = result + str(temp_node.value) + ">-" #APPROPRIATE SYNTAX

            temp_node = temp_node.next

        return ("[" + result[:-2] + "]") #RETURNING THE DESIRED RESULT

    #CLEAR FUNCTION
    def clear(self):
        """DEFINING A FUNCTION TO DELETE THE ENTIRE LL I.E MAKE IT EMPTY"""

        self.head = None #SETTING HEAD TO NONE WHICH MEANS EMPTY LL

        self.n = 0 #UPDATING NO. OF ELEMENTS IN OUR LL

    #DELETE HEAD FUNCTION 
    def del_head(self):
        """DEFINING A FUNCTION TO DELETE THE ELEMENT IN THE HEAD NODE"""

        if self.head == None: #LOGIC IF LL IS ALREADY EMPTY

            print("LL is empty")

            return

        self.head = self.head.next #REMOVING THE HEAD NODE

        self.n -= 1 #UPDATING NO. OF ELEMENTS IN OUR LL

    #POP FUNCTION
    def pop(self):
        """DEFINING A FUNCTION TO REMOVE THE ELEMENT IN TAIL NODE"""

        if self.head == None: #LOGIC IF LL IS ALREADY EMPTY

            print("LL is empty")

            return

        if self.head.next == None : #LOGIC IF THERE IS ONLY ONE ELEMENT IN OUR LL

            self.head = None 

            return

        temp = self.head #CREATING A TEMPORARY NODE FOR OUR LOOP

        while temp.next.next != None : #DEFINING OUR LOOP

            temp = temp.next

        temp.next = None #REMOVING THE LAST ELEMENT

        self.n -= 1 #UPDATING NO. OF ELEMENTS IN OUR LL

    #REMOVE FUNCTION
    def remove(self, data):
        """DEFINING A FUNCTION TO REMOVE ANY VALUE FROM OUR LL"""

        temp = self.head #CREATING A TEMPORARY NODE FOR OUR LOOP

        if temp == None : #LOGIC IF LL IS ALREADY EMPTY

            print("LL is empty")

            return

        if temp.value == data : #LOGIC IF FIRST VALUE ITSELF IS MATCHING

            self.del_head()       

            return

        for i in range(self.n+1) : #DEFINING OUR LOOP

            if temp == None : #LOGIC IF NO SUCH ELEMENT IN OUR LL

                print("No such element found in LL")

                return

            if temp.next.value == data : #LOGIC IF ELEMENT IS FOUND

                temp.next = temp.next.next

                return

            temp = temp.next 

            self.n -= 1 #UPDATING NO. OF ELEMENTS IN OUR LL

    #SEARCH FUNCTION
    def search(self, data):
        """DEFINING A FUNCTION TO SEARCH THE INDEX NO. OF ANY ELEMENT IN OUR LL"""

        temp = self.head #CREATING A TEMPORARY NODE FOR OUR LOOP

        i = 0 #DEFINING A TEMPORARY VARIABLE TO COUNT OUR INDEX NO.

        if temp == None : #LOGIC IF LL IS ALREADY EMPTY
        
                    return ("LL is empty")                   

        while temp.value != data : #DEFINING OUR LOOP

            if temp.next == None: #LOGIC IF NO SUCH ELEMENT EXISTS IN OUR LL

                return("No such element exists in our LL")

            temp = temp.next 

            i += 1

        return i

    #DELETE BY INDEX FUNCTION
    def __delitem__(self, value):
        """DEFINING A FUNCTION TO REMOVE ELEMENT USING THEIR INDEX NO. FROM OUR LL"""

        if value >= self.n or value < (-self.n): #DEFINING A LOGIC FOR INVALID INDEX
        
            return("Invalid Index")

        elif value < 0 : #DEFINING A LOGIC FOR NEGATIVE INDEX
        
            value += self.n
        
            return self.__delitem__(value)

        elif value == 0 : #LOGIC IF WE HAVE TO REMOVE ITEM AT 0TH INDEX

            self.del_head()

            return

        else : #LOGIC FOR NORMAL INDEX
        
            temp_node = self.head #CREATING A TEMPORARY NODE
        
            for i in range(value-1): #DEFINING A LOOP TO TRAVERSE IN OUR LL
        
                temp_node = temp_node.next

            temp_node.next = temp_node.next.next

            self.n -= 1

            return
        
ll = LinkedList()
ll.append(5)
ll.append(21)
ll.append(3)
print(ll)
del ll[-1]
print(ll)