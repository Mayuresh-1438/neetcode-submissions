class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r
        while l <= r :
            time = 0
            speed = (l+r)//2
            for pile in piles:
                time += math.ceil(pile/speed)
            if time <= h:
                k = speed
                r = speed - 1
            else:
                l = speed + 1
        return k      