# Flight Delay Prediction Challenge (group project)


<a><img align="center" src="https://thehill.com/wp-content/uploads/sites/2/2021/07/airlines-flights_istock_biz.jpg?w=1280" height="50%" width="80%" /></a>

<br>

## Description
Tunisair Airline is interested in reducing their flight delays, therefore they are looking for a solution based on Machine Learning techniques.

Flight delays not only irritate air passengers and disrupt their schedules but also cause :

- a decrease in efficiency
- an increase in capital costs, reallocation of flight crews and aircraft
- an additional crew expenses
- As a result, on an aggregate basis, an airline's record of flight delays may have a negative impact on passenger demand.

<br>

## Dataset

Flight Data: [Tunisair Airline dataset](https://assets.zindi.africa/competitions/ai-tunisia-hack-5-predictive-analytics-challenge-2/data)

Airports Data: [Worldwide airports dataset](https://pypi.org/project/airportsdata/)

<br>

## Evaluation
The metric used for this challenge is Root Mean Square Error.

<br>

## Stakeholder Aim: 
Traveling agency like *TUI* wants their passenger to make the bookings with no or few hours delay while traveling with Tunisair Airline, therefore this study by Tunisair Airline will help traveling agency to assist passengers with minimum hassle.

## Approach

- Detailed EDA is performed in order to understand busiest airport flight patterns, flight durations, International/National flight numbers and hourly flight patterns

- Only flight with 1 day delay has been considered

- Naive Baseline model

- Predicted flight delays based on their average delay time (RMSE) using different ML techniques (comparative study for ML models)

---
## Requirements and Environment

Requirements:
- pyenv with Python: 3.9.8

Environment: 

For installing the virtual environment you can either use the Makefile and run `make setup` or install it manually with the following commands: 

```Bash
pyenv local 3.9.8
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```


```Bash
pip install airportsdata
```