"""
Orbital Mechanics Simulator

Author: John Hidalgo

Description:
Simulates two-body orbital motion using Newtonian gravity
and numerical integration.

This project models a satellite orbiting Earth and visualizes
the resulting trajectory.

Skills demonstrated:
- Classical mechanics
- Numerical integration
- Orbital mechanics
- Scientific computing
- Python visualization
"""

import numpy as np
import matplotlib.pyplot as plt


# Constants
G = 6.67430e-11          # gravitational constant [m^3 kg^-1 s^-2]
M_EARTH = 5.972e24      # Earth mass [kg]
R_EARTH = 6.371e6       # Earth radius [m]


def gravitational_acceleration(position):
    """
    Calculate gravitational acceleration from Earth.

    Parameters
    ----------
    position : np.ndarray
        Position vector [x, y] in meters.

    Returns
    -------
    np.ndarray
        Acceleration vector [ax, ay] in m/s^2.
    """
    r = np.linalg.norm(position)
    return -G * M_EARTH * position / r**3


def simulate_orbit(position0, velocity0, dt, total_time):
    """
    Simulate orbital motion using Euler-Cromer integration.

    Parameters
    ----------
    position0 : np.ndarray
        Initial position vector [x, y] in meters.

    velocity0 : np.ndarray
        Initial velocity vector [vx, vy] in m/s.

    dt : float
        Time step in seconds.

    total_time : float
        Total simulation time in seconds.

    Returns
    -------
    positions : np.ndarray
        Array of position vectors over time.
    """
    steps = int(total_time / dt)

    positions = np.zeros((steps, 2))
    velocities = np.zeros((steps, 2))

    positions[0] = position0
    velocities[0] = velocity0

    for i in range(1, steps):
        acceleration = gravitational_acceleration(positions[i - 1])
        velocities[i] = velocities[i - 1] + acceleration * dt
        positions[i] = positions[i - 1] + velocities[i] * dt

    return positions


def plot_orbit(positions):
    """
    Plot orbital trajectory around Earth.
    """
    x = positions[:, 0]
    y = positions[:, 1]

    earth = plt.Circle((0, 0), R_EARTH, label="Earth")

    plt.figure(figsize=(8, 8))
    ax = plt.gca()

    ax.add_patch(earth)
    ax.plot(x, y, linewidth=2, label="Satellite trajectory")

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x position [m]")
    ax.set_ylabel("y position [m]")
    ax.set_title("Two-Body Orbital Motion Around Earth")
    ax.grid(True)
    ax.legend()

    plt.show()


def main():
    """
    Run example orbital simulation.
    """

    # Initial altitude above Earth's surface
    altitude = 400e3  # 400 km, similar to low Earth orbit

    # Initial position
    position0 = np.array([R_EARTH + altitude, 0.0])

    # Circular orbit speed approximation
    orbital_radius = np.linalg.norm(position0)
    circular_speed = np.sqrt(G * M_EARTH / orbital_radius)

    # Initial velocity perpendicular to radius
    velocity0 = np.array([0.0, circular_speed])

    # Simulation parameters
    dt = 10.0                 # seconds
    total_time = 2 * 90 * 60  # about two 90-minute orbits

    positions = simulate_orbit(position0, velocity0, dt, total_time)

    plot_orbit(positions)


if __name__ == "__main__":
    main()
