from manim import *

class RobocupJunior2025(Scene):
    def construct(self):
        # Create text and position it at the top center
        text = Text("Excited for Robocup Junior 2025!", font_size=48)
        text.to_edge(UP)
        
        # Display the text with an animation
        self.play(Write(text))
        
        # Keep the text on screen for a while
         
        # Fade out the text
       
        # Display a logo below the closing text
        logo = ImageMobject("Thepythons.png").scale(0.5)  # Adjust the path and scale as needed
        logo.to_edge(DOWN).shift(2.0 * UP)
        
        self.play(FadeIn(logo))
        self.wait(2)
        self.play(FadeOut(logo))
        self.play(FadeOut(text))
        
