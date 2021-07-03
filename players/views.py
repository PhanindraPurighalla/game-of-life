from django.shortcuts import render
import random

# Create your views here.
def index(request):

    if request.session.get('players'):
        request.session.get('players').clear()

    request.session['curr_player_index'] = 0
    request.session['positions_sorted'] = False

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
    i += players[0]['id']
    if i == 6:
        i = 1
    request.session['curr_player_index'] = i
    
    request.session.modified = True

    return render(request, 'players/index.html', {
        'player': [player for player in players if player['id'] == i][0]
    })

def player_details(request, player_slug):
    positions_sorted = request.session.get('positions_sorted', False)

    players = request.session['players']
    
    selected_player = next(player for player in players if player['slug'] == player_slug)
    number_spun = random.randint(1,10)
    
    while number_spun in [player['number_spun'] for player in players if 'number_spun' in player]:
        number_spun = random.randint(1,10)
    selected_player['number_spun'] = number_spun
    [player.update({'number_spun': number_spun}) for player in players if player.get('slug') == player_slug]

    
    next_player_id = selected_player['id'] + 1
    if next_player_id == 7:
        next_player_id = 1

    if not positions_sorted and len(players) == len([k['number_spun'] for k in players if k.get('number_spun')]):
        playing_position = 1
        for sorted_player in sorted(players, key = lambda i: i['number_spun'], reverse = True):
            sorted_player['id'] = playing_position
            playing_position += 1

        positions_sorted = True
        request.session['positions_sorted'] = positions_sorted
        request.session.modified = True
        next_player_id = 1

    request.session['players'] = players
    request.session.modified = True

    next_player_slug = next(player for player in players if player['id'] == next_player_id)['slug']
    
    return render(request, 'players/player-details.html', {
        'player_name': player_slug,
        'player_cash': selected_player.get('cash', 0),
        'player_base_salary': selected_player.get('base_salary',0),
        'player_bank_loans': selected_player.get('bank_loans',0),
        'player_curr_salary': selected_player.get('base_salary',0) + selected_player.get('pay_raise',0),
        'player_taxes_due': selected_player.get('taxes_due',0),
        'player_board_position': selected_player.get('board_position',0) + number_spun,
        'number_spun': selected_player['number_spun'],
        'next_player_slug': next_player_slug,
        'players': players,
        'positions_sorted': positions_sorted
    })
