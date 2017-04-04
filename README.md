# Machine and Deep Learning Code and Notes
#### Code and Notes on Machine and Deep Learning Algorithms/Techniques using various python libraries. 
#### Credit must be given to Python Machine Learning by Sebastian Raschka, Machine Learning Mastery by Jason Brownlee, Scikit Learn Documentation, Introduction to Machine Learning with Python by Andreas C Muller and Sarah Guido, Tensorflow Site and Documentation.  These resources were instrumental in my learning process.
### Please Note:  Most of the python scripts are labeled with algorithm(s) and libraries used.  Notes and my thought process are commented at the top and between code.  Data sets can be found in MNIST and Data Sets for Code folder (provided by UCI data repository, Kaggle and Project Gutenburg).  Table of contents will indicate which algorithm(s), description, libraries and data set is being used for algorithm.
### Table of Contents
#### Machine Learning Scripts
1. linear_regression_sgd.py - Linear Regression with Stoichastic Gradient Descent using the red_wine_quality.csv data set (provided by UCI data repository)
2. logistic_regression_sgd.py - Logistic Regression with Stoichastic Gradient Descent using the diabetes.csv data set (provided by UCI data repository)
3. decision_tees.py - Decision Tree using the signals_sonar_classify.csv data set (provided by UCI data repository)
4. decision_trees_xg_boosting.py - Demonstration of XG Boosting and plotting with scikit learn, pandas, numpy and matplotlib using the train_xgboost.csv (provided by Kaggle)
5. bagging_decision_trees.py - Demonstration of bagging and bootstrap aggregation using the signals_sonar_classify.csv data set (provided by UCI data repository)
6. random_forests.py - Demonstration of the random forest algorithm using the signals_sonar_classify.csv data set (provided by UCI data repository)
7. naive_bayes.py - Naive Bayes algorithm using the diabetes.csv data set (provided by UCI data repository)
8. k-nearest_neighbors.py - K-Nearest Neighbors algorithm using the iris.data classic data set
9. basic_perceptron.py - Perception algorithm using the signals_sonar_classify.csv data set (provided by UCI data repository)
10. classification_tensorflow.py - Classification with tensorflow using the MNIST data set filtered and obtained with the input_data.py file
11. ex1_tensorflow.py - Basic file outlining structure (weights, biases, tensorflow structure) using tensorflow
#### Deep Learning Scripts
1. basic_imageclass.py - Image Classification using Convolutional Neural Network with tensorflow using the MNIST data set filtered and obtained with the input_data.py file
2. basic_ann_tensforflow.py - First neural network using tensorflow, numpy and plotted with matplotlib
3. optimizers_notes_tensorflow.py - Notes on using optimizers in tensorflow
4. overfitting_tensorflow.py - Dealing with overfitting data using the dropout function in tensorflow
5. placeholders_tensorflow.py - How to use placeholder variables and pass values on after output
6. cnn_rnn_lstm_sequence_classification_keras.py - Convolutional Neural Net with LSTM Recurrent Neural Net for sequence classification using the IMDB movie review data set which is accessed using a built in Keras function
7. rnn_lstm_text_generation_keras.py - LSTM Recurrent Neural Net text generation using keras and sherlock_asib.txt data set (provided by Project Gutenburg) 
8. rnn_lstm_time_series_keras.py - LSTM Recurrent Neural Net time series prediction with keras, pandas, scikit learn, numpy and matplotlib using   data set
9. rnn_classification_tensorflow - Classification with Recurrent Neural Net using tensorflow and MNIST data set
10. rnn_regression_tensorflow - Regression with Recurrent Neural Net using tensorflow and MNIST data set
11. save_restore_tensorflow - Saving and restoring variables using tensorflow
12. session_init_tensorflow - Basic session initialization using tensorflow
13. variables_tensorflow - dealing with and initializing variables using tensorflow
14. visualize_net_basic_tensorflow.py - basic version of visualizing network using tensorflow's built in tool called tensorboard
15. visualizing_net_added_features_tensorflow.py - includes some added features, visualizing network using tensorflow's built in tool called tensorboard
#### Data Sets
1. MNIST - Developed by Yann LeCun, Corinna Cortes, Google Labs, Christopher J.C. Burges, contains a database of handwritten digits, a training set of 60,000 examples, and a test set of 10,000 examples. 
2. red_wine_quality.csv - Developed by Paulo Cortezo, A. Cerdeira, F. Almeida, T. Matos and J. Reis, contains twelve attributes including wine quality score from 0-10
3. diabetes.csv - Developed by National Institute of Diabetes and Digestive and Kidney Diseases, contains nine attributes including class variable 0-1 (0 negative and 1 positive for diabetes)
4. signals_sonar_classify.csv - Developed by Terry Sejnowski, each pattern is a set of 60 numbers in the range 0.0 to 1.0. Each number represents the energy within a particular frequency band, integrated over a certain period of time
5. train_xgboost.csv - Developed by the Otto Group, describes the 93 obfuscated details of more than 61,000 products grouped into 10 product categories
6. iris.data - Developed by R.A. Fisher, contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other
7. sherlock_asib.txt - Written by Sir Arthur Conan Doyle and prepared by Project Gutenburg, contains text for A Scandal in Bohemia
