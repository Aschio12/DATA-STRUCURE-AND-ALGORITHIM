class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows=len(mat)
        cols=len(mat[0])
        current_row,current_col=0,0
        res=[]
        going_up=True
        while len(res)<(rows*cols):
            if going_up:
                while current_row>=0 and current_col<cols:
                    res.append(mat[current_row][current_row])
                    current_row-=1
                    current_col+=1
                if current_col==cols:
                    current_col-=1
                    current_row+=2  
                else:
                    current_row+=1
                going_up=False
            else:
                while current_col>=0 and current_row<rows:
                    res.append(mat[current_row][current_col])
                    current_col-=1
                    current_row+=1
                if current_row==rows:
                    current_row-=1
                    current_col+=2
                else:
                    current_col+=1
                going_up=True
        return(res)
                    
                