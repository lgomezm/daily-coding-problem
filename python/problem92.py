# This problem was asked by Airbnb.
# We're given a hashmap associating each courseId key with 
# a list of courseIds values, which represents that the 
# prerequisites of courseId are courseIds. Return a sorted 
# ordering of courses such that we can finish all courses.
# Return null if there is no such ordering.

# For example, given {'CSC300': ['CSC100', 'CSC200'], 
# 'CSC200': ['CSC100'], 'CSC100': []}, 
# should return ['CSC100', 'CSC200', 'CSCS300'].

def sort_courses(courses):
    sorted = []
    while courses:
        curr_course = None
        for c in list(courses.keys()):
            if not courses[c]:
                curr_course = c
                sorted.append(curr_course)
                del courses[c]
                for deps in courses.values():
                    deps.remove(c)
        if not curr_course:
            return None
    return sorted

print(sort_courses({
    'CSC300': ['CSC100', 'CSC200'], 
    'CSC200': ['CSC100'], 
    'CSC100': []
}))
print(sort_courses({
    'CSC300': ['CSC100', 'CSC200'], 
    'CSC200': ['CSC100', 'CSC300'], 
    'CSC100': []
}))