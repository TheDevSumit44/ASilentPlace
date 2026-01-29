# images.rpy
# Clean transforms and image declarations for 1920x1080 project

# Background scaling (full HD)
transform bg_full:
    size (1920, 1080)

# Standard character sizing (center)
transform sprite_mid:
    zoom 0.33
    xalign 0.5
    yalign 1.0

# Left / Right positions (lightweight)
transform left_pos:
    zoom 0.33
    xalign 0.25
    yalign 1.0

transform right_pos:
    zoom 0.33
    xalign 0.75
    yalign 1.0

# Slide-in left / right (short, low-cost)
transform slide_in_left:
    xalign -0.5
    yalign 1.0
    zoom 0.33
    linear 0.45 xalign 0.25

transform slide_in_right:
    xalign 1.5
    yalign 1.0
    zoom 0.33
    linear 0.45 xalign 0.75

# Subtle blink (low cost)
transform blink:
    pause 2.5
    linear 0.06 alpha 0.0
    linear 0.06 alpha 1.0
    pause 3.0
    repeat

transform sprite_left:
    zoom 0.33
    xalign 0.25
    yalign 1.0

transform sprite_right:
    zoom 0.33
    xalign 0.75
    yalign 1.0

transform sprite_center:
    zoom 0.33
    xalign 0.5
    yalign 1.0

# Vignette overlay (semi-transparent black)
image vignette = Solid("#00000040")

# Backgrounds
image bg room = "bg_room.png"
image bg park = "bg_park.png"

# Jessy sprites
image jessy normal = "jessy_normal.png"
image jessy sad = "jessy_sad.png"
image jessy annoyed = "jessy_annoyed.png"

# Joshua sprites
image joshua happy = "joshua_happy.png"
image joshua sad = "joshua_sad.png"
