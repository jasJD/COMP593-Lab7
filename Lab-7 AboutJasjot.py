def main():

    my_info = {
        'name': 'Jasjot Singh',
        'student_Id': '10257909',  
        'pizza_toppings': [
            'Hot banana peppers' ', Jalapenos' ', pineapple'],
        
        'movies' : [
            {
                
            
              'genre' : ['action' ', Rom-Com',],
              'title': ['Ford vs Ferrari' ', Friends with benefits']

            }
        ]
    
    }
    more_toppings = {'red onions', 'green peppers'    }
    
    my_info['pizza_toppings'].append(more_toppings)

    full_info = "Hi Joe, my name is " + my_info['name']+", and my student ID is " +my_info['student_Id']
    print(full_info)
    print("My ideal pizza has")
    for p in my_info['pizza_toppings']:
        print(p)


   
    for m in my_info['movies']:
        genre = m['genre']
        
    print("I like to watch",genre,"movies" )

    
    for t in my_info['movies']:
    
        title= t['title']
        
    print("Some of my favourite movies are",title)

   


main()