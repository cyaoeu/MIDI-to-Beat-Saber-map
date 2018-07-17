#settings for MIDIbeat.py

path = "C:\\beatsaber\\"
outputpath = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Beat Saber\\CustomSongs\\"
songname = "Forbidden Fruit"
ext = ".wav"

note_favorites = [
    #config favorites here: default C7-B7 (96-107) for blue and C8-B8 (108-119) for red)
    ("note_red-line_midleft-layer_bot-cut_down", 108),
    ("note_red-line_left-layer_bot-cut_down", 109),
    ("note_red-line_midleft-layer_bot-cut_up", 110),
    ("note_red-line_left-layer_bot-cut_up", 111),
    ("note_red-line_midleft-layer_mid-cut_left", 112),
    ("note_red-line_left-layer_mid-cut_left", 113),
    ("note_red-line_right-layer_bot-cut_right", 114),
    ("note_red-line_right-layer_mid-cut_right", 115),
    ("note_red-line_midleft-layer_top-cut_any", 116),
    ("note_red-line_left-layer_top-cut_any", 117),
    ("note_red-line_midright-layer_mid-any", 118),
    ("note_red-line_midright-layer_bot-any", 119),
    
    ("note_blue-line_midright-layer_bot-cut_down", 96),
    ("note_blue-line_right-layer_bot-cut_down", 97),
    ("note_blue-line_midright-layer_bot-cut_up", 98),
    ("note_blue-line_right-layer_bot-cut_up", 99),
    ("note_blue-line_midright-layer_mid-cut_right", 100),
    ("note_blue-line_right-layer_mid-cut_right", 101),
    ("note_blue-line_left-layer_bot-cut_left", 102),
    ("note_blue-line_left-layer_mid-cut_left", 103),
    ("note_blue-line_midright-layer_top-cut_any", 104),
    ("note_blue-line_right-layer_top-cut_any", 105),
    ("note_blue-line_midleft-layer_mid-cut_any", 106),
    ("note_blue-line_midleft-layer_bot-cut_any", 107)
]

event_favorites = [
    #config favorites here: default C7-B7 (96-107) for blue and C8-B8 (108-119) for red)
    ("laser_laserleft-red_redon", 108),
    ("laser_laserright-red_redon", 109),
    ("speed_speedlaserleft-speed_speed1", 110),
    ("speed_speedlaserright-speed_speed1", 111),
    ("laser_laserbotside-red_redon", 112),
    ("laser_laserbotside-red_redflashfade", 113),
    ("laser_laserbacktop-red_redon", 114),
    ("laser_laserbacktop-red_redflashfade", 115),
    ("track_trackringneons-red_redon", 116),
    ("track_trackringneons-red_flashfade", 117),
    ("ring_ringrotation-off_off", 118),
    ("ring_smallringrotation-off_off", 119),
    
    ("laser_laserleft-blue_blueon", 96),
    ("laser_laserright-blue_blueon", 97),
    ("speed_speedlaserleft-speed_speed1", 98),
    ("speed_speedlaserright-speed_speed1", 99),
    ("laser_laserbotside-blue_blueon", 100),
    ("laser_laserbotside-blue_blueflashfade", 101),
    ("laser_laserbacktop-blue_blueon", 102),
    ("laser_laserbacktop-blue_blueflashfade", 103),
    ("track_trackringneons-blue_blueon", 104),
    ("track_trackringneons-blue_blueflashfade", 105),
    ("ring_ringrotation-off_off", 106),
    ("ring_smallringrotation-off_off", 107)
]



obstacle_tuple = [
    #Obstacles: default F6 (89) to A6 (93)
    ("obstacle_wall-obstacleline_right", 89),
    ("obstacle_wall-obstacleline_midright", 90),
    ("obstacle_wall-obstacleline_midleft", 91),
    ("obstacle_wall-obstacleline_left", 92),
    ("obstacle_ceiling-none_top", 93)
]

input_tuple = [ #configure notes here
    #Red saber: default C5 (72) to D6 (86)
    ("note_red-line_right-layer_bot", 72),
    ("note_red-line_right-layer_mid", 73),
    ("note_red-line_right-layer_top", 74),

    ("note_red-line_midright-layer_bot", 76),
    ("note_red-line_midright-layer_mid", 77),
    ("note_red-line_midright-layer_top", 78),

    ("note_red-line_midleft-layer_bot", 80),
    ("note_red-line_midleft-layer_mid", 81),
    ("note_red-line_midleft-layer_top", 82),

    ("note_red-line_left-layer_bot", 84),
    ("note_red-line_left-layer_mid", 85),
    ("note_red-line_left-layer_top", 86),

    #Blue saber: default C3 (48) to D4 (62)
    ("note_blue-line_right-layer_bot", 48),
    ("note_blue-line_right-layer_mid", 49),
    ("note_blue-line_right-layer_top", 50),

    ("note_blue-line_midright-layer_bot", 52),
    ("note_blue-line_midright-layer_mid", 53),
    ("note_blue-line_midright-layer_top", 54),

    ("note_blue-line_midleft-layer_bot", 56),
    ("note_blue-line_midleft-layer_mid", 57),
    ("note_blue-line_midleft-layer_top", 58),

    ("note_blue-line_left-layer_bot", 60),
    ("note_blue-line_left-layer_mid", 61),
    ("note_blue-line_left-layer_top", 62),

    #Mines: default C1 (24) to D2 (38)
    ("note_mine-line_right-layer_bot", 24),
    ("note_mine-line_right-layer_mid", 25),
    ("note_mine-line_right-layer_top", 26),

    ("note_mine-line_midright-layer_bot", 28),
    ("note_mine-line_midright-layer_mid", 29),
    ("note_mine-line_midright-layer_top", 30),

    ("note_mine-line_midleft-layer_bot", 32),
    ("note_mine-line_midleft-layer_mid", 33),
    ("note_mine-line_midleft-layer_top", 34),

    ("note_mine-line_left-layer_bot", 36),
    ("note_mine-line_left-layer_mid", 37),
    ("note_mine-line_left-layer_top", 38)
]

lighting_tuple = [ #configure events here
    ("laser_laserright", 72),
    ("speed_speedlaserright", 73),
    ("track_trackringneons", 74),

    ("laser_laserleft", 76),
    ("speed_speedlaserleft", 77),
    ("laser_laserbacktop", 78),

    ("laser_laserbotside", 80),
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
    ("line_midleft", 1),
    ("line_midright", 2),
    ("line_right", 3)
]

line_layers = [
    ("layer_bot", 0),
    ("layer_mid", 1),
    ("layer_top", 2)
]

#obstacles
obstacle_line_indices = [  
    ("obstacleline_left", 0),
    ("obstacleline_midleft", 1),
    ("obstacleline_midright", 2),
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
    ("laser_laserbotside", 4),
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
lines = ["line_right", "line_midright", "line_midleft", "line_left"]
layers = ["layer_bot", "layer_mid", "layer_top"]
cuts = ["cut_up", "cut_down", "cut_left", "cut_right", "cut_upleft", "cut_upright", "cut_downleft", "cut_downright", "cut_any"] 

obstacles = ["obstacle_wall", "obstacle_ceiling"]
obstaclelines = ["obstacleline_right", "obstacleline_midright", "obstacleline_midleft", "obstacleline_left"]
