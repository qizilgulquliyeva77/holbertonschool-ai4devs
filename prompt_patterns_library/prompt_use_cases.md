# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability, complexity, and runtime performance  
  - **Input**: Legacy source function in [LANGUAGE]  
  - **Output**: Optimized code block + architectural optimization summary  

- **Style Enforcement**
  - **Goal**: Enforce consistent naming, architectural formatting, and linter standards  
  - **Input**: Raw unformatted source code  
  - **Output**: Rewritten code compliant with specified [STYLE_GUIDE]  

- **Security Auditing**
  - **Goal**: Detect vulnerability vectors like injections, overflows, or hardcoded secrets  
  - **Input**: High-risk system code component  
  - **Output**: Vulnerability assessment checklist + hardened code variant  

## Debugging
- **Stack Trace Analysis**
  - **Goal**: Decode obfuscated application crash dumps and isolate root failure files  
  - **Input**: Raw console error trace log + context snippets  
  - **Output**: Failure root-cause diagnosis + execution line patch  

- **Logical Anomaly Isolation**
  - **Goal**: Resolve silent boundary failures where scripts run without explicit error signals  
  - **Input**: Misbehaving functional code + expected runtime parameters  
  - **Output**: Detected logic variance + corrected algorithmic logic  

- **Regression Optimization**
  - **Goal**: Isolate specific code changes introduced between commits that broke existing features  
  - **Input**: Git diff log + prior working performance metrics  
  - **Output**: Breakdown of regressive lines + localized fix  

## Documentation
- **API Reference Generation**
  - **Goal**: Generate production-grade interface contracts from raw logic implementations  
  - **Input**: Clean backend controller or helper logic script  
  - **Output**: Markdown-formatted API specifications with inputs, outputs, and status types  

- **Inline Docstring Automation**
  - **Goal**: Populate functions with comprehensive types, descriptions, and exception maps  
  - **Input**: Document-deficient project modules  
  - **Output**: Complete source files enriched with native documentation structures  

- **Release Note Compilation**
  - **Goal**: Synthesize multi-developer commit histories into customer-facing logs  
  - **Input**: Chronological git commit log array  
  - **Output**: Categorized changelog detailing new additions, bug fixes, and deprecations  

## Testing
- **Unit Test Case Generation**
  - **Goal**: Achieve structural path and statement test coverage requirements  
  - **Input**: Targeted processing module in [LANGUAGE]  
  - **Output**: Complete test suite utilizing [TESTING_FRAMEWORK] specifications  

- **Edge Case Mutation Extraction**
  - **Goal**: Generate hostile payload datasets to challenge baseline application resilience  
  - **Input**: Data parsing schemas or logic rules  
  - **Output**: Array of diverse mock datasets containing boundary values, empty inputs, and invalid formats  
