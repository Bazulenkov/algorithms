# %%
from operator import itemgetter


#%%
with open('input.txt') as f:
    cnt = f.readline().rstrip()
    lessons = [tuple(map(float, line.rstrip().split())) for line in f]

# %%
sort_lessons = sorted(lessons, key = itemgetter(1, 0))
# %%
timetable = []
timetable.append(sort_lessons[0])
for lesson in sort_lessons[1:]:
    if itemgetter(1)(timetable[-1]) <= lesson[0]:
        timetable.append(lesson)
# %%
print (len(timetable))
for lesson in timetable:
    print('{0:g} {1:g}'.format(lesson[0], lesson[1]))
