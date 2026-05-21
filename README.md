# Yellow Pages Egypt Scraper 📖 - Automated Business Directory Miner

A high-fidelity directory scraping tool built in Python using **SeleniumBase**. It is designed to search, crawl, and harvest comprehensive business listings (business names, verified phone numbers, physical addresses, and profile links) dynamically from **YellowPages.com.eg**—Egypt's premier commercial directory.

This project showcases expertise in **advanced DOM navigation**, **popover interactions**, **handling paginated tables**, and **robust error-tolerant data structures**.

---

## 🚀 Key Features

* **Anti-Bot Integration:** Utilizing **SeleniumBase** to naturally evade perimeter Web Application Firewalls (WAF) and bot-prevention gates.
* **Dynamic Regional Directory Search:** Enters dynamic query targets (e.g., "Supermarket / سوبر ماركت") and localizes the boundary limits by area (e.g., "El Sayeda Zeinab / السيدة زينب") through precise text search boxes.
* **Popover Dynamic Interactions:** Automatically triggers popovers (like "Show Phone Number / عرض الهاتف"), waits for dynamic popover nodes to append, extracts multiple phone elements, and compiles them.
* **Paginated Traversal:** Actively scrolls to the "Next / التالي" pagination element, tracks active page indices, and gracefully detects the final search page limit.
* **Auto-Recovery & State Check:** Employs robust try-except loops to prevent crashes when phone elements are missing, outputting "N/A" and continuing to pull names and addresses securely.
* **Clean Data Pipe:** Excludes heavy datasets through `.gitignore` while streaming extracted structures locally to a UTF-8 encoded CSV file.

---

## 📁 Repository Structure

```text
yellowpages-scraper/
│
├── main.py               # Main scraper execution file
├── requirements.txt      # Project dependencies (SeleniumBase)
├── .gitignore            # Git exclusion configuration
└── LICENSE               # MIT License
```

---

## ⚙️ Local Installation & Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BnEhab2/yellow-pages-scraper.git
   cd yellow-pages-scraper
   ```

2. **Set up a Virtual Environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Scraper:**
   ```bash
   python main.py
   ```

---

## ⚠️ Ethical & Legal Disclaimer
This scraper is designed solely for educational, presentation, and academic research purposes. Always verify the terms of service of any directory or commercial portal before utilizing automated crawlers. The developer holds no liability for unauthorized data harvesting.

---

## 🛡️ License
Distributed under the MIT License. See `LICENSE` for more information.
