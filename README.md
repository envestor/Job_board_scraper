'''Welcome to the Webscraping Project'''


Hypothesis:

"I believe that the demand for remote job roles in the tech industry has significantly increased in 2024 compared to previous years, with a particular rise in software development, data analysis, and cybersecurity roles"



Overiview:

I will be collecting recent job listings from reputable job search platforms like Reed, Glassdoor, and LinkedIn. 
I will analyse this data to view trends in job demand specifically for remote roles.
I will be targeting frequency of the 'remote' keyword in job listings to measure the popularity of remote work in tech and will look at the role type, and demand over time. 
Since these platforms don't typically provide raw data downloads, we will build a web scraper to extract the necessary information. Then, we will process and analyze the data to confirm or refute our hypothesis.




Target website for data:
Reed - https://www.reed.co.uk/jobs/remote-tech-jobs-jobs

Header:


Example Job URLhttps://www.reed.co.uk/jobs/recruitment-consultant-fully-remote-it-contract/50807860?source=searchResults&filter=%2fjobs%2fremote-tech-jobs

Job Card: <article class="card job-card_jobCard__MkcJD" data-qa="job-card" data-id="job53785230"><span class="job-card_hiddenContent__MSgqj">Job hidden.<button class="btn btn-link" type="button" data-gtm="unhide_job_icon" data-gtm-value="53785230" data-qa="UnhideJobBtn" data-page-component="job_card" data-element="unhide_job">Undo</button></span><div class="job-card_jobCard__body__86jgk card-body"><button class="job-card_jobTitleBtn__block__ZeEY5 btn btn-link" type="button" data-qa="job-title-btn-wrapper">IT Project Manager - Remote</button><div class="row"><div class="col-sm-12 col-md-7 col-lg-8 col-xl-9"><header><h2 class="job-card_jobResultHeading__title__IQ8iT job-card_jobResultHeading__hasBadges__yeRFG"><a href="/jobs/it-project-manager-remote/53785230?source=searchResults&amp;filter=%2Fjobs%2Fremote-tech-jobs" class="job-card_jobTitle__HORxw" color="link" data-id="53785230" title="IT Project Manager - Remote" data-qa="job-card-title" data-gtm="job_click" data-gtm-value="53785230" data-page-component="job_card" data-element="job_title">IT Project Manager - Remote</a></h2><div class="job-card_jobResultHeading__postedBy__sK_25">4 October by <a href="/jobs/bct-resourcing/p31174" class="job-card_profileUrl__fRi56 gtmJobListingPostedBy" data-page-component="job_card" data-element="recruiter">BCT Resourcing </a></div><ul class="job-card_jobMetadata__gjkG3 list-group list-group-horizontal" role="list" data-qa="job-card-options"><li class="job-card_jobMetadata__item___QNud list-group-item" role="listitem "><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-labelledby="title-salary" class="icons_icon__Q4sNT"><use xlink:href="#svg-salary" x="0" y="0"></use></svg>£70,000 per annum</li><li data-qa="job-card-location" class="job-card_jobMetadata__item___QNud list-group-item" role="listitem "><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-labelledby="title-location" class="icons_icon__Q4sNT"><use xlink:href="#svg-location" x="0" y="0"></use></svg>Sheffield, South Yorkshire</li><li class="job-card_jobMetadata__item___QNud list-group-item" role="listitem "><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-labelledby="title-clock" class="icons_icon__Q4sNT"><use xlink:href="#svg-clock" x="0" y="0"></use></svg>Permanent, full-time</li><li class="job-card_jobMetadata__item___QNud list-group-item" role="listitem "><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-labelledby="title-remote" class="icons_icon__Q4sNT"><use xlink:href="#svg-remote" x="0" y="0"></use></svg>Work from home</li></ul></header><div class="job-card_jobResultDescription__GaA48"><p class="job-card_jobResultDescription__details___xS_G" data-qa="jobDescriptionDetails">Job title: IT Project Manager Location: London / Remote Salary: Up to 70,000 depending on experience. Main Duties: Planning and designing IT programmes and projects, and proactively monitoring its progress Delivering IT projects within the agreed gov...</p><p class="job-card_jobResultDescription__similarLink__bvDv_">Go to similar: <a href="/jobs/manager-jobs" class="" data-gtm="internal_job_link" data-gtm-value="Manager jobs " title="Manager jobs ">Manager jobs </a></p></div><button class="job-card_btnToggleJobDescription__C8fds btn" type="button" aria-label="See job description" data-qa="toggleDescriptionBtn"><svg class="" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" style="transform: rotate(0deg);"><path fill-rule="evenodd" clip-rule="evenodd" d="M15.5807 8.08464L10.5807 13.0846C10.4141 13.2513 10.2474 13.3346 9.9974 13.3346C9.7474 13.3346 9.58073 13.2513 9.41406 13.0846L4.41406 8.08464C4.08073 7.7513 4.08073 7.2513 4.41406 6.91797C4.7474 6.58464 5.2474 6.58464 5.58073 6.91797L9.9974 11.3346L14.4141 6.91797C14.7474 6.58464 15.2474 6.58464 15.5807 6.91797C15.9141 7.2513 15.9141 7.7513 15.5807 8.08464Z" fill="#0F151A"></path><use xlink:href="#svg-chevron" x="0" y="0"></use></svg>See more</button></div><aside class="job-card_asideBlock__uthVE col-md-5 col-lg-4 col-xl-3"><div class="d-none d-sm-none d-md-block"><div class="job-card_jobResultLogo__tS3lw"><a href="/jobs/bct-resourcing/p31174" class="" data-qa="company-logo-link" title="Jobs from BCT Resourcing "><img alt="BCT Resourcing  jobs" data-qa="company-logo-image" loading="lazy" width="120" height="50" decoding="async" data-nimg="1" srcset="https://resources.reed.co.uk/profileimages/logos/thumbs/Logo_31174.png?w=128&amp;q=75 1x, https://resources.reed.co.uk/profileimages/logos/thumbs/Logo_31174.png?w=256&amp;q=75 2x" src="https://resources.reed.co.uk/profileimages/logos/thumbs/Logo_31174.png?w=256&amp;q=75" style="color: transparent;"></a></div></div></aside><div class="job-card_jobResultsActions__qyF6s"><button class="job-card_btnShortlistJob__jgO8k btn btn-inline" type="button" tabindex="0" title="Shortlist job" data-qa="shortlistBtn" aria-label="Shortlist job"><svg viewBox="0 0 20 19" class="icons_icon__Q4sNT job-card_iconShortlist__Q2sKK" fill="none" xmlns="http://www.w3.org/2000/svg"><use xlink:href="#svg-shortlist" x="0" y="0"></use></svg></button><button class="job-card_btnHideJobs__JlZ6J btn btn-inline" type="button" tabindex="0" title="Hide job" data-qa="HideJobBtn" aria-label="hide job" data-gtm="hide_job_icon" data-gtm-value="53785230" data-page-component="job_card" data-element="hide_job"><svg viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" class="icons_icon_sm__KXiku" data-page-component="job_card" data-element="hide_job"><use xlink:href="#svg-hide" x="0" y="0"></use></svg></button></div></div></div></article>



