class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedscore = sorted(score, reverse = True)
        rankmap = {} # dict to store score and its rank
        n = len(sortedscore)
        for i in range(n):  # 0 to n
            rankmap[sortedscore[i]] = i + 1 # 0+1 = 1st rank, then 2nd, 3rd...
        res = []
        for i in score:
            rank = rankmap[i] # i is key to the rankmap dict, rankmap[i] gives values which is rank of each elemnt
            if rank == 1:
                res.append("Gold Medal")
            elif rank == 2:
                res.append("Silver Medal")
            elif rank == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(rank))
        return res


#  score = [10,3,8,9,4]
#  sortedscore = [10, 9, 8, 4, 3]
#  rankmap = { 10:1, 9:2, 8:3, 4:4, 3:5 }
#  rank = rankmap[10]:1 ~ gold ; rankmap[3]: "5"; rankmap[8]:3~ bronze ;rankmap[9]:2 ~ silver; rankmap[4]: "4" 
#  res = [ gold, 5, bronze, silver, 4 ]
