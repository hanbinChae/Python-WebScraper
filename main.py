from indeed import extract_indeed_page, extract_indeed_jobs

last_indeed_pages = extract_indeed_page()
indeed_jobs = extract_indeed_jobs(last_indeed_pages)
print(indeed_jobs)
