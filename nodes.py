#file contains the definitions of nodes or script segments 
file_path = "scripts/"
class connection:#edge connecting two nodes
	self.parent = None
	self.child = None
	self.duration = 0

	def __init__(nodeA, nodeB,duration):
		self.parent = nodeA
		self.child = nodeB
		self.duration = duration

	def modifyDuration(newDur):
		self.duration = newDur

class Node:
	#dictionary might be better here
	connections = [] #connections to other nodes (for script connections as defined above) these are out going edges
	inConnection = [] #connections to nodes that lead into said edge for later deletion/ termination of current node
	name = None
	text = None
	def __init__(self, name, load=False):#init
		self.name = name 
		if load != False:
			read()
		
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

	def delete():#need to delete all edges connecting to self as well!
		