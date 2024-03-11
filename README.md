# Analysis of Road Closure Data from Kentucky

**Disclaimer:** _While I am an employee of the Kentucky Transportation Cabinet, this analysis of road closure data is not an official KYTC analysis.  There are many factors that contribute to road closures that are not disclosed in this dataset.  This dataset is not a complete or comprehensive list of all road closures and/or damaged roadways.  These are only the reports that were verified in real-time and displayed on the GoKY website.  As an employee of KYTC, I want to promote safety and mobility for everyone and I would encourage you to please utilize the following resources:_

* _"Know before you go" Real-Time Traveler Information can be found at <a href="https://goky.ky.gov" target="_blank">GoKY</a>_
* _Road Closure listings and hourly email notifications can be found at <a href="https://www.kytc.ky.gov/Pages/Weather-Related-Road-Closures.aspx" target="_blank">KYTC Road Closures</a>_
* _KYTC also shares real-time data with <a href="https://www.waze.com/en/live-map/directions?latlng=37.50318937824072%2C-85.23742675781251" target="_blank">Waze</a>_

-_Chris Lambert_

## Project Overview:
The project aims to analyze road closure data provided by the Kentucky Transportation Cabinet (KYTC). The primary objective is to identify trends in road closures to better understand network resiliency during periods of extreme weather events.


## Technical Insight:
- **Python Libraries:** To begin the project, I will begin by utilizing VS Code, Python and Jupyter Notebook extensions, and a Python virtual environment with libraries such as pandas, pyarrow, and requests for data importing, cleaning, and analysis.
- **Sources:** Road closure data will be sourced from the Transportation Operations Center (TOC) of KYTC in CSV format. This data source is updated in real-time during severe weather events.
- **Access Requirements:** No special access requirements are needed as the data is openly provided by KYTC.
- **Data Cleaning:** Standardize column names, data types (date/time), and parse/extract latitude and longitude.
- **Data Integration:** Merge/concatenate multiple data sources.
- **Optional Integration:** I may also utilize KYTC's roadway snapping API to add additional attributes to the road closures dataset.
- **Summary/Statistics:** Calculate descriptive statistics to understand the distribution of road closures by District, County, and Road Type.
- **Optional Summary/Statistics:** I may also perform an analysis by roadway elevation and/or current weather conditions if time permits.
- **Data Visualization:** Utilize libraries such as Matplotlib, Seaborn, and Plotly to create visualizations for exploring patterns and trends in road closure data.
- **Documentation:** Document the analysis process, including data preprocessing steps, exploratory data analysis, and insights gained.
- **Reporting:** Prepare a report/presentation summarizing key findings, insights, and visual outputs from the analysis.
- **Optional Reporting:** If time permits, I may also utilize PowerBI or Tableau to better visualize the data.

## Code Kentucky Feature Lists:
- Feature list #1 choice: Read multiple data files (JSON, CSV, Excel, etc.)
- Feature list #2 choice: Clean the data and perform a pandas merge, then calculate some new values based on the new data set.
- Feature list #3 choice: Make 3 matplotlib (or another plotting library) visualizations to display your data.
- Feature list #3 optional: I may use Tableau if I have time.
- Feature list #4 choice: Utilize a Python virtual environment and include instructions in your README on how the user should set one up
- Feature list #4 optional: I may build a custom data dictionary if I have time.
- Feature list #5 choice: Annotate my code with markdown cells in Jupyter Notebook, write clear code comments, and have a well-written README.md. 


# Setting up a Python Virtual Environment

A Python virtual environment is a self-contained directory that contains a Python installation for a specific project. Using virtual environments helps manage dependencies and isolate project-specific packages. Here's how to set up a Python virtual environment:

## Prerequisites

- Make sure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/).

## Instructions

1. **Open a Terminal/Command Prompt:**

    - On Windows, you can use Command Prompt or PowerShell.
    - On Unix-based systems (Linux, macOS), use the terminal.

2. **Navigate to Your Project Directory:**

    ```bash
    cd path/to/your/project
    ```

3. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

    This command creates a virtual environment named 'venv' in your project directory.

4. **Activate the Virtual Environment:**

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

5. **Install Dependencies:**

    Now that the virtual environment is active, you can install project-specific dependencies without affecting the global Python installation.

    ```bash
    pip install -r requirements.txt
    ```

    Replace `requirements.txt` with the actual name of your requirements file.

6. **Deactivate the Virtual Environment:**

    When you're done working on your project, deactivate the virtual environment.

    ```bash
    deactivate
    ```

## Additional Notes

- It's recommended to include the 'venv' directory in your project's `.gitignore` file to avoid versioning the virtual environment.
(I have not done this yet)
