# %%
import pandas as pd
from glob import glob

# read single csv file

single_file_acc = pd.read_csv(
    "../../data/raw/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Accelerometer_12.500Hz_1.4.4.csv"
)

single_file_gyro = pd.read_csv(
    "../../data/raw/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Gyroscope_25.000Hz_1.4.4.csv"
)


files = glob("../../data/raw/MetaMotion/*.csv")


def read_data_from_files(files):

    acc_df = pd.DataFrame()
    gyro_df = pd.DataFrame()

    acc_set = 1
    gyro_set = 1

    for f in files:
        file_name = f.split("\\")[1]
        label_elements = file_name.split("-")
        participant = label_elements[0]
        exercise = label_elements[1]
        category = label_elements[2].rstrip("123").rstrip("_MetaWear_2019")
        df = pd.read_csv(f)
        df["participant"] = participant
        df["category"] = category
        df["exercise"] = exercise

        if "Accelerometer" in f:
            df["set"] = acc_set
            acc_set += 1
            acc_df = pd.concat([acc_df, df])
        else:
            df["set"] = gyro_set
            gyro_set += 1
            gyro_df = pd.concat([gyro_df, df])

    acc_df["epoch (ms)"] = pd.to_datetime(acc_df["epoch (ms)"], unit="ms")
    acc_df["time (01:00)"] = pd.to_datetime(acc_df["time (01:00)"], format="ISO8601")
    gyro_df["epoch (ms)"] = pd.to_datetime(gyro_df["epoch (ms)"], unit="ms")
    gyro_df["time (01:00)"] = pd.to_datetime(gyro_df["time (01:00)"], format="ISO8601")

    acc_df.index = acc_df["epoch (ms)"]
    gyro_df.index = gyro_df["epoch (ms)"]

    del acc_df["epoch (ms)"]
    del acc_df["time (01:00)"]
    del acc_df["elapsed (s)"]

    del gyro_df["epoch (ms)"]
    del gyro_df["time (01:00)"]
    del gyro_df["elapsed (s)"]

    return acc_df, gyro_df


acc_df, gyro_df = read_data_from_files(files)


df = pd.concat([acc_df.iloc[:, :3], gyro_df], axis=1)

df.info()

df.columns = [
    "acc_x",
    "acc_y",
    "acc_z",
    "gyro_x",
    "gyro_y",
    "gyro_z",
    "participant",
    "category",
    "label",
    "set",
]

sampling = {
    "acc_x": "mean",
    "acc_y": "mean",
    "acc_z": "mean",
    "gyro_x": "mean",
    "gyro_y": "mean",
    "gyro_z": "mean",
    "participant": "last",
    "category": "last",
    "label": "last",
    "set": "last",
}


# split by day

days = [g for n,g in df.groupby(pd.Grouper(freq='D'))]
data_resampled = pd.concat([df.resample(rule='200ms').apply(sampling).dropna() for df in days])
data_resampled

data_resampled['set'] = data_resampled['set'].astype(int)
data_resampled.info()

data_resampled.to_pickle(r'../../data/interim/01_data_processed.pkl')

# %%
