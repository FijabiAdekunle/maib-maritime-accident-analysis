# MAIB Maritime Accident Analysis (2020–2024)
[![Collision-Sea.png](https://i.postimg.cc/VvP3ZqYM/Collision-Sea.png)](https://postimg.cc/349SdD0J)


This project provides a cleaned and merged version of UK Marine Accident Investigation Branch (MAIB) data covering the years 2020 to 2024. It includes an analysis-ready CSV, a full data cleaning notebook, and an interactive Streamlit dashboard for quick exploration.

### Project Summary

The goal is to help analysts, researchers, and maritime professionals study incident patterns across UK waters. The dataset covers 5,928 recorded incidents and 87 confirmed fatalities. All cleaning steps were completed in Python with Pandas.

### Key Features

- Combined three MAIB sources: occurrences, vessels, and affected persons

- Standardized fields such as dates, vessel type, tonnage, length, weather, injury type, and damage

- Removed fields with more than 80 percent missing values

- Deduplicated all records

- Clean narrative descriptions ready for text analysis

*Final dataset saved as maib_uk_maritime_accidents_2020_2024.csv*

### Data Overview
| Metric	| Value |
|---------|-------|
| Total incidents |	5,928 |
| Fatalities	| 87 |
| Years covered |	2020 to 2024 |
| Narrative entries |	More than 5,000 |
| Tables merged |	3 |

### Important Columns

- Date
- Weather
- Vessel Type
- Location
- Gross Tonnage
- Length (m)
- Injury Type
- Fatalities

### What You Can Do With the Data

- Explore vessel types with the highest incident counts
- Study weather patterns and human factor links
- Map accident locations
- Run classification or clustering models
- Perform text analysis on narrative descriptions
- Build reports for safety reviews or internal training

### Live Links

**Kaggle dataset**
https://www.kaggle.com/datasets/jeleeladekunlefijabi/uk-maib-maritime-accidents-20202024

**Streamlit dashboard**
https://maib-maritime-accident-analysis-gncw53nsays9cceaoonahs.streamlit.app/


## Author
**Fijabi J. Adekunle**

Email: fijaytwo@gmail.com

Portfolio: https://sites.google.com/view/fijabijadekunle/home

**License**

This project uses the MIT License.
