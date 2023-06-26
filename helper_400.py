import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def set_sns_style():
    # Set the style
    sns.set_style("whitegrid")

    # Set the figure size
    plt.figure(figsize=(8, 6))

    # Set the color palette
    sns.set_palette("colorblind")

    # Set the font family
    plt.rcParams["font.family"] = "PT Serif"

    # Set the font size
    plt.rcParams["font.size"] = 12
    sns.set_context("paper")


def get_var_name(short):
    options = {
        "wfday": "wildfire",
        "heatday": "heat",
        "smoke_pm_non_zero": "wildfire smoke",
        "smoke_pm_gt_five": "wildfire smoke (over 5 μg/m\u00b3)",
        "hw": "heat-wildfire",
        "hs": "heat-smoke",
        "hws": "heat-wildfire-smoke",
        "ws": "wildfire-smoke",
        "hs5": "heat-smoke (over 5 μg/m\u00b3)",
        "hws5": "heat-wildfire-smoke (over 5 μg/m\u00b3)",
        "ws5": "wildfire-smoke (over 5 μg/m\u00b3)",
    }
    return options.get(short)


hotspots = {
    "wfday": {"func": pd.cut},
    "heatday": {"func": pd.qcut},
    "ws": {"func": pd.cut},
    "hw": {"func": pd.cut},
    "hs": {"func": pd.qcut},
    "hws": {"func": pd.cut},
    "hs5": {"func": pd.qcut},
    "hws5": {"func": pd.cut},
    "ws5": {"func": pd.cut},
    "smoke_pm_non_zero": {"func": pd.qcut},
    "smoke_pm_gt_five": {"func": pd.qcut},
}


def get_cut_vars(hspt, col):
    if hspt in ["wfday"]:
        return hotspots[hspt]["func"](
            col,
            bins=pd.IntervalIndex.from_tuples(
                [(0, 1), (1, 10), (10, 50), (50, 100), (100, 1000)]
            ),
        )
    elif hspt in ["ws", "hw", "hws", "hws5", "ws5"]:
        return hotspots[hspt]["func"](
            col,
            bins=pd.IntervalIndex.from_tuples(
                [(0, 1), (1, 10), (10, 20), (20, 50), (50, 1000)]
            ),
        )
    else:
        return hotspots[hspt]["func"](col, 5, labels=False, duplicates="drop")


def get_svi_df(cols):
    df = pd.read_csv("data/California.csv", usecols=cols, dtype={"FIPS": int})
    return df


def get_exposure_df():
    exposure = pd.read_parquet("outputs/hotspots_per_fips_rolling.parquet")

    exposure = exposure[
        [
            "wfday",
            "GEOID",
            "heatday",
            "smoke_pm_non_zero",
            "smoke_pm_gt_five",
            "hw",
            "hs",
            "hws",
            "ws",
            "hs5",
            "hws5",
            "ws5",
        ]
    ]
    exposure.head()
    exposure = exposure.groupby("GEOID").sum()
    exposure = exposure.reset_index()
    return exposure


def plot_qbar(
    exposure_per_category,
    hotspot,
    figname=False,
    xlabel="Exposure level (higher is worse)",
    legloc="lower right",
):
    """Plots the bar chart"""

    # Melt the DataFrame to long format
    epc = exposure_per_category.reset_index().melt(
        id_vars="exposure_category", var_name="Hue", value_name="Proportion"
    )
    if hotspot in ["wfday", "ws", "hw", "hws", "hws5", "ws5"]:
        xlabel = "Days (intervals) of exposure"

    # Plot the bar chart using Seaborn
    plt.figure(figsize=(5, 4))
    sns.barplot(data=epc, x="exposure_category", y="Proportion", hue="Hue")

    plt.title(
        "Quantile-based demographic discretization \n per "
        + get_var_name(hotspot)
        + " exposure days"
    )
    plt.ylabel("Proportion of the demographic group (%)")
    plt.xlabel(xlabel)
    plt.legend(title="Group", loc=legloc)
    plt.xticks(rotation=0)
    # ax.set_yscale('log')
    plt.tight_layout()
    if figname:
        plt.savefig("figures/qbar_" + figname + "_" + hotspot + ".png")
    plt.show()


def __main__():
    pass
