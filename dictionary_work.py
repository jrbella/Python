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

def avg_of_grades():
    grades = my_grades['grades']
    return sum(grades)/len(grades)
    
avg_of_grades()
