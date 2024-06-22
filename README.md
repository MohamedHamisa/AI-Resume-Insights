
```
# Resume Personality Insights

This Python project uses IBM Watson Personality Insights to analyze the text extracted from a resume and visualize the personality traits. The project involves reading a PDF resume, extracting text, sending the text to IBM Watson for personality analysis, and visualizing the results.

## Features
- Extract text from a PDF resume.
- Analyze personality traits using IBM Watson Personality Insights.
- Visualize personality traits, values, and needs.

## Prerequisites
- Python 3.x
- Install the required libraries using pip:
  ```bash
  pip install PyPDF2 ibm-watson ibm-cloud-sdk-core matplotlib seaborn pandas
  ```

## Setup and Usage

### 1. Clone the repository
```
git clone https://github.com/yourusername/resume-personality-insights.git
cd resume-personality-insights
```

### 2. Update the script with your details
Open the script `app.py` and update the following placeholders:
- `YOUR RESUME FILE PATH` with the path to your resume PDF file.
- `YOUR API KEY HERE` with your IBM Watson Personality Insights API key.
- `YOUR URL HERE` with your IBM Watson Personality Insights service URL.

### 3. Run the script
```
python app.py
```

### 4. Output
- The script will print the extracted text from the resume.
- The personality traits, values, and needs will be printed in the console.
- A bar plot visualizing the needs will be displayed.

## Code Overview


```
# Install PyPDF2
!pip install PyPDF2

# Read in Resume
import PyPDF2

resume_file_path = 'YOUR RESUME FILE PATH'  # Replace with the actual path to your resume file

# Open and read the PDF file
with open(resume_file_path, 'rb') as fhandle:
    pdfReader = PyPDF2.PdfFileReader(fhandle)
    pagehandle = pdfReader.getPage(0)
    text = pagehandle.extract_text()

# Strip out unwanted text
text = text.replace('o ', '')
text = text.replace('|', '')

print(text)  # Optional: Print to check the extracted text

# Import and Authenticate to Service
from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Credentials for Personality Insights
apikey = 'YOUR API KEY HERE'  # Replace with your API key
url = 'YOUR URL HERE'         # Replace with your URL

# Authenticate to PI service
authenticator = IAMAuthenticator(apikey)
personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    authenticator=authenticator
)
personality_insights.set_service_url(url)

# Extract Resume Personality Insights
profile = personality_insights.profile(
    text,
    content_type='text/plain',
    accept='application/json'
).get_result()

# Print personality insights
for personality in profile['personality']:
    print(personality['name'], personality['percentile'])

for value in profile['values']:
    print(value['name'], value['percentile'])

for need in profile['needs']:
    print(need['name'], need['percentile'])

# Visualize
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Visualize profiles
needs = profile['needs']
result = {need['name']: need['percentile'] for need in needs}
df = pd.DataFrame.from_dict(result, orient='index')
df.reset_index(inplace=True)
df.columns = ['need', 'percentile']

df.head()

# Create Plot
plt.figure(figsize=(15, 5))
sns.barplot(y='percentile', x='need', data=df).set_title('Needs')
plt.show()
```

## Contributions
Contributions are welcome! Please fork the repository and submit a pull request with your changes.



## Acknowledgements
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [IBM Watson Personality Insights](https://www.ibm.com/cloud/watson-personality-insights)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [pandas](https://pandas.pydata.org/)

