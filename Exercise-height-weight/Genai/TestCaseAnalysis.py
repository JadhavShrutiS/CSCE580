# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 10:47:53 2025

@author: shrut
"""

from gaico import Experiment
#%%
#non data provision comparison
llm_responses = {
    "ChatGPT": "49.5, 63.6, 79.4",
    "POE": "49.5, 63.5, 80.5",
    "DeepSeek R1": "49.5, 63.6, 79.4",
}

reference_answer = "53.0, 70.0, 82.0"

#%% #uncomment section to run comparison for prediction responses after data provision
''' 
llm_responses = {
    "ChatGPT": "56.90, 74.50, 92.00",
    "POE": "53.00, 70.00, 81.50",
    "DeepSeek R1": "68.60, 76.40, 84.10",
}

reference_answer = "69.92, 83.97, 98.02"
'''
#%%

# 1. Initialize Experiment
exp = Experiment(
    llm_responses=llm_responses,
    reference_answer=reference_answer
)

# 2. Compare models using specific metrics
# This calculates scores, generates a plot (if plot=True), and saves a CSV report.
results_df = exp.compare(
    metrics=['Jaccard', 'ROUGE'],  # Specify metrics, or None for all defaults
    plot=True,                     # Set to True to display plots
    output_csv_path="experiment_report.csv",
    #custom_thresholds={"Jaccard": 0.6, "ROUGE_rouge1": 0.35} # Optional
)