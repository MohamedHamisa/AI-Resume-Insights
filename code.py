!pip install PyPDF2

# Read in Resume

import PyPDF2

resume_file_path = 'YOUR RESUME FILE PATH'
#e.g. resume_file_path = './Nicholas Renotte - Resume.pdf' 
fhandle = open(resume_file_path, 'rb')

pdfReader = PyPDF2.PdfFileReader(fhandle)

pagehandle = pdfReader.getPage(0)

text = pagehandle.extractText()

# Strip out unwanted text
text = text.replace('o ','')
text = text.replace('|', '')

text

# Import and Authenticate to Service
# Import Watson
from ibm_watson import PersonalityInsightsV3 #service enables applications to derive insights from social media

# Import authenticator
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Creds for Personality Insights
apikey = 'YOUR API KEY HERE' #according to places from IBM cloud
url = 'YOUR URL HERE' 

# Authenticate to PI service
authenticator = IAMAuthenticator(apikey)
personality_insights = PersonalityInsightsV3(
        version='2017-10-13', 
        authenticator=authenticator
)
personality_insights.set_service_url(url)

# Extract Resume Personality Insights
profile = personality_insights.profile(text, accept='application/json').get_result()
profile

for personality in profile['personality']:
    print(personality['name'], personality['percentile'])

for personality in profile['values']:
    print(personality['name'], personality['percentile'])

for personality in profile['needs']:
    print(personality['name'], personality['percentile'])

# Visualise
# Import matplotlib 
from matplotlib import pyplot as plt
# Import seaborn
import seaborn as sns
# Import pandas
import pandas as pd

# Visualise profiles 
needs = profile['needs']
result = {need['name']:need['percentile'] for need in needs}
df = pd.DataFrame.from_dict(result, orient='index')
df.reset_index(inplace=True)
df.columns = ['need', 'percentile']

df.head()

# Create Plot
plt.figure(figsize=(15,5))
sns.barplot(y='percentile', x='need', data=df).set_title('Needs')
plt.show()
