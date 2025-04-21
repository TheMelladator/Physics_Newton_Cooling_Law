from manim import *
import numpy as np

class Cooling_Law(Scene):
    def construct(self):
        # Inicial Parameters
        T0 = 90
        Ta = 25
        k = 0.1
        
        # 1. Title
        title = Text("Newton's Law of Cooling").scale(0.8)

        # 2. Coordinate Axes
        axes = Axes(
            x_range=[0, 34, 5],
            y_range=[0, 109, 10],
            x_length=7,
            y_length=5,
            axis_config={
                "color": BLUE,
                "include_numbers": True,
                "include_ticks": True,
                "stroke_width": 2, 
                "tip_width": 0.15,  
                "tip_height": 0.15,  
            },
            x_axis_config={
                "numbers_to_include": np.arange(0, 30, 5),
                "numbers_with_elongated_ticks": np.arange(0, 30, 5),
                "font_size": 18
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 100, 10),
                "numbers_with_elongated_ticks": np.arange(0, 100, 10),
                "font_size": 18
            },
        ).shift(DOWN*0.2)
        
        # Axis Labels
        x_label = Tex("Time (min)").scale(0.7).next_to(axes.x_axis.get_end(), DOWN*1.2, buff=0.5)
        y_label = Tex("Temperature (°C)").scale(0.7).rotate(90*DEGREES).next_to(axes.y_axis.get_start(), UL*1.2, buff=0.5)
        

        # 3. The graph of the function
        def cooling_law(t):
            return Ta + (T0 - Ta) * np.exp(-k * t)
        
        graph = axes.plot(cooling_law, color=GREEN)
        graph_label = axes.get_graph_label(graph, label="T(t) = T_a + (T_0 - T_a)e^{-kt}", x_val=20, direction=UR*1.2).scale(0.7)

        # 4. Animation system
        time_tracker = ValueTracker(0)
        
        # 5. Mobile poitn and its label
        moving_dot = always_redraw(
            lambda: Dot(color=RED).move_to(
                axes.c2p(
                    time_tracker.get_value(),
                    cooling_law(time_tracker.get_value())
                )
            )
        )
        
        dot_label = always_redraw(
            lambda: Tex(
                f"T = {cooling_law(time_tracker.get_value()):.1f}°C",
                font_size=24
            ).next_to(moving_dot, UR, buff=0.1)
        )
        
        # 6. Tangent Line
        def get_tangent_line():
            t = time_tracker.get_value()
            current_temp = cooling_law(t)
            derivative = -k * (current_temp - Ta)
            dx = 2
            dy = derivative * dx
            
            return Line(
                axes.c2p(t - dx, current_temp - dy),
                axes.c2p(t + dx, current_temp + dy),
                color=YELLOW,
                stroke_width=2.5
            )
        
        tangent_line = always_redraw(get_tangent_line)
        
        # 7. Derivate Label
        derivative_label = always_redraw(
            lambda: MathTex(
                r"\frac{dT}{dt} = ",
                f"{-k*(cooling_law(time_tracker.get_value()) - Ta):.2f}",
                r"\text{°C/min}"
            ).scale(0.6).next_to(axes, RIGHT).shift(UP*2)
        )
        
        # Initial animation
        self.play(Write(title))
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            title.animate.next_to(axes, UP, buff=0.8)
        )
        self.wait(0.5)
        self.play(Create(graph), run_time=2)
        self.play(Write(graph_label))
        self.play(
            FadeIn(moving_dot),
            Write(dot_label),
            run_time=1
        )
        self.play(
            Create(tangent_line),
            Write(derivative_label),
            run_time=1
        )
        self.wait(0.5)

        # 8. Principal Animation
        self.play(
            time_tracker.animate.set_value(30),
            run_time=10,
            rate_func=linear
        )
        self.wait(2)