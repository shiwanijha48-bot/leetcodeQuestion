class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a = minutes * 6 #  minute angle
        b = (hour % 12) * 30 + minutes * 0.5  # hour angle
        angle = abs(b-a)
        return min(angle, 360- angle)
