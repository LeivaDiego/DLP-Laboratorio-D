from models.node import node
from graphviz import Digraph

class Tree():
    def __init__(self, postfixExp):
        self.postfixExp = postfixExp
        self.root = None

    def generateTree(self):
        stackNodes = []
        numPos = 1
        
        for symbol in self.postfixExp:
            if (not symbol.isOperator):
                newNode = node(symbol, number=numPos)
                stackNodes.append(newNode)
                numPos += 1
            else:
                if (symbol.label in '*?+'):
                    leftNewNode = stackNodes.pop()
                    newNode = node(symbol, leftNewNode)
                    stackNodes.append(newNode)
                    
                else:
                    rightNewNode = stackNodes.pop()
                    leftNewNode = stackNodes.pop()
                    newNode = node(symbol, leftNewNode, rightNewNode)
                    stackNodes.append(newNode)
          
        self.root = stackNodes.pop()                  
        return self.root
                    
    def printTree(self, tree):
        for node in tree:
            print(node)
            
    def create_node_graph(self, node, dot):
        if node is not None:
            dot.node(str(id(node)), str(node.symbol))
            if node.leftChild is not None:
                dot.edge(str(id(node)), str(id(node.leftChild)))
                self.create_node_graph(node.leftChild, dot)
            if node.rightChild is not None:
                dot.edge(str(id(node)), str(id(node.rightChild)))
                self.create_node_graph(node.rightChild, dot)

    
    def print_final_Tree(self, nameFile):
        dot = Digraph()
        dot.format = 'png'
        self.create_node_graph(self.root, dot)
        dot.render(f'./outputs/{nameFile}', view=True, cleanup=True)