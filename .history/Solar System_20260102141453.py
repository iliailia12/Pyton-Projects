import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System Simulation")

# Create the Sun (a big yellow circle)
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)  # Adjust the size of the Sun
sun.penup()
sun.goto(0, 0)  # Position the sun at the center

# Create a list of planets with their orbital radius and color
planets_data = [
    {"name": "Mercury", "color": "gray", "radius": 30, "speed": 0.05},
    {"name": "Venus", "color": "yellow", "radius": 50, "speed": 0.04},
    {"name": "Earth", "color": "blue", "radius": 70, "speed": 0.03},
    {"name": "Mars", "color": "red", "radius": 100, "speed": 0.02},
]

# Create the planet turtles
planets = []
for data in planets_data:
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(data["color"])
    planet.penup()
    planet.goto(data["radius"], 0)  # Position the planets at their orbital radius
    planet.speed(0)  # Fastest drawing speed
    planet.orbit_radius = data["radius"]
    planet.orbit_speed = data["speed"]
    planets.append(planet)

# Orbiting logic
while True:
    for planet in planets:
        # Get current position
        x = planet.orbit_radius * math.cos(planet.orbit_speed)
        y = planet.orbit_radius * math.sin(planet.orbit_speed)
        
        # Move the planet
        planet.goto(x, y)
        
        # Increase the orbital angle
        planet.orbit_speed += 0.01

    screen.update()  # Update the screen to reflect changes
    turtle.delay(20)  # Delay to control speed

turtle.done()
