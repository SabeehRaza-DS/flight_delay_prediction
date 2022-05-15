from matplotlib.pyplot import axis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function to visualize True vs. Predicted Values as well as True Values vs. Residuals  
def error_plot(y_train, y_pred_train, y_test, y_pred_test):
    # Calculate residuals
    residuals_train = y_train - y_pred_train
    residuals_test = y_test - y_pred_test

    # Plot true values vs. predicted values for Train data
    fig, axes = plt.subplots(2,2, figsize=(15, 15))
    axes[0, 0].set_title("TRAIN: True vs. predicted values", weight="bold")
    axes[0, 0].set(xlabel="True values", ylabel="Predicted values")
    a1 = sns.regplot(ax=axes[0, 0], x=y_train, y=y_pred_train, line_kws={"color": "black"})
    

    # Plot true values vs. residuals for Train data
    axes[0, 1].set_title("TRAIN: Predicted values vs. residuals", weight="bold")
    axes[0, 1].set(xlabel="Predicted values", ylabel="Residuals")
    a2 = sns.regplot(ax=axes[0, 1], x=y_pred_train, y=residuals_train, line_kws={"color": "black"})
    

    # Plot true values vs. predicted values for Test data
    axes[1, 0].set_title("TEST: True vs. predicted values", weight="bold")
    axes[1, 0].set(xlabel="True values", ylabel="Predicted values")
    a3 = sns.regplot(ax=axes[1, 0], x=y_test, y=y_pred_test, color="g", line_kws={"color": "black"})
    

    # Plot true values vs. residuals for Test data
    axes[1, 1].set_title("TEST: Predicted values vs. residuals", weight="bold")
    axes[1, 1].set(xlabel="Predicted values", ylabel="Residuals")
    a4 = sns.regplot(ax=axes[1, 1], x=y_pred_test, y=residuals_test, color="g", line_kws={"color": "black"})

    return a1,a2,a3,a4
    