student_info = {'first_name':'Harry',
                'last_name': 'Potter',
                'age':15,
                'address':'Privet Drive, 4',
                'pets':['Hedwig', 'Buckbeak'],
                'best_friends': ('Ron Wealey', 'Hermione Granger'),
                'is_parselmouth': True,
                'houses': {'main': 'Griffyndor', 'second': 'Slytherin'}}

print(student_info['age'])
student_info['age'] += 10
student_info['address'] = 'Betzalel 8'
student_info['pets'].append('Arnold')
#print(student_info['pets'])
student_info['is parselmouth'] = 'False'
#print(student_info)


sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print (sample_dict['class']['student']['marks']['history'])

#loops and dicts


