#settings for midi_to_beatsaber_map.py

path = "C:\\beatsaber\\"
outputpath = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Beat Saber\\CustomSongs\\"
songname = "Forbidden Fruit"
ext = ".wav"

note_favorites = [
    #config favorites here: default C7-A#7 (96-106) for blue and C8-A#8 (108-118) for red)
    ("note_red-line_middleleft-layer_bottom-cut_down", 108),
    ("note_red-line_middleleft-layer_bottom-cut_up", 109),
    ("note_red-line_left-layer_bottom-cut_down", 110),
    ("note_red-line_left-layer_bottom-cut_up", 111),
    ("note_red-line_left-layer_middle-cut_left", 112),
    ("note_red-line_left-layer_bottom-cut_right", 113),
    ("note_red-line_left-layer_bottom-cut_downleft", 114),
    ("note_red-line_left-layer_top-cut_any", 115),
    ("note_red-line_middleleft-layer_bottom-cut_down", 116),
    ("note_red-line_middleleft-layer_bottom-cut_down", 117),
    ("note_red-line_middleleft-layer_bottom-cut_down", 118),
    
    ("note_blue-line_middleright-layer_bottom-cut_down", 96),
    ("note_blue-line_middleright-layer_bottom-cut_up", 97),
    ("note_blue-line_right-layer_bottom-cut_down", 98),
    ("note_blue-line_right-layer_bottom-cut_up", 99),
    ("note_blue-line_right-layer_bottom-cut_left", 100),
    ("note_blue-line_right-layer_middle-cut_right", 101),
    ("note_blue-line_right-layer_bottom-cut_downright", 102),
    ("note_blue-line_right-layer_top-cut_any", 103),
    ("note_blue-line_middleright-layer_bottom-cut_down", 104),
    ("note_blue-line_middleright-layer_bottom-cut_down", 105),
    ("note_blue-line_middleright-layer_bottom-cut_down", 106)
]

event_favorites = [
    #config favorites here: default C7-A#7 (96-106) for blue and C8-A#8 (108-118) for red)
    ("laser_laserleft-red_redon", 108),
    ("laser_laserright-red_redon", 109),
    ("speed_speedlaserleft-speed_speed1", 110),
    ("speed_speedlaserright-speed_speed1", 111),
    ("ring_ringrotation-off_off", 112),
    ("laser_laserbottomside-red_redon", 113),
    ("laser_laserbottomside-red_redflashfade", 114),
    ("laser_laserbacktop-red_redon", 115),
    ("laser_laserbacktop-red_redflashfade", 116),
    ("track_trackringneons-red_redon", 117),
    ("track_trackringneons-red_flashfade", 118),
    
    ("laser_laserleft-blue_blueon", 96),
    ("laser_laserright-blue_blueon", 97),
    ("speed_speedlaserleft-speed_speed1", 98),
    ("speed_speedlaserright-speed_speed1", 99),
    ("ring_smallringrotation-off_off", 100),
    ("laser_laserbottomside-blue_blueon", 101),
    ("laser_laserbottomside-blue_blueflashfade", 102),
    ("laser_laserbacktop-blue_blueon", 103),
    ("laser_laserbacktop-blue_blueflashfade", 104),
    ("track_trackringneons-blue_blueon", 105),
    ("track_trackringneons-blue_blueflashfade", 106)
]



obstacle_tuple = [
    #Obstacles: default F6 (89) to A6 (93)
    ("obstacle_wall-obstacleline_right", 89),
    ("obstacle_wall-obstacleline_middleright", 90),
    ("obstacle_wall-obstacleline_middleleft", 91),
    ("obstacle_wall-obstacleline_left", 92),
    ("obstacle_ceiling-none_top", 93)
]

