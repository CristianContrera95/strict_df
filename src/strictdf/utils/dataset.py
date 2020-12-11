"""
Author: Cristian Contrera <cristiancontrera95@gmail.com>
Date: 10/12/2020
License: MIT
"""

import requests
import pandas as pd
from pathlib import Path
import os


def load_credit_data():
    """
    Download credit_data file from S3 and load it with pandas in DataFrame
    :return: pd.DataFrame
    """
    local_file = Path.home() / '.strict_df' / 'datasets' / 'credit_date.csv'

    if local_file.exists():
        return pd.read_csv(str(local_file))
    else:
        os.makedirs(local_file.parent)

    url = 'https://s3-us-west-2.amazonaws.com/fligoo.data-science/TechInterviews/StrictDF/data/credit-data.csv'
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_file, 'wb') as fp:
            for chunk in r.iter_content(chunk_size=8192):
                fp.write(chunk)

    return pd.read_csv(str(local_file))
