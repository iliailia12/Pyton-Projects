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
sun.shapesize(4)  # Sun size
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
    planet.angle = 0  # Initial angle for each planet
    planets.append(planet)

# Add moons for Earth and Mars as an example
earth_moon = turtle.Turtle()
earth_moon.shape("circle")
earth_moon.color("gray")
earth_moon.penup()
earth_moon.goto(70, 10)  # Earth's initial position
earth_moon.speed(0)
earth_moon.orbit_radius = 10  # Radius from Earth
earth_moon.orbit_speed = 0.15
earth_moon.angle = 0

mars_moon = turtle.Turtle()
mars_moon.shape("circle")
mars_moon.color("lightgray")
mars_moon.penup()
mars_moon.goto(100, -10)  # Mars' initial position
mars_moon.speed(0)
mars_moon.orbit_radius = 12  # Radius from Mars
mars_moon.orbit_speed = 0.2
mars_moon.angle = 0

# Orbiting logic with spirals and moons
while True:
    for planet in planets:
        # Update position of each planet in a circular orbit
        x = planet.orbit_radius * math.cos(math.radians(planet.angle))
        y = planet.orbit_radius * math.sin(math.radians(planet.angle))

        planet.goto(x, y)

        # Gradually increase orbital radius for spiral effect
        planet.orbit_radius += 0.02
        planet.angle += planet.orbit_speed  # Update angle for orbit

    # Update the Earth's moon position
    earth_x = (70 + earth_moon.orbit_radius) * math.cos(math.radians(earth_moon.angle))
    earth_y = (70 + earth_moon.orbit_radius) * math.sin(math.radians(earth_moon.angle))
    earth_moon.goto(earth_x, earth_y)
    earth_moon.angle += earth_moon.orbit_speed  # Moon's orbital motion

    # Update the Mars' moon position
    mars_x = (100 + mars_moon.orbit_radius) * math.cos(math.radians(mars_moon.angle))
    mars_y = (100 + mars_moon.orbit_radius) * math.sin(math.radians(mars_moon.angle))
    mars_moon.goto(mars_x, mars_y)
    mars_moon.angle += mars_moon.orbit_speed  # Moon's orbital motion

    screen.update()  # Update the screen to reflect changes
    turtle.delay(10)  # Delay to control speed

turtle.done()
