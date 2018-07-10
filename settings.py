#settings for midi_to_beatsaber_map.py

path = "C:\\beatsaber\\"
ext = ".wav"

input_tuple = [ #configure notes here
    #Red saber: default C6 (84) to D7 (98)
    ("note_red-line_right-layer_bottom", 84),
    ("note_red-line_right-layer_middle", 85),
    ("note_red-line_right-layer_top", 86),

    ("note_red-line_middleright-layer_bottom", 88),
    ("note_red-line_middleright-layer_middle", 89),
    ("note_red-line_middleright-layer_top", 90),

    ("note_red-line_middleleft-layer_bottom", 92),
    ("note_red-line_middleleft-layer_middle", 93),
    ("note_red-line_middleleft-layer_top", 94),

    ("note_red-line_middleleft-layer_bottom", 96),
    ("note_red-line_middleleft-layer_middle", 97),
    ("note_red-line_middleleft-layer_top", 98),

    #Blue saber: default C4 (60) to D5 (74)
    ("note_blue-line_right-layer_bottom", 60),
    ("note_blue-line_right-layer_middle", 61),
    ("note_blue-line_right-layer_top", 62),

    ("note_blue-line_middleright-layer_bottom", 64),
    ("note_blue-line_middleright-layer_middle", 65),
    ("note_blue-line_middleright-layer_top", 66),

    ("note_blue-line_middleleft-layer_bottom", 68),
    ("note_blue-line_middleleft-layer_middle", 69),
    ("note_blue-line_middleleft-layer_top", 70),

    ("note_blue-line_middleleft-layer_bottom", 72),
    ("note_blue-line_middleleft-layer_middle", 73),
    ("note_blue-line_middleleft-layer_top", 74),

    #Mines: default C2 (36) to D3 (50)
    ("note_mine-line_right-layer_bottom", 36),
    ("note_mine-line_right-layer_middle", 37),
    ("note_mine-line_right-layer_top", 38),

    ("note_mine-line_middleright-layer_bottom", 40),
    ("note_mine-line_middleright-layer_middle", 41),
    ("note_mine-line_middleright-layer_top", 42),

    ("note_mine-line_middleleft-layer_bottom", 44),
    ("note_mine-line_middleleft-layer_middle", 45),
    ("note_mine-line_middleleft-layer_top", 46),

    ("note_mine-line_middleleft-layer_bottom", 48),
    ("note_mine-line_middleleft-layer_middle", 49),
    ("note_mine-line_middleleft-layer_top", 50)
]

cut_directions =  [
    ("cut_up", 0),
    ("cut_down", 1),
    ("cut_left", 2),
    ("cut_right", 3),
    ("cut_upleft", 4),
    ("cut_upright", 5),
    ("cut_downleft", 6), 
    ("cut_downright", 7), 
    ("cut_any", 8)
]

note_types = [
    ("note_red", 0),
    ("note_blue", 1),
    ("note_mine", 3),
]

line_indices = [
    ("line_left", 0),
    ("line_middleleft", 1),
    ("line_middleright", 2),
    ("line_right", 3)
]

line_layers = [
    ("layer_bottom", 0),
    ("layer_middle", 1),
    ("layer_top", 2)
]


#JSON (credits to ciwolsey)
map = {
    "_version": "1.5.0",
    "_beatsPerMinute": 0,
    "_beatsPerBar": 8,
    "_noteJumpSpeed": 10,
    "_shuffle": 0,
    "_shufflePeriod": 0.5,
    "_events": [],
    "_notes": [],
    "_obstacles": []
}

note = {
    "_time": 0,
    "_lineIndex": 0,
    "_lineLayer": 0,
    "_type": 0,
    "_cutDirection": 8
}

obstacle = { #todo
    "_time": 0,
    "_lineIndex": 0,
    "_type": 0,
    "_duration": 0,
    "_width": 0
}

#settings for preview_sample.py

notes = ["note_red", "note_blue", "note_mine"]
lines = ["line_right", "line_middleright", "line_middleleft", "line_left"]
layers = ["layer_bottom", "layer_middle", "layer_top"]
cuts = ["cut_up", "cut_down", "cut_left", "cut_right", "cut_upleft", "cut_upright", "cut_downleft", "cut_downright", "cut_any"] 

obstacles = ["obstacle_wall", "obstacle_ceiling"]
obstaclelines = ["obstacleline_right", "obstacleline_middleright", "obstacleline_middleleft", "obstacleline_left"]