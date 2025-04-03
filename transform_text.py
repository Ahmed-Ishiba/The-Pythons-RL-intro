
from manim import *

# Set background color
config.background_color = BLACK

class TransformText(Scene):
    def construct(self):
        # Define text with increased font size
        text_1 = Text("The", font="Pirata One", fill_color="#FFD43F", font_size=72)  # Increased font size
        text_2 = Text("Pythons", font="Pirata One", fill_color="#2A456C", font_size=72)  # Same font size as "The"
        text_3 = Text("RL", fill_color=WHITE, font_size=48)  # Smaller font size for RL
       
        # Arrange text in a single line
        text_group = VGroup(text_1, text_2, text_3).arrange(RIGHT, buff=0.2)
        text_1.shift(UP * 0.1)
        # Display the initial text
        self.play(Write(text_group))
        self.wait(1)
        
        # Create "Rescue Line" text and align it properly
        new_text_3 = Text("Rescue Line", fill_color=WHITE, font_size=48)  # Same size as RL
        new_text_3.next_to(text_2, RIGHT)  # Keep the position unchanged
        all_text = VGroup(text_1, text_2, new_text_3)
        shift_amount = new_text_3.width - text_3.width - 1
        new_text_3.shift(LEFT*shift_amount)
        move_text = all_text[:-1].animate.shift(LEFT*shift_amount)
        replace_rl = ReplacementTransform(text_3, new_text_3)
        # Transform "RL" into "Rescue Line"
        self.play(AnimationGroup(move_text, replace_rl))
        self.wait(2)

