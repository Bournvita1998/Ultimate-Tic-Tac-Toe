from simulator import *
import random

class Player7:

	def __init__(self):
		#print "entry 1"
		self.ALPHA = -100000000
		self.BETA = 100000000

	def minimax(self,old_move, depth, max_depth, alpha, beta, isMax, p_board, p_block, flag1, flag2, best_node):
		pass
	
	def check_utility(self,block,board) :
		a = random.randint(-50,50)
		#print a
		return a

	def move(self,board,old_move,flag1) :
		if flag1 == 'x' :
			flag2 = 'o'
		else :
			flag2 = 'x'
		(utility_value, best_node) = self.minimax(old_move,0,5,self.ALPHA,self.BETA,True,board, (1,1), flag1, flag2, (7,7))
		#return (int(best_node[0]), int(best_node[1]))
		# print utility_value
		# print best_node
		return best_node
