# Planetary Orbit Simulation with Pygame

This is a simple 2D planetary orbit simulation written in Python using [Pygame](https://www.pygame.org/).  
It models the Sun and the major planets (plus Pluto) using Newtonian gravity, showing their orbits with smooth, fading white trails.  

---

## Features

- **Realistic physics** using Newton's law of gravitation.
- Visualizes planets orbiting the Sun in 2D.
- Each planet has a unique fading white trail showing its orbital path.
- Trail length varies by planet to better illustrate inner vs outer orbits.
- Zoom toggle (`Z` key) to switch between full system view and zoomed-in view.
- Smooth animation at 60 FPS.
- Adjustable parameters for scale, zoom, and timestep.

---

## Installation

1. Make sure you have Python 3 installed.  
2. Install the `pygame` library if you don't have it yet:

```bash
pip install pygame