Jobtitle: <h2 class="job-card_jobResultHeading__title__IQ8iT"><a href="/jobs/tech-lead/53887250?source=searchResults&amp;filter=%2Fjobs%2Fremote-tech-jobs-in-jobs" class="job-card_jobTitle__HORxw" color="link" data-id="53887250" title="Tech Lead" data-qa="job-card-title" data-gtm="job_click" data-gtm-value="53887250" data-page-component="job_card" data-element="job_title">Tech Lead</a></h2>


Company name: <a href="/jobs/citation-pls/p37533" class="job-card_profileUrl__fRi56 gtmJobListingPostedBy" data-page-component="job_card" data-element="recruiter">Citation</a>

Location: <li class="job-card_jobMetadata__item___QNud list-group-item" role="listitem "><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-labelledby="title-clock" class="icons_icon__Q4sNT"><use xlink:href="#svg-clock" x="0" y="0"></use></svg>Permanent, full-time</li>

Date posted: <div class="job-card_jobResultHeading__postedBy__sK_25">11 July by <a href="/jobs/capital-r2r/p25815" class="job-card_profileUrl__fRi56 gtmJobListingPostedBy" data-page-component="job_card" data-element="recruiter">Capital R2R</a></div>


Type of role (WFH/Remote, Hybrid, In-person)


