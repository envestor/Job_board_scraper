'''Dependencies'''

import requests
from bs4 import BeautifulSoup
import time
import re
from dont_run import pth, clean_path #file path to csv file
import pandas as pd 
import matplotlib.pyplot as plt


# Get input from the user
role = input('What role are you looking for? ')

# Split the input into separate words
words = role.split()  # This splits the input string by spaces

# Assign the words to variables
if len(words) >= 2:
    first_word, second_word = words[0], words[1]
else:
    first_word = words[0]
    second_word = ''  # Fallback in case there's only one word

# Construct the base URL
base_url = f"https://www.reed.co.uk/jobs/{first_word}-{second_word}-jobs?pageno={{}}"

print("Generated URL:", base_url)

#Scraper Configuration
page = 1
max_jobs = 200 #set to 200 for full scrape


#Initialise Data frame
columns = ['Job Title', 'Employer', 'Location', 'Salary','Remote Work(Y/N)']
df = pd.DataFrame(columns=columns)

#Storage Location for scraped data
job_titles = []
company_data = []
locations = []
salaries = []


while len(job_titles) < max_jobs:
# Make a HTTP request to the website
    response = requests.get(base_url.format(page))
#Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')


    job_card_elements = soup.find_all('article', class_=['card', 'job-card_jobCard__MkcJD'])

    #Phase 1: Extract Job Titles, Company Names, and Job URLs, and Dates Posted, and Locations, and Salaries
    for job_card in job_card_elements:

        #Find the necessary elements from the job card
        button_element = job_card.find('button', class_='job-card_jobTitleBtn__block__ZeEY5 btn btn-link')
        company_element = job_card.find('a', class_="job-card_profileUrl__fRi56 gtmJobListingPostedBy")
        salary_element = job_card.find('li', class_="job-card_jobMetadata__item___QNud list-group-item")
        location_element = job_card.find('li', {'data-qa': 'job-card-location'})
    
        
        if button_element and company_element:
            job_title = button_element.text.strip()
            company_name = company_element.text.strip()
            job_titles.append(job_title)
            company_data.append(company_name)
            
        
            if salary_element:
                salary = salary_element.text.strip()
                salaries.append(salary)
            else:
                salaries.append('N/A')
        
        
            if location_element:
                location = location_element.text.strip()
                locations.append(location)
            else:
                locations.append('N/A')

            #Append to Data Frame 
            df = pd.concat([df, pd.DataFrame({'Job Title': [job_title], 
                                          'Employer': [company_name],
                                          'Location': [location],
                                          'Salary': [salary]
                                          })], ignore_index=True)
               
            

        if len(job_titles) >= max_jobs:
            break


    print(f"Page {page} scraped successfully, Total jobs scraped: {len(job_titles)}")
    page += 1
    time.sleep(0.5)


#exports dataframe to a csv file e.g. endpoint of 'pth'
df.to_csv(pth, index=False)
print(f"Data saved to tech_jobs.csv with {len(df)} entries")
print(df.head(10))


def remove_dups(df, subset_columns=['Job Title', 'Employer']):
    '''Function to remove duplicates from dataframe'''
    initial_count = len(df)
    # REMOVE DUPLICATES based on subset columns
    df.drop_duplicates(subset=subset_columns, keep='first', inplace=True)

    final_count = len(df)

    print(f"Duplicates removed {initial_count - final_count}, Total jobs: {final_count}")

    return df

def handle_missing_values(df, columns_to_check=['Location', 'Salary']):
    '''Function to handle missing values in dataframe'''
    for column in columns_to_check:
        print(f"Checking for missing values in {column} column")
        missing_values = df[column].isna().sum()
        if missing_values > 0:
            df['Location'].fillna('Unknown', inplace=True)
            df['Salary'].fillna('Not Specified', inplace=True)
    
    return df

def clean_salary(salary):
    '''Function to clean salary using regex'''
    #Pattern = a digit 0-9 occuring 1-3 times, followed by a comma and then 0-9 occuring 3 times
    match = re.search(r'(\d{1,3}(?:,\d{3})*)', salary)
    if match:
        # Convert the matched string to an integer
        return int(match.group(1).replace(',', ''))
    else:
        return None  # Return None instead of 'Not Specified'
    
#df = remove_dups(df) #remove duplicates

df = handle_missing_values(df) #handle missing values

def check_remote_work(job_title):
    '''Function to check if job title contains remote work'''
    if 'remote' in job_title.lower():
        return 'Y'
    else:
        return 'N'
    

def clean_job_title(job_title):
    '''Function to clean the job title'''

                # Remove common suffixes after hyphen, dash, or vertical bar
    cleaned_jt = re.split(r'[-|]|\s+-\s+', job_title)[0].strip()
    # Remove additional common suffixes like "Fully Remote", "UK", etc.
    cleaned_jt = re.sub(r'\s*(Remote|Fully|UK|Hybrid|[{}]|Contract|Permanent|Full[ -]Time|Part[ -]Time).*$', '', cleaned_jt, flags=re.IGNORECASE)

    return cleaned_jt


def apply_cleaning():
    '''Function to apply all cleaning functions'''
    df['Remote Work(Y/N)'] = df['Job Title'].apply(check_remote_work) #check remote work
    df['Cleaned Salary'] = df['Salary'].apply(clean_salary) #clean salary
    df['Job Title'] = df['Job Title'].apply(clean_job_title) #clean job title
    df[['City', 'Region']] = df['Location'].str.split(',', n=1, expand=True) #split location into city and region 
    df['City'] = df['City'].str.strip()
    df['Region'] = df['Region'].str.strip().fillna('United Kindgom')
    df['Job Title'] = df['Job Title'].apply(clean_job_title) #clean job title

