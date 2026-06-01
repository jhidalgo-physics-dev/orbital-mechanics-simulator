"""
Orbital Mechanics Simulator

Author: John Hidalgo

Description:
Simulates two-body orbital motion using Newtonian gravity
and numerical integration.
"""

import numpy as np
import matplotlib.pyplot as plt


G = 6.67430e-11
M_EARTH = 5.972e24
R_EARTH = 6.371e6


def gravitational_acceleration(position):
    r = np.linalg.norm(position)
    return -G * M_EARTH * position / r**3


def simulate_orbit(position0, velocity0, dt, total_time):
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


def plot_orbit(positions, title, filename):
    x = positions[:, 0]
    y = positions[:, 1]

    plt.figure(figsize=(8, 8))
    ax = plt.gca()

    earth = plt.Circle((0, 0), R_EARTH, label="Earth")
    ax.add_patch(earth)

    ax.plot(x, y, linewidth=2, label="Satellite trajectory")

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x position [m]")
    ax.set_ylabel("y position [m]")
    ax.set_title(title)
    ax.grid(True)
    ax.legend()

    plt.savefig(filename, dpi=300)
    plt.show()


def main():
    altitude = 400e3
    position0 = np.array([R_EARTH + altitude, 0.0])

    orbital_radius = np.linalg.norm(position0)
    circular_speed = np.sqrt(G * M_EARTH / orbital_radius)

    dt = 10.0
    total_time = 4 * 90 * 60

    circular_velocity = np.array([0.0, circular_speed])
    circular_positions = simulate_orbit(
        position0,
        circular_velocity,
        dt,
        total_time
    )

    plot_orbit(
        circular_positions,
        "Circular Low Earth Orbit Simulation",
        "figures/circular_orbit.png"
    )

    elliptical_velocity = np.array([0.0, 1.15 * circular_speed])
    elliptical_positions = simulate_orbit(
        position0,
        elliptical_velocity,
        dt,
        total_time
    )

    plot_orbit(
        elliptical_positions,
        "Elliptical Orbit Simulation",
        "figures/elliptical_orbit.png"
    )


if __name__ == "__main__":
    main()
