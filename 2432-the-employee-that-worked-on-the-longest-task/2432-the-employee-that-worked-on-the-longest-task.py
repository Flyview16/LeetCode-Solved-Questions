class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = 0
        employee_id = float('inf')
        previous_time = 0

        for log in logs:
            current_id,current_time = log
            work_time = current_time - previous_time

            if work_time > max_time:
                max_time = work_time
                employee_id = current_id
            elif work_time == max_time:
                employee_id = min(employee_id, current_id)
            
            previous_time = current_time

        return employee_id