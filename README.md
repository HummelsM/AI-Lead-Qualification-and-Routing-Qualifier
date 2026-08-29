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

# Architecture
<img width="1408" height="768" alt="Gemini_Generated_Image_hte66dhte66dhte6 (1)" src="https://github.com/user-attachments/assets/56924bbf-0587-46ad-898f-9b31a065cc45" />

