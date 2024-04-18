import pandas as pd

# Labelling FakeNewsCorpus Dataset
FakeNewsCorpus_df = pd.read_csv("news-data-12p.csv")
# Drop rows with missing labels
FakeNewsCorpus_df = FakeNewsCorpus_df.dropna(subset=['type'])

# Define function to label each row
def label_row(row):
    fake_labels = ['fake', 'satire', 'conspiracy', 'state', 'junksci', 'hate', 'clickbait', 'unreliable', 'bias']
    real_labels = ['political', 'reliable']

    if isinstance(row['type'], str):
        if any(label in row['type'] for label in fake_labels):
            return '0'
        elif any(label in row['type'] for label in real_labels):
            return '1'
    return None


# Apply the function to label each row
FakeNewsCorpus_df['label'] = FakeNewsCorpus_df.apply(label_row, axis=1)

# Save the labeled dataset
FakeNewsCorpus_df.to_csv("labeled-new-strictness-high.csv", index=False)


# Labelling Cr0ss-Domain LIAR Dataset
liar_df = pd.read_csv('test.tsv', sep='\t', header=None)

# Define function to label each row
liar_df[14] = liar_df.apply(lambda row: '0' if row[1] in ['false', 'pants-fire', 'barely-true', 'half-true'] else '1', axis=1)

# Save the labeled dataset
liar_df.to_csv('labeled-strictness-high-test.tsv', sep='\t', index=False, header=None)


