class Queue():


    def __init__(self):
        self.items = []


    def enqueue(self, value):

        self.items.insert(0, value)


    def dequeue(self):

        if self.size() > 0:
            return self.items.pop()

        else:
            return IndexError("Queue is empty.")


    def size(self):

        # Return the length of the list to say how many items there are
        return len(self.items)


    def output(self):
        print(str(self.items))


if __name__ == "__main__":

    q = Queue()

    # Add values to the queue
    q.enqueue(2)
    q.output()
    q.enqueue(5)
    q.output()

    print("Retrieved value: " + str(q.dequeue()))
    q.output()
