'''
A competition consists of n players numbered from 0 to n - 1.

You are given an integer array skills of size n and a positive integer k, where skills[i] is the skill level of player i. All integers in skills are unique.

All players are standing in a queue in order from player 0 to player n - 1.

The competition process is as follows:

The first two players in the queue play a game, and the player with the higher skill level wins.
After the game, the winner stays at the beginning of the queue, and the loser goes to the end of it.
The winner of the competition is the first player who wins k games in a row.

Return the initial index of the winning player.


You do not really have to move the elements in the array from start to end, just use i to simulate, 
when 'i' go through, set winner to record the bigger number one, 

'''

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
      # if lose one time, the number will be put at the end of the list, 
      # so there would not be situation where, lost one time but still win K game ahead

      # first detect between k and skills length
      if k > len(skills)：
        # if k >, means the array will cycle until the largest of the list win firt K game
        return skills.index(max(skills))

      score = 0 # compare with K -> to record which element would win first k game
      winner = 0 # assume the first one is the winner
      for i in range(1, len(skills)):
        if skills[i] > skills[winner]:
          score = 1
          winner = i
        else:
          score += 1

        if score >= k:
          return score
      
