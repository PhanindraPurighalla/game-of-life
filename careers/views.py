from django.shortcuts import render
import random

# Create your views here.

def index(request):
    careers = [
        { 
            'id': 1,
            'name': 'a Teacher',
            'base_salary': 40000,
            'has_max_salary': True,
            'max_salary': 70000,
            'taxes_due': 15000,
            'requires_college_degree': True,
            'slug': 'a-teacher'
        },
        { 
            'id': 2,
            'name': 'a Sales Person',
            'base_salary': 20000,
            'has_max_salary': True,
            'max_salary': 50000,
            'taxes_due': 5000,
            'requires_college_degree': False,
            'slug': 'a-sales-person'
        },
        { 
            'id': 3,
            'name': 'a Computer Designer',
            'base_salary': 50000,
            'has_max_salary': True,
            'max_salary': 80000,
            'taxes_due': 20000,
            'requires_college_degree': True,
            'slug': 'a-computer-designer'
        },
        { 
            'id': 4,
            'name': 'an Accountant',
            'base_salary': 70000,
            'has_max_salary': True,
            'max_salary': 110000,
            'taxes_due': 30000,
            'requires_college_degree': True,
            'slug': 'an-accountant'
        },
        { 
            'id': 5,
            'name': 'a Veterinarian',
            'base_salary': 80000,
            'has_max_salary': True,
            'max_salary': 120000,
            'taxes_due': 35000,
            'requires_college_degree': True,
            'slug': 'a-veterinarian'
        },
        { 
            'id': 6,
            'name': 'a Lawyer',
            'base_salary': 90000,
            'has_max_salary': False,
            'taxes_due': 40000,
            'requires_college_degree': True,
            'slug': 'a-lawyer'
        },
        { 
            'id': 7,
            'name': 'a Doctor',
            'base_salary': 100000,
            'has_max_salary': False,
            'taxes_due': 45000,
            'requires_college_degree': True,
            'slug': 'a-doctor'
        },
        { 
            'id': 8,
            'name': 'a Hair Stylist',
            'base_salary': 30000,
            'has_max_salary': True,
            'max_salary': 60000,
            'taxes_due': 10000,
            'requires_college_degree': False,
            'slug': 'a-hair-stylist'
        },
        { 
            'id': 9,
            'name': 'a Mechanic',
            'base_salary': 30000,
            'has_max_salary': True,
            'max_salary': 60000,
            'taxes_due': 10000,
            'requires_college_degree': False,
            'slug': 'a-mechanic'
        },
        { 
            'id': 10,
            'name': 'a Police Officer',
            'base_salary': 40000,
            'has_max_salary': True,
            'max_salary': 70000,
            'taxes_due': 15000,
            'requires_college_degree': False,
            'slug': 'a-police-officer',
            'special_attributes' : [
                {
                'name' : 'Speeding Fine',
                'activation_number': 1,
                'action': 'collect',
                'amount': 500
                }
                ]
        },
        { 
            'id': 11,
            'name': 'an Entertainer',
            'base_salary': 50000,
            'has_max_salary': False,
            'taxes_due': 20000,
            'requires_college_degree': False,
            'slug': 'an-entertainer'
        },
        { 
            'id': 12,
            'name': 'an Athlete',
            'base_salary': 60000,
            'has_max_salary': False,
            'taxes_due': 25000,
            'requires_college_degree': False,
            'slug': 'an-athlete'
        }
    ]
    college_careers = [d for d in careers if d['requires_college_degree'] == True]
    chosen_college_career_indices = random.sample([sub['id'] for sub in college_careers], 2)
    college_career_picked_1 = [d for d in college_careers if d['id'] in chosen_college_career_indices][0]['name']
    college_career_picked_2 = [d for d in college_careers if d['id'] in chosen_college_career_indices][1]['name']

    regular_careers = [d for d in careers if d['requires_college_degree'] == False]
    chosen_regular_career_index = random.choice([sub['id'] for sub in regular_careers])
    regular_career_picked = [d for d in regular_careers if d['id'] == chosen_regular_career_index][0]['name']


    return render(request, 'careers/index.html', {
        'careers': sorted(careers, key=lambda item: (item['requires_college_degree'], item['name'])),
        'college_careers': [d for d in careers if d['requires_college_degree'] == True],
        'college_careers_to_use': college_career_picked_1 + ' or ' + college_career_picked_2,
        'regular_career_to_use': regular_career_picked
    })

def career_details(request, career_slug):
    print(career_slug)
    selected_career = { 
            'id': 3,
            'name': 'a Computer Designer',
            'base_salary': 50000,
            'has_max_salary': True,
            'max_salary': 80000,
            'taxes_due': 20000,
            'requires_college_degree_text': 'does not require'
        }
    return render(request, 'careers/career-details.html', {
        'career_name': selected_career['name'],
        'career_base_salary': selected_career['base_salary'],
        'career_max_salary': selected_career['max_salary'],
        'career_taxes_due': selected_career['taxes_due'],
        'career_requires_college_degree_text': selected_career['requires_college_degree_text']
    })
