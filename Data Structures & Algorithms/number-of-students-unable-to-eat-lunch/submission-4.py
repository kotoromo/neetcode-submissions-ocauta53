class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num_circ_stud = students.count(0)
        num_stud = len(students)

        can_continue = True
        num_stud_circ = 0
        num_studs = 0
        for student in students:
            if student == 0 : num_stud_circ += 1
            num_studs += 1
        
        idx = 0
        while can_continue:
            if sandwiches[0] == students[idx]:
                sandwiches.pop(0)
                if students.pop(idx) == 0: num_stud_circ -= 1
                num_studs -= 1
                idx = 0
            else:
                idx = (idx + 1) % num_studs
            is_next_circ = sandwiches and sandwiches[0] == 0
            can_continue = (
                (is_next_circ and num_stud_circ > 0) or
                (not is_next_circ and 
                num_studs - num_stud_circ > 0)
            )

        return num_studs

