#file contains the definitions of nodes or script segments 

'''
	Connections are the decisions made while nodes are the actual script content
'''
file_path = "scripts/"
class connection:#edge connecting two nodes
	self.parent = None
	self.child = None
	decision = None	#the decision made (also the file name)

	def __init__(self,nodeA, nodeB,decision):#nodeA, nodeB should be pointers to objects while decision should be a string
		self.parent = nodeA
		self.child = nodeB
		self.decision = decision
	def rename(decision):
		self.decision = decision
'''
	adj list not used as there could be multiple connections between two nodes (insignificant decisions that effect future outcomes and not the current one)
'''
class Node:
	#dictionary might be better here
	connections = [] #connections to other nodes (for script connections as defined above) these are out going edges
	inConnection = [] #connections to nodes that lead into said edge for later deletion/ termination of current node
	name = None
	text = None #actual script
	self.duration

	def __init__(self, name, load=False, duration=None):#init
		self.name = name 
		if load != False:
			read()
		self.duration = duration
	
	def modifyDuration(newDur):
		self.duration = newDur	

	def write():
		file = open(file_path+name,"r")
		self.text = file.read()
		file.close()

	def read():
		file = open(file_path+name,"w")
		file.write(self.text)
		file.close()

	def add_connection(toNode,duration=None):
		self.connections.append(connection(self,toNode,duration))
		toNode.inConnection.append(self)

	def delete_connection():
		#TODO:
		
	def delete():#need to delete all edges connecting to self as well!
		#TODO:
		