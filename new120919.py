import pandas as pd

def slidingWindow(df, size, overlap=0.5):
    if size > len(df.index):
        raise Exception(
            '**Error** size of window can not be larger than input size..')
    if type(overlap) != type(0.0) or type(size) != type(0):
        raise Exception(
            '**Error** type(overlap) must be float and type(size) must be int')
    if overlap > size:
        raise Exception('**Error** overlap is larger than size...')

    print('### Number of lines in frame: ', len(df.index), ' ###')
    dfs = list()
    steps = int(size * (1 - overlap))
    for index in range(0, len(df.index) - steps, steps):
        dff = df.iloc[index:index + size].std().combine_first(
            df.iloc[index:index + size].agg(lambda x: pd.value_counts(x).index[0]))[df.columns]
        dfs.append(dff)
    print('### Number of windows: ', len(dfs), ' ###')
    return dfs

dataframes = pd.read_csv('/home/bince/Desktop/Raw Data/p-5_2015-01-08_10-18-57_0_edited.csv')
dfs = slidingWindow(dataframes, 100, 0.5)
mean_matrix = pd.concat(dfs, axis=1).T
mean_matrix.to_csv('/home/bince/PycharmProjects/csv avg/newp5sd.csv')