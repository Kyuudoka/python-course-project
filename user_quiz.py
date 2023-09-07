from palette_lists import *

# Quiz variables -takes user input to influence randomisation parameters for drawing

complexity = input("\nAre your thoughts and feelings as elaborate as the Bayeux tapestry, or closer to a knitted scarf? On a scale of 1-10, how complex are your thoughts and feelings right now? --> ")  # 1-10
# represented by more types of shapes selected for the moodstamp 

energy = input("\nDo you feel like running a marathon, or going back to bed? On a scale of 1-10, how energetic do you feel right now? --> ")  # 1-10
# represented by more shapes overall -influences the number of times it runs each shape applicator

mood_intensity = input("\nA shout or a whisper? How intense are your feelings right now? Type low, medium, or high to set the intensity. --> ")  # low, medium, high
# # Higher intensity = higher contrast, used to narrow down the palettes used. Also used to set higher spikiness.

if mood_intensity == "low":
    print("\nWhich of the following do you feel fits your current mood the most?\n1) Muted forest colours\n2) Soft and deep mauves\n3) Cool ocean shades\n4) Vibrant green leaves against a bright summer sky\n")
    palette = low_contrast[(int(input("\nType the corresponding number --> "))-1)]
elif mood_intensity == "medium":
    print("\nWhich of the following do you feel fits your current mood the most?\n1) Pastel-hued candyland\n2) Vintage propaganda posters\n3) An opulent drawing room owned by a slightly eccentric aristocrat\n4) Gentle blossom drifting through the window of a child's nursery\n")
    palette = med_contrast[(int(input("\nType the corresponding number --> "))-1)]
elif mood_intensity == "high":
    print("\nWhich of the following do you feel fits your current mood the most?\n1) A dark starless night lit by warm streetlights\n2) The end of sunset over a stormy ocean\n3) A campfire in a rain-soaked field\n4) An aggressively neon sunset\n")
    palette = high_contrast[(int(input("\nType the corresponding number --> "))-1)]
else:
    print("\nNot a valid answer; please restart and type either 'low', 'medium', or 'high' to set the intensity.")