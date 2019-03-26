list=[]
class myNode(object):
    def __init__(self,v=0):
        self.value=v
        self.left=None
        self.right=None
        


class myTree(object):
    def __init__(self):
        self.root=myNode(250)
    def insert(self,node_1):
        if(self.root.value>node_1.value):
            self.root.left=node_1.value
            # print(self.root.left)
        elif(self.root.value<node_1.value):
            self.root.right=node_1.value
            # print(self.root.right)

        else:
            print("Duplicate Error")
        

    # def search(node_1):

    # def delete(node_1):

    # def printTree():
def test():
    t1=myTree()
    t1.insert(myNode(-20))
    t1.insert(myNode(300))

    print(t1.root.value)
    print(t1.root.right)
    print(t1.root.left)
    
    

def printTree(tree):
    while(tree.left!=None):
        print(tree.left)
    print(tree.value)
    while(tree.right!=None):
        print(tree.right)

test()