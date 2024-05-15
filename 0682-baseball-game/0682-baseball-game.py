class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for item in operations:
            if record != [] and item == "C":
                record.pop()
            elif record != [] and item == "D":
                record.append(record[-1] * 2)
            elif record != [] and item == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(item))

        return sum(record)