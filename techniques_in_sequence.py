import pandas as pd

sequence = 'NNAOAAANNNOOOANOANONANAONOAANOAONOAOAON'

if __name__ == '__main__':
    df = pd.read_csv('data/inner.csv', index_col=1, names=['Technique'])
    techniques = []
    for index in df.index:
        if index in sequence:
            techniques.append(df.at[index, 'Technique'])
    if techniques:
        print(f'sequence contains {len(techniques)} techniques:')
        for technique in techniques:
            print(technique)
    else:
        print('No techniques found')
