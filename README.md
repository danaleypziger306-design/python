# Titanic Passenger Analysis Dashboard

An interactive Streamlit dashboard for exploring insights from the Titanic passenger dataset. The UI is in Hebrew and supports filtering by gender and passenger class.

## Features

- **Interactive filters** — Filter passengers by gender (`Sex`) and travel class (`Pclass`)
- **Filtered data table** — Browse the filtered passenger records
- **Survival by gender** — Bar chart showing survival rate by gender
- **Age distribution** — Histogram of passenger ages grouped by survival status
- **Survival by class** — Bar chart showing survival rate by passenger class

## Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JonathanZouari/python.git
   cd python
   ```

2. Install dependencies:

   ```bash
   pip install streamlit pandas plotly
   ```

## Usage

Run the dashboard with Streamlit:

```bash
streamlit run titanic_dasboard.py
```

Streamlit opens the app in your browser (typically at `http://localhost:8501`).

## Data Source

Passenger data is loaded from the public Titanic dataset hosted on GitHub:

`https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`

The dataset is cached locally after the first load for faster reloads.

## Project Structure

```
python/
├── titanic_dasboard.py   # Main Streamlit dashboard application
└── README.md
```

## License

This project is open source. See the repository for details.
