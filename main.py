from setup import registry
from Class.Exception import Exception
import time

# print(registry['config'])

# print(registry['in_game']['templates']['autofarm_repetition-battle'].execute())

while True:
	registry['in_game']['farms']['test_farm'].selectSequence()
	time.sleep(0.5)