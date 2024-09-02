# Satellite Communication Simulator

## Overview
The Satellite Communication Simulator is a Python-based tool designed to model and analyze satellite communications. It simulates satellite orbits, calculates link budgets, and visualizes signal strength over time, providing insights into satellite communication systems.

## Features
- Orbital mechanics simulation for satellite movement
- Path loss calculation based on distance and frequency
- Link budget analysis for satellite-to-ground communication
- Visualization of received signal power over time
- Customizable parameters including orbit height, transmit power, and frequency

## Requirements
- Python 3.7+
- NumPy
- Matplotlib

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/Eniiyanu/Satellite-Communication-Simulator.git
   ```
2. Navigate to the project directory:
   ```
   cd satellite-comm-simulator
   ```
3. Install the required packages:
   ```
   pip install numpy matplotlib
   ```

## Usage
To run the simulator, execute the main script:

```
python satellite_simulator.py
```

You can modify the simulation parameters in the script:

```python
simulator = SatelliteCommsSimulator(orbit_height=1000, transmit_power=10, frequency=2.4e9)
simulator.simulate_link(ground_station_lat=0, ground_station_lon=0)
```

## Example Output
The simulator generates a plot showing the received power over time for a 24-hour period:

[Insert a screenshot of the output plot here]

## Future Improvements
- Implement multiple satellite constellations
- Add atmospheric effects on signal propagation
- Include different types of orbits (LEO, MEO, GEO)
- Integrate real-world satellite data

## Contributing
Contributions to improve the simulator are welcome. Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
Oluwaferanmi Oladepo - oladepo.oluwaferanmi@studentambassadors.com

Project Link: [https://github.com/Eniiyanu/Satellite-Communication-Simulator](https://github.com/Eniiyanu/Satellite-Communication-Simulator)

