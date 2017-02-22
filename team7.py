from simulator import *
import random


HIGH_POS = [(0,0),(1,1),(2,2),(3,3),(0,3),(1,2),(2,1),(3,0)]
LOW_POS = [(0,1),(0,2),(1,0),(1,3),(2,0),(2,3),(3,1),(3,2)]


class Player7:

	def __init__(self):
		#print "entry 1"
		self.ALPHA = -100000000
		self.BETA = 100000000

	def minimax(self,old_move, depth, max_depth, alpha, beta, isMax, p_board, p_block, flag1, flag2, best_node):
		#print "entry2"
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
		ans = 0
		temp_block = []
		for i in range(0,4):
			for j in range(0,4):
				temp_block = [[board.board_status[4*i+k][4*j+l] for l in range(0,4)] for k in range(0,4)]
		 		ans += self.block_utility(temp_block,1,'x')
		 		ans -= self.block_utility(temp_block,1,'o')
		return ans

	def move(self,board,old_move,flag1) :
		if flag1 == 'x' :
			flag2 = 'o'
		else :
			flag2 = 'x'
		(utility_value, best_node) = self.minimax(old_move,0,3,self.ALPHA,self.BETA,True,board, (1,1), flag1, flag2, (7,7))
		return best_node

	def block_utility(self,block,value,flag):
		ans = 0
		for pos in HIGH_POS:
			if block[pos[0]][pos[1]]==flag:
				ans += value*2

		for pos in LOW_POS:
			if block[pos[0]][pos[1]]==flag:
				ans += value

		if flag == 'x':
			flag2 = 'o'
		else:
			flag2 = 'x'

		for row in range(4):
			countflag = 0
			opponentflag = 0
			for col in range(4):
				if(block[row][col] == flag):
					countflag += 1
				elif(block[row][col] == flag2):
					opponentflag += 1
			if opponentflag == 0:
				if countflag == 2:
					ans += 10*value
				elif countflag == 3:
					ans += 40*value
				elif countflag == 4:
					ans += 100*value

		for col in range(4):
			countflag = 0
			opponentflag = 0
			for row in range(4):
				if(block[row][col] == flag):
					countflag += 1
				elif(block[row][col] == flag2):
					opponentflag += 1
			if opponentflag == 0:
				if countflag == 2:
					ans += 10*value
				elif countflag == 3:
					ans += 40*value
				elif countflag == 4:
					ans += 100*value

		countflag = 0
		opponentflag = 0
		for diag in range(4):
			if(block[diag][diag] == flag):
				countflag += 1
			elif(block[row][col] == flag2):
				opponentflag += 1
		if opponentflag == 0:
			if countflag == 2:
				ans += 10*value
			elif countflag == 3:
				ans += 40*value
			elif countflag == 4:
				ans += 100*value

		countflag = 0
		opponentflag = 0
		for diag in range(4):
			if(block[diag][3-diag] == flag):
				countflag += 1
			elif(block[row][col] == flag2):
				opponentflag += 1
		if opponentflag == 0:
			if countflag == 2:
				ans += 10*value
			elif countflag == 3:
				ans += 40*value
			elif countflag == 4:
				ans += 100*value

		return ans
