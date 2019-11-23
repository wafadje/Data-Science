"""
An implementation of the Round Robin Tournament algorithm
"""

STUDENTS = ['John', 'Paul', 'Ringo', 'George', 'Another Guy']

def main():
    # Print for each day, each team
    daily_teams = schedule(STUDENTS)
    print(daily_teams)

    for index, team in enumerate(daily_teams):
        pass
        #print(index, team)

"""
        [[array.first, pivot]] + (1...(n / 2)).map { |j| [array[j], array[n - 1 - j]] }
  
        end
        array.push pivot unless pivot.nil?
        games
end
d = {key: value for (key, value) in iterable}
"""

def rotate(l, y=1):
   if len(l) == 0:
      return l
   y = -y % len(l)     # flip rotation direction
   return l[y:] + l[:y]

def schedule(students):
    # Compute all the possible teams for each day
    n = len(students)
    pivot = students.pop()

    if n % 2 != 0:
        students.append("")

    for i in range(len(students)):
        students = rotate(students)
        s = [students[0], pivot] + [[student[i], students[n -1 -i]] for student in students ]
        #print(s) 
        if len(pivot) == 0:
            students.push(pivot) 
    return s

if __name__ == "__main__":
    main()

