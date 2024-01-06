Download the file in a folder, then run "pip install requests bs4"
Run the file in terminal/ commmand prompt to enable interactivity.

If a company has different positions, only the first position will be outputted. This is to prevent duplicate results.

Example runs:

```py
if __name__ == "__main__":

    # Change keyword, location, and unwanted words list for different outputs.

    keyword = 'analyst'
    location = 'Canada'
    unwantedWordsList = ['senior', 'lead', 'sr', 'staff', 'manager']
    get_jobs(keyword, location, unwantedWordsList)
```

Output:

![image](https://github.com/KlintLee115/JobScrape/assets/54990359/b8c42966-4aa1-47f2-b8f3-b83af7d94ad7)
