from manim import *

class RobotInAction(Scene):
    def construct(self):
        # Create text with large font size
        text = Text("Robot in action!", font_size=72)
        
        # Display the text with an animation
        self.play(Write(text))
        
        # Keep the text on screen for a while
        self.wait(1)
        
        # Unwrite the text
        self.play(FadeOut(text))
        
        # Write "Line Follower:" in the top left corner with underline
        line_follower_text = Text("Line Follower:", font_size=48).to_corner(UL)
        underline = Underline(line_follower_text)
        self.play(Write(line_follower_text), Write(underline))
        
        # Display video for Line Follower
        self.wait(12)  # Adjust duration based on the video length
        
        # Unwrite text and underline
        self.play(FadeOut(line_follower_text), FadeOut(underline))
        
        # Write "Evacuation Zone:" in the top right corner with underline
        evacuation_text = Text("Evacuation Zone:", font_size=48).to_corner(UL)
        underline2 = Underline(evacuation_text)
        self.play(Write(evacuation_text), Write(underline2))
        
        # Display video for Evacuation Zone
        
        self.wait(15)  # Adjust duration based on the video length
                
        # Unwrite everything
        self.play(FadeOut(evacuation_text), FadeOut(underline2))
