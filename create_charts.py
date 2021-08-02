import pandas as pd
import matplotlib.pyplot as plt
import datetime

now = datetime.datetime.now()

def create():
    final_data = pd.read_csv("/home/james/plant-sensor/logging.csv")

    final_data = final_data.groupby(["date"], as_index=False)

    final_data = final_data.tail(30)

    plt.figure()

    plt.title("Plant status (daily, last 30 days) accurate as of {}".format(now.strftime("%d %B, %Y (%H:%M:%S)")))

    plt.xlabel("Time")

    plt.ylabel("Moisture level")

    ax = plt.gca()

    final_data.plot(kind="line", x="date", y="m1", color="green", ax=ax)

    final_data.plot(kind="line", x="date", y="m2", color="orange", ax=ax)

    final_data.plot(kind="line", x="date", y="m3", color="blue", ax=ax)

    plt.savefig("plant_data.png")
