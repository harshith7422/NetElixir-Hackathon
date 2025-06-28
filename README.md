# NetElixir-Hackathon 👾
AIgnition 2.0 Hackathon Challenge

### Title: Hyper-Personalized Landing Page Generator Agent🚀
## Team Members 👥
- Harahith YVS
- Deeksha R
- Lohiht Obulapuram

## 📌 Overview

This project is a working AI-powered prototype that dynamically generates hyper-personalized landing pages for **new or guest users** visiting an eCommerce website.  
It intelligently recommends page modules (hero banners, product carousels, CTAs) by learning from past user behavior, demographics, and transaction trends — while also solving the **cold start problem** using fallback logic.

---

## ⚙️ Solution Workflow

**1. Data Understanding & Preprocessing**
- Joined GA4-style user activity logs with transaction data using `transaction_id`.
- Reconstructed complete user sessions grouped by `user_pseudo_id`.
- Aggregated browsing and purchase behavior for every user.

**2. User Segmentation**
- Engineered user-level features: engagement levels, top events, demographics, sources, region.
- Applied `KMeans` clustering to create behavioral segments (e.g., repeat purchasers, cart abandoners).

**3. Cold Start Strategy**
- Designed fallback recommendations using:
  - Region-specific top categories & trends.
  - Profile similarity (demographic/source-based logic).
  - Rule-based default modules for anonymous users.

**4. Personalization Logic**
- Mapped each segment to landing page modules:
  - Hero banner, product carousel, and CTA block.
- For new users: fallback uses region or overall trends.

**5. Prototype**
- Simple **Streamlit** UI shows real-time landing page generation for a given user ID or new visitor.
- Easy to extend into any frontend stack.

---

## 📊 Datasets Used

- `User Activity Log`: session-level events, device, demographics, region, traffic source.
- `Transaction Data`: actual purchases, revenue, item category/brand.

---

## 🧩 Tech Stack

- **Python**, **Pandas**, **Scikit-learn**, **Streamlit**
- Jupyter Notebook

---

## ✅ How to Run

```bash
pip install pandas scikit-learn streamlit
streamlit run app.py
