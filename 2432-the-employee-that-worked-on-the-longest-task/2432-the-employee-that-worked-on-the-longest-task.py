class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        time_units = 0
        employee_id = 0
        for i in range(len(logs)):
            new_time = 0
            if i == 0:
                new_time = logs[i][1] - 0
            else:
                new_time = logs[i][1] - logs[i-1][1]
                
            if new_time > time_units:
                time_units = new_time
                employee_id = logs[i][0]
            elif new_time ==  time_units:
                employee_id = min(employee_id, logs[i][0])
        return employee_id
