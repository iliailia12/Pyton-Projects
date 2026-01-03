help_messige = """
Welcome to Ilias store! 🎉 Ready to find something special? We’ve got amazing deals just for you! Whether you're looking for the latest trends or a unique gift, we’ve got everything you need. Explore our collection today and enjoy exclusive offers – only at Ilias store. How can we help you get started?

hello this is help messige 
        if you wryte help this messige will be appear 
        also  we have sections  electronics_sect , clothing_sect , shoes_sect , kitchen_sect , skincare_sect ,  home_decor_sect , bathroom_sect ,sports_fitness_sect , accessories_sect ,kids_items_sect , toys_sect , stationery_sect , cleaning_products_sect , office_supplies_sect ,  bags_backpacks_sect , lighting_sect , furniture_small_sect , pet_supplies_sect  ,garden_items_sect , automotive_accessories_sect 
        
        if you wryte one of them the section will appear but not all of them because your Budget i hope this is ockey  for exemple  if your Budget is 100$
        and you type electronics_sect the items will appear Exactly 100$ or lower like 60$ 50$ or any price if its under 100$ or 100$ if you want View whole sect just type wholesect 
"""

command = ""

electronics_sect = {
    "computer": {"name": "Computer", "price": 1000.00, "stock": 10},
    "laptop": {"name": "Laptop", "price": 1200.00, "stock": 8},
    "mobile_phone": {"name": "Mobile Phone", "price": 900.00, "stock": 15},
    "tablet": {"name": "Tablet", "price": 600.00, "stock": 12},
    "washing_machine": {"name": "Washing Machine", "price": 700.00, "stock": 5},
    "microwave": {"name": "Microwave", "price": 250.00, "stock": 7},
    "refrigerator": {"name": "Refrigerator", "price": 1100.00, "stock": 4},
    "television": {"name": "Smart TV", "price": 1000.00, "stock": 6},
    "microphone": {"name": "Microphone", "price": 120.00, "stock": 20},
    "wireless_headphones": {"name": "Wireless Headphones", "price": 180.00, "stock": 18},
    "bluetooth_earbuds": {"name": "Bluetooth Earbuds", "price": 90.00, "stock": 30},
    "bluetooth_speaker": {"name": "Bluetooth Speaker", "price": 50.00, "stock": 25},
    "smartwatch": {"name": "Smartwatch", "price": 220.00, "stock": 14},
    "keyboard": {"name": "Keyboard", "price": 45.00, "stock": 40},
    "mouse": {"name": "Mouse", "price": 30.00, "stock": 50},
    "printer": {"name": "Printer", "price": 300.00, "stock": 9},
    "scanner": {"name": "Scanner", "price": 280.00, "stock": 6},
    "webcam": {"name": "Webcam", "price": 85.00, "stock": 22},
    "router": {"name": "Wi-Fi Router", "price": 150.00, "stock": 17},
    "power_bank": {"name": "Power Bank", "price": 60.00, "stock": 35}
}


clothing_sect = {
    "t_shirt": {"name": "T-Shirt", "price": 25.00, "stock": 50},
    "jeans": {"name": "Jeans", "price": 60.00, "stock": 30},
    "jacket": {"name": "Jacket", "price": 120.00, "stock": 15},
    "hoodie": {"name": "Hoodie", "price": 70.00, "stock": 25},
    "sweater": {"name": "Sweater", "price": 55.00, "stock": 20},
    "shorts": {"name": "Shorts", "price": 35.00, "stock": 40},
    "dress": {"name": "Dress", "price": 90.00, "stock": 18},
    "skirt": {"name": "Skirt", "price": 45.00, "stock": 22},
    "socks": {"name": "Socks", "price": 10.00, "stock": 100},
    "cap": {"name": "Cap", "price": 20.00, "stock": 60},

    "coat": {"name": "Coat", "price": 150.00, "stock": 12},
    "shirt": {"name": "Shirt", "price": 50.00, "stock": 28},
    "tracksuit": {"name": "Tracksuit", "price": 95.00, "stock": 16},
    "polo": {"name": "Polo Shirt", "price": 40.00, "stock": 35},
    "vest": {"name": "Vest", "price": 30.00, "stock": 27},
    "cardigan": {"name": "Cardigan", "price": 65.00, "stock": 19},
    "leggings": {"name": "Leggings", "price": 30.00, "stock": 45},
    "belt": {"name": "Belt", "price": 18.00, "stock": 70},
    "scarf": {"name": "Scarf", "price": 22.00, "stock": 55},
    "gloves": {"name": "Gloves", "price": 25.00, "stock": 33}
}


