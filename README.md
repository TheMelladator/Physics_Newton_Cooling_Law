# Newton's Law of Cooling - Computational Simulation

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Manim](https://img.shields.io/badge/Manim-Community-yellowgreen)](https://www.manim.community/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A comprehensive Python project featuring both computational simulation and visual animation of Newton's law of cooling. Includes:
- Interactive temperature plots
- Parameter analysis
- Professional animations with Manim
- Theoretical model visualization

## Featured Animation
![Cooling Law Animation](media/videos/graph/Cooling_Law.gif)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Theory](#theory)
- [Hardware Setup](#hardware-setup)
- [Results](#results)
- [Next Steps](#nextspteps)
- [Project Structure](#project-structure)
- [License](#license)

### Features
- **Computational Simulation**:
  - Interactive temperature plots
  - Parameter analysis with Jupyter Notebook
  - Theoretical model visualization
- **Experimental Setup**:
  - Real-time data acquisition with ESP32 + DS18B20
  - Circuit schematics and frimware
  - Raw data comparison (experimental vs theoretical)
- **Visualization**:
 - Professional animations with Manim
 - Comparative graphs (simulation/experimental)

### Simulation Module
- Interactive Jupyter notebook
- Parameter customization
- Experimental data comparison

### Animation Module
- Dynamic temperature point tracking
- Real-time tangent line visualization
- Derivative value display
- Professional mathematical typesetting


## Installation
1. Clone the repository:
   
```bash
git clone https://github.com/TheMelladator/Physics_Newton_Cooling_Law.git
cd Physics_Newton_Cooling_Law
```

2. For computational simulation:
   
```bash
pip install numpy matplotlib jupyterlab manim
```
3. For Experimental setup:
   - Install Arduino IDE or PlatformIO.
   - Add ESP32 board support (guide here).
   - Install required libaries:
     ```bash
     arduino-cli lib install "OneWire" "DallasTemperaute"
     ```

## Usage
### Computational Simulation
Run the simulation in Jupyter Notebook:

```bash
jupyter notebook src/Newton_cooling.ipynb
```

You'll be prompted to enter:
- Ambient temperature (`Tm`) in Kelvin or Celsius
- Initial object temperature (`T0`) in Kelvin or Celsius
- Cooling coefficient (`r`) in 1/second
    
Example:

```python
Tm = 294.15 #21°C
T0 = 573.15 #300°C
r = 0.2
```
Run the animation in your favorite IDE

```bash
manim -phd animation/grahp.py Cooling_Law
```



## Theory
The differential equation modeled is:

```markdown
$$
\frac{dT}{dt}=-r(T-T_{environment})
$$
```

With analytical solution:

```markdown
$$
T(t)=T_m+(T_0-T_m)e^{-rt}
$$
```
The animation visualizes:
- The solution curve
- Instantaneous rate of change (derivative)
- Tangent line at each point
- Temperature decay process

## Hardware Setup
### Componentes
- ESP32 (Wifi/Bluetooth MCU)
- DS18B20 (Temperature sensor)
- 4.7k\Omega (Pull-up for DS18B20)
- Breadboard and jumper wires

### Circuit Schematic
![Circuit Diagram](experimental/schematics/circuit.png)
*Figure 2*: Connection diagram for ESP32 and DS18B20.

### Firmware
- Code location: 'experimental/firmware/esp_cooling.ino'
- Dependecies: 'OneWire' and 'DallasTemperature' libraries.
- Data output: Serial monitor (CSV format)
  
## Results
![Simulation Results](figures/newton_cooling.png)
*Figure 1*: Temperature decay with `T0` = 300°, `Tm` = 21°C, `r` = 0.2 

## Project Structure

```markdown
/Physics_Newton_Cooling_Law/
├── animation/              # Animation scripts
│   └── graph.py       # Main cooling law animation
├── src/
│   └── Newton_cooling.ipynb  # Main simulation notebook
├── data/                     # Experimental/simulated data (in progress)
├── media/                    # Rendered animations
│   └──grahp/
│       └──Cooling_Law.mp4
├── figures/                  # Generated plots
│   └── newton_cooling.png     
├── LICENSE
└── README.md                 # This file
```

## Next Steps
- [] Add experimental data validation.
- [x] Animated experimet.
- [] Develop parameter optimization module
- [] Create comparative animation (theory vs experimental data)
- [] Add interactive GUI for simulation parameters
  
## License
Distributed under MIT License
