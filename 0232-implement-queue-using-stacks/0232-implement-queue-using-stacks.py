class MyQueue:
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def push(self, x: int) -> None:
        # Push the element to the stack used for push operation
        self.stack_push.append(x)

    def pop(self) -> int:
        # If the stack used for pop operation is empty, transfer elements from the stack used for push operation
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())

        # Pop the element from the stack used for pop operation
        return self.stack_pop.pop()

    def peek(self) -> int:
        # If the stack used for pop operation is empty, transfer elements from the stack used for push operation
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())

        # Return the top element from the stack used for pop operation
        return self.stack_pop[-1]

    def empty(self) -> bool:
        # Check if both stacks are empty
        return not self.stack_push and not self.stack_pop
