# MLOps Learning Journey 🚀

This repository documents my journey of learning **DevOps + MLOps** through project-based lessons.  
Each week builds on the previous one, moving from Git basics to full ML pipelines in the cloud.  

---

## 📅 Week 3 – CI/CD with GitHub Actions

### ✅ What I Learned
- Basics of **CI/CD** (Continuous Integration & Delivery).  
- How to write a **GitHub Actions workflow**.  
- Running ML training **automatically in the cloud** when code is pushed.  
- Saving trained models as **artifacts** for later use.  

### ⚙️ How It Works
- A workflow file is defined at `.github/workflows/ml_pipeline.yml`.  
- It runs whenever code is pushed to `main` or a Pull Request is created.  
- Steps performed:
  1. Checkout repo  
  2. Set up Python  
  3. Install dependencies (`scikit-learn`)  
  4. Run `train.py`  
  5. Save the trained model (`iris_model.pkl`) as an **artifact**  

### ▶️ Running the Workflow
1. Push code to the `main` branch:  
   ```bash
   git add .
   git commit -m "Update ML pipeline"
   git push origin main