kitchen_sect = {
    "frying_pan": {"name": "Frying Pan", "price": 40.00, "stock": 25},
    "cooking_pot": {"name": "Cooking Pot", "price": 55.00, "stock": 20},
    "knife_set": {"name": "Knife Set", "price": 70.00, "stock": 15},
    "cutting_board": {"name": "Cutting Board", "price": 18.00, "stock": 40},
    "plate_set": {"name": "Plate Set", "price": 60.00, "stock": 18},
    "glass_set": {"name": "Glass Set", "price": 35.00, "stock": 30},
    "spoon_set": {"name": "Spoon Set", "price": 25.00, "stock": 35},
    "kettle": {"name": "Electric Kettle", "price": 45.00, "stock": 22},
    "blender": {"name": "Blender", "price": 90.00, "stock": 12},
    "toaster": {"name": "Toaster", "price": 50.00, "stock": 16},
    "rice_cooker": {"name": "Rice Cooker", "price": 85.00, "stock": 10},
    "coffee_maker": {"name": "Coffee Maker", "price": 110.00, "stock": 9},
    "measuring_cups": {"name": "Measuring Cups", "price": 15.00, "stock": 45},
    "food_container": {"name": "Food Container Set", "price": 28.00, "stock": 32},
    "dish_rack": {"name": "Dish Rack", "price": 30.00, "stock": 20},

    "pressure_cooker": {"name": "Pressure Cooker", "price": 130.00, "stock": 8},
    "air_fryer": {"name": "Air Fryer", "price": 160.00, "stock": 11},
    "grater": {"name": "Grater", "price": 12.00, "stock": 50},
    "peeler": {"name": "Vegetable Peeler", "price": 8.00, "stock": 60},
    "mixing_bowl": {"name": "Mixing Bowl Set", "price": 26.00, "stock": 28},
    "rolling_pin": {"name": "Rolling Pin", "price": 14.00, "stock": 34},
    "baking_tray": {"name": "Baking Tray", "price": 22.00, "stock": 27},
    "spatula": {"name": "Spatula", "price": 10.00, "stock": 55},
    "ladle": {"name": "Ladle", "price": 9.00, "stock": 48},
    "dish_towel": {"name": "Dish Towel Set", "price": 16.00, "stock": 40}
}


shoes_sect = {
    "sneakers": {"name": "Sneakers", "price": 80.00, "stock": 25},
    "running_shoes": {"name": "Running Shoes", "price": 90.00, "stock": 20},
    "boots": {"name": "Boots", "price": 120.00, "stock": 15},
    "sandals": {"name": "Sandals", "price": 50.00, "stock": 30},
    "flip_flops": {"name": "Flip Flops", "price": 20.00, "stock": 40},
    "loafers": {"name": "Loafers", "price": 70.00, "stock": 18},
    "heels": {"name": "Heels", "price": 85.00, "stock": 12},
    "slippers": {"name": "Slippers", "price": 25.00, "stock": 35},
    "trail_shoes": {"name": "Trail Shoes", "price": 100.00, "stock": 14},
    "formal_shoes": {"name": "Formal Shoes", "price": 95.00, "stock": 16},

    "hiking_boots": {"name": "Hiking Boots", "price": 130.00, "stock": 10},
    "espadrilles": {"name": "Espadrilles", "price": 45.00, "stock": 22},
    "basketball_shoes": {"name": "Basketball Shoes", "price": 110.00, "stock": 12},
    "cycling_shoes": {"name": "Cycling Shoes", "price": 100.00, "stock": 8},
    "clogs": {"name": "Clogs", "price": 55.00, "stock": 18},
    "moccasins": {"name": "Moccasins", "price": 65.00, "stock": 15},
    "oxfords": {"name": "Oxfords", "price": 90.00, "stock": 14},
    "trail_runners": {"name": "Trail Runners", "price": 105.00, "stock": 10},
    "water_shoes": {"name": "Water Shoes", "price": 40.00, "stock": 20},
    "platform_shoes": {"name": "Platform Shoes", "price": 95.00, "stock": 12}
}


skincare_sect = {
    "cleanser": {"name": "Facial Cleanser", "price": 25.00, "stock": 40},
    "moisturizer": {"name": "Moisturizer Cream", "price": 35.00, "stock": 35},
    "sunscreen": {"name": "Sunscreen SPF50", "price": 30.00, "stock": 30},
    "serum": {"name": "Vitamin C Serum", "price": 45.00, "stock": 25},
    "eye_cream": {"name": "Eye Cream", "price": 40.00, "stock": 20},
    "face_mask": {"name": "Face Mask", "price": 15.00, "stock": 50},
    "toner": {"name": "Toner", "price": 28.00, "stock": 32},
    "exfoliator": {"name": "Exfoliating Scrub", "price": 22.00, "stock": 30},
    "lip_balm": {"name": "Lip Balm", "price": 10.00, "stock": 60},
    "body_lotion": {"name": "Body Lotion", "price": 35.00, "stock": 25},

    "facial_oil": {"name": "Facial Oil", "price": 50.00, "stock": 18},
    "makeup_remover": {"name": "Makeup Remover", "price": 20.00, "stock": 40},
    "hand_cream": {"name": "Hand Cream", "price": 15.00, "stock": 45},
    "shampoo": {"name": "Shampoo", "price": 25.00, "stock": 35},
    "conditioner": {"name": "Conditioner", "price": 25.00, "stock": 35},
    "body_scrub": {"name": "Body Scrub", "price": 30.00, "stock": 28},
    "face_mist": {"name": "Face Mist", "price": 18.00, "stock": 32},
    "night_cream": {"name": "Night Cream", "price": 45.00, "stock": 22},
    "foundation": {"name": "Foundation", "price": 40.00, "stock": 30},
    "blush": {"name": "Blush", "price": 20.00, "stock": 25},

    "concealer": {"name": "Concealer", "price": 22.00, "stock": 28},
    "eyeshadow": {"name": "Eyeshadow Palette", "price": 35.00, "stock": 20},
    "mascara": {"name": "Mascara", "price": 18.00, "stock": 30},
    "eyeliner": {"name": "Eyeliner", "price": 15.00, "stock": 32},
    "nail_polish": {"name": "Nail Polish", "price": 12.00, "stock": 40},
    "perfume": {"name": "Perfume", "price": 60.00, "stock": 15},
    "body_spray": {"name": "Body Spray", "price": 25.00, "stock": 35},
    "hair_mask": {"name": "Hair Mask", "price": 28.00, "stock": 20},
    "face_serum": {"name": "Hyaluronic Serum", "price": 50.00, "stock": 18},
    "bb_cream": {"name": "BB Cream", "price": 30.00, "stock": 25}
}


