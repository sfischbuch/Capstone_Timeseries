# Capstone_Timeseries


The Question: 

Can I create an ensemble method of 6 different ARIMA models that is able to predict outcomes  more consistently than any of them individually.

The Data: 

I have raw data in pickled form. Unpickled the raw data takes the form of a column of financial values and their associated timestamp. In addition to the raw data I have separate feeds(also pickled) from 6 ARIMA model variations.  These feeds include their associated predictions, and statistics associated with those predictions (RMSE, R**2, confidence intervals etc) for a two month period.

MVP: 

Develop an ensemble system voting system grouping the existing ARIMA models. Possible methods include using a neural net (Committee of Machines), an ensemble average, different forms of boosting, I’ll try subsampling first and then once the framework is built modify it to receive different forms of data so it can be used with greater universality.

MVP+  

From the raw data make an RNN predictor (7th model).

MVP++ 

(a)Create a web presence using Flask.
(b) Fold the 7th Model into original ensemble
