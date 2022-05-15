# Template Repo for ML Project

This template repo will give you a good starting point for your second project. Besides the files used for creating a virtual environment, you will find a simple example of how to build a simple model in a python script. This is maybe the simplest way to do it. We train a simple model in the jupyter notebook, where we select only some features and do minimal cleaning. The output is then stored in simple python scripts.

The data used for this is: [coffee quality dataset](https://github.com/jldbc/coffee-quality-database).

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

## Usage

In order to train the model and store test data in the data folder and the model in models run:

```bash
#activate env
source .venv/bin/activate

python example_files/train.py  
```

In order to test that predict works on a test set you created run:

```bash
python example_files/predict.py models/linear_regression_model.sav data/X_test.csv data/y_test.csv
```

## Limitations

Development libraries are part of the production environment, normally these would be separate as the production code should be as slim as possible.


### Milestone 1: Sabeeh, Stephan, Robert
- What is the value of the product? Stakeholder:
Tui Travel Agency / Predict flight delays to improve recommendation for customers and therefore generate more revenue
- What are you predicting?
Flight delays
- What evaluation metric did you choose and why?
R squared and Root Mean Squared Error (RMSE)
- What is your baseline model?
Dummy Regressor with median strategy
- What is the score of the baseline model?
RMSE: 123, R2: -0.09


```Bash
pip install airportsdata
```