"""
======================================================
PHYS20161 Assignment 1: Bouncy Ball

This programme calculates the number of bounces a ball makes from a starting
height to a minimum height and the time taken to complete these bounces. In
addition to this the code also performs extra calculations based on the user
input.

By: Luca Vicaria, UID: 10828724
7/10/2022
======================================================
"""

import math
import numpy as np
import matplotlib.pyplot as plt

import utils
from utils import Style


def get_initial_height_from_user() -> float:
    """
    Get initial height from user and validate it.

    Returns:
    ---------------
    h_init: float
        Initial height in metres

    """
    while True:
        temp = input(Style['YELLOW']
                     + "Please enter the initial height in meters (h): "
                     + Style['RESET'])
        if utils.validate_float_input(temp):
            h_init = float(temp)
            if utils.validate_positive_input(h_init):
                break

    return h_init


def get_minimum_height_from_user(h_init: float) -> float:
    """
    Get minimum height from user and validate it.

    Parameters:
    ---------------
    h_init: float
        Initial height in meters

    Returns:
    ---------------
    h_min: float
        Height below which we will stop counting the number of bounces

    """
    while True:
        temp = input(Style['YELLOW']
                     + "Please enter minimum height in meters "
                       f"({utils.H_MIN}): " + Style['RESET'])
        if utils.validate_float_input(temp):
            h_min = float(temp)
            if utils.validate_positive_input(h_min):
                if utils.validate_smaller_than_input(h_min, h_init):
                    break

    return h_min


def get_eta_from_user() -> float:
    """
    Get efficiency coefficient from user and validate it.

    Returns:
    ---------------
    eta: float
        Efficiency coefficient

    """

    while True:
        temp = input(Style['YELLOW']
                     + "Please enter the energy efficiency coefficient "
                       f"({utils.ETA}): " + Style['RESET'])
        if utils.validate_float_input(temp):
            eta = float(temp)
            if utils.validate_positive_input(eta):
                if utils.validate_smaller_than_input(eta, 1.0):
                    break
    return eta


def get_gravity_from_user() -> float:
    """
    Get the value of the gravitational field strength from user and validate
    it.

    Returns:
    ---------------
    grav_value: float
        Value used for the gravitational field strength

    """
    answer = utils.validate_y_n_input("Do you want to alter the value of g "
                                      "which is currently set to 9.81 "
                                      f"ms{8315:c}{178:c}? (y/n): ")
    change_grav = answer == "y"

    if change_grav:
        while True:
            temp = input(Style['YELLOW'] + "Please enter the value of the "
                                           "gravitational field strength in "
                                           f"ms{8315:c}{178:c} (g): " +
                         Style['RESET'])
            if utils.validate_float_input(temp):
                grav_value = float(temp)
                if utils.validate_positive_input(grav_value):
                    break

    else:
        grav_value = 9.81

    return grav_value


def get_ball_mass_from_user() -> float:
    """
    Gets the ball mass from user and validate it.

    Returns:
    ---------------
    ball_mass: float
        Mass of the ball (kg)
    """

    answer = utils.validate_y_n_input("Would you also like to calculate the "
                                      "total energy dissipated? (y/n) ")
    calc_energy = answer == "y"
    ball_mass = 0.0

    if calc_energy:
        while True:
            temp = input(Style['YELLOW'] + "Please enter the mass of the ball "
                                           "in kilograms (Kg): "
                         + Style['RESET'])
            if utils.validate_float_input(temp):
                ball_mass = float(temp)
                if utils.validate_positive_input(ball_mass):
                    break

    return ball_mass


def get_inputs() -> (float, float, float, float, float):
    """
    Gets user inputs and validate them accordingly.

    Returns:
    ---------------
    h_init: float
        Initial height (m)
    h_min: float
        Minimum height (m)
    eta: float
        Efficiency coefficient
    grav_value: float
        Gravitational field strength
    ball_mass: float
        Mass of the ball (kg)
    """
    h_init = get_initial_height_from_user()
    h_min = get_minimum_height_from_user(h_init)
    eta = get_eta_from_user()
    grav_value = get_gravity_from_user()
    ball_mass = get_ball_mass_from_user()

    return h_init, h_min, eta, grav_value, ball_mass


def bounce(h_init: float, eta: float, h_min: float, grav_value: float) \
        -> (float, float):
    """
    Calculation for 1 complete bounce. Returns the total time of the bounce and
    the new height.

    Parameters:
    ---------------
    h_init: float
        Initial height in meters
    eta: float
        Efficiency coefficient
    grav_value: float
        Gravitational field strength
    h_min: float
        Minimum height

    Returns:
    ---------------
    t_total: float
        Total time in seconds (2 decimal places)
    h_up: float
        Final height in meters
    """
    # Time to hit the floor is sqrt(2*h*g)
    t_down = math.sqrt(2 * h_init / grav_value)
    # Using v = v0 + at, we have 0 = v_up - gt, and conservation of energy:
    # mgh = mv^2/2

    h_up = h_init * eta
    v_up = math.sqrt(2 * grav_value * h_up)
    t_up = v_up / grav_value

    # As per spec, only add t_up if h_up is higher than h_min
    if h_up > h_min:
        t_total = t_down + t_up
    else:
        t_total = t_down

    return t_total, h_up


