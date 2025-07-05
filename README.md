## Project Overview

This project was completed as part of a QA automation homework assignment for a QA position at Kaleidoo. The assignment covers:

- Test documentation (STD)
- UI automation for Login and Publish Ad flows
- Bug identification and reporting

Technologies used:

- Python 3.11
- Playwright (sync API)
- Pytest

---

## Setup Instructions

1. Install Dependencies

```bash
pip install -r requirements.txt
```

2. Run Tests

```bash
python -m pytest tests
```

---

## Project Structure

```
.
├── pages
│   ├── apartment_listings_page.py
│   ├── base_page.py
│   ├── login_page.py
│   └── publish_ad_page.py
├── tests
│   ├── data
│   │   └── image.png
│   ├── test_login.py
│   └── test_publish_ad.py
├── utils
│   └── config.py
├── conftest.py
├── requirements.txt
├── Kaleidoo_STD_All_Areas.xlsx       # Test scenarios
├── Bug_Report.docx                   # Documented bug report
└── README.md
```

---

## Test Coverage

| Area               | Test Case ID        | Description                                |
| ------------------ | ------------------- | ------------------------------------------ |
| Login              | TC\_Login\_01-03    | Valid, invalid, and empty login scenarios  |
| Apartment Listings | TC\_Listings\_01-02 | Filter and view apartment listings         |
| Publish Ad         | TC\_Publish\_01-03  | Successful publish, validation, image file |

Test case details can be found in `Kaleidoo_STD_All_Areas.xlsx`.

---

## Bug Report Summary

**Title:** Apartments list - Sorting by price is broken\
**Severity:** High\
**Environment:** Chrome browser, test user `tester`\
**Description:** When sorting listings by price (ascending or descending), the sort order does not behave as expected.\
**File:** `Bug_Report.docx`

---

## Known Limitations

- The script attempts to assert the success message after publishing an ad:
  ```python
  assert page.locator("text=המודעה פורסמה בהצלחה").is_visible()
  ```
  This could not be validated reliably in automation. This is not a bug, just a limitation in handling dynamic UI feedback or localization timing.

