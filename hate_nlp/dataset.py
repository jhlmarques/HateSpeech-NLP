import pandas as pd



class HateSpeechDataset:

    def __init__(self, path_csv, preprocess=None) -> None:
        df = pd.read_csv(path_csv)
        df = self._relabel_dataframe(df)
        df = self._remap_columns(df)
        assert len(df.columns) == 2
        self.df_raw = df
        self.preprocess = preprocess

    def __len__(self):
        return len(self.df_raw)

    def _remap_columns(self, df):
        df = df.rename(columns={df.columns[0] : 'text', df.columns[1] : 'labels'})
        return df

    def _relabel_dataframe(self, df):
        return df

    def get_dataframe(self):
        if self.preprocess:
            return self.preprocess(self.df_raw)
        else:
            return self.df_raw

class ToldBRDataset(HateSpeechDataset):

    def _relabel_dataframe(self, df):
        hatespeech_cls = (df.iloc[:, 1:] > 0).any(axis=1)
        df = pd.concat([df.iloc[:,0], hatespeech_cls], axis=1)
        return df

class HateBRDataset(HateSpeechDataset):
    
    def _relabel_dataframe(self, df):
        df = df[['instagram_comments', 'offensive_language']]
        df = df.astype({'offensive_language' : bool})
        return df
        