home_decor_sect = {
    "vase": {"name": "Decorative Vase", "price": 30.00, "stock": 20},
    "wall_art": {"name": "Wall Art Frame", "price": 50.00, "stock": 15},
    "candle_set": {"name": "Candle Set", "price": 25.00, "stock": 30},
    "photo_frame": {"name": "Photo Frame", "price": 20.00, "stock": 40},
    "throw_pillow": {"name": "Throw Pillow", "price": 18.00, "stock": 35},
    "rug": {"name": "Area Rug", "price": 80.00, "stock": 10},
    "table_lamp": {"name": "Table Lamp", "price": 45.00, "stock": 22},
    "wall_clock": {"name": "Wall Clock", "price": 35.00, "stock": 18},
    "mirror": {"name": "Decorative Mirror", "price": 60.00, "stock": 12},
    "planter": {"name": "Indoor Plant Pot", "price": 25.00, "stock": 30},

    "curtains": {"name": "Curtains", "price": 55.00, "stock": 15},
    "shelf": {"name": "Decorative Shelf", "price": 70.00, "stock": 10},
    "coasters": {"name": "Coaster Set", "price": 12.00, "stock": 40},
    "table_runner": {"name": "Table Runner", "price": 22.00, "stock": 25},
    "wall_shelves": {"name": "Wall Shelves", "price": 60.00, "stock": 12},
    "ottoman": {"name": "Ottoman", "price": 90.00, "stock": 8},
    "decorative_bowl": {"name": "Decorative Bowl", "price": 28.00, "stock": 20},
    "cushion_cover": {"name": "Cushion Cover", "price": 15.00, "stock": 35},
    "lamp_shade": {"name": "Lamp Shade", "price": 20.00, "stock": 22},
    "wall_decal": {"name": "Wall Decal Sticker", "price": 18.00, "stock": 30}
}


bathroom_sect = {
    "towel_set": {"name": "Towel Set", "price": 30.00, "stock": 25},
    "bath_mat": {"name": "Bath Mat", "price": 20.00, "stock": 30},
    "shower_curtain": {"name": "Shower Curtain", "price": 25.00, "stock": 20},
    "toothbrush_holder": {"name": "Toothbrush Holder", "price": 12.00, "stock": 35},
    "soap_dispenser": {"name": "Soap Dispenser", "price": 15.00, "stock": 40},
    "bath_robe": {"name": "Bath Robe", "price": 45.00, "stock": 18},
    "mirror": {"name": "Bathroom Mirror", "price": 50.00, "stock": 10},
    "shampoo_holder": {"name": "Shampoo & Soap Holder", "price": 18.00, "stock": 25},
    "toilet_brush": {"name": "Toilet Brush Set", "price": 12.00, "stock": 30},
    "waste_bin": {"name": "Bathroom Waste Bin", "price": 20.00, "stock": 20},

    "loofah": {"name": "Loofah Sponge", "price": 8.00, "stock": 50},
    "bath_towel_large": {"name": "Large Bath Towel", "price": 18.00, "stock": 35},
    "hand_towel": {"name": "Hand Towel", "price": 10.00, "stock": 40},
    "face_towel": {"name": "Face Towel", "price": 8.00, "stock": 45},
    "bath_salt": {"name": "Bath Salt", "price": 15.00, "stock": 25},
    "shower_cap": {"name": "Shower Cap", "price": 5.00, "stock": 60},
    "toothpaste": {"name": "Toothpaste", "price": 6.00, "stock": 50},
    "mouthwash": {"name": "Mouthwash", "price": 12.00, "stock": 30},
    "hair_brush": {"name": "Hair Brush", "price": 10.00, "stock": 40},
    "bathroom_rug": {"name": "Bathroom Rug", "price": 25.00, "stock": 22},

    "body_wash": {"name": "Body Wash", "price": 12.00, "stock": 35},
    "shaving_cream": {"name": "Shaving Cream", "price": 10.00, "stock": 30},
    "razor": {"name": "Razor", "price": 15.00, "stock": 25},
    "facial_wipes": {"name": "Facial Wipes", "price": 8.00, "stock": 40},
    "cotton_balls": {"name": "Cotton Balls", "price": 5.00, "stock": 60},
    "q_tips": {"name": "Q-tips", "price": 4.00, "stock": 70},
    "bath_sponges": {"name": "Bath Sponges", "price": 7.00, "stock": 50},
    "hair_towel_wrap": {"name": "Hair Towel Wrap", "price": 12.00, "stock": 30},
    "toilet_paper": {"name": "Toilet Paper Pack", "price": 8.00, "stock": 80},
    "soap_bar_set": {"name": "Soap Bar Set", "price": 10.00, "stock": 40}
}


