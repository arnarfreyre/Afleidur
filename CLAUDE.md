# T-503-AFLE Derivatives Course Project

## Project Overview

This repository contains a comprehensive HTML-based derivatives course with interactive solutions, problem sets, and verification tools. The course is designed as a complete online learning platform for financial derivatives at Reykjavik University.

### Course Information
- **Course Code:** T-503-AFLE
- **Course Name:** Derivatives
- **Institution:** Reykjavik University
- **Format:** HTML-based interactive course with Python verification
- **Focus Areas:** Bond pricing, term structures, options, futures, swaps, risk management

## 📁 Project Structure & Organization

```
Afleiður/
│
├── 📄 Core Files
│   ├── index.html                    # Main course homepage with navigation
│   ├── formula-sheet.html            # Comprehensive formula reference (auto-updated)
│   ├── styles.css                    # Shared styles for all HTML pages
│   └── CLAUDE.md                     # This file - project guidelines
│
├── 📚 Chapters/                      # Course content organized by topic
│   ├── chapter-1-introduction.html   # Introduction to derivatives
│   ├── chapter-2-forwards-futures.html # Forward contracts and futures
│   ├── chapter-3-options.html        # Options pricing and strategies
│   ├── chapter-4-bonds.html          # Bond pricing and duration
│   ├── chapter-5-swaps.html          # Interest rate and currency swaps
│   └── chapter-6-risk-management.html # Risk metrics and hedging
│
├── 📝 Problem-Sets/                  # Practice problems (PDF format)
│   ├── problem-set-1.pdf            # Introduction and basic concepts
│   ├── problem-set-2.pdf            # Forwards and futures problems
│   ├── problem-set-3.pdf            # Options problems
│   └── problem-set-4.pdf            # Advanced derivatives
│
├── ✅ Solutions/                     # HTML solutions with calculations
│   ├── Solutions-1.html             # Problem Set 1 solutions
│   ├── Solutions-2.html             # Problem Set 2 solutions
│   ├── Solutions-3.html             # Problem Set 3 solutions
│   └── solutions.txt                # Text-based solution reference
│
├── 🐍 Python-Fact-Checking/         # ALL Python verification scripts
│   ├── python-solver.py             # Main fact-checking engine
│   ├── comprehensive_fact_checker.py # Detailed verification tool
│   ├── bond_pricing_corrected.py    # Bond pricing verification
│   ├── duration_investigation.py    # Duration calculation checks
│   ├── verify_solutions.py          # Solution verification
│   ├── final_verification.py        # Final validation script
│   └── problem_set_*/               # Organized by problem set
│       ├── ps1_checker.py
│       ├── ps2_checker.py
│       └── ...
│
└── 📂 Resources/                     # Additional materials
    ├── images/                       # Graphs, charts, diagrams
    ├── data/                        # Market data, examples
    └── references/                  # Academic papers, links
```

## 🎯 Folder Purpose & Content Guidelines

### **index.html** (Main Page)
- Central navigation hub for the entire course
- Links to all chapters, problem sets, solutions
- Quick access to formula sheet
- Course overview and learning objectives
- Progress tracking suggestions

### **Chapters/** Folder
**Purpose:** Sequential course content with theory and examples
- Each chapter is self-contained HTML with internal navigation
- Must include: Learning objectives, theory, examples, key formulas
- Links to: Previous/next chapter, relevant problem sets, formula sheet
- Update formula sheet when new concepts introduced

### **Problem-Sets/** Folder
**Purpose:** Practice problems for student assessment
- PDF format for easy printing and offline work
- Correspond to chapter content
- Increasing difficulty within each set
- Clear problem numbering for solution reference

### **Solutions/** Folder
**Purpose:** Detailed HTML solutions with step-by-step explanations
- **MANDATORY:** All numerical answers must be Python-verified first
- Include: Problem statement, methodology, calculations, final answer
- Show multiple solution approaches when applicable
- Link to corresponding Python verification script

### **Python-Fact-Checking/** Folder
**Purpose:** Centralized location for ALL verification scripts
- **Primary Rule:** Every solution must have a corresponding Python check
- Organized by problem set for easy reference
- Include comprehensive comments and documentation
- Output clear PASS/FAIL indicators

### **Resources/** Folder
**Purpose:** Supporting materials and references
- Images for chapters and solutions
- Market data files for examples
- Academic references and further reading

## 🚨 MANDATORY REQUIREMENTS

### 1. Python Verification First Policy

**ALL numerical answers MUST be verified in Python BEFORE being written to any solution file.**

Workflow for creating new solutions:

```bash
# Step 1: Create Python verification script
cd "Python-Fact-Checking"
touch problem_set_X/psX_problemY.py

# Step 2: Implement and verify calculations
python3 problem_set_X/psX_problemY.py

# Step 3: Only if verification passes, create HTML solution
# NEVER skip steps 1 and 2!
```

### 2. Formula Sheet Maintenance

**The formula-sheet.html must be updated whenever new formulas are introduced:**

1. After completing each chapter, review for new formulas
2. Add formulas to appropriate section in formula-sheet.html
3. Include: Formula name, mathematical expression, variable definitions, usage notes
4. Maintain consistent formatting and organization

