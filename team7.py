from simulator import *
import random



class Player7:

	def __init__(self):
		self.ALPHA = -100000000
		self.BETA = 100000000

	def minimax(self,old_move, depth, max_depth, alpha, beta, isMax, p_board, p_block, flag1, flag2, best_node):
		if depth==max_depth:
			utility = self.check_utility(p_block,p_board)
			if flag1 == 'o':
				return (-utility,old_move)
			return (utility,old_move)
		else:
			children_list = p_board.find_valid_move_cells(old_move)
			if len(children_list) == 0:
				utility = self.check_utility(p_block,p_board)
				if flag1 == 'o':
					return (-utility,old_move)
				return (utility,old_move)
			for child in children_list:
				if isMax:
					p_board.board_status[child[0]][child[1]] = flag1
				else:
					p_board.board_status[child[0]][child[1]] = flag2
				if isMax:
					score = self.minimax (child,depth+1,max_depth,alpha,beta,False,p_board,p_block,flag1,flag2,best_node)
					if (score[0] > alpha):
		        	          alpha = score[0]
		        	          best_node = child
				else:
					score = self.minimax (child,depth+1,max_depth,alpha,beta,True,p_board,p_block,flag1,flag2,best_node)
					if (score[0] < beta):
		        	          beta = score[0]
		        	          best_node = child
				p_board.board_status[child[0]][child[1]] = '-'
				if (alpha >= beta):
					 break
			if isMax:
				return (alpha, best_node)
			else:
				return(beta, best_node)

	def check_utility(self,block,board) :
		a = random.randint(-50,50)
		return a

	def move(self,board,old_move,flag1) :
		if flag1 == 'x' :
			flag2 = 'o'
		else :
			flag2 = 'x'
		(utility_value, best_node) = self.minimax(old_move,0,5,self.ALPHA,self.BETA,True,board, (1,1), flag1, flag2, (7,7))
		return best_node
