from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def eval_metrics(train, train_pred, test, test_pred):

    print('Training Evaluation Metrics')
    print('Mean_Absolute_error (MAE): ', mean_absolute_error(train, train_pred))
    print('Mean_square_error (MSE): ', mean_squared_error(train, train_pred))
    print('Root_Mean_square_error (RMSE) : ', mean_squared_error(train, train_pred) **0.5)
    print('R2_error (R2) : ', r2_score(train, train_pred))
    print('')
    print('---'*5)
    print('Test Evaluation Metrics')
    print('Mean_Absolute_error (MAE): ', mean_absolute_error(test, test_pred))
    print('Mean_square_error (MSE): ', mean_squared_error(test, test_pred))
    print('Root_Mean_square_error (RMSE) : ', mean_squared_error(test, test_pred) **0.5)
    print('R2_error (R2) : ', r2_score(test, test_pred))

    #return {
    #    print('---'*5),
    #    print('Mean_Absolute_error (MAE): ', MEA), 
    #    print('Mean_square_error (MSE): ', MSE)
    #    }

    #return {
    #    'Mean_Absolute_error (MAE)' : mean_absolute_error(target, prediction),
    #    'Mean_square_error (MSE)' : mean_squared_error(target, prediction),
    #    'Root_Mean_square_error (RMSE)' : mean_squared_error(target, prediction) **0.5,
    #    'R2_error (R2)' : r2_score(target, prediction)
    #}