sports_fitness_sect = {
    "yoga_mat": {"name": "Yoga Mat", "price": 25.00, "stock": 30},
    "dumbbells_set": {"name": "Dumbbells Set", "price": 50.00, "stock": 20},
    "treadmill": {"name": "Treadmill", "price": 400.00, "stock": 5},
    "resistance_bands": {"name": "Resistance Bands", "price": 15.00, "stock": 40},
    "kettlebell": {"name": "Kettlebell", "price": 35.00, "stock": 15},
    "jump_rope": {"name": "Jump Rope", "price": 10.00, "stock": 50},
    "exercise_ball": {"name": "Exercise Ball", "price": 30.00, "stock": 20},
    "pull_up_bar": {"name": "Pull-Up Bar", "price": 40.00, "stock": 12},
    "fitness_tracker": {"name": "Fitness Tracker", "price": 60.00, "stock": 18},
    "water_bottle": {"name": "Sports Water Bottle", "price": 12.00, "stock": 50},

    "gym_bag": {"name": "Gym Bag", "price": 35.00, "stock": 25},
    "running_shoes": {"name": "Running Shoes", "price": 90.00, "stock": 20},
    "sports_gloves": {"name": "Sports Gloves", "price": 20.00, "stock": 30},
    "foam_roller": {"name": "Foam Roller", "price": 25.00, "stock": 15},
    "yoga_block": {"name": "Yoga Block", "price": 10.00, "stock": 35},
    "exercise_bike": {"name": "Exercise Bike", "price": 300.00, "stock": 4},
    "treadmill_accessory": {"name": "Treadmill Mat", "price": 25.00, "stock": 10},
    "protein_shaker": {"name": "Protein Shaker", "price": 12.00, "stock": 40},
    "ab_wheel": {"name": "Ab Wheel", "price": 15.00, "stock": 20},
    "resistance_tube": {"name": "Resistance Tube", "price": 18.00, "stock": 30},

    "medicine_ball": {"name": "Medicine Ball", "price": 35.00, "stock": 15},
    "pull_up_assist_band": {"name": "Pull-Up Assist Band", "price": 20.00, "stock": 25},
    "yoga_strap": {"name": "Yoga Strap", "price": 10.00, "stock": 40},
    "balance_board": {"name": "Balance Board", "price": 45.00, "stock": 10},
    "speed_ladder": {"name": "Speed Ladder", "price": 25.00, "stock": 20},
    "jump_box": {"name": "Jump Box", "price": 60.00, "stock": 8},
    "push_up_bars": {"name": "Push-Up Bars", "price": 18.00, "stock": 30},
    "exercise_ring": {"name": "Pilates Ring", "price": 22.00, "stock": 25},
    "resistance_ball": {"name": "Resistance Ball", "price": 28.00, "stock": 20},
    "cycling_gloves": {"name": "Cycling Gloves", "price": 15.00, "stock": 35}
}


accessories_sect = {
    "watch": {"name": "Wrist Watch", "price": 80.00, "stock": 25},
    "sunglasses": {"name": "Sunglasses", "price": 50.00, "stock": 30},
    "belt": {"name": "Leather Belt", "price": 35.00, "stock": 40},
    "hat": {"name": "Cap / Hat", "price": 20.00, "stock": 35},
    "wallet": {"name": "Wallet", "price": 40.00, "stock": 25},
    "scarf": {"name": "Scarf", "price": 25.00, "stock": 30},
    "bracelet": {"name": "Bracelet", "price": 15.00, "stock": 50},
    "necklace": {"name": "Necklace", "price": 45.00, "stock": 20},
    "earrings": {"name": "Earrings", "price": 30.00, "stock": 35},
    "keychain": {"name": "Keychain", "price": 10.00, "stock": 60},

    "backpack": {"name": "Backpack", "price": 60.00, "stock": 20},
    "handbag": {"name": "Handbag", "price": 70.00, "stock": 15},
    "phone_case": {"name": "Phone Case", "price": 15.00, "stock": 40},
    "socks": {"name": "Socks", "price": 8.00, "stock": 50},
    "gloves": {"name": "Gloves", "price": 18.00, "stock": 30},
    "watch_band": {"name": "Watch Band", "price": 25.00, "stock": 20},
    "hair_band": {"name": "Hair Band", "price": 12.00, "stock": 40},
    "anklet": {"name": "Anklet", "price": 15.00, "stock": 25},
    "ring": {"name": "Ring", "price": 35.00, "stock": 20},
    "brooch": {"name": "Brooch", "price": 20.00, "stock": 30},

    "pocket_square": {"name": "Pocket Square", "price": 12.00, "stock": 25},
    "cufflinks": {"name": "Cufflinks", "price": 30.00, "stock": 15},
    "hair_clip": {"name": "Hair Clip", "price": 8.00, "stock": 40},
    "beanie": {"name": "Beanie", "price": 18.00, "stock": 30},
    "sun_hat": {"name": "Sun Hat", "price": 22.00, "stock": 20},
    "tie": {"name": "Tie", "price": 20.00, "stock": 25},
    "key_holder": {"name": "Key Holder", "price": 10.00, "stock": 35},
    "luggage_tag": {"name": "Luggage Tag", "price": 15.00, "stock": 20},
    "sunglass_case": {"name": "Sunglasses Case", "price": 12.00, "stock": 30},
    "bracelet_watch_combo": {"name": "Bracelet & Watch Combo", "price": 65.00, "stock": 15}
}


