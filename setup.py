#/ Imports \# 

from Class.DataLayer import DataLayer
from Class.Type import Type
from Class.Template import Template
from Class.Action import Action
from Class.Sequence import Sequence
from Class.Farm import Farm

#/ Config and Setup Datalayers init \# 

config = DataLayer('config.json')
setup = DataLayer('setup.json')

#/ Types of dungeon enumeration \#

types = {
}

#/ Actions enumeration \#

actions = {
	"click": Action(0),
	"bj5_send-message": Action(1, task = setup._data['bj5_paste-message'])
}

#/ Templates enumeration \#

templates = {
	"test_template": Template("autofarm_repetition"),
	"autofarm_replay": Template("autofarm_rejouer"),
	"autofarm_repetition-battle": Template("autofarm_repetition"),
	"refill-energy_shop": Template("shop"),
	"refill-energy_energy": Template("190"),
	"refill-energy_validate": Template("oui"),
	"refill-energy_ok": Template("ok"),
	"refill-energy_close": Template("fermer"),
	"bj5_chat": Template("chat"),
	"bj5_message": Template("message", actions = [actions['click'], actions['bj5_send-message']], activeRate = 150),
	"bj5_accept": Template("accepter"),
	"bj5_validate": Template("oui_bj5"),
	"bj5_ready": Template("pret"),
	"bj5_loot": Template("loot")
}

#/ Sequences enumeration \#

sequences = {
	"test_sequence": Sequence(templates = [templates["test_template"]]),
	"autofarm_launch-battles": Sequence(templates = [templates["autofarm_replay"], templates["autofarm_repetition-battle"]]),
	"autofarm_launch-launch": Sequence(templates = [templates["autofarm_repetition-battle"]]),
	"autofarm_launch-refill": Sequence(templates = [templates["refill-energy_shop"], templates["refill-energy_energy"], templates["refill-energy_validate"], templates["refill-energy_ok"], templates["refill-energy_close"], templates["autofarm_repetition-battle"]]),
	"bj5_invite-chat": Sequence(templates = [templates["bj5_chat"], templates["bj5_message"], templates["bj5_accept"], templates["bj5_validate"]], starter = True),
	"bj5_launch-battle": Sequence(templates = [templates["bj5_ready"], templates["bj5_loot"], templates["refill-energy_ok"], templates["bj5_validate"]]),
	"bj5-refill": Sequence(templates = [templates["refill-energy_shop"], templates["refill-energy_energy"], templates["refill-energy_validate"], templates["refill-energy_ok"], templates["refill-energy_close"], templates["autofarm_repetition-battle"]]),
}

#/ Sequences enumeration \#

farms = {
	"test_farm": Farm([sequences["test_sequence"]]),
	"autofarm": Farm([sequences["autofarm_launch-battles"], sequences["autofarm_launch-refill"]]),
	"bj5": Farm([sequences["bj5-refill"], sequences["bj5_launch-battle"]]),
	"bj5 2": Farm([sequences["bj5-refill"], sequences["bj5_launch-battle"], sequences["bj5_invite-chat"]]),
}

#/ Building the global registry \# 

registry = {
	'config': config,
	'setup': setup,
	'in_game': {
		'types': types,
		'actions': actions,
		'templates': templates,
		'sequences': sequences,
		'farms': farms
	}
}

