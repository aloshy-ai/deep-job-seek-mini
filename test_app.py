#!/usr/bin/env python3
"""
Simple test script for Deep Job Seek Mini
"""

import json
from resume_data import RESUME_DATABASE
from utils import extract_key_requirements, build_resume_json

def test_resume_data():
    """Test that resume data is properly formatted"""
    print("🧪 Testing resume data...")
    
    assert len(RESUME_DATABASE) > 0, "Resume database should not be empty"
    
    for i, person in enumerate(RESUME_DATABASE):
        assert "basics" in person, f"Person {i} missing basics section"
        assert "work" in person, f"Person {i} missing work section"
        assert "skills" in person, f"Person {i} missing skills section"
        
        # Test basics
        basics = person["basics"]
        assert "name" in basics, f"Person {i} missing name"
        assert "email" in basics, f"Person {i} missing email"
        
        print(f"✅ Person {i+1}: {basics['name']}")
    
    print(f"✅ All {len(RESUME_DATABASE)} resume profiles are valid")

def test_key_extraction():
    """Test key requirement extraction"""
    print("\n🧪 Testing key requirement extraction...")
    
    test_job = """
    Senior Python Developer with 5+ years experience.
    Required skills: Flask, Docker, PostgreSQL, REST APIs.
    Bachelor's degree in Computer Science preferred.
    Experience with AWS and Kubernetes is a plus.
    """
    
    requirements = extract_key_requirements(test_job)
    print(f"Extracted requirements: {requirements}")
    
    # Should find some key requirements
    assert len(requirements) > 0, "Should extract some requirements"
    
    expected_keywords = ["Python", "Flask", "Docker", "PostgreSQL"]
    found_keywords = [req for req in requirements if any(exp.lower() in req.lower() for exp in expected_keywords)]
    
    assert len(found_keywords) > 0, f"Should find some expected keywords, got: {requirements}"
    print("✅ Key requirement extraction works")

def test_resume_building():
    """Test resume JSON building"""
    print("\n🧪 Testing resume building...")
    
    sample_basics = {
        "name": "Test Candidate",
        "email": "test@example.com",
        "phone": "+1-555-0000",
        "summary": "Test summary"
    }
    
    sample_work = [
        {
            "name": "Test Company",
            "position": "Test Position",
            "summary": "Test work summary",
            "highlights": ["Achievement 1", "Achievement 2"]
        }
    ]
    
    sample_skills = ["Python", "Testing", "JSON"]
    
    resume = build_resume_json(sample_basics, sample_work, sample_skills)
    
    # Validate structure
    assert "$schema" in resume, "Missing JSON Resume schema"
    assert "basics" in resume, "Missing basics section"
    assert "work" in resume, "Missing work section"
    assert "skills" in resume, "Missing skills section"
    
    # Validate content
    assert resume["basics"]["name"] == "Test Candidate"
    assert len(resume["work"]) == 1
    assert len(resume["skills"]) == 3
    
    print("✅ Resume building works")
    print(f"Sample resume structure: {list(resume.keys())}")

def main():
    """Run all tests"""
    print("🚀 Running Deep Job Seek Mini tests...\n")
    
    try:
        test_resume_data()
        test_key_extraction()
        test_resume_building()
        
        print("\n🎉 All tests passed! The app should work correctly.")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)