kids_items_sect = {
    "teddy_bear": {"name": "Teddy Bear", "price": 20.00, "stock": 40},
    "lego_set": {"name": "LEGO Set", "price": 50.00, "stock": 25},
    "toy_car": {"name": "Toy Car", "price": 15.00, "stock": 50},
    "doll": {"name": "Doll", "price": 25.00, "stock": 30},
    "puzzle": {"name": "Puzzle", "price": 12.00, "stock": 40},
    "crayons": {"name": "Crayon Set", "price": 10.00, "stock": 60},
    "story_book": {"name": "Story Book", "price": 15.00, "stock": 50},
    "board_game": {"name": "Board Game", "price": 35.00, "stock": 20},
    "action_figure": {"name": "Action Figure", "price": 20.00, "stock": 30},
    "play_dough": {"name": "Play Dough Set", "price": 18.00, "stock": 40},

    "water_color_set": {"name": "Water Color Set", "price": 12.00, "stock": 50},
    "building_blocks": {"name": "Building Blocks", "price": 25.00, "stock": 30},
    "tricycle": {"name": "Tricycle", "price": 60.00, "stock": 10},
    "scooter": {"name": "Scooter", "price": 70.00, "stock": 12},
    "jump_rope_kids": {"name": "Kids Jump Rope", "price": 10.00, "stock": 40},
    "toy_train": {"name": "Toy Train Set", "price": 30.00, "stock": 20},
    "stuffed_animal": {"name": "Stuffed Animal", "price": 20.00, "stock": 35},
    "kids_table": {"name": "Kids Activity Table", "price": 50.00, "stock": 15},
    "chalk_set": {"name": "Chalk Set", "price": 8.00, "stock": 60},
    "drawing_pad": {"name": "Drawing Pad", "price": 10.00, "stock": 50}
}


toys_sect = {
    "teddy_bear": {"name": "Teddy Bear", "price": 20.00, "stock": 40},
    "lego_set": {"name": "LEGO Set", "price": 50.00, "stock": 25},
    "toy_car": {"name": "Toy Car", "price": 15.00, "stock": 50},
    "doll": {"name": "Doll", "price": 25.00, "stock": 30},
    "puzzle": {"name": "Puzzle", "price": 12.00, "stock": 40},
    "crayons": {"name": "Crayon Set", "price": 10.00, "stock": 60},
    "story_book": {"name": "Story Book", "price": 15.00, "stock": 50},
    "board_game": {"name": "Board Game", "price": 35.00, "stock": 20},
    "action_figure": {"name": "Action Figure", "price": 20.00, "stock": 30},
    "play_dough": {"name": "Play Dough Set", "price": 18.00, "stock": 40},

    "water_color_set": {"name": "Water Color Set", "price": 12.00, "stock": 50},
    "building_blocks": {"name": "Building Blocks", "price": 25.00, "stock": 30},
    "tricycle": {"name": "Tricycle", "price": 60.00, "stock": 10},
    "scooter": {"name": "Scooter", "price": 70.00, "stock": 12},
    "jump_rope_kids": {"name": "Kids Jump Rope", "price": 10.00, "stock": 40},
    "toy_train": {"name": "Toy Train Set", "price": 30.00, "stock": 20},
    "stuffed_animal": {"name": "Stuffed Animal", "price": 20.00, "stock": 35},
    "kids_table": {"name": "Kids Activity Table", "price": 50.00, "stock": 15},
    "chalk_set": {"name": "Chalk Set", "price": 8.00, "stock": 60},
    "drawing_pad": {"name": "Drawing Pad", "price": 10.00, "stock": 50},

    "rc_car": {"name": "Remote Control Car", "price": 40.00, "stock": 25},
    "drone": {"name": "Mini Drone", "price": 60.00, "stock": 15},
    "lego_city": {"name": "LEGO City Set", "price": 55.00, "stock": 20},
    "barbie_doll": {"name": "Barbie Doll", "price": 25.00, "stock": 30},
    "board_game_classic": {"name": "Classic Board Game", "price": 35.00, "stock": 20},
    "puzzle_3d": {"name": "3D Puzzle", "price": 30.00, "stock": 25},
    "stuffed_bear": {"name": "Giant Teddy Bear", "price": 45.00, "stock": 15},
    "play_kitchen": {"name": "Play Kitchen Set", "price": 70.00, "stock": 10},
    "marble_run": {"name": "Marble Run Set", "price": 40.00, "stock": 20},
    "action_figure_set": {"name": "Action Figure Set", "price": 30.00, "stock": 25},

    "toy_robot": {"name": "Toy Robot", "price": 45.00, "stock": 20},
    "water_gun": {"name": "Water Gun", "price": 15.00, "stock": 40},
    "bubble_machine": {"name": "Bubble Machine", "price": 25.00, "stock": 30},
    "stuffed_dog": {"name": "Stuffed Dog", "price": 35.00, "stock": 25},
    "magic_set": {"name": "Magic Trick Set", "price": 30.00, "stock": 20},
    "toy_camera": {"name": "Kids Toy Camera", "price": 20.00, "stock": 30},
    "wooden_train": {"name": "Wooden Train Set", "price": 40.00, "stock": 15},
    "craft_kit": {"name": "Craft Kit", "price": 18.00, "stock": 35},
    "mini_golf_set": {"name": "Mini Golf Set", "price": 50.00, "stock": 10},
    "toy_drum": {"name": "Kids Toy Drum", "price": 25.00, "stock": 20},

    "lego_friends": {"name": "LEGO Friends Set", "price": 55.00, "stock": 20},
    "mini_puzzle_box": {"name": "Mini Puzzle Box", "price": 10.00, "stock": 50},
    "toy_truck": {"name": "Toy Truck", "price": 18.00, "stock": 35},
    "play_tent": {"name": "Kids Play Tent", "price": 45.00, "stock": 15},
    "soft_doll": {"name": "Soft Doll", "price": 22.00, "stock": 30},
    "toy_airplane_set": {"name": "Toy Airplane Set", "price": 30.00, "stock": 20},
    "mini_lego_set": {"name": "Mini LEGO Set", "price": 25.00, "stock": 40},
    "toy_kitchen_tools": {"name": "Toy Kitchen Tools", "price": 35.00, "stock": 25},
    "stuffed_bunny": {"name": "Stuffed Bunny", "price": 28.00, "stock": 30},
    "toy_trampoline": {"name": "Mini Trampoline", "price": 60.00, "stock": 10}
}


