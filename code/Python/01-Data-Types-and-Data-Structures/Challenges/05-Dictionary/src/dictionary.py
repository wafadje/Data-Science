"""
Play with dictionaries
"""

def main():
    # TODO: print all the keys of the following dictionary
    feminist_dictionary = {
        'Simone de Beauvoir': 1908,
        'Monique Wittig': 1935,
        'Virginie Despentes': 1969,
        'Angela Davies': 1944,
        'Andrea Dworkin': 1946
    }

    print(feminist_dictionary.keys())


    # TODO: print the birthdate of Angela Davies (2 methods)
    print(feminist_dictionary['Angela Davies'])
    print(feminist_dictionary.get('Angela Davies'))

    # TODO: create a dictionary with 5 entries where keys are strings and values are lists of 4 integers
    # (ex:student/grades, player/scores)
    diction = {'Jake': [10, 12, 11, 13],
    'Connor': [5, 9, 5, 16],
    'Jacob': [14, 11, 12, 10],
    'Amelia': [9, 15, 11, 14],
    'James': [5, 10, 12, 10]}


    # TODO: print all the values of the dictionary
    print(diction.values())

    # TODO: print the 2nd element of the 3rd key
    print(diction['Jacob'][3])

    # TODO: print the keys of cities_dictionary
    cities_dictionary = {
        'Paris' : {
            'population': 2000000,
            'area': 105,
            'density': 21000
        },
        'London': {
            'population': 8000000,
            'area': 1572,
            'density': 5600
        },
        'New-York': {
            'population': 8000000,
            'area': 1214,
            'density': 7100
        }
    }
    print(cities_dictionary.keys())


    # TODO: print the keys of New-York
    print(cities_dictionary['New-York'].keys())

    # TODO: print the area of London
    print(cities_dictionary['London']['area'])

    # TODO: add a new key: Tokyo, with population: 13000000, area: 2190 and density: 6313
    # then print the dictionary
    cities_dictionary['Tokyo'] = {'population': 13000000, 'area': 2190, 'density': 6313}
    print(cities_dictionary)

if __name__ == "__main__":
    main()
