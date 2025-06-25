
# 🔥 GitHub Trending Repositories Scraper

This Python script scrapes the **top 5 trending repositories** from [GitHub Trending](https://github.com/trending) using `requests` and `BeautifulSoup`, and saves the results to a CSV file.

## 📌 Features

- Extracts trending repositories (top 5)
- Captures repository name and GitHub link
- Saves results to a CSV file: `trending_repos.csv`

## 🛠️ Technologies Used

- Python 3
- Requests
- BeautifulSoup
- CSV module

## 🚀 How to Run

1. Clone or download this repository.
2. Install dependencies:

   ```bash
   pip install requests beautifulsoup4
   ```

3. Run the script:

   ```bash
   python github_trending_scraper.py
   ```

4. Check the output file: `trending_repos.csv`

## 📄 Sample Output

### CSV Preview

| Repository Name             | Link                                               |
|----------------------------|----------------------------------------------------|
| DioxusLabs/dioxus          | https://github.com/DioxusLabs/dioxus              |
| vitejs/vite                | https://github.com/vitejs/vite                    |
| musistudio/claude-code-router | https://github.com/musistudio/claude-code-router |
| AykutSarac/jsoncrack.com   | https://github.com/AykutSarac/jsoncrack.com       |
| ripienaar/free-for-dev     | https://github.com/ripienaar/free-for-dev         |

## 📂 Output File

- `trending_repos.csv` is generated in the current directory after script execution.

## 📬 Contact

Feel free to reach out or contribute to the project by submitting pull requests.

---

Made with ❤️ using Python