stationery_sect = {
    "pencil": {"name": "Pencil", "price": 1.50, "stock": 100},
    "pen": {"name": "Ballpoint Pen", "price": 2.00, "stock": 80},
    "eraser": {"name": "Eraser", "price": 0.50, "stock": 120},
    "sharpener": {"name": "Pencil Sharpener", "price": 1.00, "stock": 90},
    "notebook": {"name": "Notebook", "price": 3.00, "stock": 70},
    "drawing_pad": {"name": "Drawing Pad", "price": 5.00, "stock": 50},
    "marker": {"name": "Marker Set", "price": 6.00, "stock": 60},
    "highlighter": {"name": "Highlighter", "price": 2.50, "stock": 80},
    "ruler": {"name": "Ruler", "price": 1.20, "stock": 100},
    "sticky_notes": {"name": "Sticky Notes", "price": 3.50, "stock": 70},

    "scissors": {"name": "Scissors", "price": 4.00, "stock": 50},
    "glue_stick": {"name": "Glue Stick", "price": 1.80, "stock": 90},
    "tape_roll": {"name": "Tape Roll", "price": 2.50, "stock": 60},
    "paper_clip": {"name": "Paper Clip Pack", "price": 1.00, "stock": 100},
    "binder": {"name": "Binder", "price": 5.50, "stock": 40},
    "folder": {"name": "Document Folder", "price": 3.00, "stock": 60},
    "calculator": {"name": "Calculator", "price": 12.00, "stock": 30},
    "stamp": {"name": "Stamp", "price": 4.50, "stock": 40},
    "ink_pad": {"name": "Ink Pad", "price": 3.50, "stock": 30},
    "envelope": {"name": "Envelope Pack", "price": 2.50, "stock": 70}
}


cleaning_products_sect = {
    "all_purpose_cleaner": {"name": "All-Purpose Cleaner", "price": 5.00, "stock": 40},
    "dish_soap": {"name": "Dish Soap", "price": 3.00, "stock": 60},
    "laundry_detergent": {"name": "Laundry Detergent", "price": 10.00, "stock": 35},
    "floor_cleaner": {"name": "Floor Cleaner", "price": 7.00, "stock": 30},
    "glass_cleaner": {"name": "Glass Cleaner", "price": 4.50, "stock": 25},
    "scrub_brush": {"name": "Scrub Brush", "price": 3.50, "stock": 50},
    "sponges": {"name": "Sponges Pack", "price": 2.50, "stock": 60},
    "cleaning_cloths": {"name": "Cleaning Cloths", "price": 4.00, "stock": 40},
    "toilet_cleaner": {"name": "Toilet Cleaner", "price": 5.50, "stock": 25},
    "garbage_bags": {"name": "Garbage Bags", "price": 6.00, "stock": 50},

    "dishwasher_tablets": {"name": "Dishwasher Tablets", "price": 12.00, "stock": 30},
    "air_freshener": {"name": "Air Freshener", "price": 4.50, "stock": 40},
    "mop": {"name": "Mop", "price": 15.00, "stock": 20},
    "broom": {"name": "Broom", "price": 10.00, "stock": 25},
    "dustpan": {"name": "Dustpan", "price": 5.00, "stock": 30},
    "rubber_gloves": {"name": "Rubber Gloves", "price": 3.50, "stock": 50},
    "floor_squeegee": {"name": "Floor Squeegee", "price": 8.00, "stock": 20},
    "window_wiper": {"name": "Window Wiper", "price": 6.50, "stock": 25},
    "disinfectant_spray": {"name": "Disinfectant Spray", "price": 7.50, "stock": 30},
    "microfiber_cloths": {"name": "Microfiber Cloths", "price": 6.00, "stock": 40}
}


office_supplies_sect = {
    "stapler": {"name": "Stapler", "price": 8.00, "stock": 40},
    "staples": {"name": "Staples Pack", "price": 2.50, "stock": 60},
    "hole_punch": {"name": "Hole Punch", "price": 6.50, "stock": 30},
    "paper_ream": {"name": "Paper Ream", "price": 5.00, "stock": 50},
    "clipboard": {"name": "Clipboard", "price": 7.00, "stock": 35},
    "file_folder": {"name": "File Folder", "price": 3.50, "stock": 40},
    "desk_organizer": {"name": "Desk Organizer", "price": 12.00, "stock": 20},
    "whiteboard_markers": {"name": "Whiteboard Markers", "price": 6.00, "stock": 50},
    "push_pins": {"name": "Push Pins", "price": 2.00, "stock": 60},
    "sticky_tape": {"name": "Sticky Tape", "price": 3.00, "stock": 40},

    "label_maker": {"name": "Label Maker", "price": 25.00, "stock": 15},
    "scissors": {"name": "Scissors", "price": 5.50, "stock": 50},
    "binder_clips": {"name": "Binder Clips Pack", "price": 4.00, "stock": 60},
    "calculator": {"name": "Calculator", "price": 15.00, "stock": 25},
    "notepad": {"name": "Notepad", "price": 3.50, "stock": 70},
    "envelope": {"name": "Envelope Pack", "price": 4.00, "stock": 50},
    "rubber_stamp": {"name": "Rubber Stamp", "price": 7.50, "stock": 20},
    "ink_pad": {"name": "Ink Pad", "price": 6.00, "stock": 30},
    "desk_calendar": {"name": "Desk Calendar", "price": 8.50, "stock": 25},
    "paper_tray": {"name": "Paper Tray", "price": 10.00, "stock": 20}
}


