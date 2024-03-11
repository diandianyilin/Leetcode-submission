class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_map = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        result = []

        for s in score:
            rank = sorted_score.index(s) + 1
            if rank in rank_map:
                result.append(rank_map[rank])
            else:
                result.append(str(rank))

        return result
