
class Stack():


    def __init__(self):

        self.items = []


    def push(self, value):

        return self.items.append(value) # Adds a value to top of the stack


    def pop(self):

        # If there is nothing in the stack, return null object
        if self.size() == 0:
            return None

        return self.items.pop() # Return the item at the top of the stack


    def size(self):

        # Return the length of the list to say how many items there are
        return len(self.items)


    def output(self):
        print(str(self.items))


if __name__ == "__main__":

    s = Stack()

    # Add values to the stack
    s.push(2)
    s.output()
    s.push(5)
    s.output()

    print("Retrieved value: " + str(s.pop()))
