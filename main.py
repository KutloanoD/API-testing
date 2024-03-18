import requests



def get_jobs_by_city(city):
   url = "https://devitjobs.com/api/jobsLight"  #URL used to fetch the job listings

   # Send a get  request to the API
   response = requests.get(url)

   # Check if the request was successful
   if response.status_code == 200:
       jobs = response.json()


       if isinstance(jobs, list):

        # Filtered the job listings based on which city was chosen by the user
           city_jobs = [job for job in jobs if job.get(   #This is how I filtered the response to match user city
               'actualCity').lower() == city.lower()]

           print(city_jobs)


        #Return only three job listings for the city provided
           result = []
           for job in city_jobs[:3]:
               job_info = {
                   'company_name': job.get('company', 'Unknown'),
                   'job_title': job.get('name', 'Unknown'),
                   'annual_salary': f"{job.get('annualSalaryFrom', 'Not available')} to {job.get('annualSalaryTo', 'Not available')}"
               }
               result.append(job_info)


           return result
       else:
           print("Invalid data format.")  #print a error message of the data format is unexpected
           return []
   else:
       print("Error fetching jobs.")
       return []



def main():

    #Allow user to enter or search for trchnology jobs in a city of their choice
   city = input("Enter the city to search for technology jobs: ")

    # Get the top 3 technology jobs in the city provided by user
   jobs = get_jobs_by_city(city)
   if jobs:
       print(f"Top 3 technology jobs in {city}:")
       for index, job in enumerate(jobs, start=1):
           print(f"Job {index}:")
           print(f"Company Name: {job['company_name']}")  #print out the company name
           print(f"Job Title: {job['job_title']}")  #Print the job title
           print(f"Annual Salary: {job['annual_salary']}")   #print the annual salary
           print()
   else:
       print(f"No technology jobs found in {city}.")   # Print this message if no technology jobs were found in that specific city



if __name__ == "__main__":
   main()