def calc_energy_dissipated(h_start: float, h_final: float,
                           grav_value: float, mass_ball: float) -> float:
    """
    Calculates the total energy dissipated.

    Parameters:
    ---------------
    h_start: float
        Initial height in meters
    h_final: float
        Final height in meters
    grav_value: float
        Gravitational field in m/s^2
    mass_ball: float
        Mass of the ball (kg)

    Returns:
    ---------------
    energy_lost: float
        Total energy lost during bounces
    """
    energy_lost = mass_ball * grav_value * (h_start - h_final)

    return energy_lost


def perform_calculation(h_start: float, h_min: float, eta: float,
                        grav_value: float, mass_ball: float) -> (int, float):
    """
    Performs the  overall calculations for a bouncing ball.

    Parameters:
    ---------------
    h_start: float
        Initial height in meters
    h_min: float
        Minimum height in meters
    eta: float
        Efficiency coefficient
    mass_ball: float
        Mass of the ball (kg)
    grav_value: float
        Gravitational field in m/s^2

    Returns:
    ---------------
    n_bounces: int
        Number of bounces
    t_total: float
        Total time in seconds (2 decimal places)
    energy_lost: float
        Total energy lost during bounces
    """

    h_curr = h_start
    n_bounces = 0
    t_total = 0.0

    # Bounce until h is smaller than h_min
    # Increment bounces and sum times.
    while h_curr > h_min:
        time, h_curr = bounce(h_curr, eta, h_min, grav_value)
        t_total += time
        if h_curr >= h_min:
            n_bounces = n_bounces + 1
        else:
            break

    if mass_ball > 0:
        energy_dissipated = calc_energy_dissipated(h_start, h_curr, grav_value,
                                                   mass_ball)
    else:
        energy_dissipated = 0

    return n_bounces, t_total, energy_dissipated


def present_results(n_bounces: int, t_total: float, energy_lost: float,
                    mass_ball: float = 0) -> None:
    """
    Performs the  overall calculations for a bouncing ball.

    Parameters:
    ---------------
    n_bounces: int
        Number of bounces
    t_total: float
        Total time in seconds (2 decimal places)
    energy_lost: float
        Total energy lost during bounces
    mass_ball: float
        Mass of the ball (kg)

    """
    print()
    print(Style['GREEN'] + f"Number of bounces: {n_bounces}" + Style['RESET'])
    print(Style['GREEN'] + f"Total time: {t_total:.2f} seconds" +
          Style['RESET'])
    if mass_ball > 0:
        print(Style['GREEN'] + f"Energy Lost: {energy_lost:.2f} joules" +
              Style['RESET'])

    print()


def plot_graph(h_init, grav_value, n_bounces, eta, t_total, h_min):
    """
    Plots a graph of height against time.

    Parameters:
    ---------------
    h_init: float
        Initial height in meters
    grav_value: float
        Gravitational field in m/s^2
    n_bounces: int
        Number of bounces
    eta: float
        Efficiency coefficient
    t_total: float
        Total time in seconds (2 decimal places)
    h_min: float
        Minimum height in meters
    """
    answer = utils.validate_y_n_input("Do you want to plot a graph of height "
                                      "against time? (y/n): ")
    plot_graphs = answer == "y"

    if plot_graphs:

        plt.title('Height of the ball with increasing time.')
        plt.xlabel('Time (s)')
        plt.ylabel('Height (m)')

        plt.axvline(t_total, 0, 1, color='r', linestyle='--')
        plt.axhline(h_min, 0, 1, color='r', linestyle='--')
        plt.text(t_total, h_min, '$h_{min}$', verticalalignment='center')
        plt.text(t_total, 0, 'total t', verticalalignment='top')

        time_axis = np.linspace(0, math.sqrt(2 * h_init / grav_value), 100)
        height_axis = [h_init - 0.5 * grav_value * i ** 2 for i in time_axis]
        plt.plot(time_axis, height_axis, color='black')

        start_time = math.sqrt(2 * h_init / grav_value)

        for i in range(n_bounces + 1):
            time_axis = np.linspace(start_time, start_time + 2 * math.sqrt(
                2 * h_init * eta ** (i + 1) / grav_value), 100)
            time_range = np.linspace(0, 2 * math.sqrt(
                2 * h_init * eta ** (i + 1) / grav_value), 100)
            height_axis = [math.sqrt(2 * grav_value * h_init * (
                        eta ** (i + 1))) * time - 0.5 * grav_value * time ** 2
                 for time in time_range]
            plt.plot(time_axis, height_axis, color='black')

            start_time += 2 * math.sqrt(
                2 * h_init * eta ** (i + 1) / grav_value)

        plt.show()


def loop():
    """
    Keep looping until user quits.
    """
    input("To perform a calculation press any key or [CTRL+C] to quit at any "
          "point.")
    print()
    new_calc = True
    while new_calc:
        h_init, h_min, eta, grav_value, mass_ball = get_inputs()
        n_bounces, t_total, energy_lost = perform_calculation(h_init,
                                                              h_min,
                                                              eta,
                                                              grav_value,
                                                              mass_ball)

        present_results(n_bounces, t_total, energy_lost, mass_ball)
        plot_graph(h_init, grav_value, n_bounces, eta, t_total, h_min)

        answer = utils.validate_y_n_input("Do you want to run the code again? "
                                          "(y/n) ")
        new_calc = answer == "y"
        print()
    print("Bye!")


def main():
    """
    Entry point for the programme
    """
    utils.print_title()
    utils.print_explanation()
    loop()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        utils.print_cancelled_by_user()
        