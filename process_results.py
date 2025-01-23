import glob

import pandas

def process_frame(frame, train_portions=[1]):
    if "Unnamed: 0" in frame.columns:
        del frame["Unnamed: 0"]

    if "train portion" in frame.columns:
        frame = frame[frame["train portion"].isin(train_portions)]

    frame["linguistic competencies"] = frame["linguistic subfield"]
    del frame["linguistic subfield"]

    frame = frame.groupby(["probing dataset", "linguistic phenomena", "probe type", "probe", "linguistic competencies"]).mean().reset_index()
    if "seed" in frame.columns:
        del frame["seed"]

    if "train portion" in frame.columns:
        del frame["train portion"]

    return frame

def read_data(path, train_portions=[1]):
    frame = pandas.read_csv(path)
    return process_frame(frame, train_portions)


flash_holmes_results = read_data("data/holmes_results_f1_raw_free.csv", train_portions=[0.03125])


result_files = glob.glob("/Users/tresi/Downloads/roberta-different-layers/*")
for result_file in result_files:
    results = pandas.read_csv(result_file, index_col=0)

    pivot_results = results.pivot_table(index=['probing_dataset'], columns=["model_name"], values="score").reset_index()
    pivot_results = pivot_results[pivot_results["probing_dataset"].isin(flash_holmes_results["probing dataset"])]

    flash_holmes_results = flash_holmes_results.set_index("probing dataset").join(pivot_results.set_index("probing_dataset")).reset_index()

flash_holmes_results.to_csv("combined_results.csv")
print()