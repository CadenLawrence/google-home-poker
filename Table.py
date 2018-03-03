from Player import Player 

class Table:
	
	def __init__(self, Players, pot, big_blind, small_blind, blind_timer, current_dealer, current_player, current_bet, id, intial_count, round_number):
		self.Players = Players
		self.pot = pot
		self.big_blind = big_blind
		self.small_blind = small_blind
		self.blind_timer = blind_timer
		self.current_dealer = current_dealer
		self.current_player = current_player
		self.cucurrent_bet = current_bet
		self.id = id
		self.intial_count = intial_count
		self.round_number = round_number
	
	Players = []
	Players.append(Player('Caden',7,True))
	print(Players[0].name)