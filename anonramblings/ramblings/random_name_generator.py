import random

ANIMALS = ['Canidae', 'Felidae', 'Cat', 'Cattle', 'Dog', 'Donkey', 'Goat',
           'Guinea pig',
           'Horse', 'Pig', 'Rabbit', 'Fancy rat varieties',
           'laboratory rat strains',
           'Sheep breeds', 'Water buffalo breeds', 'Chicken breeds',
           'Duck breeds',
           'Goose breeds', 'Pigeon breeds', 'Turkey breeds', 'Aardvark',
           'Aardwolf',
           'African buffalo', 'African elephant', 'African leopard',
           'Albatross',
           'Alligator', 'Alpaca', 'American buffalo (bison)', 'American robin',
           'Amphibian', 'list', 'Anaconda', 'Angelfish', 'Anglerfish', 'Ant',
           'Anteater',
           'Antelope', 'Antlion', 'Ape', 'Aphid', 'Arabian leopard',
           'Arctic Fox',
           'Arctic Wolf', 'Armadillo', 'Arrow crab', 'Asp', 'Ass (donkey)',
           'Baboon',
           'Badger', 'Bald eagle', 'Bandicoot', 'Barnacle', 'Barracuda',
           'Basilisk',
           'Bass', 'Bat', 'Beaked whale', 'Bear', 'list', 'Beaver', 'Bedbug',
           'Bee',
           'Beetle', 'Bird', 'list', 'Bison', 'Blackbird', 'Black panther',
           'Black widow spider', 'Blue bird', 'Blue jay', 'Blue whale', 'Boa',
           'Boar',
           'Bobcat', 'Bobolink', 'Bonobo', 'Booby', 'Box jellyfish', 'Bovid',
           'Buffalo, African', 'Buffalo, American (bison)', 'Bug', 'Butterfly',
           'Buzzard',
           'Camel', 'Canid', 'Cape buffalo', 'Capybara', 'Cardinal', 'Caribou',
           'Carp',
           'Cat', 'list', 'Catshark', 'Caterpillar', 'Catfish', 'Cattle',
           'list',
           'Centipede', 'Cephalopod', 'Chameleon', 'Cheetah', 'Chickadee',
           'Chicken',
           'list', 'Chimpanzee', 'Chinchilla', 'Chipmunk', 'Clam', 'Clownfish',
           'Cobra',
           'Cockroach', 'Cod', 'Condor', 'Constrictor', 'Coral', 'Cougar',
           'Cow',
           'Coyote', 'Crab', 'Crane', 'Crane fly', 'Crawdad', 'Crayfish',
           'Cricket',
           'Crocodile', 'Crow', 'Cuckoo', 'Cicada', 'Damselfly', 'Deer',
           'Dingo',
           'Dinosaur', 'list', 'Dog', 'list', 'Dolphin', 'Donkey', 'list',
           'Dormouse',
           'Dove', 'Dragonfly', 'Dragon', 'Duck', 'list', 'Dung beetle',
           'Eagle',
           'Earthworm', 'Earwig', 'Echidna', 'Eel', 'Egret', 'Elephant',
           'Elephant seal',
           'Elk', 'Emu', 'English pointer', 'Ermine', 'Falcon', 'Ferret',
           'Finch',
           'Firefly', 'Fish', 'Flamingo', 'Flea', 'Fly', 'Flyingfish', 'Fowl',
           'Fox',
           'Frog', 'Fruit bat', 'Gamefowl', 'list', 'Galliform', 'list',
           'Gazelle',
           'Gecko', 'Gerbil', 'Giant panda', 'Giant squid', 'Gibbon',
           'Gila monster',
           'Giraffe', 'Goat', 'list', 'Goldfish', 'Goose', 'list', 'Gopher',
           'Gorilla',
           'Grasshopper', 'Great blue heron', 'Great white shark',
           'Grizzly bear',
           'Ground shark', 'Ground sloth', 'Grouse', 'Guan', 'list', 'Guanaco',
           'Guineafowl', 'list', 'Guinea pig', 'list', 'Gull', 'Guppy',
           'Haddock',
           'Halibut', 'Hammerhead shark', 'Hamster', 'Hare', 'Harrier', 'Hawk',
           'Hedgehog', 'Hermit crab', 'Heron', 'Herring', 'Hippopotamus',
           'Hookworm',
           'Hornet', 'Horse', 'list', 'Hoverfly', 'Hummingbird',
           'Humpback whale',
           'Hyena', 'Iguana', 'Impala', 'Irukandji jellyfish', 'Jackal',
           'Jaguar', 'Jay',
           'Jellyfish', 'Junglefowl', 'Kangaroo', 'Kangaroo mouse',
           'Kangaroo rat',
           'Kingfisher', 'Kite', 'Kiwi', 'Koala', 'Koi', 'Komodo dragon',
           'Krill',
           'Ladybug', 'Lamprey', 'Landfowl', 'Land snail', 'Lark', 'Leech',
           'Lemming',
           'Lemur', 'Leopard', 'Leopon', 'Limpet', 'Lion', 'Lizard', 'Llama',
           'Lobster',
           'Locust', 'Loon', 'Louse', 'Lungfish', 'Lynx', 'Macaw', 'Mackerel',
           'Magpie',
           'Mammal', 'Manatee', 'Mandrill', 'Manta ray', 'Marlin', 'Marmoset',
           'Marmot',
           'Marsupial', 'Marten', 'Mastodon', 'Meadowlark', 'Meerkat', 'Mink',
           'Minnow',
           'Mite', 'Mockingbird', 'Mole', 'Mollusk', 'Mongoose',
           'Monitor lizard',
           'Monkey', 'Moose', 'Mosquito', 'Moth', 'Mountain goat', 'Mouse',
           'Mule',
           'Muskox', 'Narwhal', 'Newt', 'New World quail', 'Nightingale',
           'Ocelot',
           'Octopus', 'Old World quail', 'Opossum', 'Orangutan', 'Orca',
           'Ostrich',
           'Otter', 'Owl', 'Ox', 'Panda', 'Panther', 'Panthera hybrid',
           'Parakeet',
           'Parrot', 'Parrotfish', 'Partridge', 'Peacock', 'Peafowl', 'Pelican',
           'Penguin', 'Perch', 'Peregrine falcon', 'Pheasant', 'Pig', 'Pigeon',
           'list',
           'Pike', 'Pilot whale', 'Pinniped', 'Piranha', 'Planarian',
           'Platypus',
           'Polar bear', 'Pony', 'Porcupine', 'Porpoise',
           "Portuguese man o' war",
           'Possum', 'Prairie dog', 'Prawn', 'Praying mantis', 'Primate',
           'Ptarmigan',
           'Puffin', 'Puma', 'Python', 'Quail', 'Quelea', 'Quokka', 'Rabbit',
           'list',
           'Raccoon', 'Rainbow trout', 'Rat', 'Rattlesnake', 'Raven',
           'Ray (Batoidea)',
           'Ray (Rajiformes)', 'Red panda', 'Reindeer', 'Reptile', 'Rhinoceros',
           'Right whale', 'Roadrunner', 'Rodent', 'Rook', 'Rooster',
           'Roundworm',
           'Saber-toothed cat', 'Sailfish', 'Salamander', 'Salmon', 'Sawfish',
           'Scale insect', 'Scallop', 'Scorpion', 'Seahorse', 'Sea lion',
           'Sea slug',
           'Sea snail', 'Shark', 'list', 'Sheep', 'list', 'Shrew', 'Shrimp',
           'Silkworm',
           'Silverfish', 'Skink', 'Skunk', 'Sloth', 'Slug', 'Smelt', 'Snail',
           'Snake',
           'list', 'Snipe', 'Snow leopard', 'Sockeye salmon', 'Sole', 'Sparrow',
           'Sperm whale', 'Spider', 'Spider monkey', 'Spoonbill', 'Squid',
           'Squirrel',
           'Starfish', 'Star-nosed mole', 'Steelhead trout', 'Stingray',
           'Stoat', 'Stork',
           'Sturgeon', 'Sugar glider', 'Swallow', 'Swan', 'Swift', 'Swordfish',
           'Swordtail', 'Tahr', 'Takin', 'Tapir', 'Tarantula', 'Tarsier',
           'Tasmanian devil', 'Termite', 'Tern', 'Thrush', 'Tick', 'Tiger',
           'Tiger shark',
           'Tiglon', 'Toad', 'Tortoise', 'Toucan', 'Trapdoor spider',
           'Tree frog',
           'Trout', 'Tuna', 'Turkey', 'list', 'Turtle', 'Tyrannosaurus',
           'Urial',
           'Vampire bat', 'Vampire squid', 'Vicuna', 'Viper', 'Vole', 'Vulture',
           'Wallaby', 'Walrus', 'Wasp', 'Warbler', 'Water Boa', 'Water buffalo',
           'Weasel',
           'Whale', 'Whippet', 'Whitefish', 'Whooping crane', 'Wildcat',
           'Wildebeest',
           'Wildfowl', 'Wolf', 'Wolverine', 'Wombat', 'Woodpecker', 'Worm',
           'Wren',
           'Xerinae', 'X-ray fish', 'Yak', 'Yellow perch', 'Zebra',
           'Zebra finch',
           'Animals by number of neurons', 'Animals by size',
           'Common household pests',
           'Common names of poisonous animals', 'Alpaca', 'Bali cattle', 'Cat',
           'Cattle',
           'Chicken', 'Dog', 'Domestic Bactrian camel', 'Domestic canary',
           'Domestic dromedary camel', 'Domestic duck', 'Domestic goat',
           'Domestic goose',
           'Domestic guineafowl', 'Domestic hedgehog', 'Domestic pig',
           'Domestic pigeon',
           'Domestic rabbit', 'Domestic silkmoth', 'Domestic silver fox',
           'Domestic turkey', 'Donkey', 'Fancy mouse', 'Fancy rat', 'Lab rat',
           'Ferret',
           'Gayal', 'Goldfish', 'Guinea pig', 'Guppy', 'Horse', 'Koi', 'Llama',
           'Ringneck dove', 'Sheep', 'Siamese fighting fish', 'Society finch',
           'Yak',
           'Water buffalo']

