# AI-Lead-Qualification-and-Routing-Qualifier

An automated lead-processing pipeline that collects inbound leads through Google Forms, uses Gemini to classify lead intent and solution category, sends structured data to a Python/Flask qualification API, and automatically assigns a priority and recommended action.

# Architecture
Google Form
     ↓
Google Sheets
     ↓
Make
     ↓
Gemini
     ↓
Structured JSON
     ↓
Flask API
     ↓
Score + Priority
     ↓
Make Router



# Input Example
{
  "intent": "High",
  "urgency": "High",
  "company_size": 75,
  "category": "AI Classification"
}


# Output Example
{
  "score": 90,
  "priority": "High",
  "recommended_action": "Sales follow-up"
}
