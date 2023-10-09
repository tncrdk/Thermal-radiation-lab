import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from dataclasses import dataclass


R_1 = 10e3
R_3 = 100
R_2 = 37 - 6.1
R_0 = R_3 * R_2 / R_1


@dataclass
class BoltzmannData:
    voltage_multimeter: np.ndarray  # [V]
    voltage_power_supply: np.ndarray  # [V]
    current_multimeter: np.ndarray  # [A]
    current_power_supply: np.ndarray  # [A]
    voltage_intensity_sensor: np.ndarray  # [V]


@dataclass
class LeslieData:
    resistance: np.ndarray
    black: np.ndarray
    grey: np.ndarray
    mirror: np.ndarray
    white: np.ndarray


def load_boltzmann_data() -> BoltzmannData:
    filepath = Path("results_boltzmann.csv")
    results = np.loadtxt(filepath, delimiter=",")
    return BoltzmannData(
        results[:, 0], results[:, 1], results[:, 2], results[:, 3], results[:, 4] / 1000
    )


def load_leslie_data() -> LeslieData:
    filepath = Path("results_leslie.csv")
    results = np.loadtxt(filepath, delimiter=",", skiprows=1, usecols=[1, 2, 3, 4])
    return LeslieData(results[0], results[1], results[2], results[3], results[4])


def get_resistance(U: np.ndarray, I: np.ndarray) -> np.ndarray:
    return U / I


boltzmann_results = load_boltzmann_data()
power_supply_R = get_resistance(
    boltzmann_results.voltage_power_supply, boltzmann_results.current_power_supply
)
multimeter_R = get_resistance(
    boltzmann_results.voltage_multimeter, boltzmann_results.current_multimeter
)


print(power_supply_R)
print(multimeter_R)
print(multimeter_R - power_supply_R)
