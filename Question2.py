def store_family_members():

    for p_id, p_info in family.items():
        print()

        for key in p_info:
            print(key + ':', p_info[key])


family = {1: {'First name': 'John', 'Last name': 'Maxwell', 'Relationship': 'Father'},
          2: {'First name': 'Elizabeth', 'Last name': 'Maxwell', 'Relationship': 'Mother'}}
