import java.util.Scanner;
class MiniMaxFinal
{

	static int row, col;
	static char player='x', opponent='o';
	static boolean isMovesLeft(char board[][])
	{
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3;j++)
			{
				if(board[i][j]=='-')
					return true;
			}
		}
		return false;
	}
	//Evaluating and checking whether or not the game will be Won
	static int evaluate(char b[][])
	{
		//Checking rows for victory
		for(int row=0; row<3;row++)
		{
			if(b[row][0]==b[row][1] && b[row][1]==b[row][2])
			{
				if(b[row][0]==player)
					return 10;
				else if(b[row][0]==opponent)
					return -10;
			}
		}
		//Checking columns for victory
		for(int col=0;col<3;col++)
		{
			if(b[0][col]==b[1][col] && b[1][col]==b[2][col])
			{
				if(b[0][col]==player)
					return 10;
				else if(b[0][col]==opponent)
					return -10;
							
			}
		}
		
		//Checking for Diagonals
		if(b[0][0] == b[1][1] && b[1][1] == b[2][2])
		{
			if(b[0][0]==player)
				return 10;
			else if(b[0][0]==opponent)
				return -10;
		}
		
		if(b[0][2]==b[1][1] && b[1][1]==b[2][0])
		{
			if(b[1][1]==player)
				return 10;
			else if(b[1][1]==opponent)
				return -10;
		}
		//If draw then return 0
		return 0;	
	}
	
	static int minimax(char board[][], int depth, boolean isMax)
	{
		int score=evaluate(board);
		if(score == 10)
			return score;
		
		if(score==-10)
			return score;
		
		if(isMovesLeft(board)==false)
			return 0;
		
		if (isMax)
		{
			int best= -1000;
			
			//Traverse all cells
			for(int i=0; i<3;i++)
			{
				for(int j=0;j<3;j++)
				{
					if(board[i][j]=='-')
					{
						board[i][j]=player;
						
						//Call minimax recursively and choose the maximum value
						best = Math.max(best, minimax(board, depth+1, !isMax));
						board[i][j]='-';		
					}
				}
			}
			return best;
		}
		
		else
		{
			int best=1000;
			for(int i=0; i<3;i++)
			{
				for(int j=0;j<3;j++)
				{
					//Check if cell is empty
					if(board[i][j]=='-')
					{
						board[i][j]= opponent;
						best = Math.min(minimax(board, depth+1, !isMax), best);
						board[i][j]='-';
					}
				}
			}
			return best;
		}
					
	}
	
	//Returning the best possible move for the player
	static int[] findBestMove(char board[][])
	{
		int bestVal=-1000;
		row=-1;
		col=-1;
		
		for(int i=0; i<3;i++)
		{
			for(int j=0;j<3;j++)
			{
				if(board[i][j]=='-')
				{
					board[i][j]=player;
					
					int moveVal = minimax(board, 0, false);
					board[i][j]='-';
					
					if(moveVal>bestVal)
					{
						row=i;
						col=j;
						bestVal = moveVal;
					}					
				}
			}
		}
		//System.out.println("The value of the Best Move is "+bestVal);
		
	 int a[]= {row, col};
	 return a;
	}
	
	public static void main(String args[])
	{
		char board[][]=
			{
					{'-','-','-'},
					{'-','-','-'},
					{'-','-','-'},
			};

		
		Scanner sc = new Scanner(System.in);
		System.out.println("Tic Tac Toe ");
		int turn=0;
		
		System.out.println("Who Goes First? 1->You, 0->Opponent ");
		turn=sc.nextInt();
		int eval;
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3;j++)
			{
				System.out.print(board[i][j]+" ");
			}
			System.out.println("");
		}
		System.out.println();
		if(turn==0)
		{
			
			int bestmove[]=findBestMove(board);
			board[bestmove[0]][bestmove[1]]='x';
			
			for(int i=0;i<3;i++)
			{
				for(int j=0;j<3;j++)
				{
					System.out.print(board[i][j]+" ");
				}
				System.out.println("");
			}
			System.out.println();
						
		}
		
				
		
		while(isMovesLeft(board))
		{
			System.out.println("Your Turn ");
			int pos=sc.nextInt();
			if(pos<=3)
			{
				board[0][pos-1]='o';
			}
			if(pos>3 && pos<=6)
			{
				board[1][pos-4]='o';
			}
			if(pos>6 && pos<=9)
			{
				board[2][pos-7]='o';
			}
			
			for(int i=0;i<3;i++)
			{
				for(int j=0;j<3;j++)
				{
					System.out.print(board[i][j]+" ");
				}
				System.out.println("");
			}
			System.out.println();
			
			eval=evaluate(board);
			if(eval==-10)
			{
				System.out.println("You Win");
				break;
			}
			if(!isMovesLeft(board))
			{
				System.out.println("Draw");
				break;
			}
			int bestmove[]=findBestMove(board);
			board[bestmove[0]][bestmove[1]]='x';
			System.out.println("Opponent's Turn");
			for(int i=0;i<3;i++)
			{
				for(int j=0;j<3;j++)
				{
					System.out.print(board[i][j]+" ");
				}
				System.out.println("");
			}			
			System.out.println();
			eval=evaluate(board);
			if(eval==10)
			{
				System.out.println("Opponent Wins");
				break;
			}
			if(!isMovesLeft(board))
			{
				System.out.println("Draw");
				break;
			}
			
		}		
	}
	
}