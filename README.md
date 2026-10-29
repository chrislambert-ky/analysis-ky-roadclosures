# Analysis of Road Closure Data from Kentucky

> ## 🚀 This project has moved!
> Active development has continued in **[report-ky-roadclosures](https://github.com/chrislambert-ky/report-ky-roadclosures)**. This repository is no longer the recommended place to start and will receive few or no further updates.

| | |
|---|---|
| 🌐 **Live interactive report** | [chrislambert-ky.github.io/report-ky-roadclosures](https://chrislambert-ky.github.io/report-ky-roadclosures/) |
| 📦 **New repository** | [github.com/chrislambert-ky/report-ky-roadclosures](https://github.com/chrislambert-ky/report-ky-roadclosures) |
| 📖 **New README** | [README.md](https://github.com/chrislambert-ky/report-ky-roadclosures/blob/main/README.md) |

---

### Why move?

The new project combines everything from this repository (the original Python analysis and ETL) with a much more capable, interactive web experience:

- **Interactive dashboards** for closures by count and by duration, built with Apache eCharts.
- **Map view** powered by Leaflet with marker clustering to explore where closures happen.
- **Table view** with filtering and sorting (Tabulator) so you can focus on the closures you care about.
- **Enriched location data** using the KYTC Spatial API, reprocessing closures with current roadway attributes.
- **Nightly automatic updates** through GitHub Actions, so the data stays current without running any notebooks.
- **Multiple export formats** (CSV, Excel, and Parquet) from the Python ETL.
- **Nothing to install**: the report is a static site that runs in any browser, with client-side caching (IndexedDB) for fast reloads.

### What remains here

This repository is preserved for reference and contains the original Jupyter notebooks and Power BI file:

- [analysis-ky-roadclosures.ipynb](https://github.com/chrislambert-ky/analysis-ky-roadclosures/blob/main/analysis-ky-roadclosures.ipynb): the first version of the analysis.
- [analysis-ky-roadclosures_final_analysis_after_refactoring.ipynb](https://github.com/chrislambert-ky/analysis-ky-roadclosures/blob/main/analysis-ky-roadclosures_final_analysis_after_refactoring.ipynb): the refactored version.

The original README is archived at [README_ARCHIVE.md](./README_ARCHIVE.md).

---

### Disclaimers

- _While I am an employee of the Kentucky Transportation Cabinet, this analysis is not an official KYTC analysis. This project exists for me to learn and grow my skills._
- _This dataset is not a complete or comprehensive list of all road closures or damaged roadways. It only contains reports verified by the Transportation Operations Center and displayed on the GoKY website._
- **_"Know before you go" real-time traveler information is available at [GoKY](https://goky.ky.gov). KYTC also shares real-time data with [Waze](https://www.waze.com/en/live-map/)._**

**-_Chris Lambert_**
