class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students and sandwiches:
            try:
                idx_of_sand_at_stud = students.index(sandwiches[0])
                sandwiches.pop(0)
                students.pop(idx_of_sand_at_stud)
            except ValueError: break
        return len(students)