apply_cleaning()

def top_jobs_by_city(city_name):
    """
    Function to visualise top paying jobs in a specific city and their company.
    """
    # Step 1: Filter DataFrame for the specified city
    city_jobs = df[df['Location'].str.contains(city_name, case=False, na=False)]

    # Step 2: Ensure Salary column contains numeric values
    city_jobs['Salary'] = pd.to_numeric(city_jobs['Cleaned Salary'], errors='coerce')
    city_jobs.dropna(subset=['Salary'], inplace=True)

    city_jobs['Salary'] = city_jobs['Salary'].astype(int)

    # Step 3: Remove jobs with salary value of 0
    city_jobs = city_jobs[city_jobs['Salary'] > 1000]

    # Step 4: Create visualization
    plt.figure(figsize=(12, 6))
    plt.barh(city_jobs['Job Title'] + " (" + city_jobs['Employer'] + ")", 
             city_jobs['Salary'], color='lightcoral')
    plt.title(f"Top Paying Jobs in {city_name.title()} (with Companies)")
    plt.xlabel("Salary (£)")
    plt.ylabel("Job Title (Company)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.gca().invert_yaxis()  # Invert Y-axis to show highest paying job at the top
    plt.show()

# Example usage for "London"
top_jobs_by_city("manchester")




#Ensure the Salary column contains only numeric values
df['Salary'] = pd.to_numeric(df['Cleaned Salary'], errors='coerce')

#Drop rows with missing or invalid salary values
df.dropna(subset=['Salary'], inplace=True)

#Convert Salary column to integer for grouping
df['Salary'] = df['Salary'].astype(int)


#Phase 3 - Data Visualisation

#Top Paying Companies
top_paying_companies = df.groupby('Employer')['Salary'].mean().sort_values(
    ascending=False).head(10)
plt.figure(figsize=(10,5))
top_paying_companies.plot(kind='bar', color='skyblue')
plt.title("Top 10 Paying Companies (Average Salary)")
plt.xlabel('Company')
plt.ylabel('Avg Salary (£)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


#Top paying companies in London
london_companies = df[df['Location'].str.contains("London", case=False, na=False)]
top_paying_london = london_companies.groupby('Employer')['Salary'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
top_paying_london.plot(kind='bar', color='lightgreen')
plt.title("Top 10 Paying Companies in London (Average Salary)")
plt.xlabel("Company")
plt.ylabel("Average Salary (£)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


#Top Paying Companies in Manchester
manchester_companies = df[df['Location'].str.contains("Manchester", case=False, na=False)]
if not manchester_companies.empty:
    top_paying_manchester = manchester_companies.groupby('Employer')['Salary'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 5))
    top_paying_manchester.plot(kind='bar', color='orange')
    plt.title("Top 10 Paying Companies in Manchester (Average Salary)")
    plt.xlabel("Company")
    plt.ylabel("Average Salary (£)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("No data available for companies in Manchester.")

#Companies Hiring for the Most Roles
most_roles = df['Employer'].value_counts().head(10)
plt.figure(figsize=(10, 5))
most_roles.plot(kind='bar', color='purple')
plt.title("Top 10 Companies Hiring for the Most Roles")
plt.xlabel("Company")
plt.ylabel("Number of Roles")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()






#Job Titles vs Salaries
# Filter the DataFrame to ensure only valid salary data is used
valid_data = df.dropna(subset=['Cleaned Salary', 'Job Title'])  # Remove rows with missing values
valid_data = valid_data[valid_data['Cleaned Salary'] > 0]  # Ensure salaries are positive

# Extract job titles and salaries
job_titles = valid_data['Job Title']
salaries = valid_data['Cleaned Salary']

# Sort by salary for better visualization (optional)
valid_data = valid_data.sort_values(by='Cleaned Salary', ascending=False)

# Plotting
plt.figure(figsize=(12, 6))  # Set figure size
plt.scatter(valid_data['Job Title'], valid_data['Cleaned Salary'], color='blue', alpha=0.7)

# Set plot titles and labels
plt.title('Job Titles vs. Salaries', fontsize=16)
plt.xlabel('Job Titles', fontsize=12)
plt.ylabel('Salaries (£)', fontsize=12)

# Rotate x-axis labels for readability
plt.xticks(rotation=65, fontsize=10)
#plt.tight_layout()  # Adjust layout to prevent clipping





plt.tight_layout()
#plt.show()




#Top 10 most common job titles
#Only use if remove_duplicates function is off
top_job_titles = df['Job Title'].value_counts().head(10)
plt.figure(figsize=(8, 4)) #set figure size (width, height)
top_job_titles.plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Common Job Titles')
plt.xlabel('Job Title')
plt.ylabel('Number of Listings')
plt.xticks(rotation=90) #rotation of x axis labels
#plt.show()



#Top 10 Companies with most job postings
top_companies = df['Employer'].value_counts().head(15)
plt.figure(figsize=(8, 4)) #set figure size (width, height)
top_companies.plot(kind='bar', color='lightgreen')
plt.title('Top 10 Companies with Most Job Postings')
plt.xlabel('Company Name')
plt.ylabel('Number of Listings')
plt.xticks(rotation=90) #rotation of x axis labels
#plt.show()





