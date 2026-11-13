Prompt Use Cases
This document identifies recurring situations in software development where reusable AI prompt patterns can improve productivity, consistency, and reliability.

Each use case defines its goal, the information that should be provided to the AI assistant, and the expected output. Placeholders such as [LANGUAGE] and [CODE] can be replaced with task-specific information.
1. Code Quality and Refactoring
- Code Refactoring
  - Goal: Improve code readability, maintainability, and efficiency without changing its existing behavior.
  - Input: Source code in [LANGUAGE], relevant requirements, and any performance or compatibility constraints.
  - Output: Refactored code, a summary of the changes, and an explanation of how behavior is preserved.
- Code Review
  - Goal: Identify defects, maintainability problems, and potential improvements before code is merged.
  - Input: [CODE], the intended behavior, and applicable project conventions.
  - Output: A prioritized list of findings with explanations, suggested fixes, and relevant code examples.
- Style and Convention Enforcement
  - Goal: Make code consistent with a specified style guide and naming conventions.
  - Input: [CODE], [LANGUAGE], and the required style guide or project conventions.
  - Output: Updated code that follows the specified conventions, plus a concise list of changes.
2. Debugging and Troubleshooting
- Error Diagnosis
  - Goal: Determine the likely cause of an error and recommend a targeted fix.
  - Input: Error message or stack trace, [CODE], expected behavior, actual behavior, and relevant environment details.
  - Output: A ranked explanation of likely causes, a proposed fix, and steps to verify the solution.
- Bug Reproduction and Isolation
  - Goal: Reduce a reported bug to a minimal, reproducible example.
  - Input: Bug description, steps to reproduce, sample input data, observed output, and relevant code.
  - Output: A minimal reproduction, the conditions that trigger the bug, and a description of the suspected faulty component.
- Performance Troubleshooting
  - Goal: Find likely performance bottlenecks and recommend measurable optimizations.
  - Input: [CODE], workload description, performance measurements or profiling results, and system constraints.
  - Output: Potential bottlenecks ranked by impact, recommended changes, and a method for benchmarking the result.
3. Documentation
- Function and API Documentation
  - Goal: Generate accurate documentation that explains how a function or API should be used.
  - Input: [CODE], parameter and return-value details, exceptions, and intended usage.
  - Output: Documentation in [FORMAT] (for example, docstrings or Markdown), including parameters, return values, errors, and examples.
- README Generation
  - Goal: Create or improve project documentation so that new contributors can understand and run the project.
  - Input: Project structure, purpose, dependencies, installation steps, configuration requirements, and usage examples.
  - Output: A structured README.md with an overview, setup instructions, usage examples, and contribution guidance where applicable.
- Technical Explanation
  - Goal: Explain an unfamiliar codebase, module, or algorithm to a specified audience.
  - Input: [CODE] or architecture description, the reader's technical level, and the topics that need explanation.
  - Output: A step-by-step explanation of the logic, key components, dependencies, and important design decisions.
4. Testing and Validation
- Unit Test Generation
  - Goal: Create unit tests that verify the expected behavior of a function or class.
  - Input: [CODE], expected behavior, edge cases, and the testing framework [TEST_FRAMEWORK].
  - Output: Executable unit tests covering normal cases, boundary conditions, and invalid inputs, with a brief explanation of each test.
- Test Case Design
  - Goal: Identify a comprehensive set of test scenarios before implementation or release.
  - Input: Feature requirements, acceptance criteria, input constraints, and known failure conditions.
  - Output: A structured test-case list containing inputs, preconditions, expected results, and priority.
- Test Failure Analysis
  - Goal: Explain why a test is failing and distinguish a code defect from an issue in the test or environment.
  - Input: Test code, failure output, relevant implementation, and environment or dependency details.
  - Output: An explanation of the failure, the most likely cause, a proposed correction, and regression tests to prevent recurrence.
5. Architecture and Implementation Planning
- Feature Implementation Planning
  - Goal: Break a feature request into manageable development steps before writing code.
  - Input: Feature description, existing architecture, technical constraints, and acceptance criteria.
  - Output: An implementation plan with subtasks, affected components, dependencies, risks, and validation steps.
- Design and Architecture Review
  - Goal: Evaluate whether a proposed design meets functional and non-functional requirements.
  - Input: Architecture description or diagram, requirements, expected scale, and constraints.
  - Output: An assessment of strengths, weaknesses, trade-offs, potential risks, and practical alternatives.
General Prompting Requirements
For all use cases, prompts should instruct the AI assistant to:
- Use only the information provided and clearly state when important information is missing.
- Avoid inventing APIs, dependencies, requirements, or test results.
- Preserve existing behavior unless the task explicitly requests a behavior change.
- Explain assumptions and highlight risks or limitations.
- Provide output in the requested format and ask for clarification when essential details are ambiguous.
