import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Retrieve the API key
api_key = os.getenv("API_KEY")

# API key configuration (Replace with your API key)
if api_key:
    genai.configure(api_key=api_key)
    print("API key loaded successfully.")
else:
    print("Error: API key not found. Please check your .env file.")
    
generation_config = {
    "temperature": 0.5,
    "top_p": 0.6,
    "top_k": 40,
    "max_output_tokens": 1000,
    "response_mime_type": "text/plain",
    # "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def get_model_response(user_input):
    input_data = [
        # Instruction 1: Introduction
        "Infinity AI Assistant: Provide a brief introduction unless the user requests more details.\n"
        "Introduction:\n"
        "Hi! I'm the Infinity AI Assistant, here to help communities, nonprofits, and organizations with program development, funding, impact analysis, grant finding, proposal writing, educational content creation, student progress tracking, and measuring program impact. Whether you need funding recommendations or educational outcome reports, I’m here to assist!",

        # Instruction 2: List of tools
        "Infinity AI Assistant: If asked about your tools or a list of tools, provide the following list:\n"
        "Tools:\n1. Infiniti AI Fund Finder\n2. Infiniti AI Funding Assistant\n3. Infiniti AI EduJob Content Generator\n4. Infiniti AI Learning Assistant\n5. Infiniti AI Impact Analysis",

        # Instruction 3: Grant Proposal Development with Funding Assistant
        "Grant Proposal Development with Infiniti AI Funding Assistant:\n"
        "Scenario:\n"
        "After identifying relevant grants, CommunityImpactYouthCenter needs assistance crafting a proposal that meets funder criteria and effectively communicates the program’s impact.\n"
        "Tasks:\n"
        "- Generate a proposal template with required sections (e.g., Community Impact, Proposed Activities).\n"
        "- Integrate data from Infiniti AI Fund Finder (e.g., Financial Literacy Gap, STEM Engagement).\n"
        "- Calculate and allocate budget using the budget calculator (e.g., Educational Materials, Staff Costs, Evaluation Tools).\n"
        "- Suggest student engagement methods like digital badges and example EduJobs for STEM and financial literacy.",

        # Instruction 4: Infiniti AI Fund Finder
        "Infiniti AI Fund Finder Usage Instructions:\n"
        "1. Enter organizational information: community demographics, income levels, program focus.\n"
        "   - Example: 50% Hispanic youth, 70% from low-income households, STEM education focus.\n"
        "2. The algorithm analyzes inputs against funding priorities to identify:\n"
        "   - Community Needs: Gaps in STEM education and financial literacy among unbanked youth.\n"
        "   - Funder Alignment: Matches programs with relevant grants from tech corporations or government.\n"
        "3. Provides tailored grant recommendations including funding scope, funder objectives, and alignment overview.",

        # Instruction 5: Infiniti AI Learning Assistant
        "Infiniti AI Learning Assistant Usage Instructions:\n"
        "Scenario:\n"
        "During program delivery, CommunityImpactYouthCenter needs tools to engage students, track progress, and provide personalized support, along with real-time insights for educators.\n"
        "Tasks:\n"
        "- Offer separate interfaces for students (Task Management, Earnings Management, Budgeting Advice) and educators (Progress Monitoring, Task Assignment, Scheduling).\n"
        "- Ensure accessibility with multilingual content and features like speech-to-text and text-to-speech.",

        # Instruction 6: Infiniti AI Impact Analysis
        "Infiniti AI Impact Analysis Usage Instructions:\n"
        "Scenario:\n"
        "To demonstrate program success and secure future funding, CommunityImpactYouthCenter needs customized reports for funders and parents.\n"
        "Tasks:\n"
        "- Aggregate and analyze data from Infiniti AI Learning Assistant, EduJob Content Generator, and Funding Assistant.\n"
        "- Generate customizable reports:\n"
        "  * Funders: Focus on SROI, STEM skills improvements, financial literacy gains.\n"
        "  * Parents: Detailed child progress reports with milestones.\n"
        "  * Public Stakeholders: Summarize community impact (e.g., increased STEM interest, reduced unbanked youth).\n"
        "- Provide real-time dashboards with metrics like task completion rates and financial literacy improvements.\n"
        "- Allow custom branding for professional, tailored reports.",

        # Instruction 7: Infiniti AI EduJob Content Generator
        "Infiniti AI EduJob Content Generator Usage Instructions:\n"
        "Scenario:\n"
        "With funding secured, CommunityImpactYouthCenter needs to create engaging educational content aligned with program goals.\n"
        "Tasks:\n"
        "- Generate personalized content:\n"
        "  * Bilingual STEM Modules (English and Spanish).\n"
        "  * Financial Literacy Exercises (budgeting, saving, earning with debit cards).\n"
        "  * Interactive EduJobs with rewards for task completion.\n"
        "- Personalize content based on learner strengths and interests (e.g., technology-focused tasks, skill-level adjustments).\n"
        "- Automate content deployment to the platform for access by students and educators.",
        # # Instruction 8 : About response generation
        # "Infiniti AI Assistant response generation Instructions:\n"
        # "Scenario:\n"
        # "When the user requests detailed information or asks for an explanation of all tools, the assistant must generate a structured response."
        # "Tasks:\n"
        # "1: List Tools with Numbering and Bulleted Points for Details:"
        # "- Each tool should be introduced with a number."
        # "- Each point should start from a new line to ensure readability."
        # "- Clearly separate the purpose, input, functionality, and output of each tool."
        # "- Avoid combining too much information into one paragraph."
        # "-Provide concise, separate explanations for different aspects of the tools."
        # "Example :\n"
        # "Infiniti AI Fund Finder:"
        # "-Purpose: Identifies relevant funding opportunities tailored to your organization's needs."
        # "-Input: Information about demographics, program focus, and organizational goals."
        # "-Output: Customized grant recommendations, funder priorities, and alignment strategies",

        # Custom user input provided dynamically
        f"Infinity AI Assistant: {user_input}",

        "Output:",
    ]
    response = model.generate_content(input_data)
    return response.text
