import pandas as pd 
import numpy as np           # NumPy: used for numerical operations and working with arrays
# import seaborn as sns       # Seaborn: used for creating statistical data visualizations
import matplotlib.pyplot as plt  # Matplotlib: used for plotting graphs and customizing visualizations
import matplotlib
df = pd.read_csv("dataset/ai_job_dataset.csv")
#print(employee_count)
# print(df.columns)
# Index(['job_id', 'job_title', 'salary_usd', 'salary_currency',
#        'experience_level', 'employment_type', 'company_location',
#        'company_size', 'employee_residence', 'remote_ratio', 'required_skills',
#        'education_required', 'years_experience', 'industry', 'posting_date',
#        'application_deadline', 'job_description_length', 'benefits_score',
#        'company_name'])

### Q1.How many employee_residence in the dataset?
def Q1(df): #
    # TO DO: 
    employee_count = df["employee_residence"].unique()
    print("Number of employee_residence in the dataset: ",employee_count, len(employee_count))

# Q1(df)

### Q2. Compare the number of job postings based on employee_residence.
def Q2(df):
    # TO DO: 
    job_postings = df["employee_residence"].value_counts()
    print("Number of job postings based on employee_residence: \n", job_postings)
# Q2(df)

### Q3. Plot a graph to compare which job titles require Python,Java, and R programming skills
def Q3(df):
    # TO DO:
    python_dix = df["required_skills"].str.contains("Python")
    job_with_Python = df["job_title"][python_dix].value_counts()
    
    
    java_dix = df["required_skills"].str.contains("Java")
    job_with_Java = df["job_title"][java_dix].value_counts()
    

    r_dix = df["required_skills"].str.contains("R")
    job_with_R = df["job_title"][r_dix].value_counts()

    # Combine the results into a DataFrame for plotting
    
    combined_df = pd.DataFrame({
        'Python': job_with_Python,
        'Java': job_with_Java,
        'R': job_with_R
    }).fillna(0)  
    combined_df.plot(kind='bar', figsize=(12, 6))
    plt.title('Number of Job Postings Requiring Python, Java, and R Skills')
    plt.xlabel('Job Title')
    plt.ylabel('Number of Job Postings')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Programming Language')
    plt.tight_layout()
    plt.show()

# Q3(df)

### Q4. What kind of jobs require a PhD degree?
def Q4(df):
    # TO DO:
    phd_dix = df["education_required"].str.contains("PhD", na=False)
    jobs_requiring_phd = df["job_title"][phd_dix].unique()
    print("Jobs that require a PhD degree: \n", jobs_requiring_phd)
# Q4(df)

### Q5. Which company provides the longest application deadline?
def Q5(df):
    # TO DO:
    df["application_deadline"] = pd.to_datetime(df["application_deadline"], errors='coerce')
    longest_deadline_index = df["application_deadline"].idxmax()
    company_with_longest_deadline = df.loc[longest_deadline_index, "company_name"]
    deadline_time = df.loc[longest_deadline_index, "application_deadline"]
    print("Company with the longest application deadline: ", company_with_longest_deadline)
    print("Time of the deadline: ",deadline_time)

# Q5(df)

### Q6. Education Level and Salary
# The dataset contains an education_required column with four levels: Associate, Bachelor, Master, and PhD.

# - Compute the `average salary` for each education level
# - Visualize the result using a bar chart
# - Does a higher education level always lead to a higher salary? Explain your observation.
def Q6(df):
    # TO DO:
    education_salary = df.groupby("education_required")["salary_usd"].mean()
    # computation
    print("Average salary for each education level: \n", education_salary)
    # bar chart
    education_salary.plot(kind='bar', figsize=(8, 5))
    plt.title('Average Salary by Education Level')
    plt.xlabel('Education Level')
    plt.ylabel('Average Salary (USD)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
# Q6(df)
### Higher education levels does not necessarily lead to higher salaries. The average salary for the Associate degree is higher than that of the Bachelor degree, and the average salary for the Master degree is higher than that of the PhD degree. This could be due to various factors such as job roles, industry demand, and experience levels that may not always correlate directly with education level.

### Q7. Industry and Salary
# There are 15 industries in this dataset.

# - Compute the `average salary` for each industry
# - Sort from highest to lowest and display only the top 5
# - Visualize using a horizontal bar chart
def Q7(df):
    # TO DO:
    # console
    industry_salary = df.groupby("industry")["salary_usd"].mean().sort_values(ascending=False).head(5)
    print("Average salary for each industry (top 5): \n", industry_salary)
    # graph
    industry_salary[::-1].plot(kind='barh', figsize=(8, 5))
    plt.title('Average Salary by Industry (Top 5)')
    plt.xlabel('Average Salary (USD)')
    plt.ylabel('Industry')
    plt.tight_layout()
    plt.show()
# Q7(df)

### Q8. Is there a relationship between experience level and salary?
def Q8(df):
    # TO DO:
    experience_salary = df.groupby("experience_level")["salary_usd"].mean()
    print("Average salary for each experience level: \n", experience_salary)
    experience_salary.plot(kind='bar', figsize=(8, 5))
    plt.title('Average Salary by Experience Level')
    plt.xlabel('Experience Level')
    plt.ylabel('Average Salary (USD)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# Q8(df)

### Q9. Which job title has the highest number of fully remote (100%) positions?
def Q9(df):
    # TO DO:
    remote_dix = df["remote_ratio"] == 100
    fully_remote_jobs = df[remote_dix]
    job_title_counts = fully_remote_jobs["job_title"].value_counts()
    highest_remote_job_title = job_title_counts.idxmax()
    print("Job title with the highest number of fully remote (100%) positions: ", highest_remote_job_title)

# Q9(df)
### Q10. What types of AI jobs in the United States require a Bachelor’s degree and are offered by large companies?
def Q10(df):
    # TO DO:
    us_dix = df["company_location"] == "United States"
    bachelor_dix = df["education_required"].str.contains("Bachelor", na=False)
    large_company_dix = df["company_size"] == "L"
    
    filtered_jobs = df[us_dix & bachelor_dix & large_company_dix]
    job_titles = filtered_jobs["job_title"].unique()
    
    print("Types of AI jobs in the United States that require a Bachelor’s degree and are offered by large companies: \n", job_titles)

Q10(df)