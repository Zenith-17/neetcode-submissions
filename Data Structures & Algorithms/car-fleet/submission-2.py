class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for p, s in zip(position, speed):
            time = (target - p) / s
            cars.append((p, time))

        cars.sort(reverse=True)  

        fleet = 0
        last_time = 0

        for _, time in cars:
            if time > last_time:
                fleet += 1
                last_time = time

        return fleet