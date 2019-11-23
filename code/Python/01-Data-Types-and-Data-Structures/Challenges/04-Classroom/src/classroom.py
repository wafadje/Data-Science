"""
Analyse a classromm performance
"""

def main():
    # TODO: Print the complete sentence (don't forget the whitespaces when it is appropriate)
    quote = ["Education", "is", "what", "remains", "after", "one", "has", "forgotten", "what",
            "one", "has", "learned", "in", "school", "."]
    print(" ".join(quote))

    # TODO: Print the number of elements in the list.
    grades = [12, 11, 15, 9, 17, 12, 8, 18, 5, 14, 11, 17, 11]


    # TODO: Print the higher grade
    print(max(grades))

    # TODO: Print the lowest grade
    print(min(grades))

    # TODO: Print the 5th element
    print(grades[4])

    # TODO: Sort the list and print the 3 lowest grades
    grades = sorted(grades)
    print(grades[:3])

    # TODO: Add grades: 12, 19, 10
    grade = [12, 19, 10]
    grades.extend(grade)
    print(grades)

    # TODO: print the student with the lowest grade, as '____ has the lowest grade: __/20'
    students = ['Jake', 'Connor', 'Jacob', 'Amelia', 'James', 'Olivia', 'Rhys', 'Deirdre', 'Emma',
                'Poppy', 'Thomas', 'Margaret', 'Oscar', 'Llewyn', 'Emily', 'Joe']
    print("the student with the lowest grade, as '{} has the lowest grade: {} /20'".format(students[0], grades[0]))
    #print("the student with the lowest grade, as "+ str(students[0]) +" has the lowest grade: "+ str(grades[0])+"/20'")

if __name__ == "__main__":
    main()
