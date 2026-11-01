class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap: self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap.get(key,[])
        start = 0
        end = len(values)-1
        res = ""
        while(start <= end):
            pivot = (start + end) // 2
            if values[pivot][1] == timestamp: return values[pivot][0]
            elif values[pivot][1] < timestamp:
                res = values[pivot][0]
                start = pivot + 1
            else : end = pivot - 1
        
        return res

# {alice : [(happy,1),(sad,3)]} 
