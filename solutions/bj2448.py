import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

k = int(math.log2(n / 3))

N_LIST = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072]



if n == 3:
    result = [[' ' for i in range(5)] for j in range(n)]
else:
    result = [[' ' for i in range(int(6 * n / 3))] for j in range(n)]

def star(n,k,x,y):
    if (n == 3):
        result[x][y + 2] = "*"
        result[x + 1][y + 1] = "*"
        result[x + 1][y + 3] = "*"
        for i in range(5):
            result[x + 2][y + i] = "*"

    else:
        next_n = N_LIST[k - 1]
        next_k = k - 1

        star(next_n,next_k,x,y+next_n)
        star(next_n,next_k,x+next_n,y)
        star(next_n,next_k,x+next_n,y+n)

    
star(n,k,0,0)

for i in result:
    i = "".join(i)
    print("%s\n" % i)


#                        *                        
#                       * *                       
#                      *****                      
#                     *     *                     
#                    * *   * *                    
#                   ***** *****                   
#                  *           *                  
#                 * *         * *                 
#                *****       *****                
#               *     *     *     *               
#              * *   * *   * *   * *              
#             ***** ***** ***** *****             
#            *                       *            
#           * *                     * *           
#          *****                   *****          
#         *     *                 *     *         
#        * *   * *               * *   * *        
#       ***** *****             ***** *****       
#      *           *           *           *      
#     * *         * *         * *         * *     
#    *****       *****       *****       *****    
#   *     *     *     *     *     *     *     *   
#  * *   * *   * *   * *   * *   * *   * *   * *  
# ***** ***** ***** ***** ***** ***** ***** *****