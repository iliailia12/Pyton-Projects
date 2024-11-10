import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
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
    {"name": "Jupiter", "color": "orange", "radius": 140, "speed": 0.01},
    {"name": "Saturn", "color": "lightyellow", "radius": 180, "speed": 0.009},
    {"name": "Uranus", "color": "lightblue", "radius": 220, "speed": 0.008},
    {"name": "Neptune", "color": "blue", "radius": 260, "speed": 0.007},
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

# Orbiting logic with spiral effect
angle = 0
while True:
    for planet in planets:
        # Calculate new x and y positions for the spiral orbit
        x = planet.orbit_radius * math.cos(math.radians(angle))
        y = planet.orbit_radius * math.sin(math.radians(angle))

        # Move the planet to the new position
        planet.goto(x, y)

        # Increase orbital radius slowly for the spiral effect
        planet.orbit_radius += 0.02  # Gradually increase the radius for spiral effect

        # Update angle to simulate rotation (planets will move in a circular path)
        angle += planet.orbit_speed

    screen.update()  # Update the screen to reflect changes
    turtle.delay(10)  # Delay to control speed of the animation

turtle.done()
