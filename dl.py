from urllib.request import urlopen
from urllib.error import HTTPError
import os
import json

from colorama import init, Style, Fore

DEFAULT_EXTENSION = 'png'
VERBOSE = True

# Data to fetch
enabled = ['competence']

new = 0
cache = 0
fail = 0

# Returns array of arrays representing each possible case when combining all the arrays in iter
def allPossibleCases (iter):
	if len(iter) == 1: return iter[0]
	else:
		result = []
		allCasesOfRest = allPossibleCases(iter[1:]) # recur with rest of the iter
		for i in iter[0]:
			for j in allCasesOfRest:
				if isinstance(j, list):
					result.append([i] + j)
				else:
					result.append([i, j])
		return result

# Download a given file
def getFile (dir, fname):
	global new, cache, fail
	path = dir + '/' + fname

	try:
		if os.path.exists(path):
			cache += 1
			return 2
		response = urlopen('http://data2.alidhan.net/img/' + dir + '/' + fname)
		new += 1
		if not os.path.exists(dir):
			os.makedirs(dir)
		with open(path, 'wb') as out:
			out.write(response.read())
			return 0
	except HTTPError as e:
		fail += 1
		return 1
	except IOError:
		return 1

# Try to get a file, print the result
def tryFile (dir, name, ext):
	# Return value of getFile (0=success, 1=failure, 2=cache)
	ret = {0: Fore.GREEN, 1: Fore.RED, 2: Fore.MAGENTA}
	fname = name + '.' + ext
	disp = fname + ' ' if VERBOSE else '+'

	try:
		x = getFile(dir, fname)
		print(f'{ret[x]}{disp}', end='')
	except TypeError as e:
		print(f'{Fore.RED}{disp}', end='')
		pass

# Handle an item and print it
def processItem (dir, item):
	if not 'format' in item:
		print(f'{Fore.RED}Warning: missing mandatory field \'format\' in item')
		return
	
	disp = item['name'] if 'name' in item else '<' + item['format'] + '>'
	exts = item['ext'] if 'ext' in item and isinstance(item['ext'], list) else [DEFAULT_EXTENSION]
	
	print(f"{disp} : ", end='', flush=True)
	
	for ext in exts:
		# Multiple files
		if 'iter' in item and item['iter']:	
			# Create arrays to iterate over
			values = []
			for iter in item['iter']:
				# Iterate over a list
				if isinstance(iter, list):
					values.append(iter)
				# Iterate over a range
				elif isinstance(iter, int):
					values.append(list(range(1, iter + 1)))
			
			# Get every possible file for this item
			for args in allPossibleCases(values):
				if isinstance(args, list):
					args = tuple(args)
				tryFile(dir, item['format'] % args, ext)
		# Single file
		else:
			tryFile(dir, item['format'], ext)
		print() # end

# Main
init(autoreset=True)

with open('data.json') as file:
	data = json.load(file)
	if len(enabled) == 0:
		for key in data:
			print('---' +key + '---')
			items = data[key]
			for item in items:
				processItem(key,item)
	else:
		for key in set(enabled):
			if key not in data: continue
			print('--- ' + key + ' ---')
			items = data[key]
			for item in items:
				processItem(key, item)


print('--- ' + str(new) + ' files downloaded, ' + str(cache) + ' cached, ' + str(fail) + ' failed ---')
