#!/usr/bin/env python3
"""
Deep Job Seek Mini - HuggingFace Space
AI-powered resume generation with HuggingFace native models
"""

import gradio as gr
import json
from datetime import datetime
from sentence_transformers import SentenceTransformer
import numpy as np
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch
from resume_data import RESUME_DATABASE
from utils import build_resume_json, extract_key_requirements

# Initialize models
@gr.cache
def load_models():
    """Load and cache HuggingFace models"""
    
    # Embedding model for similarity search
    embedding_model = SentenceTransformer('BAAI/bge-small-en-v1.5')
    
    # Text generation model for resume content
    generator = pipeline(
        "text-generation",
        model="gpt2",
        device=0 if torch.cuda.is_available() else -1,
        do_sample=True,
        temperature=0.7,
        max_new_tokens=100,
        pad_token_id=50256
    )
    
    return embedding_model, generator

def find_relevant_experience(job_description, embedding_model, top_k=5):
    """Find most relevant resume experiences using semantic search"""
    
    # Get job description embedding
    job_embedding = embedding_model.encode([job_description])
    
    # Get all experience embeddings
    experiences = []
    embeddings = []
    
    for person in RESUME_DATABASE:
        for exp in person.get('work', []):
            experiences.append({
                'person': person['basics']['name'],
                'company': exp.get('name', ''),
                'position': exp.get('position', ''),
                'summary': exp.get('summary', ''),
                'highlights': exp.get('highlights', []),
                'skills': person.get('skills', [])
            })
            
            # Create searchable text
            searchable_text = f"{exp.get('position', '')} {exp.get('summary', '')} {' '.join(exp.get('highlights', []))}"
            embeddings.append(embedding_model.encode([searchable_text])[0])
    
    # Calculate similarities
    if embeddings:
        embeddings_matrix = np.vstack(embeddings)
        similarities = np.dot(job_embedding, embeddings_matrix.T)[0]
        
        # Get top experiences
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        return [experiences[i] for i in top_indices]
    
    return []

def generate_resume_content(job_description, relevant_experiences, generator):
    """Generate tailored resume content using HuggingFace models"""
    
    # Extract key requirements from job description
    requirements = extract_key_requirements(job_description)
    
    # Build base resume structure
    resume = {
        "$schema": "https://raw.githubusercontent.com/jsonresume/resume-schema/v1.0.0/schema.json",
        "_metadata": {
            "generated_at": datetime.now().strftime("%Y%m%d-%H%M%S"),
            "model": "HuggingFace/gpt2",
            "source": "Deep Job Seek Mini"
        },
        "basics": {
            "name": "AI-Generated Candidate",
            "email": "candidate@example.com", 
            "phone": "+1-555-0123",
            "summary": generate_professional_summary(job_description, requirements, generator)
        },
        "work": [],
        "skills": [],
        "projects": [],
        "education": []
    }
    
    # Add relevant work experiences
    for i, exp in enumerate(relevant_experiences[:3]):  # Top 3 experiences
        tailored_exp = {
            "name": exp['company'],
            "position": exp['position'],
            "summary": exp['summary'],
            "highlights": exp['highlights'][:3],  # Top 3 highlights
            "startDate": "2020-01-01",  # Placeholder
            "endDate": "2023-12-31" if i == 0 else "2020-12-31"
        }
        resume['work'].append(tailored_exp)
    
    # Add relevant skills
    all_skills = []
    for exp in relevant_experiences:
        all_skills.extend(exp.get('skills', []))
    
    # Deduplicate and prioritize skills
    unique_skills = list(set(all_skills))[:10]  # Top 10 skills
    resume['skills'] = [{"name": skill, "level": "Advanced"} for skill in unique_skills]
    
    return resume