Website URL: https://www.reed.co.uk/jobs/remote-tech-jobs

Salary: <li class="job-card_jobMetadata__item___QNud list-group-item" role="listitem "><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-labelledby="title-salary" class="icons_icon__Q4sNT"><use xlink:href="#svg-salary" x="0" y="0"></use></svg>£70,000 per annum</li>class="icons_icon__Q4sNT"><use xlink:href="#svg-salary" x="0" y="0"></use></svg>






Libraries:
''' Setting up the environment '''
'requests' - to fetch the web pages
'beautifulsoup4' - to parse the HTML content of the job listings
'pandas' - to organised scraped data into a dataframe
'matplotlib' - to create visualizations

Skills used:
using a while loop to scrap multiple pages of a website(pagination)
using dictionary attributes to find the location element required



skills learned:
using enumerate to create a numbered list of job titles





Problems encountered:

Finding the browsers developer tools
    - Opened the site in chrome and used the inspect tool to find the HTML elements containing the job listings
        - "cmd + option + i"

Effectively scraping the job title from the website was difficult as the job title was nested in an article element with a class of 'card job-card_jobCard__MkcJD'
    - I used ChatGPT to help me find the correct elements to parse the job title from

Once I had the job title I needed to clean it up to remove the ' - Remote' suffix, or any unwanted text
    - I used the split function to split the string at '-' as the delimiter and then used the strip function to remove any unwanted text

I found that the number of job listings scraped was less than expected, I realised that the issue was due to the scraper was stuck on 1 page of the website. I added pagination to the scraper to scrape multiple pages and also added a max number of different job listings to scrape.


After fixing the pagination issue I found that the scraper was scraping duplicate job listings. I added a check to ensure that the job title was not already in the list of job titles to avoid duplicates.
    - for the purposes of the project I want to save the frequency of each job title to see the most popular job titles in the tech industry.

I managed to scrape the salary and location data but decided against getting the job URL and date posted as the date posted was not posted in a consistent format. 



------------------------------------------
11/11/2024
So next I want each company name to also have a frequency count.
I am assuming that for each job title there is only one company name and python will automatically assign the company name to the job title.
We will write code to check this assumption.

15/11/2024
I have now added a dataframe to store the job titles and will next be cleaning my data to remove duplicates and unwanted texts
- This step entails using regular expressions  



10/12/2024
- The next step will be to Visualise data in a manner that I am happy with, I want the figures produced to be clean and consice and paint an accurate picture. 
I will use: 
    - the ploty module and its Bar and Layout classes to produce an interactive image
    - I will use a similar format to that from dice.py
    - I will use the csv reader combined with matplotlib to iterate into the rows of the csv and extract useful info that can be used to display data on a chart.

------------------------------------------
Code Graveyard:

- Code to check if the job title is unique to the company name
 #job_company_key = f"{cleaned_jt}_{company_name}"
            
#if job_company_key not in company_data:
#job_titles[cleaned_jt] = job_titles.get(cleaned_jt, 0) + 1
    #company_data[job_company_key] = company_name
    #total_jobs_collected += 1
----------
- Code to print the job titles and their companies

  #job_title = job_company_key.rsplit('_', 1)[0]  # Split off the company name
    #print(f"Job: {job_title} | Company: {company}")

#print("\nJob Title Frequencies:")
#for num, (title, count) in enumerate(job_titles.items(), start=1):
    #print(f"{num}. {title}: {count} occurrences")

#next_page_button = soup.find('a', {'aria-label': 'Next Page'})
#if not next_page_button:
    #break
--------





