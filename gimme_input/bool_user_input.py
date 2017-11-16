from .resolvable import Resolvable
import sys

class BoolUserInput( Resolvable):
	'''
	Asks user for a yes no input.

	Requires a default
	'''

	def __init__(self, prompt, default, type=str, fineControlOnly=False):
		super(BoolUserInput, self).__init__()
		self.prompt = prompt
		self.default = default
		self.type = type
		self.fineOnly = fineControlOnly

	def _resolve(self, useDefaults, fineControl):
		if useDefaults or (self.fineOnly and not fineControl):
			return str(self.default)
		try_again = True

		while try_again:
			if self.default:
				prompt = self.prompt + ' ([y]/n): '
			else:
				prompt = self.prompt + ' (y/[n]): '
			inp = out_input(prompt)
			try_again = False
			if not inp: # use the default
				inp = self.default
				break
			
			if 'y' in inp.lower():
				return True
			elif 'n' in inp.lower():
				return False
			else:
				sys.stderr.write("Input must be yes/no".format(self.type))
				inp = None
				try_again = True
		