def generate_professional_summary(job_description, requirements, generator):
    """Generate a professional summary using HuggingFace model"""
    
    # Create a prompt for summary generation
    prompt = f"Professional summary for a candidate applying to: {job_description[:200]}... Key requirements: {', '.join(requirements[:5])}. Summary:"
    
    try:
        # Generate summary
        result = generator(prompt, max_new_tokens=50, num_return_sequences=1, truncation=True)
        generated_text = result[0]['generated_text']
        
        # Extract just the summary part
        if "Summary:" in generated_text:
            summary = generated_text.split("Summary:")[-1].strip()
        else:
            summary = generated_text.replace(prompt, "").strip()
            
        # Clean up and limit length
        summary = summary.split('.')[0] + '.' if '.' in summary else summary
        return summary[:200] if len(summary) > 200 else summary
        
    except Exception as e:
        # Fallback summary
        return f"Experienced professional with expertise in {', '.join(requirements[:3])} seeking to contribute to innovative projects and drive business success."

def generate_resume(job_description, progress=gr.Progress()):
    """Main function to generate tailored resume"""
    
    if not job_description.strip():
        return None, "Please enter a job description."
    
    try:
        progress(0.1, desc="Loading AI models...")
        embedding_model, generator = load_models()
        
        progress(0.3, desc="Analyzing job requirements...")
        relevant_experiences = find_relevant_experience(job_description, embedding_model)
        
        progress(0.6, desc="Generating tailored resume...")
        resume = generate_resume_content(job_description, relevant_experiences, generator)
        
        progress(0.9, desc="Finalizing resume...")
        
        # Format for display
        resume_json = json.dumps(resume, indent=2)
        
        progress(1.0, desc="Complete!")
        
        return resume_json, "✅ Resume generated successfully!"
        
    except Exception as e:
        return None, f"❌ Error generating resume: {str(e)}"

# Create Gradio interface
def create_interface():
    """Create the Gradio interface"""
    
    # Custom CSS for branding
    css = """
    .container {
        max-width: 1200px !important;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        padding: 1rem;
        border-top: 1px solid #e0e0e0;
        font-family: monospace;
    }
    """
    
    with gr.Blocks(css=css, title="Deep Job Seek Mini") as demo:
        
        # Header
        gr.Markdown("# 🚀 Deep Job Seek Mini")
        gr.Markdown("*AI-powered resume generation with HuggingFace models*")
        
        # Main interface
        with gr.Row():
            with gr.Column(scale=1):
                job_input = gr.Textbox(
                    label="📝 Job Description",
                    placeholder="Paste the job description here...",
                    lines=10,
                    max_lines=15
                )
                
                generate_btn = gr.Button(
                    "✨ Generate Tailored Resume", 
                    variant="primary",
                    size="lg"
                )
                
                status_output = gr.Textbox(
                    label="Status",
                    interactive=False,
                    max_lines=2
                )
                
            with gr.Column(scale=2):
                resume_output = gr.JSON(
                    label="📄 Generated Resume (JSON Resume Schema)",
                    show_label=True
                )
        
        # Examples
        gr.Markdown("## 💡 Example Job Descriptions")
        
        example_jobs = [
            "Senior Python Developer with Flask experience, 5+ years building REST APIs, Docker expertise required",
            "DevOps Engineer specializing in AWS, Kubernetes, and CI/CD pipelines with 3+ years experience",
            "Full-Stack Developer proficient in React, Node.js, and PostgreSQL for e-commerce applications"
        ]
        
        gr.Examples(
            examples=[[job] for job in example_jobs],
            inputs=[job_input],
            label="Click an example to try:"
        )
        
        # Event handlers
        generate_btn.click(
            fn=generate_resume,
            inputs=[job_input],
            outputs=[resume_output, status_output],
            show_progress=True
        )
        
        # Footer with branding
        gr.Markdown(
            """
            ---
            
            **🔗 Links:**
            - [Full API with Docker](https://github.com/aloshy-ai/deep-job-seek) 
            - [Documentation](https://github.com/aloshy-ai/deep-job-seek#readme)
            
            ```
            ▄▀█ █░░ █▀█ █▀ █░█ █▄█ ░ ▄▀█ █
            █▀█ █▄▄ █▄█ ▄█ █▀█ ░█░ ▄ █▀█ █
            ```
            """,
            elem_classes=["footer"]
        )
    
    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )