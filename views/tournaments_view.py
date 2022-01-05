from datetime import date
from utils.constants import APP_NAME, NUMBER_PLAYERS
from utils.functions import clear, prompt


class TournamentsView:

    @classmethod
    def main_display(cls):
        clear()
        print(f"[{APP_NAME}]\n")
        print(f"{cls.title}\n")

    @classmethod
    def display_tournament(cls, tournament_infos, finished=False):
        cls.title = f"{tournament_infos['name']}"
        cls.main_display()
        print(f"Description:\n{tournament_infos['description']}\n")
        print(f"Contrôle du temps:\n{tournament_infos['time']}\n")
        choices = ['C', 'R', 'T']
        if not finished:
            choices.append('P')
            print(f"Tour actuel:\n{tournament_infos['current_round']}"
                  f"/{tournament_infos['total_rounds']}\n")
            _input = prompt("[C]lassement | [P]rochains matchs | "
                            "[T]ours précédents (résultats) | "
                            "[R]etour à la liste des tournois").upper()
        elif finished:
            print("Tournoi terminé.\n")
            _input = prompt("[C]lassement | "
                            "[R]etour à la liste des tournois").upper()

        if _input in choices:
            return _input

    @classmethod
    def display_ranking(cls, tournament_infos):
        print("Joueurs participants:")
        cls.main_display()
        i = 1
        for id, player_infos in tournament_infos['players'].items():
            print(f"{i}  -  {player_infos['name']} | "
                  f"Score: {player_infos['score']} | "
                  f"Rang: {player_infos['rank']}")
            i += 1
        prompt("Appuyer sur une touche pour revenir "
               "à la gestion du tournoi:").upper()
        return None

    @classmethod
    def display_round(cls, versus_list, tournament_infos):
        while True:
            players_infos = tournament_infos['players']
            cls.main_display()
            print("Prochains matchs:")
            i, choices = 1, ['E', 'R']
            for players in versus_list:
                print(f"{i}  -  {players_infos[players[0]]['name']} "
                      f"  VS  {players_infos[players[1]]['name']}")
                i += 1
            _input = prompt("[E]ntrer les résultats | "
                            "[R]etour").upper()
            if _input in choices:
                return _input

    @classmethod
    def display_list(cls, tournaments_infos, display='all'):
        '''
        tournments_infos = [{'id': tournament_id, 'name': tournament_name}]
        '''
        while True:
            cls.title = "Liste des tournois\n"
            cls.main_display()
            i, choices = 1, ['C', 'M', 'Q']
            for tournament in tournaments_infos:
                print(f"[{i}] - {tournament['name']}")
                choices.append(i)
                i += 1
            text = "Selectionnez un tournoi"
            if display == 'all':
                _input = prompt(f"{text} pour afficher plus d'infos\n"
                                "[C]réer un tournoi | [M]enu principal | "
                                "[Q]uitter le programme")
            elif display == 'minimal':
                _input = prompt(f"{text} :")
            try:
                user_choice = int(_input)
            except ValueError:
                user_choice = _input.upper()
            if user_choice in choices:
                if isinstance(user_choice, int):
                    return tournaments_infos[user_choice - 1]['id']
                else:
                    return user_choice
            else:
                continue

    @classmethod
    def display_rounds(cls, rounds_data):
        cls.main_display()
        for round, matchs in rounds_data.items():
            print(f"{round}")
            for match, players in matchs.items():
                print(f"{match}: "
                      f"{players['player_1']['name']} "
                      f"({players['player_1']['score']}) "
                      f"VS "
                      f"{players['player_2']['name']} "
                      f"({players['player_2']['score']}) ")
            print("\n--------------------\n")
        prompt("Appuyez sur une touche pour revenir au tournoi:")
        return None

    @classmethod
    def set_name(cls):
        cls.main_display()
        name = prompt("Entrez le nom du tournoi :").title()
        return name

    @classmethod
    def set_location(cls):
        cls.main_display()
        location = prompt("Entrez le lieu du tournoi :").upper()
        return location

    @classmethod
    def set_description(cls):
        cls.main_display()
        description = prompt("Entrez la description du tournoi :").capitalize()
        return description

    @classmethod
    def set_date(cls):
        valid_date = False
        while not valid_date:
            cls.main_display()
            _input = prompt("Entrez le date de l'évènement (JJ/MM/AAAA) :")
            try:
                _input = _input.split('/')
                year = int(_input[2])
                month = int(_input[1])
                day = int(_input[0])
                birth = str(date(year, month, day))
                break
            except ValueError:
                continue
            except IndexError:
                continue
        return birth

    @classmethod
    def set_time(cls):
        while True:
            cls.main_display()
            print("[1] - Bullet\n"
                  "[2] - Blitz\n"
                  "[3] - Coup rapide\n")
            _input = prompt("Choisissez le type de contrôle de temps:")
            if _input == '1':
                return 'Bullet'
            elif _input == '2':
                return 'Blitz'
            elif _input == '3':
                return 'Coup rapide'

    @classmethod
    def set_round_name(cls):
        cls.main_display()
        _input = prompt("Entrez un nom pour ce round ou "
                        "laissez vide pour un nom auto:")
        if _input == '':
            return None
        else:
            return _input

    @classmethod
    def set_nb_players(cls):
        return NUMBER_PLAYERS

    @classmethod
    def add_player(cls):
        cls.main_display()
        _input = prompt("Entrez le nom du joueur recherché :").upper()
        return _input

    @classmethod
    def display_matchs_list(cls, round, matchs):
        if round == 1:
            round = "1er"
        else:
            round = f"{round}ème"
        print(f"Liste des matchs pour le {round} tour:\n")
        for players in matchs:
            player_1, player_2 = players
            print(f"  -  {player_1.full_name}  vs {player_2.full_name}")

    @classmethod
    def set_score_match(cls, round, players):
        while True:
            cls.title = f"Tour {round}:\n"
            cls.main_display()
            player_1, player_2 = players
            print(f"[1] - {player_1}")
            print(f"[2] - {player_2}")
            print("[E] - Égalité")
            _input = prompt("Selectionnez le joueur gagnant").upper()
            if _input == "1":
                return (1.0, 0.0)
            elif _input == "2":
                return (0.0, 1.0)
            elif _input == "E":
                return (0.5, 0.5)

    @classmethod
    def create_new_tournament(cls):
        '''
        Displays a form to create a new tournament
        '''
        cls.title = "Création d'un nouveau tournoi"
        tournament = {
            "name": cls.set_name(),
            "description": cls.set_description(),
            "date": cls.set_date(),
            "location": cls.set_location(),
            "time": cls.set_time(),
            "nb_players": cls.set_nb_players(),
            }
        return tournament
