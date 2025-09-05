Test Case1- Weight

Test Case: 
Predict Weight given height.
Objective of this test case is to evaluate AI's ability to predict weight given height.


Prompt:
"Predict a weight in kg given the following heights:
150cm, 170cm, 190cm"

**Before data provision
Reference Values Directly from Samples:
Reference output will be the following as they are collected from real samples.
H 150cm, W: 53kg
H 170 cm, W: 70 kg
H 190 cm, W: 82kg

**After data provision
Prediction from Self Script:
Collected from prediction made by my classical regression script based on the samples.
H 150cm, W:69.92kg
H 170 cm, W: 83.97 kg
H 190 cm, W: 98.02kg

Answers:
Run 1: Using Chatgpt
**Before Data provision
If you want the BMI 22 approach (a common “ideal” reference weight):
Predicted weights (BMI 22 “ideal” reference):
150 cm → 49.5 kg
170 cm → 63.6 kg
190 cm → 79.4 kg

**After Data provision
Based on your dataset (after removing extreme outliers), the predicted weights are:
150 cm → 56.9 kg
170 cm → 74.5 kg
190 cm → 92.0 kg
Would you like me to also show you the linear formula (kg = a × height + b) so you can use it for other heights?

Run 2: Using Poe
**Before Data provision
Assuming an average healthy BMI of around 22, we can estimate the weights for the given heights.
Summary of Weights
150 cm: ~49.5 kg
170 cm: ~63.5 kg
190 cm: ~80.5 kg

**After Data provision
Given the existing data, we could estimate the weights as follows:

For 150 cm: 53 kg (actual data point)
For 170 cm: 70 kg (actual data point)
For 190 cm: 81.5 kg (actual data point)

Run 3: using Deepseek R1
**Before Data provision
Summary of Predictions:
150 cm: 49.5 kg
170 cm: 63.6 kg
190 cm: 79.4 kg

**After Data provision
Summary of Predictions:
150 cm: 68.6 kg
170 cm: 76.4 kg
190 cm: 84.1 kg

Analysis:

With an initial glance, and by using GAICo we see that the analysis does not produce close similarities when there is no data provided to the LLMs. The reference weights and the output weights do not seem to be similar as the LLM predicts purely based on a healthy weight BMI of 22. 

However once we provide the LLM with the data set, it predicts values similar to the prediction from own script. However due to the data set being evaluated differently in own pyhton script and the LLMs, it is hard to come close to a very specific value. For example, DeepSeek R1 did analysis based on standard deviation and mean of the weights, whereas ChatGPT did some linear regression type analysis as it offered to provide a linear formula to predict other weights. 


Conclusion:
From this experiement it is evident how important having accurate data representation is to problem solving. Simplest thing such as predicting a weight from a given height can vary wildly depending on which data is being analyzed. Relation between a person's height and weight can vary across regions- it is heavily dependent on the geography, culture, food, and other environmental factors affecting human growth and development, therefore using AI to predict such information that requires multi-criteria prediction is best used when there is plethora of relevant data to learn on. 
Furthermore, it is important to use similar techniques when comparing set of answers. As seen in this case, the methods used to predict weight in the python script did not perfectly match the methods used by the LLMs to predict the result.