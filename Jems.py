class Solution(object):
    #You're given strings J representing the types of stones that are jewels, 
    #and S representing the stones you have.  Each character in S is a type 
    #of stone you have.  You want to know how many of the stones you have are also jewels.
    def numJewelsInStones(self, J, S):
       count = 0
       for i in range(0, len(J)):
            for j in range(0, len(S)):
                if J[i]==S[j]:
                    count += 1
       return count
                
