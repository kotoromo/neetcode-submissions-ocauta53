class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq_map = {
            0 : 0,
            1 : 0
        }

        for student in students:
            freq_map[student] = freq_map[student] + 1
        for sandwich in sandwiches:
            freq_map[sandwich] = freq_map[sandwich] - 1
            if freq_map[sandwich] < 0: 
                freq_map[sandwich] = 0
                break
        return freq_map[0] + freq_map[1]