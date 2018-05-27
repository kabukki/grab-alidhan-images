import urllib2
import os

from colorama import init, Style, Fore

# All data
all = {
	'coffre': [
		{'iter': 4}
	],
	'objet': [
		{'name': 'bec', 'iter': 2, 'underscore': True},
		{'name': 'blood'},
		{'name': 'bolef5'},
		{'name': 'bouteille_vide'},
		{'name': 'cadavre_chenille'},
		{'name': 'carapace', 'iter': 2},
		{'name': 'chapeau', 'iter': 5},
		{'name': 'chardon'},
		{'name': 'coquille', 'iter': 6},
		{'name': 'cristal', 'iter': 9},
		{'name': 'dent', 'iter': 5},
		{'name': 'feuille', 'iter': 3},
		{'name': 'fiolevide'},
		{'name': 'fragment'},
        {'name': 'griffe'},
        {'name': 'grimoire'},
		{'name': 'jevx7i5doqbh'},
		{'name': 'lame_depeceur'},
		{'name': 'manche_mineur'},
		{'name': 'minerai','iter':11},
		{'name': 'p9jp2wnq9bsa'},
		{'name': 'patte'},
		{'name': 'peau', 'iter': 6},
		{'name': 'piece', 'iter': 1},
		{'name': 'pierre', 'iter': 12},
		{'name': 'pierre_golem'},
		{'name': 'plume_coq'},
		{'name': 'zj20ek71lkzk'},
	],
	'objetquete': [
		{'name': 'bousolle'},
		{'name': 'clef', 'iter': 10, 'underscore': True},
		{'name': 'gateau_noel', 'iter': 10, 'underscore': True, 'pad': True},
		{'name': 'parchemin','iter': 5},
	],
	'pnj': [
		{'name': 'pnj', 'iter': 200},
		{'name': 'swirl', 'iter': 20},
		{'name': 'gardeTP', 'iter': 20},
		{'name': 'paladin_varox'},
		{'name': 'jeune_guerrier'},
		{'name': 'bougie'},
		{'name': 'lynus'},
		{'name': 'moine_copiste'},
		{'name': 'tynus'},
		{'name': 'new_garde', 'iter': ['r', 'e', 'c'], 'underscore': True},
	],
	'pnjDetail': [
		{'name': 'bougie'},
		{'name': 'competence'},
		{'name': 'Eidola'},
		{'name': 'fille_couteau'},
		{'name': 'garde3_detail'},
		{'name': 'garde4_detail'},
		{'name': 'garde5_detail'},
		{'name': 'jeune_guerrier'},
		{'name': 'lynus'},
		{'name': 'moine_copiste'},
		{'name': 'paladin_varox'},
		{'name': 'pr_lactos'},
		{'name': 'soldat_arene'},
		{'name': 'Tynus'},
	],
	'potion': [
		{'name': 'bonbec', 'iter': 13},
		{'name': 'buffpot', 'iter': 8},
		{'name': 'carotte'},
		{'name': 'feuille', 'iter': 11},
		{'name': 'flacon'},
		{'name': 'gateau'},
		{'name': 'millefeuilleschamsrz6'},
		{'name': 'poisson', 'iter': 5},
		{'name': 'pomme', 'iter': 2},
		{'name': 'potion', 'iter': 50},
		{'name': 'potion_constit_majeure'},
		{'name': 'potion_dext_majeure'},
		{'name': 'potion_force_majeure'},
		{'name': 'potiron'},
		{'name': 'viande', 'iter': 7},
	],
	'competence': [
		{'name': 'skill', 'iter': 100}
	],
	'classe': [
		{'name': 'manant', 'iter': ['m','f'], 'underscore': True},
		{'name': 'magicien', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'moine', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'guerrier', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'archer', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'franctireur', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'druide', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'barbare', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'paladin', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'pretre', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'geomancien', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'aquamancien', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'heros', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'heros_m', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_mr', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_me', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_mc', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_f', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_fr', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_fe', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_fc', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'bagnard','iter':2},
		{'name': 'balrog'},
		{'name': 'felin'},
		{'name': 'grenouille'},
		{'name': 'ogre'},
		{'name': 'metal'},
	],
	'arme': [
		{'name': 'champi'},
	],
	'monstre/insecte': [
		{'name': 'lezard'},
		{'name': 'gecko', 'iter': 2},
		{'name': 'escargot', 'iter': 3},
		{'name': 'insecte', 'iter': 2, 'pad': True},
		{'name': 'fourmi', 'iter': 2},
		{'name': 'chenille', 'iter': 3},
		{'name': 'mouche', 'iter': 2},
		{'name': 'lezard', 'iter': 5},
		{'name': 'scarabe', 'iter': 9},
		{'name': 'cloporte', 'iter': 2},
		{'name': 'grenouille', 'iter': 2},
		{'name': 'araignee', 'iter': 5},
		{'name': 'abeille', 'iter': 3},
		{'name': 'abeille', 'iter': 1, 'pad': True},
		{'name': 'libellule', 'iter': 4},
	],
	'monstre/prison': [
		{'name': 'poisson'},
		{'name': 'prisonnier'},
	],
	'monstre/bizarre': [
		{'name': 'tortue'},
		{'name': 'galahaad'},
		{'name': 'epouvantail'},
		{'name': 'MudGolem'},
		{'name': 'fantome', 'iter': 1},
		{'name': 'elemental', 'iter': 13},
		{'name': 'ange', 'iter': 2},
	],
	'monstre/bestiaux': [
		{'name': 'chat3nd2'},
		{'name': 'chat1do2'},
		{'name': 'renard'},
		{'name': 'hog'},
		{'name': 'wolf'},
		{'name': 'lizardman'},
		{'name': 'serpentmer'},
		{'name': 'coq', 'iter': 2},
		{'name': 'serpent', 'iter': 4},
		{'name': 'poisson', 'iter': 3},
		{'name': 'goblin', 'iter': 1},
		{'name': 'demon', 'iter': 1},
		{'name': 'ours', 'iter': 6},
		{'name': 'ours', 'iter': 8},
		{'name': 'chauve_souris', 'iter': 1},
	],
	'monstre/boss': [
		{'name': 'poisson'},
		{'name': 'herisson-lion'},
		{'name': 'bouquetin'},
		{'name': 'dragon'},
		{'name': 'ombre_ailee'},
		{'name': 'Gomina'},
		{'name': 'fv1006'},
		{'name': 'aigle'},
		{'name': 'yeti'},
	],
	'monstre/flore': [
		{'name': 'tournesol', 'iter': 2},
		{'name': 'champignon', 'iter': 4},
		{'name': 'champignon', 'iter': 3, 'pad': True},
		{'name': 'plantecarnivore', 'iter': 3},
		{'name': 'arbre', 'iter': 6},
	],
}

# Data to fetch
enabled = ['objet', 'monstre/flore']

new = 0
skip = 0
fail = 0

# Download a given file
def getFile (dir, name):
	global new, skip, fail

	fname = name + '.png'
	path = dir + '/' + fname
	try:
		if os.path.exists(path):
			skip += 1
			print Fore.MAGENTA + name + ' already exists, skipping'
			return
		response = urllib2.urlopen('http://data2.alidhan.net/img/' + dir + '/' + fname)
		new += 1
		if not os.path.exists(dir):
			os.makedirs(dir)
		with open(path, 'wb') as out:
			out.write(response.read())
			print Fore.GREEN + name
	except urllib2.HTTPError as e:
		fail += 1
		print Fore.RED + name
	except IOError:
		pass

# Build name from index and formatting options
def nthItem (name, n, underscore=False, pad=False):
	if (underscore): name += '_'
	if (pad): name += '0'
	name += str(n)
	return name

# Main
init(autoreset=True)
for key in set(enabled):
	if key not in all: continue
	items = all[key]
	print '--- ' + key + ' ---'
	for item in items:
		if 'iter' in item and item['iter']:
			values = []
			# Iterate over a list
			if isinstance(item['iter'], list):
				values = item['iter']
			# Iterate over a range
			elif isinstance(item['iter'], int):
				values = range(1, item['iter'] + 1)
			for n in values:
				getFile(key, nthItem(
					item['name'] if 'name' in item else '',
					n,
					item['underscore'] if 'underscore' in item else False,
					item['pad'] if 'pad' in item else False)
				)
		else:
			getFile(key, item['name'])
	print '--- ' + str(new) + ' files downloaded, ' + str(skip) + ' skipped, ' + str(fail) + ' failed ---'
