class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_map = {}
        for i in range(len(position)):
            position_speed_map[position[i]] = speed[i]
        
        position = sorted(position, reverse = True)
        # print(position)
        # print(position_speed_map)
        stack = []
        for i in range(len(position)):
            speed = position_speed_map[position[i]]
            time = (target - position[i])/speed
            if stack and time <= stack[-1]:
                continue

            stack.append(time)
        
        return len(stack)
                

# target=10
# position=[7, 4, 1, 0]
# speed=[2,2,1,1]


        