__author__ = "imscreed"

class Member:

  def __init__(self,firstName,lastName):
    self.firstName = firstName
    self.lastName = lastName


  def setFirstName(self,firstName):
      self.firstName = firstName

  def setLastName(self,lastName):
      self.lastName = lastName

  def __str__(self):
    return self.firstName + " "+self.lastName

class FamilyTree:
  def __init__(self):
    self.childList = dict()

  #Find and Return the upper level node of a node
  def findParent(self,person):
    if person is None:
      return None
    for parent, children in self.childList.iteritems():
      for child in children:
        if child == person:
          return parent
    return None

  #Return the 2nd upper level node of a node - Find Parent and find the parent of the parent
  def getGrandParentNode(self,person):
    parent = self.findParent(person)
    grandParent = self.findParent(parent)
    return grandParent

  #Add a node to the parent node
  def addFamilyMember(self,person):
    if person is None:
      print "Person cannot be None"
      return
    if person not in self.childList:
      self.childList[person] = []
    else:
     print str(person) + " already present"
 
  #Set the root node
  def setFounder(self,person):
    if person is not None and person in self.childList:
      self.rootParent = person

  #Assign Parent and Children nodes
  def assign_Relationship(self,PARENT_NODE,CHILD_NODE):
    if PARENT_NODE == CHILD_NODE:
      print "Same Person"
      return
    if PARENT_NODE in self.childList and CHILD_NODE in self.childList:
       parent = self.findParent(CHILD_NODE)
       if parent is not None:
         children = self.childList[parent]
         children.remove(CHILD_NODE)
       vals = self.childList[PARENT_NODE]
       if CHILD_NODE not in vals:
          vals.append(CHILD_NODE)
    else:
       print "Add " + str(PARENT_NODE)


  #Find Degree of two nodes
  def find_degree(self, NODE_A, NODE_B):
    if NODE_A == NODE_B:
      print "Same Person, degree cannot be found"
      return
    PARENT_OF_NODE_A = self.findParent(NODE_A)
    PARENT_OF_NODE_B = self.findParent(NODE_B)
    if(PARENT_OF_NODE_A == PARENT_OF_NODE_B):
      return 2
    elif PARENT_OF_NODE_A == NODE_B or PARENT_OF_NODE_B == NODE_A:
      return 1
    else:
      return 3


   
  #Return the child node list after getting rootnode
  def __printTreeWithRootParent(self,person,spaces):
    if person is not None:
      print spaces + str(person)
      children = self.childList[person]
      for child in children:
        self.__printTreeWithRootParent(child,spaces + '\t')

  #Print Tree
  def printTree(self):
      self.__printTreeWithRootParent(self.rootParent,'')

  #Traverse each node and print as string
  def __str__(self):
   objStr=''
   for key,value in self.childList.iteritems():
     objStr = objStr + str(key) + ":["
     for person in value:
         objStr=objStr+ str(person)+", "
     objStr = objStr + "]\n"
   return objStr



if __name__ == "__main__":

  family_tree = FamilyTree()
  Marnush = Member("Marnush","Khan")
  Bee = Member("Bee","Khan")
  Cikandar = Member("Cikandar","Khan")
  Refaya = Member("Refaya","Mohammed")
  Dawood = Member("Dawood","Khan")
  Safiya = Member("Safiya","Ali")
  Somal = Member("Somal","Fara")
  Mariam = Member("Mariam","Ki")
  Tanvir = Member("Tanvir","Ahmed")
  Fathima = Member("Fathima","Awwal")
  FamilyMembers=[Marnush,Bee,Cikandar,Refaya,Dawood,Safiya,Somal,Mariam,Tanvir,Fathima]
  for member in FamilyMembers:
    family_tree.addFamilyMember(member)

  family_tree.assign_Relationship(Marnush,Cikandar)
  family_tree.assign_Relationship(Marnush,Dawood)
  family_tree.assign_Relationship(Marnush,Bee)
  family_tree.assign_Relationship(Cikandar,Refaya)
  family_tree.assign_Relationship(Dawood,Safiya)
  family_tree.assign_Relationship(Dawood,Somal)
  family_tree.assign_Relationship(Safiya,Mariam)
  family_tree.assign_Relationship(Refaya,Tanvir)
  family_tree.assign_Relationship(Refaya,Fathima)
  family_tree.setFounder(Marnush)
  family_tree.printTree()
  print "\nParent of Tanvir is:", family_tree.findParent(Tanvir)
  print "Grandparent of Tanvir is:", family_tree.getGrandParentNode(Tanvir)
  print "\nParent of Marnush is:", family_tree.findParent(Marnush)
  print "Grandparent of Safiya is:", family_tree.getGrandParentNode(Safiya)
  print "\nParent of Safiya is:", family_tree.findParent(Safiya)
  print "Grandparent of Mariam is:", family_tree.getGrandParentNode(Mariam)
  print "\nThe Relationship degree of Fathima and Tanvir is: ", family_tree.find_degree(Fathima, Tanvir)
  print "The Relationship degree of Safiya and Tanvir is: ", family_tree.find_degree(Safiya, Tanvir)
  print "The Relationship degree of Refaya and Cikandar is: ", family_tree.find_degree(Refaya, Cikandar)