ADJECTIVES = ['abandoned', 'able', 'absolute', 'adorable', 'adventurous',
              'academic', 'acceptable', 'acclaimed', 'accomplished', 'accurate',
              'aching', 'acidic', 'acrobatic', 'active', 'actual', 'adept',
              'admirable', 'admired', 'adolescent', 'adorable', 'adored',
              'advanced', 'afraid', 'affectionate', 'aged', 'aggravating',
              'aggressive', 'agile', 'agitated', 'agonizing', 'agreeable',
              'ajar', 'alarmed', 'alarming', 'alert', 'alienated', 'alive',
              'all', 'altruistic', 'amazing', 'ambitious', 'ample', 'amused',
              'amusing', 'anchored', 'ancient', 'angelic', 'angry', 'anguished',
              'animated', 'annual', 'another', 'antique', 'anxious', 'any',
              'apprehensive', 'appropriate', 'apt', 'arctic', 'arid',
              'aromatic', 'artistic', 'ashamed', 'assured', 'astonishing',
              'athletic', 'attached', 'attentive', 'attractive', 'austere',
              'authentic', 'authorized', 'automatic', 'avaricious', 'average',
              'aware', 'awesome', 'awful', 'awkward', 'babyish', 'bad', 'back',
              'baggy', 'bare', 'barren', 'basic', 'beautiful', 'belated',
              'beloved', 'beneficial', 'better', 'best', 'bewitched', 'big',
              'big-hearted', 'biodegradable', 'bite-sized', 'bitter', 'black',
              'black-and-white', 'bland', 'blank', 'blaring', 'bleak', 'blind',
              'blissful', 'blond', 'blue', 'blushing', 'bogus', 'boiling',
              'bold', 'bony', 'boring', 'bossy', 'both', 'bouncy', 'bountiful',
              'bowed', 'brave', 'breakable', 'brief', 'bright', 'brilliant',
              'brisk', 'broken', 'bronze', 'brown', 'bruised', 'bubbly',
              'bulky', 'bumpy', 'buoyant', 'burdensome', 'burly', 'bustling',
              'busy', 'buttery', 'buzzing', 'calculating', 'calm', 'candid',
              'canine', 'capital', 'carefree', 'careful', 'careless', 'caring',
              'cautious', 'cavernous', 'celebrated', 'charming', 'cheap',
              'cheerful', 'cheery', 'chief', 'chilly', 'chubby', 'circular',
              'classic', 'clean', 'clear', 'clear-cut', 'clever', 'close',
              'closed', 'cloudy', 'clueless', 'clumsy', 'cluttered', 'coarse',
              'cold', 'colorful', 'colorless', 'colossal', 'comfortable',
              'common', 'compassionate', 'competent', 'complete', 'complex',
              'complicated', 'composed', 'concerned', 'concrete', 'confused',
              'conscious', 'considerate', 'constant', 'content', 'conventional',
              'cooked', 'cool', 'cooperative', 'coordinated', 'corny',
              'corrupt', 'costly', 'courageous', 'courteous', 'crafty', 'crazy',
              'creamy', 'creative', 'creepy', 'criminal', 'crisp', 'critical',
              'crooked', 'crowded', 'cruel', 'crushing', 'cuddly', 'cultivated',
              'cultured', 'cumbersome', 'curly', 'curvy', 'cute', 'cylindrical',
              'damaged', 'damp', 'dangerous', 'dapper', 'daring', 'darling',
              'dark', 'dazzling', 'dead', 'deadly', 'deafening', 'dear',
              'dearest', 'decent', 'decimal', 'decisive', 'deep', 'defenseless',
              'defensive', 'defiant', 'deficient', 'definite', 'definitive',
              'delayed', 'delectable', 'delicious', 'delightful', 'delirious',
              'demanding', 'dense', 'dental', 'dependable', 'dependent',
              'descriptive', 'deserted', 'detailed', 'determined', 'devoted',
              'different', 'difficult', 'digital', 'diligent', 'dim', 'dimpled',
              'dimwitted', 'direct', 'disastrous', 'discrete', 'disfigured',
              'disgusting', 'disloyal', 'dismal', 'distant', 'downright',
              'dreary', 'dirty', 'disguised', 'dishonest', 'dismal', 'distant',
              'distinct', 'distorted', 'dizzy', 'dopey', 'doting', 'double',
              'downright', 'drab', 'drafty', 'dramatic', 'dreary', 'droopy',
              'dry', 'dual', 'dull', 'dutiful', 'each', 'eager', 'earnest',
              'early', 'easy', 'easy-going', 'ecstatic', 'edible', 'educated',
              'elaborate', 'elastic', 'elated', 'elderly', 'electric',
              'elegant', 'elementary', 'elliptical', 'embarrassed',
              'embellished', 'eminent', 'emotional', 'empty', 'enchanted',
              'enchanting', 'energetic', 'enlightened', 'enormous', 'enraged',
              'entire', 'envious', 'equal', 'equatorial', 'essential',
              'esteemed', 'ethical', 'euphoric', 'even', 'evergreen',
              'everlasting', 'every', 'evil', 'exalted', 'excellent',
              'exemplary', 'exhausted', 'excitable', 'excited', 'exciting',
              'exotic', 'expensive', 'experienced', 'expert', 'extraneous',
              'extroverted', 'extra-large', 'extra-small', 'fabulous',
              'failing', 'faint', 'fair', 'faithful', 'fake', 'false',
              'familiar', 'famous', 'fancy', 'fantastic', 'far', 'faraway',
              'far-flung', 'far-off', 'fast', 'fat', 'fatal', 'fatherly',
              'favorable', 'favorite', 'fearful', 'fearless', 'feisty',
              'feline', 'female', 'feminine', 'few', 'fickle', 'filthy', 'fine',
              'finished', 'firm', 'first', 'firsthand', 'fitting', 'fixed',
              'flaky', 'flamboyant', 'flashy', 'flat', 'flawed', 'flawless',
              'flickering', 'flimsy', 'flippant', 'flowery', 'fluffy', 'fluid',
              'flustered', 'focused', 'fond', 'foolhardy', 'foolish',
              'forceful', 'forked', 'formal', 'forsaken', 'forthright',
              'fortunate', 'fragrant', 'frail', 'frank', 'frayed', 'free',
              'French', 'fresh', 'frequent', 'friendly', 'frightened',
              'frightening', 'frigid', 'frilly', 'frizzy', 'frivolous', 'front',
              'frosty', 'frozen', 'frugal', 'fruitful', 'full', 'fumbling',
              'functional', 'funny', 'fussy', 'fuzzy', 'gargantuan', 'gaseous',
              'general', 'generous', 'gentle', 'genuine', 'giant', 'giddy',
              'gigantic', 'gifted', 'giving', 'glamorous', 'glaring', 'glass',
              'gleaming', 'gleeful', 'glistening', 'glittering', 'gloomy',
              'glorious', 'glossy', 'glum', 'golden', 'good', 'good-natured',
              'gorgeous', 'graceful', 'gracious', 'grand', 'grandiose',
              'granular', 'grateful', 'grave', 'gray', 'great', 'greedy',
              'green', 'gregarious', 'grim', 'grimy', 'gripping', 'grizzled',
              'gross', 'grotesque', 'grouchy', 'grounded', 'growing',
              'growling', 'grown', 'grubby', 'gruesome', 'grumpy', 'guilty',
              'gullible', 'gummy', 'hairy', 'half', 'handmade', 'handsome',
              'handy', 'happy', 'happy-go-lucky', 'hard', 'hard-to-find',
              'harmful', 'harmless', 'harmonious', 'harsh', 'hasty', 'hateful',
              'haunting', 'healthy', 'heartfelt', 'hearty', 'heavenly', 'heavy',
              'hefty', 'helpful', 'helpless', 'hidden', 'hideous', 'high',
              'high-level', 'hilarious', 'hoarse', 'hollow', 'homely', 'honest',
              'honorable', 'honored', 'hopeful', 'horrible', 'hospitable',
              'hot', 'huge', 'humble', 'humiliating', 'humming', 'humongous',
              'hungry', 'hurtful', 'husky', 'icky', 'icy', 'ideal',
              'idealistic', 'identical', 'idle', 'idiotic', 'idolized',
              'ignorant', 'ill', 'illegal', 'ill-fated', 'ill-informed',
              'illiterate', 'illustrious', 'imaginary', 'imaginative',
              'immaculate', 'immaterial', 'immediate', 'immense', 'impassioned',
              'impeccable', 'impartial', 'imperfect', 'imperturbable', 'impish',
              'impolite', 'important', 'impossible', 'impractical',
              'impressionable', 'impressive', 'improbable', 'impure', 'inborn',
              'incomparable', 'incompatible', 'incomplete', 'inconsequential',
              'incredible', 'indelible', 'inexperienced', 'indolent',
              'infamous', 'infantile', 'infatuated', 'inferior', 'infinite',
              'informal', 'innocent', 'insecure', 'insidious', 'insignificant',
              'insistent', 'instructive', 'insubstantial', 'intelligent',
              'intent', 'intentional', 'interesting', 'internal',
              'international', 'intrepid', 'ironclad', 'irresponsible',
              'irritating', 'itchy', 'jaded', 'jagged', 'jam-packed', 'jaunty',
              'jealous', 'jittery', 'joint', 'jolly', 'jovial', 'joyful',
              'joyous', 'jubilant', 'judicious', 'juicy', 'jumbo', 'junior',
              'jumpy', 'juvenile', 'kaleidoscopic', 'keen', 'key', 'kind',
              'kindhearted', 'kindly', 'klutzy', 'knobby', 'knotty',
              'knowledgeable', 'knowing', 'known', 'kooky', 'kosher', 'lame',
              'lanky', 'large', 'last', 'lasting', 'late', 'lavish', 'lawful',
              'lazy', 'leading', 'lean', 'leafy', 'left', 'legal', 'legitimate',
              'light', 'lighthearted', 'likable', 'likely', 'limited', 'limp',
              'limping', 'linear', 'lined', 'liquid', 'little', 'live',
              'lively', 'livid', 'loathsome', 'lone', 'lonely', 'long',
              'long-term', 'loose', 'lopsided', 'lost', 'loud', 'lovable',
              'lovely', 'loving', 'low', 'loyal', 'lucky', 'lumbering',
              'luminous', 'lumpy', 'lustrous', 'luxurious', 'mad', 'made-up',
              'magnificent', 'majestic', 'major', 'male', 'mammoth', 'married',
              'marvelous', 'masculine', 'massive', 'mature', 'meager', 'mealy',
              'mean', 'measly', 'meaty', 'medical', 'mediocre', 'medium',
              'meek', 'mellow', 'melodic', 'memorable', 'menacing', 'merry',
              'messy', 'metallic', 'mild', 'milky', 'mindless', 'miniature',
              'minor', 'minty', 'miserable', 'miserly', 'misguided', 'misty',
              'mixed', 'modern', 'modest', 'moist', 'monstrous', 'monthly',
              'monumental', 'moral', 'mortified', 'motherly', 'motionless',
              'mountainous', 'muddy', 'muffled', 'multicolored', 'mundane',
              'murky', 'mushy', 'musty', 'muted', 'mysterious', 'naive',
              'narrow', 'nasty', 'natural', 'naughty', 'nautical', 'near',
              'neat', 'necessary', 'needy', 'negative', 'neglected',
              'negligible', 'neighboring', 'nervous', 'new', 'next', 'nice',
              'nifty', 'nimble', 'nippy', 'nocturnal', 'noisy', 'nonstop',
              'normal', 'notable', 'noted', 'noteworthy', 'novel', 'noxious',
              'numb', 'nutritious', 'nutty', 'obedient', 'obese', 'oblong',
              'oily', 'oblong', 'obvious', 'occasional', 'odd', 'oddball',
              'offbeat', 'offensive', 'official', 'old', 'old-fashioned',
              'only', 'open', 'optimal', 'optimistic', 'opulent', 'orange',
              'orderly', 'organic', 'ornate', 'ornery', 'ordinary', 'original',
              'other', 'our', 'outlying', 'outgoing', 'outlandish',
              'outrageous', 'outstanding', 'oval', 'overcooked', 'overdue',
              'overjoyed', 'overlooked', 'palatable', 'pale', 'paltry',
              'parallel', 'parched', 'partial', 'passionate', 'past', 'pastel',
              'peaceful', 'peppery', 'perfect', 'perfumed', 'periodic', 'perky',
              'personal', 'pertinent', 'pesky', 'pessimistic', 'petty', 'phony',
              'physical', 'piercing', 'pink', 'pitiful', 'plain', 'plaintive',
              'plastic', 'playful', 'pleasant', 'pleased', 'pleasing', 'plump',
              'plush', 'polished', 'polite', 'political', 'pointed',
              'pointless', 'poised', 'poor', 'popular', 'portly', 'posh',
              'positive', 'possible', 'potable', 'powerful', 'powerless',
              'practical', 'precious', 'present', 'prestigious', 'pretty',
              'precious', 'previous', 'pricey', 'prickly', 'primary', 'prime',
              'pristine', 'private', 'prize', 'probable', 'productive',
              'profitable', 'profuse', 'proper', 'proud', 'prudent', 'punctual',
              'pungent', 'puny', 'pure', 'purple', 'pushy', 'putrid', 'puzzled',
              'puzzling', 'quaint', 'qualified', 'quarrelsome', 'quarterly',
              'queasy', 'querulous', 'questionable', 'quick', 'quick-witted',
              'quiet', 'quintessential', 'quirky', 'quixotic', 'quizzical',
              'radiant', 'ragged', 'rapid', 'rare', 'rash', 'raw', 'recent',
              'reckless', 'rectangular', 'ready', 'real', 'realistic',
              'reasonable', 'red', 'reflecting', 'regal', 'regular', 'reliable',
              'relieved', 'remarkable', 'remorseful', 'remote', 'repentant',
              'required', 'respectful', 'responsible', 'repulsive', 'revolving',
              'rewarding', 'rich', 'rigid', 'right', 'ringed', 'ripe',
              'roasted', 'robust', 'rosy', 'rotating', 'rotten', 'rough',
              'round', 'rowdy', 'royal', 'rubbery', 'rundown', 'ruddy', 'rude',
              'runny', 'rural', 'rusty', 'sad', 'safe', 'salty', 'same',
              'sandy', 'sane', 'sarcastic', 'sardonic', 'satisfied', 'scaly',
              'scarce', 'scared', 'scary', 'scented', 'scholarly', 'scientific',
              'scornful', 'scratchy', 'scrawny', 'second', 'secondary',
              'second-hand', 'secret', 'self-assured', 'self-reliant',
              'selfish', 'sentimental', 'separate', 'serene', 'serious',
              'serpentine', 'several', 'severe', 'shabby', 'shadowy', 'shady',
              'shallow', 'shameful', 'shameless', 'sharp', 'shimmering',
              'shiny', 'shocked', 'shocking', 'shoddy', 'short', 'short-term',
              'showy', 'shrill', 'shy', 'sick', 'silent', 'silky', 'silly',
              'silver', 'similar', 'simple', 'simplistic', 'sinful', 'single',
              'sizzling', 'skeletal', 'skinny', 'sleepy', 'slight', 'slim',
              'slimy', 'slippery', 'slow', 'slushy', 'small', 'smart', 'smoggy',
              'smooth', 'smug', 'snappy', 'snarling', 'sneaky', 'sniveling',
              'snoopy', 'sociable', 'soft', 'soggy', 'solid', 'somber', 'some',
              'spherical', 'sophisticated', 'sore', 'sorrowful', 'soulful',
              'soupy', 'sour', 'Spanish', 'sparkling', 'sparse', 'specific',
              'spectacular', 'speedy', 'spicy', 'spiffy', 'spirited',
              'spiteful', 'splendid', 'spotless', 'spotted', 'spry', 'square',
              'squeaky', 'squiggly', 'stable', 'staid', 'stained', 'stale',
              'standard', 'starchy', 'stark', 'starry', 'steep', 'sticky',
              'stiff', 'stimulating', 'stingy', 'stormy', 'straight', 'strange',
              'steel', 'strict', 'strident', 'striking', 'striped', 'strong',
              'studious', 'stunning', 'stupendous', 'stupid', 'sturdy',
              'stylish', 'subdued', 'submissive', 'substantial', 'subtle',
              'suburban', 'sudden', 'sugary', 'sunny', 'super', 'superb',
              'superficial', 'superior', 'supportive', 'sure-footed',
              'surprised', 'suspicious', 'svelte', 'sweaty', 'sweet',
              'sweltering', 'swift', 'sympathetic', 'tall', 'talkative', 'tame',
              'tan', 'tangible', 'tart', 'tasty', 'tattered', 'taut', 'tedious',
              'teeming', 'tempting', 'tender', 'tense', 'tepid', 'terrible',
              'terrific', 'testy', 'thankful', 'that', 'these', 'thick', 'thin',
              'third', 'thirsty', 'this', 'thorough', 'thorny', 'those',
              'thoughtful', 'threadbare', 'thrifty', 'thunderous', 'tidy',
              'tight', 'timely', 'tinted', 'tiny', 'tired', 'torn', 'total',
              'tough', 'traumatic', 'treasured', 'tremendous', 'tragic',
              'trained', 'tremendous', 'triangular', 'tricky', 'trifling',
              'trim', 'trivial', 'troubled', 'true', 'trusting', 'trustworthy',
              'trusty', 'truthful', 'tubby', 'turbulent', 'twin', 'ugly',
              'ultimate', 'unacceptable', 'unaware', 'uncomfortable',
              'uncommon', 'unconscious', 'understated', 'unequaled', 'uneven',
              'unfinished', 'unfit', 'unfolded', 'unfortunate', 'unhappy',
              'unhealthy', 'uniform', 'unimportant', 'unique', 'united',
              'unkempt', 'unknown', 'unlawful', 'unlined', 'unlucky',
              'unnatural', 'unpleasant', 'unrealistic', 'unripe', 'unruly',
              'unselfish', 'unsightly', 'unsteady', 'unsung', 'untidy',
              'untimely', 'untried', 'untrue', 'unused', 'unusual', 'unwelcome',
              'unwieldy', 'unwilling', 'unwitting', 'unwritten', 'upbeat',
              'upright', 'upset', 'urban', 'usable', 'used', 'useful',
              'useless', 'utilized', 'utter', 'vacant', 'vague', 'vain',
              'valid', 'valuable', 'vapid', 'variable', 'vast', 'velvety',
              'venerated', 'vengeful', 'verifiable', 'vibrant', 'vicious',
              'victorious', 'vigilant', 'vigorous', 'villainous', 'violet',
              'violent', 'virtual', 'virtuous', 'visible', 'vital', 'vivacious',
              'vivid', 'voluminous', 'wan', 'warlike', 'warm', 'warmhearted',
              'warped', 'wary', 'wasteful', 'watchful', 'waterlogged', 'watery',
              'wavy', 'wealthy', 'weak', 'weary', 'webbed', 'wee', 'weekly',
              'weepy', 'weighty', 'weird', 'welcome', 'well-documented',
              'well-groomed', 'well-informed', 'well-lit', 'well-made',
              'well-off', 'well-to-do', 'well-worn', 'wet', 'which',
              'whimsical', 'whirlwind', 'whispered', 'white', 'whole',
              'whopping', 'wicked', 'wide', 'wide-eyed', 'wiggly', 'wild',
              'willing', 'wilted', 'winding', 'windy', 'winged', 'wiry', 'wise',
              'witty', 'wobbly', 'woeful', 'wonderful', 'wooden', 'woozy',
              'wordy', 'worldly', 'worn', 'worried', 'worrisome', 'worse',
              'worst', 'worthless', 'worthwhile', 'worthy', 'wrathful',
              'wretched', 'writhing', 'wrong', 'wry', 'yawning', 'yearly',
              'yellow', 'yellowish', 'young', 'youthful', 'yummy', 'zany',
              'zealous', 'zesty', 'zigzag']


def get_random_name():
    return "%s%s%s" % (
        random.choice(ADJECTIVES),
        random.choice(ANIMALS).replace(" ", "_"),
        random.randint(10, 99),
    )
