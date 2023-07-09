# 55. Min Stack
# Medium

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.


# Solution Start provided:
# class MinStack:

#     def __init__(self):
        

#     def push(self, val: int) -> None:
        

#     def pop(self) -> None:
        

#     def top(self) -> int:
        

#     def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# -------- SOLUTION ------------------

# 1. Restate question
# 2. Ask clarifying questions
# 3. State assumptions
    # Must be done with O(1) time complexity (constant time), no loops cannot be used
    # The operations must be done on the front or end of the array
    # starts with empty stacks
# 4. Think through process out loud
#     4a. Brainstorm solution ideas
#     4b. Explain your rationale
#     4c. Discuss tradeoffs
#     4d. Suggest improvements

# start with two empty stacks, one to work with and one to keep track of minimum element

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val) # val pushed onto the stack
        if not self.min_stack or val <= self.min_stack[-1]: # if val less than or equal to the last (top) element of min_stack,
            self.min_stack.append(val)                      # then val gets pushed onto (appended) the top (end) of min_stack
                                                 
    def pop(self) -> None:
        # if the top element of the stack  is equal to the top element of the min_stack, then the top element of the min_stack is removed
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        # top element of the stack
        return self.stack[-1]
        

    def getMin(self) -> int:
        # the top element of the min_stack
        return self.min_stack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

