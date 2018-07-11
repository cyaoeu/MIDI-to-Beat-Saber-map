#settings for midi_to_beatsaber_map.py

path = "C:\\beatsaber\\"
ext = ".wav"

obstacle_tuple = [
    #Obstacles: default F7 (101) to A7 (105)
    ("obstacle_wall-obstacleline_right", 101),
    ("obstacle_wall-obstacleline_middleright", 102),
    ("obstacle_wall-obstacleline_middleleft", 103),
    ("obstacle_wall-obstacleline_left", 104),
    ("obstacle_ceiling-none_top", 105)
]

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

    ("note_red-line_left-layer_bottom", 96),
    ("note_red-line_left-layer_middle", 97),
    ("note_red-line_left-layer_top", 98),

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

    ("note_blue-line_left-layer_bottom", 72),
    ("note_blue-line_left-layer_middle", 73),
    ("note_blue-line_left-layer_top", 74),

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

    ("note_mine-line_left-layer_bottom", 48),
    ("note_mine-line_left-layer_middle", 49),
    ("note_mine-line_left-layer_top", 50)
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

#obstacles
obstacle_line_indices = [  
    ("obstacleline_left", 0),
    ("obstacleline_middleleft", 1),
    ("obstacleline_middleright", 2),
    ("obstacleline_right", 3)
]

obstacle_types = [
    ("obstacle_wall", 0),
    ("obstacle_ceiling", 1)
]
obstacle_durations = [
    ("duration_duration0", 0),
    ("duration_duration0.5", 0.5),
    ("duration_duration1", 1),
    ("duration_duration2", 2),
    ("duration_duration3", 3),
    ("duration_duration4", 4),
    ("duration_duration5", 5),
    ("duration_duration6", 6),
    ("duration_duration7", 7),
    ("duration_duration8", 8),
    ("duration_duration9", 9),
    ("duration_duration10", 10),
    ("duration_duration11", 11),
    ("duration_duration12", 12),
    ("duration_duration13", 13),
    ("duration_duration14", 14),
    ("duration_duration15", 15),
    ("duration_duration16", 16)
]

obstacle_widths = [
    ("width_width0", 0),
    ("width_width1", 1),
    ("width_width2", 2),
    ("width_width3", 3),
    ("width_width4", 4),
    ("width_width5", 5),
    ("width_width6", 6),
    ("width_width7", 7),
    ("width_width8", 8),
    ("width_width9", 9)
]

#lighting
lighting_types = [
    ("light_light0", 0),
    ("light_light1", 1),
    ("light_light2", 2),
    ("light_light3", 3),
    ("light_light4", 4),
    ("turn_turnmiddle", 8),
    ("zoom_zoomin", 9),
    ("move_movelight1", 12),
    ("move_movelight2", 13)
] 

lighting_values = [
    ("off_off", 0),
    ("blue_blue0", 1),
    ("blue_blue1", 2),
    ("blue_fade", 3),
    ("unknown_unknown", 4),
    ("red_red0", 5),
    ("red_red1", 6),
    ("red_fade", 7),
    ("unknown_unknown", 8),
    ("unknown_unknown", 9),
    ("unknown_unknown", 10)
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
