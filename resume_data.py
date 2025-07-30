"""
Resume database for Deep Job Seek Mini
Contains sample resume data in JSON Resume schema format
"""

RESUME_DATABASE = [
    {
        "basics": {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "+1-555-0123",
            "summary": "Full-stack software engineer with 5 years of experience in Python, Flask, and API development"
        },
        "work": [
            {
                "name": "Tech Corp",
                "position": "Senior Software Engineer",
                "startDate": "2021-01-01",
                "endDate": "2024-01-01",
                "summary": "Developed REST APIs using Flask and Python, implemented vector search with Qdrant",
                "highlights": [
                    "Built scalable APIs handling 10K+ requests/day",
                    "Implemented vector search with Qdrant for 90% faster queries",
                    "Led team of 3 developers on microservices architecture",
                    "Reduced API response time by 60% through optimization"
                ]
            },
            {
                "name": "StartupXYZ",
                "position": "Python Developer",
                "startDate": "2019-06-01",
                "endDate": "2020-12-31",
                "summary": "Developed machine learning pipelines and data processing systems",
                "highlights": [
                    "Built ML pipelines processing 1M+ records daily",
                    "Implemented data processing systems with 99.9% uptime",
                    "Integrated with 15+ external APIs",
                    "Automated deployment with Docker and CI/CD"
                ]
            }
        ],
        "skills": [
            "Python", "Flask", "FastAPI", "Docker", "Qdrant", "PostgreSQL", 
            "REST APIs", "Microservices", "Vector Search", "Machine Learning"
        ],
        "projects": [
            {
                "name": "Resume Generator API",
                "description": "Built an AI-powered resume generation system using Flask, Qdrant, and LM Studio",
                "highlights": [
                    "Flask API with vector search capabilities",
                    "Qdrant database for semantic matching",
                    "LM Studio integration for AI generation",
                    "Docker containerization for easy deployment"
                ],
                "url": "https://github.com/example/resume-generator"
            }
        ]
    },
    {
        "basics": {
            "name": "Sarah Chen",
            "email": "sarah.chen@example.com",
            "phone": "+1-555-0456",
            "summary": "DevOps engineer specializing in AWS, Kubernetes, and CI/CD automation with 4+ years experience"
        },
        "work": [
            {
                "name": "CloudTech Solutions",
                "position": "Senior DevOps Engineer",
                "startDate": "2022-03-01",
                "endDate": "2024-12-31",
                "summary": "Managed AWS infrastructure and Kubernetes clusters for high-traffic applications",
                "highlights": [
                    "Managed AWS infrastructure serving 50M+ users",
                    "Orchestrated Kubernetes clusters with 99.99% uptime",
                    "Implemented CI/CD pipelines reducing deployment time by 80%",
                    "Cost optimization saved company $100K annually"
                ]
            },
            {
                "name": "Digital Innovations",
                "position": "DevOps Engineer",
                "startDate": "2020-01-01",
                "endDate": "2022-02-28",
                "summary": "Built automation tools and managed cloud infrastructure",
                "highlights": [
                    "Automated infrastructure deployment with Terraform",
                    "Implemented monitoring with Prometheus and Grafana",
                    "Built CI/CD pipelines with Jenkins and GitLab",
                    "Managed multi-region AWS deployments"
                ]
            }
        ],
        "skills": [
            "AWS", "Kubernetes", "Docker", "Terraform", "Jenkins", "GitLab CI",
            "Prometheus", "Grafana", "Python", "Bash", "Infrastructure as Code"
        ],
        "projects": [
            {
                "name": "Kubernetes Monitoring Stack",
                "description": "Comprehensive monitoring solution for Kubernetes clusters with alerting and dashboards",
                "highlights": [
                    "Prometheus and Grafana setup",
                    "Custom metrics and alerting rules",
                    "Multi-cluster monitoring",
                    "Automated deployment with Helm"
                ]
            }
        ]
    },
    {
        "basics": {
            "name": "Mike Rodriguez",
            "email": "mike.rodriguez@example.com",
            "phone": "+1-555-0789",
            "summary": "Full-stack developer with expertise in React, Node.js, and database design, 6+ years building web applications"
        },
        "work": [
            {
                "name": "E-Commerce Giants",
                "position": "Full-Stack Developer",
                "startDate": "2020-06-01",
                "endDate": "2024-12-31",
                "summary": "Developed e-commerce platform serving millions of customers with React and Node.js",
                "highlights": [
                    "Built React frontend serving 2M+ daily users",
                    "Developed Node.js APIs handling 100K+ transactions/day",
                    "Optimized PostgreSQL queries for 50% faster page loads",
                    "Implemented real-time features with WebSocket connections"
                ]
            },
            {
                "name": "WebDev Studio",
                "position": "Frontend Developer",
                "startDate": "2018-01-01",
                "endDate": "2020-05-31",
                "summary": "Created responsive web applications and mobile-first user interfaces",
                "highlights": [
                    "Built responsive React applications",
                    "Implemented mobile-first design principles",
                    "Integrated with RESTful APIs and GraphQL",
                    "Performance optimization achieving 95+ Lighthouse scores"
                ]
            }
        ],
        "skills": [
            "React", "Node.js", "JavaScript", "TypeScript", "PostgreSQL", "MongoDB",
            "GraphQL", "REST APIs", "WebSocket", "HTML5", "CSS3", "Responsive Design"
        ],
        "projects": [
            {
                "name": "Real-time Chat Application",
                "description": "Scalable chat application with React frontend and Node.js backend supporting 10K+ concurrent users",
                "highlights": [
                    "React frontend with real-time updates",
                    "Node.js backend with WebSocket support",
                    "MongoDB for message persistence",
                    "Horizontal scaling with Redis pub/sub"
                ]
            }
        ]
    },
    {
        "basics": {
            "name": "Dr. Lisa Wang",
            "email": "lisa.wang@example.com", 
            "phone": "+1-555-0321",
            "summary": "Data scientist and ML engineer with PhD in Computer Science, specializing in NLP and deep learning"
        },
        "work": [
            {
                "name": "AI Research Lab",
                "position": "Senior Data Scientist",
                "startDate": "2021-09-01",
                "endDate": "2024-12-31",
                "summary": "Led research and development of NLP models and recommendation systems",
                "highlights": [
                    "Developed transformer models achieving 95% accuracy",
                    "Built recommendation systems increasing engagement by 40%",
                    "Published 8 papers in top-tier ML conferences",
                    "Led team of 5 researchers on multimodal AI projects"
                ]
            },
            {
                "name": "Data Analytics Corp",
                "position": "Data Scientist",
                "startDate": "2019-01-01",
                "endDate": "2021-08-31",
                "summary": "Built predictive models and analytics platforms for business intelligence",
                "highlights": [
                    "Developed predictive models with 90%+ accuracy",
                    "Built real-time analytics dashboards",
                    "Implemented A/B testing frameworks",
                    "Automated ML pipeline reducing model training time by 70%"
                ]
            }
        ],
        "skills": [
            "Python", "TensorFlow", "PyTorch", "scikit-learn", "Pandas", "NumPy",
            "NLP", "Deep Learning", "Computer Vision", "MLOps", "Docker", "Kubernetes"
        ],
        "projects": [
            {
                "name": "Multi-modal AI Assistant",
                "description": "Advanced AI system processing text, images, and audio for intelligent task automation",
                "highlights": [
                    "Transformer-based NLP models",
                    "Computer vision with CNNs",
                    "Audio processing with RNNs",
                    "Multi-modal fusion techniques"
                ]
            }
        ]
    },
    {
        "basics": {
            "name": "Alex Thompson",
            "email": "alex.thompson@example.com",
            "phone": "+1-555-0654",
            "summary": "Security engineer with 5+ years experience in cybersecurity, penetration testing, and secure system design"
        },
        "work": [
            {
                "name": "CyberSec Solutions",
                "position": "Senior Security Engineer",
                "startDate": "2022-01-01",
                "endDate": "2024-12-31", 
                "summary": "Designed secure architectures and conducted security assessments for enterprise clients",
                "highlights": [
                    "Conducted 50+ penetration tests identifying critical vulnerabilities",
                    "Designed secure architectures for Fortune 500 companies",
                    "Implemented zero-trust security frameworks",
                    "Reduced security incidents by 85% through proactive measures"
                ]
            },
            {
                "name": "SecureTech Inc",
                "position": "Security Analyst",
                "startDate": "2019-06-01", 
                "endDate": "2021-12-31",
                "summary": "Monitored security threats and implemented incident response procedures",
                "highlights": [
                    "Monitored 24/7 SOC operations",
                    "Implemented SIEM solutions",
                    "Developed incident response playbooks",
                    "Conducted security awareness training for 500+ employees"
                ]
            }
        ],
        "skills": [
            "Penetration Testing", "Cybersecurity", "SIEM", "Zero Trust", "Python",
            "Network Security", "Incident Response", "Risk Assessment", "Compliance"
        ],
        "projects": [
            {
                "name": "Enterprise Security Framework",
                "description": "Comprehensive security framework implementing zero-trust principles for large organizations",
                "highlights": [
                    "Zero-trust architecture design",
                    "Multi-factor authentication implementation",
                    "Automated threat detection",
                    "Compliance monitoring and reporting"
                ]
            }
        ]
    }
]