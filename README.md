# AI-Lead-Qualification-and-Routing-Qualifier

An automated lead-processing pipeline that collects inbound leads through Google Forms, uses Gemini to classify lead intent and solution category, sends structured data to a Python/Flask qualification API, and automatically assigns a priority and recommended action.


# Input Example
```
{
  "intent": "High",
  "urgency": "High",
  "company_size": 75,
  "category": "AI Classification"<img width="1408" height="768" alt="Gemini_Generated_Image_hte66dhte66dhte6 (1)" src="https://github.com/user-attachments/assets/d6527888-3ae4-4923-a428-704f7e59b7d1" />
<img width="1408" height="768" alt="Gemini_Generated_Image_hte66dhte66dhte6 (1)" src="https://github.com/user-attachments/assets/854c394c-9083-4d6e-a39e-56ef3fa21d17" />


}
```

# Output Example
```
{
  "score": 90,
  "priority": "High",
  "recommended_action": "Sales follow-up"
}
```

# Results/Outcomes
Outcomes

Automated lead qualification

> 50 test leads processed through the complete workflow without manual qualification.

Automated scoring

> Each lead received a deterministic qualification score based on intent, urgency, company size and solution category.

Automated routing

> Leads were automatically classified into High, Medium and Low priority with a corresponding recommended action.

Estimated manual effort avoided

> ~2.5 hours per 50 leads, based on an assumed 3-minute manual qualification time per lead.


# Architecture
<img width="1408" height="768" alt="Gemini_Generated_Image_696d1l696d1l696d" src="https://github.com/user-attachments/assets/930042da-5ea3-4f36-aaed-261562bae416" />


