# 🛡️ Cyber Threat Analytics

## 📝 Business Scenario
The Security Operations Center (SOC) provided a raw dump of 10,000 cyber incident logs. The goal was to clean the data, link threat identifiers to their severity levels, and build an interactive dashboard to track attack types and volumes.

## 🏗️ Architecture & Workflow
This practice uses a layered architecture to separate raw data from the final visual dashboard:
* **Row_Logs:** The untouched raw dataset and lookup tables (`threat_matrix`, `server_nodes`).
* **Clean_Data:** Parsed dates, fixed hidden blank values, and used `XLOOKUP`/`INDEX+MATCH` to pull in missing data like Severity Level.
* **Dashboard_Engine & UI:** Built Pivot Tables to power a web-style, interactive dashboard using an F-Pattern layout and a high data-ink ratio (removing gridlines and borders).

## 🔍 Key Findings
* **No Priority in Response Times:** Whether a threat is "Critical" or "Low" priority, the IT team takes the exact same amount of time (about 75 hours) to fix it. 
* **Alert Fatigue:** Almost half (45%) of all incidents are labeled as "Critical." When everything is an emergency, it is hard for the team to know what is actually a true threat.

## 💡 Business Recommendations
1. **Set Strict Time Limits (SLAs):** Require "Critical" threats to be contained in under 24 hours. Move "Low" priority issues to a regular weekly schedule to free up the team's time.
2. **Update the Alarm Rules:** Redefine what actually counts as a "Critical" threat so the highest alarm goes off less often. This helps the security team focus their energy only on real, dangerous network breaches.

## 📊 Dashboard Preview
![SOC Threat Analytics Dashboard](dashboard_preview.jpeg)