input_tuple = [ #configure notes here
    #Red saber: default C5 (72) to D6 (86)
    ("note_red-line_right-layer_bottom", 72),
    ("note_red-line_right-layer_middle", 73),
    ("note_red-line_right-layer_top", 74),

    ("note_red-line_middleright-layer_bottom", 76),
    ("note_red-line_middleright-layer_middle", 77),
    ("note_red-line_middleright-layer_top", 78),

    ("note_red-line_middleleft-layer_bottom", 80),
    ("note_red-line_middleleft-layer_middle", 81),
    ("note_red-line_middleleft-layer_top", 82),

    ("note_red-line_left-layer_bottom", 84),
    ("note_red-line_left-layer_middle", 85),
    ("note_red-line_left-layer_top", 86),

    #Blue saber: default C3 (48) to D4 (62)
    ("note_blue-line_right-layer_bottom", 48),
    ("note_blue-line_right-layer_middle", 49),
    ("note_blue-line_right-layer_top", 50),

    ("note_blue-line_middleright-layer_bottom", 52),
    ("note_blue-line_middleright-layer_middle", 53),
    ("note_blue-line_middleright-layer_top", 54),

    ("note_blue-line_middleleft-layer_bottom", 56),
    ("note_blue-line_middleleft-layer_middle", 57),
    ("note_blue-line_middleleft-layer_top", 58),

    ("note_blue-line_left-layer_bottom", 60),
    ("note_blue-line_left-layer_middle", 61),
    ("note_blue-line_left-layer_top", 62),

    #Mines: default C1 (24) to D2 (38)
    ("note_mine-line_right-layer_bottom", 24),
    ("note_mine-line_right-layer_middle", 25),
    ("note_mine-line_right-layer_top", 26),

    ("note_mine-line_middleright-layer_bottom", 28),
    ("note_mine-line_middleright-layer_middle", 29),
    ("note_mine-line_middleright-layer_top", 30),

    ("note_mine-line_middleleft-layer_bottom", 32),
    ("note_mine-line_middleleft-layer_middle", 33),
    ("note_mine-line_middleleft-layer_top", 34),

    ("note_mine-line_left-layer_bottom", 36),
    ("note_mine-line_left-layer_middle", 37),
    ("note_mine-line_left-layer_top", 38)
]

lighting_tuple = [ #configure events here
    ("laser_laserright", 72),
    ("speed_speedlaserright", 73),
    ("track_trackringneons", 74),

    ("laser_laserleft", 76),
    ("speed_speedlaserleft", 77),
    ("laser_laserbacktop", 78),

    ("laser_laserbottomside", 80),
    ("ring_ringrotation", 81),
    ("ring_smallringrotation", 82)
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

#lighting (not sure names are correct)
lighting_types = [
    ("laser_laserbacktop", 0),
    ("track_trackringneons", 1),
    ("laser_laserleft", 2),
    ("laser_laserright", 3),
    ("laser_laserbottomside", 4),
    ("ring_ringrotation", 8),
    ("ring_smallringrotation", 9),
    ("speed_speedlaserleft", 12),
    ("speed_speedlaserright", 13)
] 

lighting_lightvalues = [
    ("off_off", 0),
    ("blue_blueon", 1),
    ("blue_blueflashstay", 2),
    ("blue_blueflashfade", 3),
    ("red_redon", 5),
    ("red_redflashstay", 6),
    ("red_redflashfade", 7)
]

lighting_rotationvalues = [
    ("stop_stop", 0),
    ("speed_speed1", 1),
    ("speed_speed2", 2),
    ("speed_speed3", 3),
    ("speed_speed4", 4),
    ("speed_speed5", 5),
    ("speed_speed6", 6),
    ("speed_speed7", 7),
    ("speed_speed8", 8)
]

#JSON (credits to ciwolsey for map+note)
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

obstacle = {
    "_time": 0,
    "_lineIndex": 0,
    "_type": 0,
    "_duration": 0,
    "_width": 0
}

event = {
    "_time": 0,
    "_type": 0,
    "_value": 0
}

#settings for preview_sample.py

notes = ["note_red", "note_blue", "note_mine"]
lines = ["line_right", "line_middleright", "line_middleleft", "line_left"]
layers = ["layer_bottom", "layer_middle", "layer_top"]
cuts = ["cut_up", "cut_down", "cut_left", "cut_right", "cut_upleft", "cut_upright", "cut_downleft", "cut_downright", "cut_any"] 

obstacles = ["obstacle_wall", "obstacle_ceiling"]
obstaclelines = ["obstacleline_right", "obstacleline_middleright", "obstacleline_middleleft", "obstacleline_left"]
