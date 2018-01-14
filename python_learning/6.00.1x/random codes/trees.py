class Member(object):
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a member. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent 

    def is_parent(self, mother):
        """
        mother: Member
        Returns: Boolean, whether or not `mother` is the 
        parent of this Member
        """
        return self.parent == mother  

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children 


class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)
    
        
            
    def distance_to_root(self,a):
        """
        Returns the distance of node member  a from the root of the tree
        """
        a_node=self.names_to_nodes[a]
        dummy=a_node
        count=1
        if a_node==self.root:
            return 0
        while not dummy.is_parent(self.root):
            count+=1
            dummy=dummy.get_parent()
        return count    
        
             
    def find_ancestor(self,a,b):
        """
        finds the comon ancestror for nodes a and b
        """
        a_node=self.names_to_nodes[a]
        b_node=self.names_to_nodes[b]
        d1=a_node
        d2=b_node
        l1=[d1]
        l2=[d2]
        if d1==d2:
            return d1
        if d1==self.root or d2==self.root:
            return self.root    
        while (d1.get_parent() not in l2) and (d2.get_parent() not in l1)and d1!=d2:
            l1.append(d1.get_parent())
            l2.append(d2.get_parent())
            if d1.get_parent()!=self.root:
                d1=d1.get_parent()
            if d2.get_parent()!=self.root:
                d2=d2.get_parent()
        
        if d1==d2:
            return d1                
                    
        if d1.get_parent() in l2:
            return d1.get_parent()        
        else:
            return d2.get_parent()                         
                            

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 

        Keyword arguments: 
        a -- string that is the name of node a
        b -- string that is the name of node b

        cousin type:
          -1 if a and b are the same node.
          -1 if either one is a direct descendant of the other
          >=0 otherwise, it calculates the distance from 
          each node to the common ancestor.  Then cousin type is 
          set to the smaller of the two distances, as described 
          in the exercises above

        degrees removed:
          >= 0
          The absolute value of the difference between the 
          distance from each node to their common ancestor.
        """
        
        ## YOUR CODE HERE ####
        a_node=self.names_to_nodes[a]
        b_node=self.names_to_nodes[b]
        level1=self.distance_to_root(a)
        level2=self.distance_to_root(b)
        degree=abs(level1-level2)
        common_ancestor=self.find_ancestor(a,b)
        
        if common_ancestor==a_node or common_ancestor==b_node:
            cousin=-1
            return(cousin,degree)
        
        else:        
            for i in self.names_to_nodes.keys():
                if self.names_to_nodes[i]==common_ancestor:
                    common=i
                    break
                    
            levelc=self.distance_to_root(common)
            cousin=min(abs(level1-levelc),abs(level2-levelc))
            return (cousin-1,degree)            


f = Family("a")
f.set_children("a", ["b", "c"])
f.set_children("b", ["d", "e"])
f.set_children("c", ["f", "g"])

f.set_children("d", ["h", "i"])
f.set_children("e", ["j", "k"])
f.set_children("f", ["l", "m"])
f.set_children("g", ["n", "o", "p", "q"])

words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]

## These are your test cases. 

## The first test case should print out:
## 'b' is a zeroth cousin 0 removed from 'c'
t, r = f.cousin("b", "c")
print "'b' is a", words[t],"cousin", r, "removed from 'c'"

## For the remaining test cases, use the graph to figure out what should 
## be printed, and make sure that your code prints out the appropriate values.

t, r = f.cousin("d", "f")
print "'d' is a", words[t],"cousin", r, "removed from 'f'"

t, r = f.cousin("i", "n")
print "'i' is a", words[t],"cousin", r, "removed from 'n'"

t, r = f.cousin("q", "e")
print "'q' is a", words[t], "cousin", r, "removed from 'e'"

t, r = f.cousin("h", "c")
print "'h' is a", words[t], "cousin", r, "removed from 'c'"

t, r = f.cousin("h", "a")
print "'h' is a", words[t], "cousin", r, "removed from 'a'"

t, r = f.cousin("h", "h")
print "'h' is a", words[t], "cousin", r, "removed from 'h'"

t, r = f.cousin("a", "a")
print "'a' is a", words[t], "cousin", r, "removed from 'a'"
