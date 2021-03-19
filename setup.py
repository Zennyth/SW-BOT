#/ Imports \# 

from Class.DataLayer import DataLayer
from Class.Type import Type
from Class.Template import Template
from Class.Action import Action
from Class.Sequence import Sequence
from Class.Farm import Farm
from Class.ImageAnalyser import ImageAnalyser

from PIL import ImageGrab

#/ Config and Setup Datalayers init \# 

config = DataLayer('config.json')
setup = DataLayer('setup.json')

#/ Types of dungeon enumeration \#

types = {
	"start": Type("launch", "Launch game"),
	"change": Type("change", "Change dungeon"),
	"db": Type("db12", "Dragon's B12"),
}

#/ Actions enumeration \#

actions = {
	"click": Action(0),
	"bj5_send-message": Action(1, task = setup._data['bj5_paste-message'])
}

#/ Templates enumeration \#

templates = {
	"launch_skip-event" : Template("launch_skip-event"),
	"launch_start" : Template("launch_start"),
	"launch_coffre" : Template("launch_coffre"),
	"launch_cairos": Template("autobattle/cairos-dungeon/cairos"),
	"launch_cairos-dungeon": Template("autobattle/cairos-dungeon/necro"),
	"launch_cairos-go": Template("autobattle/cairos-dungeon/go"),
	"change_select" : Template("autobattle/select", threshold = 0.85),
	"autobattle_batiment": Template("autofarm_batiment"),
	"autobattle_bouton": Template("autofarm_bouton"),
	"test_template": Template("autofarm_batiment"),
	"autofarm_replay": Template("autofarm_rejouer"),
	"autofarm_repetition-battle": Template("autofarm_repetition", threshold = 0.85),
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
	"launch_skip-event": Sequence(templates = [templates["launch_skip-event"]]),
	"launch_start": Sequence(templates = [templates["launch_start"]]),
	"launch_coffre": Sequence(templates = [templates["launch_coffre"]]),
	"autobattle_menu": Sequence(templates = [templates["autobattle_batiment"], templates["autobattle_bouton"], templates["launch_cairos"], templates["launch_cairos-dungeon"], templates["launch_cairos-go"], templates["autofarm_repetition-battle"]]),
	"change_dungeon": Sequence(templates = [templates["change_select"], templates["launch_cairos"], templates["launch_cairos-dungeon"], templates["launch_cairos-go"], templates["autofarm_repetition-battle"]]),
	"autofarm_launch-battles": Sequence(templates = [templates["autofarm_replay"], templates["autofarm_repetition-battle"]]),
	"autofarm_launch-launch": Sequence(templates = [templates["autofarm_repetition-battle"]]),
	"autofarm_launch-refill": Sequence(templates = [templates["refill-energy_shop"], templates["refill-energy_energy"], templates["refill-energy_validate"], templates["refill-energy_ok"], templates["refill-energy_close"], templates["autofarm_repetition-battle"]]),
	"bj5_invite-chat": Sequence(templates = [templates["bj5_chat"], templates["bj5_message"], templates["bj5_accept"], templates["bj5_validate"]], starter = True),
	"bj5_launch-battle": Sequence(templates = [templates["bj5_ready"], templates["bj5_loot"], templates["refill-energy_ok"], templates["bj5_validate"]]),
	"bj5-refill": Sequence(templates = [templates["refill-energy_shop"], templates["refill-energy_energy"], templates["refill-energy_validate"], templates["refill-energy_ok"], templates["refill-energy_close"], templates["autofarm_repetition-battle"]]),
}

#/ Farms enumeration \#

farms = {
	"change": Farm([sequences["change_dungeon"]], types["change"]),
	"launch": Farm([sequences["launch_skip-event"], sequences["launch_start"], sequences["launch_coffre"], sequences["autobattle_menu"]], types["start"], 3),
	"autofarm": Farm([sequences["autofarm_launch-battles"], sequences["autofarm_launch-refill"]], types["db"], 0),
}

#/ Status \#

from Class.Status import Status
status = Status(setup._data['tasks'])

#/ Mail \#
# send_mail('Bonjour ce mail provient d un bot')

#/ Building the global registry \# 

if not('screen' in config._data.keys()):
	img = ImageGrab.grab()
	config._data["screen"] = {
		"top": 0,
		"left": 0,
		"width": img.size[0],
		"height": img.size[1]
	}
	ImageAnalyser.set_screen(config._data["screen"])

registry = {
	'config': config,
	'setup': setup,
	'status': status,
	'in_game': {
		'types': types,
		'actions': actions,
		'templates': templates,
		'sequences': sequences,
		'farms': farms,
		'activeFarm': {
			'farm': "launch",
			'times': 1,
			'user': False
		}
	}
}

