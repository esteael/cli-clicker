# Item effects:
# - points_per_second, self explanatory
# - points_per_character: self explanatory
# - next_words_seen: self explanatory
# - multiplier: multiplies points per second by this value

shop_items = [
    {
        "id": 1,
        "name": "auto clicker",
        "description": "get passive point per second",
        "cost": 50,
        "effects": {
            "points_per_second": 1,
            "points_per_character": 0,
            "next_words_seen": 0,
            "multiplier": 0
        }
    },
    {
        "id": 2,
        "name": "mechanic keyboard",
        "description": "earn an extra point per character typed",
        "cost": 100,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 1,
            "next_words_seen": 0,
            "multiplier": 0
        }
    },
    {
        "id": 3,
        "name": "glasses",
        "description": "see the following word",
        "cost": 125,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 0,
            "next_words_seen": 1,
            "multiplier": 0
        }
    },
    {
        "id": 4,
        "name": "another auto clicker",
        "description": "earn 5 points per second",
        "cost": 200,
        "effects": {
            "points_per_second": 5,
            "points_per_character": 0,
            "next_words_seen": 0,
            "multiplier": 0
        }
    },
    {
        "id": 5,
        "name": "killstreak",
        "description": "multiply your passive point gain by 1.5x",
        "cost": 500,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 0,
            "next_words_seen": 0,
            "multiplier": 0.5
        }
    },
    {
        "id": 6,
        "name": "gaming keyboard",
        "description": "earn an extra point per character typed",
        "cost": 600,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 3,
            "next_words_seen": 0,
            "multiplier": 0
        }
    },
    {
        "id": 7,
        "name": "wallhacks",
        "description": "see 2 of the following words",
        "cost": 750,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 0,
            "next_words_seen": 1,
            "multiplier": 0
        }
    },
    {
        "id": 8,
        "name": "farmbot",
        "description": "earn 15 points per second",
        "cost": 1200,
        "effects": {
            "points_per_second": 15,
            "points_per_character": 0,
            "next_words_seen": 0,
            "multiplier": 0
        }
    },
    {
        "id": 9,
        "name": "spawn camping",
        "description": "multiplies points per second by 2x",
        "cost": 1800,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 0,
            "next_words_seen": 0,
            "multiplier": 1.0
        }
    },
    {
        "id": 10,
        "name": "telekenisis typing",
        "description": "earn 5 points per character typed",
        "cost": 1500,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 5,
            "next_words_seen": 0,
            "multiplier": 0
        }
    },
    {
        "id": 11,
        "name": "artificial intelligence",
        "description": "see 3 words coming up",
        "cost": 2000,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 0,
            "next_words_seen": 1,
            "multiplier": 0
        }
    },
    {
        "id": 12,
        "name": "NUKE",
        "description": "multiplies points per second by 3x",
        "cost": 3500,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 0,
            "next_words_seen": 0,
            "multiplier": 2.0
        }
    },
    {
        "id": 13,
        "name": "phone a friend",
        "description": "automatically earns 30 points per second",
        "cost": 3000,
        "effects": {
            "points_per_second": 30,
            "points_per_character": 0,
            "next_words_seen": 0,
            "multiplier": 0
        }
    },
    {
        "id": 14,
        "name": "words per minute course",
        "description": "earn 10 points per character typed",
        "cost": 4000,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 10,
            "next_words_seen": 0,
            "multiplier": 0
        }
    },
    {
        "id": 15,
        "name": "omniscience",
        "description": "see 4 words coming up",
        "cost": 5000,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 0,
            "next_words_seen": 1,
            "multiplier": 0
        }
    },
    {
        "id": 16,
        "name": "BECOME THE PROFESSOR",
        "description": "multiplies points per second by 5x",
        "cost": 8000,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 0,
            "next_words_seen": 0,
            "multiplier": 4.0
        }
    },
    {
        "id": 17,
        "name": "bitcoin miner",
        "description": "earns 100 points per second",
        "cost": 10000,
        "effects": {
            "points_per_second": 100,
            "points_per_character": 0,
            "next_words_seen": 0,
            "multiplier": 0
        }
    },
    {
        "id": 18,
        "name": "typing champion for hire",
        "description": "Earn +25 points per character typed",
        "cost": 15000,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 25,
            "next_words_seen": 0,
            "multiplier": 0
        }
    },
    {
        "id": 19,
        "name": "BECOME THE DEAN",
        "description": "multiplies points per second by 10x",
        "cost": 25000,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 0,
            "next_words_seen": 0,
            "multiplier": 9.0
        }
    },
    {
        "id": 20,
        "name": "THE ALL KNOWNING",
        "description": "see 5 words coming up",
        "cost": 20000,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 0,
            "next_words_seen": 1,
            "multiplier": 0
        }
    },
    {
        "id": 21,
        "name": "quantom tunnel typing",
        "description": "Automatically earns 500 points per second",
        "cost": 50000,
        "effects": {
            "points_per_second": 500,
            "points_per_character": 0,
            "next_words_seen": 0,
            "multiplier": 0
        }
    },
    {
        "id": 22,
        "name": "ITS OVER 9000!!",
        "description": "multiplies points per second by 100x",
        "cost": 100000,
        "effects": {
            "points_per_second": 0,
            "points_per_character": 0,
            "next_words_seen": 0,
            "multiplier": 99.0
        }
    },
        {
        "id": 23,
        "name": "STOP PLAYING THE GAME.",
        "description": "IM BEGGING YOU. PLEASE STOP.",
        "cost": 1000000000,
        "effects": {
            "points_per_second": 999999,
            "points_per_character": 999999,
            "next_words_seen": 0,
            "multiplier": 9999.0
        }
    }
]

# function to get item by ID
def get_item_by_id(item_id):
    for item in shop_items:
        if item["id"] == item_id:
            return item
    return None