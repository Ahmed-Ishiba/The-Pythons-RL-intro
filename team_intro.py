from manim import *

class MeetOurTeam(Scene):
    def construct(self):
        # Title in the top-left corner
        title = Text("Meet our Team:", font_size=48).to_corner(UL)
        underline = Line(start=title.get_left(), end=title.get_right()).next_to(title, DOWN, buff=0.1)

        # Animate title and underline
        self.play(Write(title))
        self.play(Create(underline))
        self.wait(1)

        # Team Members Info
        team_info = [
            ("Nour_raoof.png", "Nour Raoof", "Design and assembly of robot chasis "),
            ("Ahmed_elsayed.png", "Ahmed Elsayed", "Programming and control\nof robot in Line follower"),
            ("Eyad.jpg", "Eyad Nazary", "Electrical and electronics \ncircuit design"),
            ("Moaz.jpg", "Moaz Mahmoud", "Programming and control\nof robot in evacuation zone")
           
        ]
        positions = [
            [-5, 1.0, 0],  # Top-left
            [2, 1.2, 0],   # Top-right
            [-5, -2.0, 0], # Bottom-left
            [2, -2.0, 0]   # Bottom-right
        ]

        # Create a group for all members
        team_members = Group()

        for i, (photo, name, role) in enumerate(team_info):
            # Load Image (Scaled to fit properly)
            image = ImageMobject(photo).scale(0.4).move_to(positions[i])
            
            # Name & Role (aligned to the right of each image)
            name_text = Text(name, font_size=30).next_to(image, RIGHT, buff=0.2)
            role_text = Text(role, font_size=30 ,color=GRAY).scale(0.7).next_to(name_text, DOWN, buff=0.2).align_to(name_text, LEFT)

            # Grouping elements properly
            person_group = Group(image, name_text, role_text)
            team_members.add(person_group)

        # Display all members at once
        self.play(FadeIn(team_members))
        self.wait(4)