bags_backpacks_sect = {
    "school_backpack": {"name": "School Backpack", "price": 35.00, "stock": 40},
    "laptop_bag": {"name": "Laptop Bag", "price": 50.00, "stock": 30},
    "handbag": {"name": "Handbag", "price": 45.00, "stock": 25},
    "tote_bag": {"name": "Tote Bag", "price": 30.00, "stock": 35},
    "duffle_bag": {"name": "Duffle Bag", "price": 60.00, "stock": 20},
    "crossbody_bag": {"name": "Crossbody Bag", "price": 40.00, "stock": 25},
    "drawstring_bag": {"name": "Drawstring Bag", "price": 20.00, "stock": 50},
    "travel_backpack": {"name": "Travel Backpack", "price": 55.00, "stock": 15},
    "fanny_pack": {"name": "Fanny Pack", "price": 25.00, "stock": 40},
    "messenger_bag": {"name": "Messenger Bag", "price": 45.00, "stock": 20},

    "gym_bag": {"name": "Gym Bag", "price": 35.00, "stock": 30},
    "cosmetic_bag": {"name": "Cosmetic Bag", "price": 20.00, "stock": 40},
    "camera_bag": {"name": "Camera Bag", "price": 60.00, "stock": 15},
    "lunch_bag": {"name": "Lunch Bag", "price": 15.00, "stock": 50},
    "pencil_case": {"name": "Pencil Case", "price": 10.00, "stock": 60},
    "weekender_bag": {"name": "Weekender Bag", "price": 70.00, "stock": 10},
    "hiking_backpack": {"name": "Hiking Backpack", "price": 65.00, "stock": 15},
    "diaper_bag": {"name": "Diaper Bag", "price": 50.00, "stock": 20},
    "beach_bag": {"name": "Beach Bag", "price": 30.00, "stock": 35},
    "laptop_sleeve": {"name": "Laptop Sleeve", "price": 25.00, "stock": 40}
}


lighting_sect = {
    "table_lamp": {"name": "Table Lamp", "price": 25.00, "stock": 30},
    "floor_lamp": {"name": "Floor Lamp", "price": 45.00, "stock": 20},
    "ceiling_light": {"name": "Ceiling Light", "price": 60.00, "stock": 15},
    "desk_lamp": {"name": "Desk Lamp", "price": 20.00, "stock": 40},
    "wall_sconce": {"name": "Wall Sconce", "price": 35.00, "stock": 25},
    "led_strip": {"name": "LED Strip Light", "price": 30.00, "stock": 35},
    "pendant_light": {"name": "Pendant Light", "price": 50.00, "stock": 15},
    "night_light": {"name": "Night Light", "price": 15.00, "stock": 50},
    "lamp_shade": {"name": "Lamp Shade", "price": 10.00, "stock": 40},
    "chandelier": {"name": "Chandelier", "price": 120.00, "stock": 10},

    "smart_bulb": {"name": "Smart Bulb", "price": 25.00, "stock": 30},
    "flashlight": {"name": "Flashlight", "price": 12.00, "stock": 50},
    "outdoor_lantern": {"name": "Outdoor Lantern", "price": 40.00, "stock": 20},
    "ceiling_fan_light": {"name": "Ceiling Fan with Light", "price": 80.00, "stock": 10},
    "torch_light": {"name": "Torch Light", "price": 15.00, "stock": 40},
    "solar_lamp": {"name": "Solar Lamp", "price": 35.00, "stock": 20},
    "desk_led_light": {"name": "Desk LED Light", "price": 22.00, "stock": 30},
    "string_lights": {"name": "String Lights", "price": 18.00, "stock": 40},
    "reading_lamp": {"name": "Reading Lamp", "price": 25.00, "stock": 30},
    "motion_sensor_light": {"name": "Motion Sensor Light", "price": 28.00, "stock": 25}
}


furniture_small_sect = {
    "side_table": {"name": "Side Table", "price": 45.00, "stock": 20},
    "stool": {"name": "Stool", "price": 25.00, "stock": 30},
    "shelf_unit": {"name": "Shelf Unit", "price": 60.00, "stock": 15},
    "coffee_table": {"name": "Coffee Table", "price": 55.00, "stock": 10},
    "nightstand": {"name": "Nightstand", "price": 40.00, "stock": 20},
    "storage_box": {"name": "Storage Box", "price": 20.00, "stock": 35},
    "ottoman": {"name": "Ottoman", "price": 35.00, "stock": 25},
    "bookshelf": {"name": "Bookshelf", "price": 65.00, "stock": 15},
    "desk_chair": {"name": "Desk Chair", "price": 50.00, "stock": 20},
    "footrest": {"name": "Footrest", "price": 18.00, "stock": 30},

    "wall_shelf": {"name": "Wall Shelf", "price": 30.00, "stock": 25},
    "bedside_lamp_table": {"name": "Bedside Lamp Table", "price": 45.00, "stock": 15},
    "shoe_rack": {"name": "Shoe Rack", "price": 35.00, "stock": 20},
    "coat_rack": {"name": "Coat Rack", "price": 25.00, "stock": 15},
    "folding_table": {"name": "Folding Table", "price": 40.00, "stock": 10},
    "small_cabinet": {"name": "Small Cabinet", "price": 55.00, "stock": 12},
    "night_lamp_table": {"name": "Night Lamp Table", "price": 38.00, "stock": 18},
    "kitchen_stool": {"name": "Kitchen Stool", "price": 22.00, "stock": 25},
    "storage_basket": {"name": "Storage Basket", "price": 18.00, "stock": 30},
    "plant_stand": {"name": "Plant Stand", "price": 20.00, "stock": 20}
}


