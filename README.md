# Sequence Alignment

## Overview
This project implements sequence alignment algorithms using different approaches, including a basic and an efficient implementation. The project analyzes CPU time and memory usage to compare the performance of these implementations.

## Project Structure
```
Sequence_Alignment/
│── Code/
│   ├── basic.py          # Basic sequence alignment implementation
│   ├── efficient.py      # Optimized sequence alignment implementation
│   ├── plot.py           # Script to visualize performance metrics
│   ├── basic.sh          # Shell script to execute basic.py
│   ├── efficient.sh      # Shell script to execute efficient.py
│   ├── CPU Time.png      # Graph comparing CPU time of implementations
│   ├── Memory Usage.png  # Graph comparing memory usage of implementations
│
│── datapoints/
│   ├── in1.txt           # Sample input file
│   ├── in10.txt          # Additional test case
│   ├── ...               # More input test cases
```

## Prerequisites
- Python 3.x
- Required Python libraries (install using `requirements.txt` if available)

## Installation
Clone the repository and navigate into the project directory:
```sh
git clone <repository_url>
cd Sequence_Alignment
```

## Usage
Run the basic implementation:
```sh
python Code/basic.py < input_file
```

Run the optimized implementation:
```sh
python Code/efficient.py < input_file
```

Run the performance visualization script:
```sh
python Code/plot.py
```

## Performance Analysis
- The project includes CPU time and memory usage graphs comparing the two implementations.
- `CPU Time.png` and `Memory Usage.png` illustrate the computational efficiency of each approach.

## Contributing
Feel free to open an issue or submit a pull request if you find any improvements or bugs.

## License
This project is licensed under the MIT License.