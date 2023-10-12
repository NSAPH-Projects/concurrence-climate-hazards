# Data Analysis and Visualization Repository for Climate Co-exposure Study

This repository contains Jupyter notebooks, Python scripts, and related assets used for data analysis and visualization of for Climate Co-exposure Study.

## Data 

- **Space Resolution**: Census tract
- **Time Span**: 2006 - 2020

We incorporate climate exposure data on:
- Temperature 
- Wildfire Smoke PM2.5
- Wildfire

### Definitions:

- **Heat Day**: A day is categorized as a heat day when the average daily temperature surpasses the 95th percentile of the summer months (June, July, August, September) for that specific location across all time and it is greater than 90F. It can be denoted as 1 (occurred) or 0 (not occurred) for each day and place.
- **Wildfire Day** and **Wildfire Smoke Days**: Days with wildfire and wildfire smoke respectively.
- **Hotspot Day**: A day is defined as a hotspot day when two or more events (such as a heat day, wildfire day, and smoke PM day) co-occur. For a day to be categorized as a hotspot, the following conditions must be met:
  - Hotspot (denoted as HD for Heat Day, WF for Wildfire, and SM for Smoke PM): HD & WF & SM
  - Representation: Hotspot = 1 & 1 & 1

This helps in identifying days and places that have a high concentration of multiple climate exposure events.

## Repository Structure

### Jupyter Notebooks

1. `200_merge_data.ipynb`: Merging different data sources.
2. `250_get_metrics.ipynb`: Retrieving key metrics such as heat day and wildfire day for analysis.
3. `301_hotspots.ipynb`: Identify co-exposure hotspots. `301_stats_hotspots.ipynb`: Get stats for each of the hotspots.
4. `302_hotspots_agg_plt_svi.ipynb`: Aggregated hotspot data with SVI.
5. `303_lineplot_hotspot_trends.ipynb`: Line plots depicting hotspot trends.
6. `305_hotspot_profiling.ipynb`: Profiling of hotspots.
7. `310_bivariate_plot.ipynb`: Bivariate plotting.
8. `320_get_grid_plots.ipynb`: Creating grid plots of exposure per year.
9. `401_demographic_pies.ipynb`: Pie charts showing demographic distributions.
10. `401_demographics.ipynb`: Other charts showing demographic distributions.
11. `402_age-hotspot.ipynb`: Age-based hotspot analysis.
12. `403_income-hotspot.ipynb`: Income-based hotspot analysis.
13. `500_kmeans_hotspots.ipynb`: K-means clustering for hotspots.
14. `association_testing.ipynb`: Tests for data association.
15. `regression.ipynb`: Regression analysis.

### Python Scripts

- `bivariate_plotting.py`: Functions for bivariate plotting.
- `helper_400.py`: Helper functions for demographic analyses.
- `plotting.py`: General plotting functions.

### Directories

- `data`: Folder containing raw data and shapefiles.
- `outputs`: Location for storing generated outputs (e.g., CSVs).
- `figures`: Folder to store generated figures/plots.
- `misc`: Miscellaneous files.

### Additional Files

- `requirements.txt`: Python package dependencies for this project.

## Installation

To run the Jupyter notebooks and Python scripts, you'll need to have the required packages installed. Install them using:

```
pip install -r requirements.txt
```


## Data Dictionary

| Variable                 | Description                                                                                               |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| `date`                   | Date of the observation                                                                                   |
| `GEOID`                  | Unique identifier for the geographical region (Census Tract)                                             |
| `wfday`                  | Indicator for wildfire day (binary: 1 if wildfire day, 0 otherwise)                                       |
| `heatday`                | Indicator for heat day (binary: 1 if heat day, 0 otherwise)                                               |
| `smoke_pm_non_zero`      | Indicator for days with wildfire smoke particulate matter (PM) presence (binary: 1 if PM present, 0 otherwise)    |
| `smoke_pm_gt_five`       | Indicator for days with wildfire smoke PM > 5ug/m^3 (binary: 1 if PM > 5ug/m^3, 0 otherwise)                      |
| `hw`                     | Indicator for co-occurrence of `heatday` and `wildfire` (binary: 1 if both true, 0 otherwise)                                                              |
| `_hws`                   | Indicator if any of `heatday`, `wfday`, or `smoke_pm_non_zero` is true (binary: 1 if any true, 0 otherwise)|
| `hs`                     | Indicator for co-occurrence of `heatday` and `smoke_pm_non_zero` (binary: 1 if both true, 0 otherwise)    |
| `hws`                    | Indicator for co-occurrence of `heatday`, `wfday`, and `smoke_pm_non_zero` (binary: 1 if all true, 0 otherwise)|
| `ws`                     | Indicator for co-occurrence of `wfday` and `smoke_pm_non_zero` (binary: 1 if both true, 0 otherwise)    |
| `hs5`                    | Indicator for co-occurrence of `heatday` and `smoke_pm_gt_five` (binary: 1 if both true, 0 otherwise)                                                                   |
| `hws5`                   | Indicator for co-occurrence of `heatday`, `wfday`, and `smoke_pm_gt_five` (binary: 1 if all true, 0 otherwise)                                                                  |
| `ws5`                    | Indicator for co-occurrence of `wfday` and `smoke_pm_gt_five` (binary: 1 if both true, 0 otherwise)                                                                   |
| `heatday_2d`             | Indicator for heat day occurrence within 2 days (binary: 1 if occurred, 0 otherwise)                       |
| `smoke_pm_non_zero_2d`   | Indicator for smoke PM presence within 2 days (binary: 1 if occurred, 0 otherwise)                        |
| `wfday_2d`               | Indicator for wildfire day occurrence within 2 days (binary: 1 if occurred, 0 otherwise)                   |
| `_hws_2d`                | Indicator if any of `heatday`, `wfday`, or `smoke_pm_non_zero` occurred within 2 days (binary: 1 if any true, 0 otherwise)|
| `hs_2d`                  | Indicator for co-occurrence of `heatday` and `smoke_pm_non_zero` within 2 days (binary: 1 if both true, 0 otherwise)|
| `hws_2d`                 | Indicator for co-occurrence of `heatday`, `wfday`, and `smoke_pm_non_zero` within 2 days (binary: 1 if all true, 0 otherwise)|
| `ws_2d`                  | Indicator for co-occurrence of `wfday` and `smoke_pm_non_zero` within 2 days (binary: 1 if both true, 0 otherwise)|

**Notes**:
- `s5`: Represents wildfire smoke with a concentration greater than 5ug/m^3.
- `_2d`: Denotes that the climate co-exposure event occurred within a span of 2 days.


## Contributing

If you'd like to contribute to this repository, please fork the repository and submit a pull request.


## Contact

For questions or feedback, reach out to Kate Hu.
