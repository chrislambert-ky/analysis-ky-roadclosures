# Analysis of Road Closure Data from Kentucky

### Personal Disclaimer:
- _While I am an employee of the Kentucky Transportation Cabinet, this analysis of road closure data is not an official KYTC analysis.  This project exists for me to learn and grow my skills in web development (HTML, CSS, Javascript)._
- _My background is in:_
  - IT Project Manager / Data Analyst
  - SQL (Google BigQuery, Oracle)
  - BI Tools (Looker Studio, Tableau, PowerBI).
  - Python ETLs
### Data Disclaimer:
- _There are many factors that contribute to road closures that are not disclosed in this dataset. This dataset is not a complete or comprehensive list of all road closures and/or damaged roadways.  These are only the reports that were verified by the Transportatioin Operatations Center in real-time and displayed on the GoKY website. As an employee of KYTC, I want to promote safety and mobility for everyone and I would encourage you to please utilize the following resources:_<br>
- **_"Know before you go" Real-Time Traveler Information can be found at [GoKY](https://goky.ky.gov)_**
- **_KYTC also shares real-time data with [Waze](https://www.waze.com/en/live-map/)._**

**-_Chris Lambert_**

---

### Project Overview
The project aims to analyze road closure data provided by the Kentucky Transportation Cabinet (KYTC). The primary objective is to identify trends in road closures to better understand network resiliency during periods of extreme weather events.

Thre are two primary notebooks in this repository:

* [analysis-ky-roadclosures.ipynb](https://github.com/chrislambert-ky/analysis-ky-roadclosures/blob/main/analysis-ky-roadclosures.ipynb) is my first version.  During the development process, I worked through each year independently and developed code to clean only that one year.  I did this to avoid any frustrations with trying to create code that tried to do too much at once.
* [analysis-ky-roadclosures_final_analysis_after_refactoring.ipynb](https://github.com/chrislambert-ky/analysis-ky-roadclosures/blob/main/analysis-ky-roadclosures_final_analysis_after_refactoring.ipynb) was produced after refactoring.  I received feedback concerning my documentation and the need to utilize functions to produce cleaner, more efficient code.  Both notebooks produce the same results but this notebook will display cleaner code with a slightly different process of ingesting, cleaning, and reporting on the same data.

---

### Technical Insight

- **Python Libraries:** To begin the project, I started by utilizing VS Code, Python and Jupyter Notebook extensions, and a Python virtual environment with libraries such as pandas, pyarrow, matplotlib and requests for data importing, cleaning, and analysis.
- **Sources:** Road closure data was sourced from the Transportation Operations Center (TOC) of KYTC in CSV format. This data source continues to be updated during severe weather events.
- **Access Requirements:** No special access was needed.  This data source is freely provided by KYTC.
- **Data Cleaning:** Standardized column names, data types (date/time), and parsed/extracted latitude and longitude, removed carriage returns from comments, etc.
- **Data Integration:** Merged/concatenated multiple data sources.
- **Summary/Statistics:** Calculated descriptive statistics to understand the distribution of road closures by District, County, and Road Type.
- **Data Visualization:** Utilized Matplotlib to create visualizations for exploring patterns and trends in road closure data.
- **Documentation:** Documented the analysis process, including data preprocessing steps, exploratory data analysis, and insights gained.
- **Reporting:** Prepare a report/presentation summarizing key findings, insights, and visual outputs from the analysis.
- **Optional Visualization / Reporting:** Leveraged PowerBI to produce a more interactive and visually appealing collection of dashboards.
- **Optional Summaries/Statistics (incomplete):** These may appear in future versions.  I hope to perform a more detailed analysis of closures by adding roadway elevations and weather conditions.
    - For historic weather data, I plan to learn and utilize the National Weather Service [NWS API](https://www.weather.gov/documentation/services-web-api)
    - To obtain more etailed roadway information, such as roadway elevation at the point of the closure, I will utilize KYTC's Intelligent Transportation Systems (ITS) API.

---

### Methodology
- Imported/loaded road closure data directly from hosted web server into Pandas.
- Parsed out the Latitude and Longitude by stripping unneeded hyperlink characters.
- Produced standalone latitude and longitude columns/fields, which is preferred for mapping in most BI software.
- Standardized timestamps to assist with calculating duration.
- Removed carriage returns in the comments, which causes problems during importing/exporting to/from a CSV.
- Modified the duration calculation to show hours as float64, making it easier to use in popular BI tools.
- Summarized the results by year, county, and roadway using record counts and caculated durations.
- OPTIONAL:  I hope to develop an overall score that takes into consideration the frequency and duration of events in future versions.



---

### Code Kentucky Required Features (here are my choices):
Code Kentucky provided a list of requirements but then allowed developers to choose from a list of options to satisfy the requirements.  These are my choices to meet those requirements:
- Feature list #1 choice: Read multiple data files (JSON, CSV, Excel, etc.)
- Feature list #2 choice: Clean the data and perform a pandas merge, then calculate some new values based on the new data set.
- Feature list #3 choice: Make 3 matplotlib (or another plotting library) visualizations to display your data.
- Feature list #4 choice: Utilize a Python virtual environment and include instructions in your README on how the user should set one up.
- Feature list #5 choice: Annotate code with markdown cells in Jupyter Notebook, write clear code comments, and have a well-written README.md.

#### *I've chosen the following optional features:*
- Feature #3 (optional): Tableau and/or PowerBI visualizations.
    - Download PowerBI from here: [PowerBI](https://powerbi.microsoft.com/en-us/downloads/)
    - There is also a PowerBI file in the repo for anyone who downloads PowerBI
    - [PowerBI PDF Export](https://github.com/chrislambert-ky/analysis-ky-roadclosures/blob/main/analysis-ky-roadclosures-powerbi-pdf-export.pdf) for anyone that doesn't want to use PowerBI
- Feature #4 (optional): Build a custom data dictionary.
    - The Road Closure Data Dictionary has been added directly into the notebooks.
    - The Road Closure Data Dictionary can also be found here, as a standalone document: <br>
[Road Closure Data Dictionary](https://github.com/chrislambert-ky/analysis-ky-roadclosures/blob/main/kytc-closures-datadictionary.md)

---

### The following libraries were used for this project:

- pandas
- pyarrow
- jupyterlab
- notebook
- openpyxl
- matplotlib
- numpy

Notes:  I added in Jupyter Labs and Notebook libraries as a convenience to anyone who may not have VS Code with Jupyter extensions installed.

---

### Setting up a Python Virtual Environment

A Python virtual environment is a self-contained directory that contains a Python installation for a specific project. Using virtual environments helps manage dependencies and isolate project-specific packages. Here's how to set up a Python virtual environment:

### Prerequisites

- Make sure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/).

### Instructions

1. **Open a Terminal/Command Prompt**

    - On Windows, you can use Command Prompt or PowerShell.
    - On Unix-based systems (Linux, macOS), use the terminal.

2. **Navigate to Your Project Directory**

    ```bash
    cd path/to/your/project
    ```

3. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

    This command creates a virtual environment named 'venv' in your project directory.

4. **Activate the Virtual Environment**

    - On Windows (Command Prompt):

        ```bash
        venv\Scripts\activate
        ```

    - On Windows (PowerShell):

        ```bash
        .\venv\Scripts\Activate
        ```

    - On Unix-based systems:

        ```bash
        source venv/bin/activate
        ```

    After activation, your terminal prompt should change, indicating that the virtual environment is active.

5. **Install Dependencies**

    Now that the virtual environment is active, you can install project-specific dependencies without affecting the global Python installation.

    ```bash
    pip install -r requirements.txt
    ```

    Replace `requirements.txt` with the actual name of your requirements file.

6. **Deactivate the Virtual Environment**

    When you're done working on your project, deactivate the virtual environment.

    ```bash
    deactivate
    ```

---
