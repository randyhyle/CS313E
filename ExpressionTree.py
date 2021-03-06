#  File: ExpressionTree.py
#  Description: A program that outputs the prefix and postfix expression.
#  Student Name: Hoang Randy Hy Le
#  Student UT EID: hhl385
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number:52590
#  Date Created:
#  Date Last Modified:

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

    def __str__(self):
        return '(' + str(self.data) + ')'


class Tree(object):
    def __init__(self):
        self.root = Node()

    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree(self, expr):
        # Must split expr with spaces
        expr = expr.split(' ')
        # Create a new stack
        new_stack = Stack()
        # Start the tree at its root
        current = self.root
        for token in expr:
            if token == '(':
                current.lChild = Node()
                new_stack.push(current)
                current = current.lChild
            elif token in operators:
                current.data = token
                new_stack.push(current)
                current.rChild = Node()
                current = current.rChild
            elif token == ')':
                if not new_stack.is_empty():
                    current = new_stack.pop()
            elif token != ' ':
                current.data = token
                current = new_stack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        # If the left child and the right child don't exist, return
        # current nodes data as a string after evaluating
        if not aNode.lChild and not aNode.rChild:
            return str(aNode.data)
        # Otherwise, evaluate in a format like so, (oper1) operand (oper2)
        return float(eval(f'{self.evaluate(aNode.lChild)} {aNode.data} '
                          f'{self.evaluate(aNode.rChild)}'))

    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        if not aNode.lChild and not aNode.rChild:
            return str(aNode.data)
        # Using recursion. node.data is placed before other nodes.
        return f'{aNode.data} {self.pre_order(aNode.lChild)} ' \
               f'{self.pre_order(aNode.rChild)}'

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        if not aNode.lChild and not aNode.rChild:
            return str(aNode.data)
        # Use recursion. Data is after everything.
        return f'{self.post_order(aNode.lChild)} ' \
               f'{self.post_order(aNode.rChild)} {aNode.data}'


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
