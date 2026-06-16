class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        p = list(zip(heights, names))
        p.sort(reverse = True)
        return [name for heights, name in p]
