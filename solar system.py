
# Import the pygame library
import pygame
import math
import os

# Initialize Pygame
pygame.init()

# Set the window size
size = (800, 800)
screen = pygame.display.set_mode(size)

# Set the title of the window   
pygame.display.set_caption("SOLAR SYSTEM")

# Load the images for each planet
sun_image = pygame.image.load(os.path.join("planets", "sun.png"))
mercury_image = pygame.image.load(os.path.join("planets", "mercury.png"))
venus_image = pygame.image.load(os.path.join("planets", "venus.png"))
earth_image = pygame.image.load(os.path.join("planets", "earth.png"))
mars_image = pygame.image.load(os.path.join("planets", "mars.png"))
jupiter_image = pygame.image.load(os.path.join("planets", "jupiter.png"))
saturn_image = pygame.image.load(os.path.join("planets", "saturn_ring.png"))
uranus_image = pygame.image.load(os.path.join("planets", "uranus.png"))
neptune_image = pygame.image.load(os.path.join("planets", "neptune.png"))

# Load the background image
background_image = pygame.image.load(os.path.join("planets", "space.png"))

# Reducing image size of the planets
sun_image = pygame.transform.scale(sun_image, (80, 80))
mercury_image = pygame.transform.scale(mercury_image, (15, 15))
venus_image = pygame.transform.scale(venus_image, (25, 25))
earth_image = pygame.transform.scale(earth_image, (30, 30))
mars_image = pygame.transform.scale(mars_image, (20, 20))
saturn_image = pygame.transform.scale(saturn_image, (100, 40))
uranus_image = pygame.transform.scale(uranus_image, (35, 35))
jupiter_image = pygame.transform.scale(jupiter_image, (50, 50))
neptune_image = pygame.transform.scale(neptune_image, (40, 40))

# Create a list of planets with their properties
planets = [
    {"name": "Sun", "image": sun_image, "radius": 200, "x": 400, "y": 390, "vx": 0, "vy": 0},
    {"name": "Mercury", "image": mercury_image, "angle": 0, "distance": 65, "period": 0.24, "radius": 10},
    {"name": "Venus", "image": venus_image, "angle": 0, "distance": 90, "period": 0.62, "radius": 20},
    {"name": "Earth", "image": earth_image, "angle": 0, "distance": 125, "period": 1, "radius": 25},
    {"name": "Mars", "image": mars_image, "angle": 0, "distance": 155, "period": 1.88, "radius": 15},
    {"name": "Jupiter", "image": jupiter_image, "angle": 0, "distance": 195, "period": 11.86, "radius": 45},
    {"name": "Saturn", "image": saturn_image, "angle": 0, "distance": 260, "period": 29.5, "radius": 40},
    {"name": "Uranus", "image": uranus_image, "angle": 0, "distance": 320, "period": 84, "radius": 30},
    {"name": "Neptune", "image": neptune_image, "angle": 0, "distance": 370, "period": 164.8, "radius": 35}
]

# initialize the positions of the planets
for planet in planets[1:]:
    planet["x"] = planets[0]["x"] + math.cos(planet["angle"]) * planet["distance"]
    planet["y"] = planets[0]["y"] + math.sin(planet["angle"]) * planet["distance"]

# Create a list of past positions for each planet
for planet in planets[1:]:
    planet["past_positions"] = []

# Set the clock to control framerate
clock = pygame.time.Clock()
fps = 30

# Run the game loop
running = True
while running:

    # Handle events in the game loop
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with background image
    screen.blit(background_image, (0, 0))

    
    # Display the sun at the center
    image_rect = planets[0]["image"].get_rect()
    image_rect.center = (int(planets[0]["x"]), int(planets[0]["y"]))
    screen.blit(planets[0]["image"], image_rect)
   
    # Draw and update the position of the planets
    for planet in planets[1:]:

        # Increment the angle based on the period of the planet 
        # so that it completes one orbit in the given period
        planet["angle"] += 0.05 * (1 / planet["period"])

        # Calculate the position of the planet based on the angle
        planet["x"] = planets[0]["x"] + math.cos(planet["angle"]) * planet["distance"]
        planet["y"] = planets[0]["y"] + math.sin(planet["angle"]) * planet["distance"]

        # Add the current position to the list of past positions
        # and draw a trail behind the planet
        planet["past_positions"].append((planet["x"], planet["y"]))

        # Draw the trail
        for i in range(1, len(planet["past_positions"])):
            pygame.draw.line(screen, (153,153,0), planet["past_positions"][i-1], planet["past_positions"][i], 1)

        # Get the rect for the planet's image and set its center to the planet's position   
        image_rect = planet["image"].get_rect()
        image_rect.center = (int(planet["x"]), int(planet["y"]))
        
        # Draw the planet's image
        screen.blit(planet["image"], image_rect)

    # Update the display
    pygame.display.update()

    # Wait for the specified number of frames per second
    clock.tick(fps)

# Quit pygame
pygame.quit()