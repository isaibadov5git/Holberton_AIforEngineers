# Refactoring Prompt Template

**Role**: Senior Developer  
**Task**: Refactor the given [LANGUAGE] code for clarity, modularity, and performance.  
**Input Placeholder**: [CODE_BLOCK]  
**Expected Output**: Clean, optimized code with inline comments explaining the refactoring choices.

# Code Generation Prompt Template

**Role**: Expert [LANGUAGE] Programmer  
**Task**: Write an efficient and robust implementation for the described functionality.  
**Input Placeholder**: [FUNCTIONALITY_DESCRIPTION_AND_CONSTRAINTS]  
**Expected Output**: Ready-to-run [LANGUAGE] code without external unrequested dependencies, including basic error handling.

# Debugging Prompt Template

**Role**: Troubleshooting Specialist  
**Task**: Identify the root cause of the provided error and fix the code.  
**Input Placeholder**: 
- Code: [CODE_BLOCK]
- Error Message/Stack Trace: [ERROR_MESSAGE]  
**Expected Output**: A brief explanation of the bug followed by the corrected code block.

# Code Review Prompt Template

**Role**: Principal Software Engineer  
**Task**: Conduct a comprehensive code review focusing on best practices, edge cases, and maintainability.  
**Input Placeholder**: [CODE_BLOCK_OR_PULL_REQUEST_DIFF]  
**Expected Output**: A bulleted list of constructive feedback, highlighting both strengths and areas for improvement, followed by a suggested revised code snippet.

# Unit Testing Prompt Template

**Role**: QA Automation Engineer  
**Task**: Write comprehensive unit tests for the provided code using [TESTING_FRAMEWORK].  
**Input Placeholder**: [CODE_BLOCK_TO_TEST]  
**Expected Output**: A complete test suite covering positive cases, negative cases, and edge cases, using appropriate mocks where necessary.

# Documentation Prompt Template

**Role**: Technical Writer  
**Task**: Generate clear, developer-friendly documentation for the provided code/module.  
**Input Placeholder**: [CODE_BLOCK_OR_SYSTEM_DESCRIPTION]  
**Expected Output**: Markdown documentation including an overview, parameter descriptions, return values, and a usage example.

# Query Optimization Prompt Template

**Role**: Database Administrator  
**Task**: Analyze and optimize the provided database query to reduce execution time and resource consumption.  
**Input Placeholder**: 
- Database Engine: [SQL/NOSQL_ENGINE]
- Query: [QUERY_BLOCK]
- Schema (optional): [SCHEMA_DEFINITION]  
**Expected Output**: The optimized query accompanied by a brief explanation of why the changes improve performance (e.g., index utilization).

# Code Explanation Prompt Template

**Role**: Technical Mentor  
**Task**: Break down the provided code and explain how it works step-by-step for a beginner audience.  
**Input Placeholder**: [COMPLEX_CODE_BLOCK]  
**Expected Output**: A clear, jargon-free paragraph explaining the overall goal, followed by a line-by-line or logical block breakdown of the execution flow.# Security Vulnerability Scan Prompt Template

**Role**: Application Security Analyst  
**Task**: Review the provided code for security vulnerabilities (e.g., OWASP Top 10 like SQL injection, XSS).  
**Input Placeholder**: [CODE_BLOCK]  
**Expected Output**: A security audit report listing any identified vulnerabilities, their severity, and the specific remediation code.

# System Design Prompt Template

**Role**: Software Architect  
**Task**: Propose a high-level system architecture for the described application.  
**Input Placeholder**: [APPLICATION_REQUIREMENTS_AND_SCALE]  
**Expected Output**: A structured design document outlining core components, data flow, tech stack recommendations, and scalability strategies.
