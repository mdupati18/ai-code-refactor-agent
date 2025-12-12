# 🚀 AI Code Refactoring Agent

An automated **AI-powered code analysis & refactoring system** built to demonstrate agent-driven developer tooling.

---

## ⭐ Key Features
- Static analysis of any Python file  
- AI-generated refactor suggestions using LLMs  
- Automatic rewrite + output file generation  
- Extensible rules via `agent_config.json`  
- Structured architecture (Analyzer → Agent → Output)  

---

## 📁 Project Structure
src/
analyzer/ → Code analysis module
refactor/ → AI agent refactoring engine
utils/ → File helpers
main.py → Entry point
examples/ → Before/after examples
agent_config.json
requirements.txt

yaml
Copy code

---

## 🧠 How It Works
The system:

1. Reads a Python file  
2. Analyzes it for structure + basic issues  
3. Sends it to an AI refactoring agent  
4. Generates a clean improved version  
5. Saves it as `<filename>_refactored.py`  

---

## ▶️ Run the Project

```bash
pip install -r requirements.txt
python src/main.py
