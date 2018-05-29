from urllib.request import urlopen
from urllib.error import HTTPError
import os

from colorama import init, Style, Fore

# All data
all = {
    'coffre': [
        {'iter': 4}
    ],
    'objet': [
        {'name': 'ashkran'},
        {'name': 'aile', 'iter': 1},
        {'name': 'aile', 'iter': 5, 'underscore': True},
        {'name': 'bec', 'iter': 2, 'underscore': True},
        {'name': 'blood'},
        {'name': 'bolef5'},
        {'name': 'boue', 'iter': 1},
        {'name': 'bouteille_vide'},
        {'name': 'cadavre_chenille'},
        {'name': 'carapace', 'iter': 2},
        {'name': 'chapeau', 'iter': 5},
        {'name': 'chardon'},
        {'name': 'clochette06yx7'},
        {'name': 'coquille', 'iter': 6},
        {'name': 'crane'},
        {'name': 'crane', 'iter': 4},
        {'name': 'criniere_herisson'},
        {'name': 'cristal', 'iter': 9},
        {'name': 'dent', 'iter': 5},
        {'name': 'defaut', 'ext': ['gif']},
        {'name': 'feuille', 'iter': 3},
        {'name': 'fiolevide'},
        {'name': 'fourrure'},
        {'name': 'fourrure', 'iter': 2},
        {'name': 'fragment'},
        {'name': 'griffe'},
        {'name': 'griffe', 'iter': 2},
        {'name': 'grimoire'},
        {'name': 'jevx7i5doqbh'},
        {'name': 'lame_depeceur'},
        {'name': 'manche_mineur'},
        {'name': 'minerai', 'iter': 11},
        {'name': 'minerai_cristal_rouge', 'iter': 1, 'underscore': True},
        {'name': 'p9jp2wnq9bsa'},
        {'name': 'patte'},
        {'name': 'peau', 'iter': 6},
        {'name': 'piece', 'iter': 1},
        {'name': 'pierre', 'iter': 12},
        {'name': 'pierre_golem'},
        {'name': 'plume_coq'},
        {'name': 'queue', 'iter': 6},
        {'name': 'zj20ek71lkzk'},
    ],
    'objetquete': [
        {'name': 'bousolle'},
        {'name': 'branche', 'iter': 1},
        {'name': 'clef', 'iter': 10, 'underscore': True},
        {'name': 'gateau_noel', 'iter': 1, 'underscore': True, 'pad': True},
        {'name': 'parchemin', 'iter': 5},
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
        {'name': 'Bamou'},
        {'name': 'bougie'},
        {'name': 'competence'},
        {'name': 'defaut'},
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
        # Detail pour les pnj existants
        {'name': 'pnj20detail'},
        {'name': 'pnj25_detail'},
        {'name': 'pnj28detail'},
        {'name': 'pnj29detail'},
        {'name': 'pnj75_detail'},
        {'name': 'pnj80_detail'},
        {'name': 'pnj86_detail'},
    ],
    'potion': [
        {'name': 'bonbec', 'iter': 13},
        {'name': 'buffpot', 'iter': 8},
        {'name': 'carotte'},
        {'name': 'cheese'},
        {'name': 'feuille', 'iter': 11},
        {'name': 'flacon'},
        {'name': 'gateau'},
        {'name': 'millefeuilleschamsrz6'},
        {'name': 'poisson', 'iter': 5},
        {'name': 'pomme', 'iter': 2},
        {'name': 'potion', 'iter': 50},
        {'name': 'potion_agile_majeure'},
        {'name': 'potion_constit_majeure'},
        {'name': 'potion_dext_majeure'},
        {'name': 'potion_force_majeure'},
        {'name': 'potiron'},
        {'name': 'tete_chenille', 'ext': ['jpg']},
        {'name': 'viande', 'iter': 7},
    ],
    'competence': [
        {'name': 'BSA'},
        {'name': 'chasseur_de_prime'},
        {'name': 'coup_precis', 'ext': ['gif']},
        {'name': 'cueillette'},
        {'name': 'depecage'},
        {'name': 'esprit_voyageur', 'ext': ['gif']},
        {'name': 'esprit_voyageur_majeur', 'ext': ['gif']},
        {'name': 'justicier', 'ext': ['gif']},
        {'name': 'lien_tellurique'},
        {'name': 'minage'},
        {'name': 'peche'},
        {'name': 'piege_meurtrier'},
        {'name': 'piege_mortel'},
        {'name': 'pousser'},
        {'name': 'regeneration_energie', 'ext': ['gif']},
        {'name': 'regeneration_vie', 'ext': ['gif']},
        {'name': 'skill', 'iter': 100, 'ext': ['png', 'gif']},
        {'name': 'suractivite_mineure', 'ext': ['gif']},
        {'name': 'tempete'},
        {'name': 'tirer'},
    ],
    'classe': [
        {'name': 'manant', 'iter': ['m', 'f'], 'underscore': True},
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
        {'name': 'bagnard', 'iter': 2},
        {'name': 'magicien_f', 'ext': ['gif']},
        {'name': 'balrog'},
        {'name': 'felin'},
        {'name': 'grenouille'},
        {'name': 'ogre'},
        {'name': 'metal'},
        {'name': 'murdoc', 'ext': ['gif']},
        {'name': 'sparkman2', 'ext': ['gif']},
    ],
    'ecran': [
        {'name': 'auberge'}
    ],
    'arme': [
        {'name': 'amulette', 'iter': 13, 'pad': True},
        # la faute est volontaire
        {'name': 'amuremort'},
        {'name': 'anneau','iter': 1},
        {'name': 'anneaufer'},
        {'name': 'anneauHallo'},
        {'name': 'arbalete', 'iter': 7},
        {'name': 'arc', 'iter': 16},
        {'name': 'arc9_s'},
        {'name': 'armemort'},
        {'name': 'armure', 'iter': 16},
        {'name': 'badgeduconscritrvk5'},
        {'name': 'bague', 'iter': 9, 'pad': True},
        {'name': 'bague', 'iter': 17},
        {'name': 'bague_bete_puissante'},
        {'name': 'bague_bete_sup'},
        {'name': 'bague_immortel'},
        {'name': 'baguerouge01lt5'},
        {'name': 'baguette', 'iter': 4},
        {'name': 'bague', 'iter': 7, 'pad': True},
        {'name': 'bague', 'iter': 17},
        {'name': 'bandeau', 'iter': 6, 'pad': True},
        {'name': 'bandeau', 'iter': 4},
        {'name': 'bas', 'iter': 45},
        {'name': 'bas2_l'},
        {'name': 'bas8_l'},
        {'name': 'bas_tempete_scinti'},
        {'name': 'bas_tempete_sup'},
        {'name': 'baton', 'iter': 30},
        {'name': 'baton_bete_puissant'},
        {'name': 'baton_volcanos'},
        {'name': 'baton_volcanos_scinti'},
        {'name': 'batonmagique1cl0'},
        {'name': 'beret'},
        {'name': 'bonnet_noel', 'iter': ['', '2', '_new']},
        {'name': 'botte_justice_leg'},
        {'name': 'botte_justice_sup'},
        {'name': 'botte_noel', 'iter': ['', '2', '_new']},
        {'name': 'bottes', 'iter': 26},
        {'name': 'bottes', 'iter': 8, 'pad': True},
        {'name': 'bottes07_l'},
        {'name': 'bottes08_l'},
        {'name': 'botte_sauvage_puiss'},
        {'name': 'boucle', 'iter': 10},
        {'name': 'bouclier', 'iter': 18},
        {'name': 'bottes11_l'},
        {'name': 'bottes14_l'},
        {'name': 'cacheoreilles'},
        {'name': 'canne_a_peche'},
        {'name': 'cape', 'iter': 8},
        {'name': 'capenoel'},
        {'name': 'cape_noel', 'iter': ['2', '_new']},
        {'name': 'capuche_chasseur_puissant'},
        {'name': 'capuche_chasseur_sup'},
        {'name': 'capucheti9'},
        {'name': 'cas_consc'},
        {'name': 'cape', 'iter': 28},
        {'name': 'casque', 'iter': 28},
        {'name': 'casque_de_justice_puissant'},
        {'name': 'champi'},
        {'name': 'chapeau', 'iter': 28},
        {'name': 'chapka', 'iter': 10},
        {'name': 'chaussons_volcano_scintillant'},
        {'name': 'chaussons_volcano_sup'},
        {'name': 'chaussure_chasseur_sup'},
        {'name': 'chaussures', 'iter': 12},
        {'name': 'bottes7_l'},
        {'name': 'chemise', 'iter': 2},
        {'name': 'citrouille'},
        {'name': 'cle', 'iter': 1},
        {'name': 'collier01', 'iter': ['a', 'g', 'm', 'p'], 'underscore': True},
        {'name': 'collier', 'iter': 4, 'pad': True},
        {'name': 'collier_infini_scintillant'},
        {'name': 'collier_infini_sup'},
        {'name': 'colliermort'},
        {'name': 'collier_zephyr'},
        {'name': 'cor'},
        {'name': 'couronne', 'iter': 4},
        # la faute est volontaire
        {'name': 'coutea', 'iter': 10},
        {'name': 'couteau', 'iter': 1, 'pad': True},
        {'name': 'crane', 'iter': 2},
        {'name': 'croix'},
        {'name': 'crosse', 'iter': 5},
        {'name': 'dague', 'iter': 2},
        {'name': 'defaut_torse'},
        {'name': 'diademe', 'iter': 7},
        {'name': 'echarpeduperenoeleg5'},
        {'name': 'epee', 'iter': 22},
        {'name': 'epee_justice_sup'},
        {'name': 'epee_justice_scin'},
        {'name': 'equip', 'iter': 61},
        {'name': 'escarpins01id3'},
        {'name': 'fronde', 'iter': 1, 'pad': True},
        {'name': 'gant', 'iter': 9, 'pad': True},
        {'name': 'gant', 'iter': 10},
        {'name': 'cape_noel', 'iter': ['', '2']},
        {'name': 'gants01gf6'},
        {'name': 'griffe', 'iter': 4},
        {'name': 'griffe'},
        {'name': 'grimoire', 'iter': 6},
        {'name': 'grimoiremort'},
        {'name': 'hache', 'iter': 11},
        {'name': 'hache_sauvage_pui'},
        {'name': 'hache_sauvage_sup'},
        {'name': 'hachette'},
        {'name': 'haut', 'iter': 30},
        {'name': 'haut8_l'},
        {'name': 'haut14_l'},
        # les fautes sont volontaires
        {'name': 'madail', 'iter': 10},
        {'name': 'marteau', 'iter': 10},
        {'name': 'masque', 'iter': 2, 'pad': True},
        {'name': 'masque_nature_scintillant'},
        {'name': 'masque_nature_sup'},
        {'name': 'masse', 'iter': 8},
        # la faute est volontaire
        {'name': 'mitain', 'iter': 10},
        {'name': 'ombrelle01tq1'},
        {'name': 'paire_pantoufle_puissante'},
        {'name': 'paire_pantoufle_sup'},
        {'name': 'pdtfnv1c2vk5'},
        {'name': 'pelle', 'iter': 1},
        {'name': 'pelle', 'iter': 2, 'pad': True},
        {'name': 'pendentif'},
        {'name': 'pendentif', 'iter': 11, 'pad': True},
        {'name': 'pied', 'iter': 2, 'pad': True},
        {'name': 'pierre', 'iter': 8},
        {'name': 'pioche'},
        {'name': 'pioche', 'iter': 2, 'pad': True},
        {'name': 'robebal2jd4'},
        {'name': 'sabre', 'iter': 4, 'pad': True},
        {'name': 'sandales', 'iter': 5},
        {'name': 'serpe'},
        {'name': 'teteabeillerouge'},
        {'name': 'tetechauvesouris'},
        {'name': 'tetereduite'},
        {'name': 'tetine'},
        {'name': 'tiare01qr5'},
        {'name': 'toge_pelerin_puissant'},
        {'name': 'toge_pelerin_sup'},
        {'name': 'tunique_aventurier'},
        # JPG
        {'name': '20039517vg7', 'ext': ['jpg']},
        {'name': 'arf_consc', 'ext': ['jpg']},
        {'name': 'arm_consc', 'ext': ['jpg']},
        {'name': 'cons_pant', 'ext': ['jpg']},
        {'name': 'consc_bouc', 'ext': ['jpg']},
    ],
    'map': [
        {'name': '1ioedfza'},
        {'name': '2dffqsjy'},
        {'name': '3xrpttdsa'},
        {'name': '4sdzezoid'},
        {'name': 'cne8585sd'},
        {'name': 'ezrgpok52k2'},
        {'name': '6re4hr54z'},
        {'name': 'dfsdf342354'},
        {'name': '9llleze5'},
        {'name': '5lllezesd4'},
        {'name': '13zesdqs3'},
        {'name': 'xcvxc4422365'},
        {'name': 'vxcvxcvx14sfsf'},
        {'name': 'fzef8ezr6sdf3sdf1'},
        {'name': '1alllezesdqs1'},
        {'name': '1alllezesdqs2'},
        {'name': 'cvfghnjkloi865'},
        {'name': 'sdfgxcxciopklmjkluyaz2'},
        {'name': 'sdfgxcxciopklmjkluyaz'},
        {'name': 'scxcvxcbhrturtujkolo'},
        {'name': 'ergsdfsdckxjbcvbor'},
        {'name': 'xcvxcvcbnvgjghjyikklpo'},
        {'name': 'ergsdfsdckxjbcvbor'},
        {'name': 'ghrimlong10yjzjb'},
        {'name': 'ghrimlong11btfeu'},
        {'name': 'cimetiere', 'iter': 2},
        {'name': 'foret', 'iter': 19},
        #Sous sol Mérulik
        {'name': 'boutiquemilieusoussol'},
        #Mérulik
        {'name': 'boutiquemilieu'},
        #Dernière map protégé roya avant Broquir
        {'name': '2s4f6e1sdf51qaa'},
        #Plaine verdoyante Rhogan
        {'name': 'dghrdf3vb2sd26'},
        #Rhogan
        {'name': 'fsf51zefsqf1'},
        #Auberge de Rhogan
        {'name': 'dfh5rdf5sg4'},
        #Faille est
        {'name': 'vbxbcvbncvneiiii'},
        #Map juste à côté Faille est
        {'name': 'foret__14'},
        {'name': 'douane'},
        {'name': 'maptuto'},
        {'name': 'sous_sol'},
        {'name': 'villetuto'},
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
        {'name': 'chauve_souris', 'iter': 1},
        {'name': 'rat'},
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
#enabled = ['competence']
enabled = all.keys()

new = 0
skip = 0
fail = 0

# Download a given file
def getFile (dir, name, ext='png'):
    global new, skip, fail
    fname = name + '.' + ext
    path = dir + '/' + fname

    try:
        if os.path.exists(path):
            skip += 1
            print(Fore.MAGENTA + name + ' already exists, skipping')
            return
        response = urlopen('http://data2.alidhan.net/img/' + dir + '/' + fname)
        new += 1
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(path, 'wb') as out:
            out.write(response.read())
            print(Fore.GREEN + name)
    except HTTPError as e:
        fail += 1
        print(Fore.RED + name)
    except IOError:
        pass

# Build name from value in iter and formatting options
def nthItem (name, n, underscore=False, pad=False):
    if (underscore): name += '_'
    if (pad and isinstance(n, int) and n < 10): name += '0'
    name += str(n)
    return name

# Main
init(autoreset=True)
for key in set(enabled):
    if key not in all: continue
    items = all[key]
    print('--- ' + key + ' ---')
    for item in items:
        exts = item['ext'] if 'ext' in item and isinstance(item['ext'], list) else ['png']
        for ext in exts:
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
                        item['pad'] if 'pad' in item else False
                    ), ext)
            else:
                getFile(key, item['name'])
print('--- ' + str(new) + ' files downloaded, ' + str(skip) + ' skipped, ' + str(fail) + ' failed ---')
