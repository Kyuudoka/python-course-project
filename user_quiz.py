from palette_lists import *

# Quiz variables -takes user input to influence randomisation parameters for drawing
print(''' 

███╗   ███╗ ██████╗  ██████╗ ██████╗ ███████╗████████╗ █████╗ ███╗   ███╗██████╗ 
████╗ ████║██╔═══██╗██╔═══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗████╗ ████║██╔══██╗
██╔████╔██║██║   ██║██║   ██║██║  ██║███████╗   ██║   ███████║██╔████╔██║██████╔╝
██║╚██╔╝██║██║   ██║██║   ██║██║  ██║╚════██║   ██║   ██╔══██║██║╚██╔╝██║██╔═══╝ 
██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██████╔╝███████║   ██║   ██║  ██║██║ ╚═╝ ██║██║     
╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ''')

complexity = input("\nHow complex are your thoughts and feelings right now? Give a number between 1 and 6, where 1 represents having only a few thoughts and 6 represents thinking about many different things simultaneously --> ")  # 1-10
# represented by more types of shapes selected for the moodstamp 

energy = input("\nHow energetic do you feel right now? Give a number between 1 and 10, where 1 represents being almost asleep and 10 represents being ready to run a marathon --> ")  # 1-10
# represented by more shapes overall -influences the number of times it runs each shape applicator

mood_intensity = input("\nRegarding your current feelings, how intensely are you feeling them? Type 'low', 'medium', or 'high' to set the intensity of your mood --> ")  # low, medium, high
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