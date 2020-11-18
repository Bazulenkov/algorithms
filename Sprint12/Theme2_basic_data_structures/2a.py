#%%
with open('input.txt') as f:
    visited_optional_courses = [line.rstrip() for line in f]
del visited_optional_courses[0]
#%%
while visited_optional_courses != []:
    item = visited_optional_courses[0]
    print(item)
    while item in visited_optional_courses:
        visited_optional_courses.remove(item)
# %%
# def recursion(array):
#     if array == []:
#         return
#     else:
#         item = array[0]
#         print(item)
#         while item in array:
#             array.remove(item)
#         return recursion(array)

# recursion(visited_optional_courses)

# %%
