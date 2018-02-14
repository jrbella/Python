#Dictionary Work


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

my_grade_avg = (sum(my_grades['grades']))/len(my_grades['grades'])

print(my_grade_avg)