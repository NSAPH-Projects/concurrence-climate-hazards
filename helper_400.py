import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict


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
        "_hws": "heat or wildfire or smoke",
        "ws": "wildfire-smoke",
        "hs5": "heat-smoke (over 5 μg/m\u00b3)",
        "hws5": "heat-wildfire-smoke (over 5 μg/m\u00b3)",
        "ws5": "wildfire-smoke (over 5 μg/m\u00b3)",
    }
    if short[-2:] == "2d":
        return options[short[:-3]] + " (2-day)"
    return options.get(short)


# hotspots_init = {
#     "wfday": {"func": pd.cut},
#     "heatday": {"func": pd.qcut},
#     "ws": {"func": pd.cut},
#     "hw": {"func": pd.cut},
#     "hs": {"func": pd.qcut},
#     "hws": {"func": pd.cut},
#     "hws_": {"func": pd.qcut},
#     "hs5": {"func": pd.qcut},
#     "hws5": {"func": pd.cut},
#     "ws5": {"func": pd.cut},
#     "smoke_pm_non_zero": {"func": pd.qcut},
#     "smoke_pm_gt_five": {"func": pd.qcut},
# }

# # Create defaultdict from existing dictionary, with 'other' as the default value
# hotspots = defaultdict(lambda: {"func": pd.cut}, hotspots_init)


def get_title(hspt):
    """Returns the title for a given hotspot"""

    prefix = ""
    if "wfday" in hspt:
        prefix = "The "
    else:
        prefix = "Quantile-based "
    return (
        prefix + get_var_name(hspt) + " exposure-day discretization \n per demography"
    )


def get_cut_vars(hspt, col):
    """Returns the cut variables for a given hotspot"""

    if "_hws" in hspt:
        return pd.qcut(col, 5, labels=["I", "II", "III", "IV", "V"], duplicates="drop")
    if hspt in ["hw", "hws", "ws", "hws5", "ws5", "hws_2d", "ws_2d"]:
        return pd.cut(
            col,
            bins=pd.IntervalIndex.from_tuples(
                [(0, 1), (1, 10), (10, 20), (20, 30), (30, 1000)], closed="left"
            ),
        )
    if "wfday" in hspt:
        return pd.cut(
            col,
            bins=pd.IntervalIndex.from_tuples(
                [(0, 1), (1, 10), (10, 50), (50, 100), (100, 1000)], closed="left"
            ),
        )
    return pd.qcut(col, 5, labels=["I", "II", "III", "IV", "V"], duplicates="drop")


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
    sns.barplot(
        data=epc,
        x="exposure_category",
        y="Proportion",
        hue="Hue",
        errorbar="sd",
        capsize=0.4,
        errcolor=".5",
    )

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
