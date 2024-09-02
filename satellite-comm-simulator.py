import numpy as np
import matplotlib.pyplot as plt

class SatelliteCommsSimulator:
    def __init__(self, orbit_height, transmit_power, frequency):
        self.orbit_height = orbit_height  # km
        self.transmit_power = transmit_power  # Watts
        self.frequency = frequency  # Hz
        self.c = 3e8  # Speed of light in m/s

    def calculate_path_loss(self, distance):
        wavelength = self.c / self.frequency
        return 20 * np.log10((4 * np.pi * distance) / wavelength)

    def simulate_link(self, ground_station_lat, ground_station_lon):
        # Simplified orbit simulation
        time = np.linspace(0, 24*60*60, 1000)  # 24 hours in seconds
        satellite_lat = 45 * np.sin(2 * np.pi * time / (24*60*60))
        satellite_lon = 45 * np.cos(2 * np.pi * time / (24*60*60))
        
        distances = np.sqrt((satellite_lat - ground_station_lat)**2 + 
                            (satellite_lon - ground_station_lon)**2 + 
                            self.orbit_height**2)
        
        path_losses = self.calculate_path_loss(distances * 1000)  # Convert km to m
        received_power = self.transmit_power - path_losses

        plt.figure(figsize=(10, 6))
        plt.plot(time / 3600, received_power)
        plt.xlabel('Time (hours)')
        plt.ylabel('Received Power (dBW)')
        plt.title('Satellite Link Budget over Time')
        plt.grid(True)
        plt.show()

# Usage
simulator = SatelliteCommsSimulator(orbit_height=1000, transmit_power=10, frequency=2.4e9)
simulator.simulate_link(ground_station_lat=0, ground_station_lon=0)