pet_supplies_sect = {
    "dog_food": {"name": "Dog Food", "price": 25.00, "stock": 40},
    "cat_food": {"name": "Cat Food", "price": 20.00, "stock": 50},
    "pet_bed": {"name": "Pet Bed", "price": 45.00, "stock": 25},
    "dog_leash": {"name": "Dog Leash", "price": 15.00, "stock": 35},
    "cat_litter": {"name": "Cat Litter", "price": 12.00, "stock": 40},
    "pet_toy_ball": {"name": "Pet Toy Ball", "price": 8.00, "stock": 60},
    "aquarium": {"name": "Aquarium", "price": 70.00, "stock": 10},
    "bird_cage": {"name": "Bird Cage", "price": 50.00, "stock": 15},
    "pet_brush": {"name": "Pet Brush", "price": 10.00, "stock": 45},
    "pet_food_bowl": {"name": "Pet Food Bowl", "price": 8.00, "stock": 50},

    "dog_shampoo": {"name": "Dog Shampoo", "price": 12.00, "stock": 30},
    "cat_shampoo": {"name": "Cat Shampoo", "price": 10.00, "stock": 35},
    "pet_clothes": {"name": "Pet Clothes", "price": 20.00, "stock": 25},
    "pet_collar": {"name": "Pet Collar", "price": 10.00, "stock": 40},
    "pet_treats": {"name": "Pet Treats", "price": 15.00, "stock": 50},
    "dog_house": {"name": "Dog House", "price": 80.00, "stock": 10},
    "cat_tree": {"name": "Cat Tree", "price": 60.00, "stock": 15},
    "pet_nail_clipper": {"name": "Pet Nail Clipper", "price": 12.00, "stock": 25},
    "fish_food": {"name": "Fish Food", "price": 6.00, "stock": 50},
    "pet_carrier": {"name": "Pet Carrier", "price": 40.00, "stock": 20}
}


garden_items_sect = {
    "flower_pots": {"name": "Flower Pots", "price": 15.00, "stock": 50},
    "garden_shovel": {"name": "Garden Shovel", "price": 12.00, "stock": 30},
    "watering_can": {"name": "Watering Can", "price": 10.00, "stock": 40},
    "garden_gloves": {"name": "Garden Gloves", "price": 5.00, "stock": 60},
    "garden_hose": {"name": "Garden Hose", "price": 25.00, "stock": 20},
    "rake": {"name": "Rake", "price": 15.00, "stock": 25},
    "lawn_mower": {"name": "Lawn Mower", "price": 150.00, "stock": 10},
    "pruning_shears": {"name": "Pruning Shears", "price": 20.00, "stock": 30},
    "fertilizer": {"name": "Fertilizer", "price": 8.00, "stock": 50},
    "plant_seeds": {"name": "Plant Seeds", "price": 3.00, "stock": 100},
    "garden_lights": {"name": "Garden Lights", "price": 35.00, "stock": 20},
    "outdoor_planter": {"name": "Outdoor Planter", "price": 40.00, "stock": 15},
    "compost_bin": {"name": "Compost Bin", "price": 60.00, "stock": 10},
    "garden_kneeler": {"name": "Garden Kneeler", "price": 25.00, "stock": 20},
    "garden_table_chairs": {"name": "Garden Table & Chairs", "price": 120.00, "stock": 5}
}


automotive_accessories_sect = {
    "car_seat_cover": {"name": "Car Seat Cover", "price": 35.00, "stock": 20},
    "steering_wheel_cover": {"name": "Steering Wheel Cover", "price": 15.00, "stock": 30},
    "car_floor_mats": {"name": "Car Floor Mats", "price": 25.00, "stock": 25},
    "car_phone_holder": {"name": "Car Phone Holder", "price": 10.00, "stock": 40},
    "car_vacuum_cleaner": {"name": "Car Vacuum Cleaner", "price": 50.00, "stock": 15},
    "car_air_freshener": {"name": "Car Air Freshener", "price": 5.00, "stock": 50},
    "car_sunshade": {"name": "Car Sunshade", "price": 20.00, "stock": 30},
    "jump_starter": {"name": "Jump Starter", "price": 60.00, "stock": 10},
    "tire_pressure_gauge": {"name": "Tire Pressure Gauge", "price": 12.00, "stock": 40},
    "car_charger": {"name": "Car Charger", "price": 18.00, "stock": 50},
    "car_organizer": {"name": "Car Organizer", "price": 25.00, "stock": 20},
    "windshield_washer_fluid": {"name": "Windshield Washer Fluid", "price": 8.00, "stock": 40},
    "car_cover": {"name": "Car Cover", "price": 55.00, "stock": 15},
    "roof_rack": {"name": "Roof Rack", "price": 80.00, "stock": 10},
    "portable_car_pump": {"name": "Portable Car Pump", "price": 30.00, "stock": 20}
}






