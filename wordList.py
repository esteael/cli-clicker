# program words
programming_words = [
    "python", "javascript", "coding", "algorithm", "variable",
    "function", "class", "module", "library", "framework",
    "database", "server", "client", "debug", "compiler",
    "syntax", "runtime", "object", "method", "parameter"
]

# hardware words
hardware_words = [
    "computer", "keyboard", "monitor", "mouse", "processor",
    "memory", "storage", "graphics", "network", "router",
    "motherboard", "peripheral", "battery", "display", "camera",
    "speaker", "microphone", "hardware", "circuit", "device"
]

# internet words
internet_words = [
    "browser", "website", "internet", "online", "download",
    "upload", "streaming", "cloud", "server", "domain",
    "bandwidth", "protocol", "encryption", "firewall", "cookie",
    "cache", "router", "wireless", "ethernet", "connection"
]

# gaming words
gaming_words = [
    "player", "level", "score", "achievement", "character",
    "quest", "mission", "strategy", "victory", "defeat",
    "controller", "console", "screen", "graphics", "avatar",
    "inventory", "power", "skill", "multiplayer", "boss"
]

# pokemon (first gen only 20)
pokemon_words = [
    "bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon",
    "charizard", "squirtle", "wartortle", "blastoise", "caterpie",
    "metapod", "butterfree", "weedle", "kakuna", "beedrill",
    "pidgey", "pidgeotto", "pidgeot", "rattata", "raticate"
]

# popular pokemon
more_pokemon = [
    "pikachu", "eevee", "jigglypuff", "mewtwo", "mew",
    "lugia", "tyranitar", "blaziken", "gardevoir", "lucario",
    "garchomp", "zoroark", "greninja", "sylveon", "mimikyu",
    "charizard", "gengar", "dragonite", "snorlax", "gyarados"
]

# anime heroes
anime_heroes = [
    "goku", "naruto", "luffy", "ichigo", "eren",
    "tanjiro", "deku", "light", "edward", "saitama",
    "inuyasha", "vegeta", "sasuke", "zoro", "hinata",
    "mikasa", "sakura", "killua", "lelouch", "kirito"
]

# anime villains
anime_villains = [
    "frieza", "madara", "aizen", "dio", "meruem",
    "toguro", "pain", "kira", "majin", "garou",
    "cell", "orochimaru", "all", "titan", "hisoka",
    "doflamingo", "muzan", "griffith", "blackbeard", "accelerator"
]

# food items
food_words = [
    "pizza", "burger", "pasta", "sushi", "taco",
    "curry", "sandwich", "salad", "noodles", "steak",
    "chocolate", "pancake", "waffle", "donut", "cookie",
    "burrito", "ramen", "cupcake", "croissant", "muffin"
]

# countries
country_words = [
    "japan", "canada", "brazil", "france", "australia",
    "egypt", "mexico", "germany", "india", "italy",
    "china", "spain", "russia", "thailand", "greece",
    "sweden", "kenya", "argentina", "iceland", "singapore"
]

# mythical creatures
mythical_words = [
    "dragon", "phoenix", "unicorn", "griffin", "mermaid",
    "centaur", "werewolf", "vampire", "zombie", "fairy",
    "goblin", "troll", "ogre", "sphinx", "kraken",
    "chimera", "minotaur", "siren", "harpy", "cyclops"
]

# list balancing
max_list_size = max(len(programming_words), len(hardware_words), 
                    len(internet_words), len(gaming_words), 
                    len(pokemon_words), len(more_pokemon),
                    len(anime_heroes), len(anime_villains),
                    len(food_words), len(country_words),
                    len(mythical_words))

# combine all the words into one list
all_words = programming_words + hardware_words + internet_words + gaming_words + \
            pokemon_words + more_pokemon + anime_heroes + anime_villains + \
            food_words + country_words + mythical_words

# dictionary of categories, never ended up using this lmao
categories = {
    "programming": programming_words,
    "hardware": hardware_words,
    "internet": internet_words,
    "gaming": gaming_words,
    "pokemon": pokemon_words + more_pokemon,
    "anime_heroes": anime_heroes,
    "anime_villains": anime_villains,
    "food": food_words,
    "countries": country_words,
    "mythical": mythical_words,
    "all": all_words
}