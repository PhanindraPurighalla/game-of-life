from django.shortcuts import render
import random

# Create your views here.
def index(request):

    del request.session['spun_players']
    players = [
        { 
            'id': 1,
            'name': 'Player 1',
            'slug': 'player-1'
        },
        { 
            'id': 2,
            'name': 'Player 2',
            'slug': 'player-2'
        },
        { 
            'id': 3,
            'name': 'Player 3',
            'slug': 'player-3'
        },
        { 
            'id': 4,
            'name': 'Player 4',
            'slug': 'player-4'
        },
        { 
            'id': 5,
            'name': 'Player 5',
            'slug': 'player-5'
        },
        { 
            'id': 6,
            'name': 'Player 6',
            'slug': 'player-6'
        }
    ]

    request.session['players'] = players
    i = request.session.get('curr_player_index', 0)
    i += 1
    if i == 6:
        i = 0
    request.session['curr_player_index'] = i
    
    request.session.modified = True

    return render(request, 'players/index.html', {
        'player': players[i]
    })

def player_details(request, player_slug):
    spun_players = request.session.get('spun_players', {})
    print('Printing from session')
    print(spun_players)
    print('Printed from session')

    players = request.session['players']
    print('Players playing the game')
    print(players)
    
    selected_player = { 
            'id': 3,
            'name': 'Player 3',
            'cash': 250000,
            'bank_loans': 100000,
            'base_salary': 50000,
            'pay_raise': 30000,
            'taxes_due': 20000,
            'board_position': 0
        }
    number_spun = random.randint(1,10)
    spin_again = False
    if number_spun in spun_players.values():
        spin_again = True
        print('Spin Again')
    
    spun_players[player_slug] = number_spun
    request.session['spun_players'] = spun_players
    request.session.modified = True

    if len(spun_players) == len(players):
        print('All players have spun for positions')
        print('Sort players based on numbers spun')

        for item in players:
            item['spin_value'] = spun_players[item['slug']]

    print('Players is now as below')
    print(players)
    
    return render(request, 'players/player-details.html', {
        'player_name': player_slug,
        'player_cash': selected_player['cash'],
        'player_base_salary': selected_player['base_salary'],
        'player_bank_loans': selected_player['bank_loans'],
        'player_curr_salary': selected_player['base_salary'] + selected_player['pay_raise'],
        'player_taxes_due': selected_player['taxes_due'],
        'player_board_position': selected_player['board_position'] + number_spun,
        'number_spun': number_spun,
        'spin_again': spin_again
    })
