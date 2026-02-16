### PHASE 5: TEST REPOSITORY

- OBJECTIVE: Create a test repository with intentional security issues to
  validate our extractors.
- TASK 12: Create Test Repository with Known Issues
    - **Initialize git repo**
         ```bash
            git init
            git config user.email "mygeekboxpro@proton.me"
            git config user.name "mygeekboxpro"
         ```
    - **Initial Commit**
       ```bash
          git commit -m "first commit" 
       ```
    - **Create main branch**
      ```bash
         git branch -M main
         git remote add origin https://github.com/mygeekboxpro/test_repo.git
         git push -u origin main      
      ```
    - **Checkout main branch:**
      ```bash
        git checkout -b main
      ```
    - **Create .gitignore file**
    - **Create a sample requirements.txt file**
      ```
      requests==2.31.0
      click==8.1.0
      pyyaml==5.3.1
      ```
    - **Create branch with no issues**
        - **Create a simple, safe module with no issues**
          FILE: `src/safe_module.py`
          ```
            """
            A simple, safe module with no issues.
            """
          
          
            def add_numbers(a, b):
                """Add two numbers."""
                return a + b
          
          
            def greet(name):
                """Greet someone."""
                return f"Hello, {name}!"
          ```

        - **Commit and push code to `origin main`**
             ```bash
                git add requirements.txt src/safe_module.py .gitignore
             ```
             ```bash
                git commit -m "Initial commit - clean code"
             ```
             ```bash
                git push
             ```

    - **Create feature branch with issues**
        - **Add new dependency**
          FILE: `requirements.txt`
          ```
            pyyaml==5.3.1
          ```
        - **Create a simple, module containing hardcoded secret**
          FILE: `tests/test_repo/src/auth.py`
          ```
          """
          Authentication module - INTENTIONALLY HAS SECURITY ISSUES.
          """
          # This is not complete code. Refe to code file or 
          https://claude.ai/chat/26a31eb4-ecc7-4536-91f8-a7a1c1b08010
          ```
        - Now create feature branch
             ```bash
                git checkout -b feature-with-issues
             ```
        - **Commit and push code to `origin main`**
             ```bash
                git add requirements.txt src/auth.py
             ```
        - **Commit and push code to `origin feature-with-issues`**
             ```bash
                git commit -m "Add authentication module"
             ```
             ```bash
                git push
             ```
- **Create tags for testing**
     ```bash
        git tag base-clean main
        git tag head-with-issues feature-with-issues
     ```
