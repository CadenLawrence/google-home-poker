from player import Player 

class Table:
	
	def __init__(self, players=[], pot=0, big_blind=0, blind_timer=0, current_dealer=0, current_player=0, current_bet=0, id=None, intial_count=0, round_number=0):
		self.players = players
		self.pot = pot
		self.big_blind = big_blind
		self.small_blind = big_blind/2
		self.blind_timer = blind_timer
		self.current_dealer = current_dealer
		self.current_player = current_player
		self.current_bet = current_bet
		self.id = id
		self.intial_count = intial_count
		self.round_number = round_number