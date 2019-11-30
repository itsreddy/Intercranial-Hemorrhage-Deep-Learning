import pandas as pd


##PATHS##
full_labels_filepath = "Data/RSNA_full_labels.csv"
sample_filepath = "Data/sample_paths.csv"
destination_filepath = "Data/"

##START##
full_labels = pd.read_csv(full_labels_filepath)
sample_labels = pd.read_csv(sample_filepath)

samples = []
for i in sample_labels.values:
    samples.append(i[0].split(".")[0])
sample_labels = samples

sample_df = full_labels.loc[full_labels['ID'].isin(sample_labels)]
sample_df.to_csv(destination_filepath + 'RSNA_sample_labels.csv', index=False)