Formula categories to maintain:
- Time Value of Money
- Bond Pricing & Duration
- Forward & Futures Pricing
- Options (Black-Scholes, Greeks)
- Swaps Valuation
- Risk Metrics

### 3. HTML Consistency Standards

All HTML files must:
- Use shared styles.css for consistent appearance
- Include navigation header with links to:
  - Main page (index.html)
  - Formula sheet
  - Previous/Next content (where applicable)
- Use semantic HTML5 elements
- Include KaTeX for mathematical expressions

### 4. File Naming Conventions

- **Chapters:** `chapter-[number]-[topic].html` (lowercase, hyphens)
- **Problem Sets:** `problem-set-[number].pdf`
- **Solutions:** `Solutions-[number].html` (capital S)
- **Python Scripts:** `ps[number]_problem[letter].py` or descriptive names
- **Images:** `[chapter]_[description].[ext]`

## 📋 Quality Assurance Checklist

### Before Creating New Content

- [ ] Review existing chapters for consistency
- [ ] Check formula sheet for required updates
- [ ] Prepare Python verification scripts

### For Each New Solution

- [ ] Python script created in Python-Fact-Checking/
- [ ] All calculations verified programmatically
- [ ] Multiple solution methods tested (when applicable)
- [ ] Results show "✓ CORRECT" in verification output
- [ ] HTML solution matches Python output exactly
- [ ] Links to main page and formula sheet included
- [ ] Proper mathematical notation using KaTeX

### For Each New Chapter

- [ ] Learning objectives clearly stated
- [ ] Theory explained with examples
- [ ] New formulas identified for formula sheet
- [ ] Links to relevant problem sets included
- [ ] Navigation to previous/next chapters
- [ ] Consistent styling with styles.css

## 🔧 Development Workflow

### Adding a New Chapter

1. Create chapter HTML in Chapters/ folder
2. Update index.html with link to new chapter
3. Identify and add new formulas to formula-sheet.html
4. Create corresponding problem set PDF
5. Prepare Python verification scripts for problems

### Adding a New Problem Set Solution

1. **First:** Write Python verification in Python-Fact-Checking/
2. **Verify:** Run script and confirm all answers
3. **Document:** Create HTML solution with explanations
4. **Cross-check:** Final verification against Python output
5. **Link:** Update index.html and relevant pages

### Updating the Formula Sheet

```html
<!-- Add new formula in appropriate section -->
<div class="formula-item">
    <h4>Formula Name</h4>
    <div class="math">
        <!-- KaTeX formula here -->
    </div>
    <p class="description">When to use this formula...</p>
</div>
```

## 🐛 Error Prevention & Debugging

### Common Pitfalls to Avoid

1. **Creating solutions without Python verification**
   - ❌ Never write HTML solutions first
   - ✅ Always verify in Python, then document

2. **Forgetting formula sheet updates**
   - ❌ Don't leave formulas only in chapters
   - ✅ Systematically update formula sheet with each chapter

3. **Inconsistent file locations**
   - ❌ Don't mix Python scripts with HTML files
   - ✅ Keep all Python in Python-Fact-Checking/

4. **Broken navigation links**
   - ❌ Don't hardcode absolute paths
   - ✅ Use relative paths for portability

### Error History & Lessons Learned

1. **Q3a Bond Pricing:** Was $1,002.41 → Corrected to $994.87
   - **Cause:** Wrong compounding method
   - **Prevention:** Always verify compounding frequency in Python first

2. **Q3c Duration:** Was 19.40 → Corrected to 7.95
   - **Cause:** Calculation error in PV values
   - **Prevention:** Verify intermediate calculations, not just final results

## 📚 Quick Reference Commands

```bash
# Navigate to fact-checking directory
cd "Python-Fact-Checking"

# Run main solver
python3 python-solver.py

# Comprehensive verification for Problem Set 1
python3 comprehensive_fact_checker.py

# Check specific problem
python3 problem_set_1/ps1_problem3a.py

# Final validation before publishing
python3 final_verification.py
```

## 🔗 Course Navigation Structure

```
index.html
    ├── Chapters
    │   ├── Chapter 1: Introduction
    │   ├── Chapter 2: Forwards & Futures
    │   └── ...
    ├── Problem Sets
    │   ├── Problem Set 1 (PDF)
    │   ├── Problem Set 2 (PDF)
    │   └── ...
    ├── Solutions
    │   ├── Solutions 1 (HTML)
    │   ├── Solutions 2 (HTML)
    │   └── ...
    └── Formula Sheet (continuously updated)
```

## 📝 Version Control & Updates

- **Always commit Python verification scripts first**
- **Tag releases when problem sets are complete**
- **Document formula sheet updates in commit messages**
- **Never commit unverified numerical answers**

---

**Golden Rule:** Every number displayed in the course must be traceable to a Python calculation in the Python-Fact-Checking/ folder. No exceptions.

*Last Updated: Project restructured for comprehensive HTML course delivery*
*Next Steps: Create formula-sheet.html with existing formulas from Problem Set 1*