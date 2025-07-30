"""
Utility functions for Deep Job Seek Mini
"""

import re
import json
from datetime import datetime
from typing import List, Dict, Any

def extract_key_requirements(job_description: str) -> List[str]:
    """Extract key requirements and skills from job description"""
    
    # Common technical keywords to look for
    tech_keywords = [
        # Programming Languages
        'python', 'javascript', 'java', 'typescript', 'go', 'rust', 'c++', 'c#', 'php', 'ruby',
        
        # Frameworks & Libraries
        'react', 'angular', 'vue', 'flask', 'django', 'fastapi', 'express', 'spring', 'laravel',
        
        # Databases
        'postgresql', 'mysql', 'mongodb', 'redis', 'elasticsearch', 'qdrant', 'pinecone',
        
        # Cloud & Infrastructure  
        'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform', 'jenkins', 'gitlab',
        
        # Tools & Technologies
        'git', 'linux', 'api', 'rest', 'graphql', 'microservices', 'ci/cd', 'devops',
        
        # Data & AI
        'machine learning', 'data science', 'tensorflow', 'pytorch', 'pandas', 'numpy',
        
        # Other
        'agile', 'scrum', 'testing', 'security', 'performance', 'monitoring'
    ]
    
    # Convert to lowercase for matching
    job_lower = job_description.lower()
    
    # Find matching keywords
    found_keywords = []
    for keyword in tech_keywords:
        if keyword in job_lower:
            found_keywords.append(keyword.title())
    
    # Extract years of experience
    experience_patterns = [
        r'(\d+)\+?\s*years?\s+(?:of\s+)?experience',
        r'(\d+)\+?\s*years?\s+(?:in|with)',
        r'minimum\s+(\d+)\s+years?',
        r'at\s+least\s+(\d+)\s+years?'
    ]
    
    for pattern in experience_patterns:
        match = re.search(pattern, job_lower)
        if match:
            years = match.group(1)
            found_keywords.append(f"{years}+ Years Experience")
            break
    
    # Extract degree requirements
    degree_patterns = [
        r'bachelor.?s?\s+degree',
        r'master.?s?\s+degree', 
        r'phd',
        r'computer\s+science',
        r'engineering\s+degree'
    ]
    
    for pattern in degree_patterns:
        if re.search(pattern, job_lower):
            found_keywords.append("Degree Required")
            break
    
    return list(set(found_keywords))[:10]  # Return unique keywords, max 10

def build_resume_json(basics: Dict, work_experiences: List[Dict], skills: List[str], projects: List[Dict] = None) -> Dict[str, Any]:
    """Build a complete JSON Resume schema compliant resume"""
    
    resume = {
        "$schema": "https://raw.githubusercontent.com/jsonresume/resume-schema/v1.0.0/schema.json",
        "_metadata": {
            "generated_at": datetime.now().strftime("%Y%m%d-%H%M%S"),
            "generator": "Deep Job Seek Mini",
            "model": "HuggingFace/sentence-transformers"
        },
        "basics": {
            "name": basics.get("name", "AI-Generated Candidate"),
            "email": basics.get("email", "candidate@example.com"),
            "phone": basics.get("phone", "+1-555-0123"),
            "summary": basics.get("summary", "Professional with relevant experience")
        },
        "work": work_experiences or [],
        "skills": [{"name": skill, "level": "Advanced"} for skill in skills] if skills else [],
        "projects": projects or [],
        "education": [
            {
                "institution": "University of Technology",
                "area": "Computer Science",
                "studyType": "Bachelor of Science",
                "startDate": "2015-09-01",
                "endDate": "2019-05-31"
            }
        ]
    }
    
    return resume

def calculate_relevance_score(job_requirements: List[str], candidate_skills: List[str]) -> float:
    """Calculate relevance score between job requirements and candidate skills"""
    
    if not job_requirements or not candidate_skills:
        return 0.0
    
    # Convert to lowercase for comparison
    job_lower = [req.lower() for req in job_requirements]
    skills_lower = [skill.lower() for skill in candidate_skills]
    
    # Count matches
    matches = 0
    for req in job_lower:
        for skill in skills_lower:
            if req in skill or skill in req:
                matches += 1
                break
    
    # Calculate percentage
    return min(matches / len(job_requirements), 1.0)

def format_resume_for_display(resume: Dict[str, Any]) -> str:
    """Format resume for readable display"""
    
    output = []
    
    # Basics
    basics = resume.get("basics", {})
    output.append(f"# {basics.get('name', 'N/A')}")
    output.append(f"📧 {basics.get('email', 'N/A')} | 📞 {basics.get('phone', 'N/A')}")
    output.append(f"\n**Summary:** {basics.get('summary', 'N/A')}")
    
    # Work Experience
    work = resume.get("work", [])
    if work:
        output.append("\n## 💼 Work Experience")
        for job in work:
            output.append(f"\n### {job.get('position', 'N/A')} at {job.get('name', 'N/A')}")
            output.append(f"*{job.get('startDate', 'N/A')} - {job.get('endDate', 'Present')}*")
            output.append(f"\n{job.get('summary', 'N/A')}")
            
            highlights = job.get('highlights', [])
            if highlights:
                output.append("\n**Key Achievements:**")
                for highlight in highlights:
                    output.append(f"• {highlight}")
    
    # Skills
    skills = resume.get("skills", [])
    if skills:
        output.append("\n## 🛠️ Skills")
        skill_names = [skill.get('name', skill) if isinstance(skill, dict) else skill for skill in skills]
        output.append(", ".join(skill_names))
    
    # Projects
    projects = resume.get("projects", [])
    if projects:
        output.append("\n## 🚀 Projects")
        for project in projects:
            output.append(f"\n### {project.get('name', 'N/A')}")
            output.append(f"{project.get('description', 'N/A')}")
            
            highlights = project.get('highlights', [])
            if highlights:
                for highlight in highlights:
                    output.append(f"• {highlight}")
    
    return "\n".join(output)

def validate_json_resume(resume: Dict[str, Any]) -> bool:
    """Validate if resume follows JSON Resume schema"""
    
    required_fields = ["basics"]
    optional_fields = ["work", "skills", "projects", "education", "volunteer", "awards", "publications"]
    
    # Check required fields
    for field in required_fields:
        if field not in resume:
            return False
    
    # Validate basics section
    basics = resume.get("basics", {})
    if not isinstance(basics, dict):
        return False
    
    # Check work experience format
    work = resume.get("work", [])
    if work and not isinstance(work, list):
        return False
    
    return True