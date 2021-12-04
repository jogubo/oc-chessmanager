from views.player_form_view import PlayerFormView
from models.player import Player
from utils.database import Database


class NewPlayerCtrl:
    def __call__(self):
        new_player_form = PlayerFormView("Ajouter un nouveau joueur")
        form = new_player_form.new()
        player = Player(
                form['first_name'],
                form['last_name'],
                form['birth'],
                form['civility']
                )
        serialized_players = []
        serialized_players.append(player.serialize)
        Database.add('players', serialized_players)
