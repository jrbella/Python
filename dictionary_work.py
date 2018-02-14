#Dictionary Work completed 2/13/2018


my_dict = {
    'name': 'Jeff',
    'age': 31,
    'eyes' : 'Hazel'
}

my_grades ={
    'subject' : 'math',
    'grades': (66,77,88,99,100,100)
}

cities  = [
    {
        'name': 'Chicago',
        'location': 'United States'
    },
    {
        'name': 'Mexico City',
        'location': 'Mexico'
    }
]
grades = my_grades['grades']
my_grade_avg = sum(grades)/len(grades)

print(my_grade_avg)
