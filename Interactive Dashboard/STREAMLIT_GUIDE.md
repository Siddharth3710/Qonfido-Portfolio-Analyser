# 🎨 Interactive Dashboard Guide

## 📊 Streamlit Portfolio Analyzer

This interactive web dashboard provides a beautiful UI for analyzing Axis MF portfolios.

---

## ✨ Features

### 📤 **File Upload**
- Drag & drop Excel files
- Automatic processing
- Real-time validation

### 📊 **Visual Analytics**
- Asset type distribution (pie chart)
- Top 10 holdings (bar chart)
- Scheme distribution
- Value distribution histogram

### 📋 **Data Table**
- Searchable portfolio data
- Adjustable rows (10/25/50/100)
- Clean, professional display

### 💾 **Export**
- Download CSV
- Download Excel
- Includes all processed data

---

## 🚀 Quick Start

### **Step 1: Install Dependencies**

```bash
pip install -r requirements_streamlit.txt
```

This installs:
- streamlit (web framework)
- plotly (interactive charts)
- pandas & openpyxl (data processing)

### **Step 2: Run the Dashboard**

```bash
streamlit run streamlit_app.py
```

### **Step 3: Open in Browser**

The dashboard automatically opens at:
```
http://localhost:8501
```

---

## 📖 How to Use

### **1. Upload File**
- Click "Browse files" or drag & drop
- Select your Excel file (e.g., `Monthly Portfolio-31 12 25.xlsx`)
- File must be from Axis MF statutory disclosures

### **2. Process Data**
- Click the "🔄 Process Portfolio Data" button
- Wait 5-10 seconds for processing
- Green success message appears

### **3. Explore Analytics**
- **Metrics**: View total holdings, schemes, value, debt %
- **Charts**: Interactive visualizations (hover for details)
- **Table**: Search and filter portfolio data

### **4. Download Results**
- Click "📥 Download CSV" for consolidated data
- Or "📥 Download Excel" for Excel format
- File includes all processed holdings

---

## 📸 Dashboard Sections

### **Header**
- Clean, professional title
- Upload interface

### **Sidebar**
- About section
- Features list
- Developer info

### **Analytics Dashboard** (after processing)
1. **Key Metrics Cards**
   - Total holdings count
   - Number of schemes
   - Total portfolio value
   - Debt percentage

2. **Asset Distribution Chart**
   - Pie chart showing Debt/Equity/Other split
   - Interactive (click to filter)

3. **Top Holdings Chart**
   - Horizontal bar chart
   - Shows largest 10 positions by value

4. **Scheme Distribution**
   - Bar chart of top 10 schemes
   - By number of holdings

5. **Value Distribution**
   - Histogram showing value spread
   - Helps identify concentration

6. **Data Table**
   - Search box to filter
   - Adjustable row count
   - Shows key columns

7. **Download Section**
   - CSV export
   - Excel export
   - Date-stamped filenames

8. **Summary Statistics**
   - Data quality metrics
   - Asset breakdown
   - Value statistics

---

## 🎨 Dashboard Features

### **Interactive Charts**
- **Hover**: See exact values
- **Click**: Filter data
- **Zoom**: Pan and zoom on charts
- **Download**: Save charts as images

### **Search & Filter**
- Type in search box to filter instruments
- Searches instrument code and name
- Real-time filtering

### **Responsive Design**
- Works on desktop and tablet
- Clean, modern UI
- Professional color scheme

---

## 🐛 Troubleshooting

### **Dashboard won't start**
```bash
# Check if streamlit is installed
pip list | grep streamlit

# Reinstall if needed
pip install streamlit==1.29.0
```

### **Charts not showing**
```bash
# Install plotly
pip install plotly==5.18.0
```

### **File upload fails**
- Check file is .xlsx or .xls format
- Ensure file is from Axis MF (correct structure)
- File should have multiple scheme sheets

### **"Module not found" error**
```bash
# Install all requirements
pip install -r requirements_streamlit.txt
```

### **Port already in use**
```bash
# Use different port
streamlit run streamlit_app.py --server.port 8502
```

---

## 💡 Tips & Tricks

### **Tip 1: Share the Dashboard**

Generate a shareable link:
```bash
streamlit run streamlit_app.py --server.enableCORS=false
```

Then share your local IP:
```
http://192.168.1.X:8501
```

### **Tip 2: Deploy Online**

Deploy to Streamlit Cloud (free):
1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect your repo
4. Deploy!

### **Tip 3: Customize Colors**

Edit the CSS in `streamlit_app.py` (lines 31-70) to match your brand.

### **Tip 4: Add More Charts**

The code is modular - easy to add new visualizations:
```python
# Add after line 350
st.markdown("### Your New Chart")
fig = px.scatter(df, x='quantity', y='market_fair_value_(rs._in_lakhs)')
st.plotly_chart(fig, use_container_width=True)
```

---

## 📁 File Structure

```
Interactive Dashboard/
├── streamlit_app.py              ← Main dashboard code
├── requirements_streamlit.txt    ← Dependencies
└── STREAMLIT_GUIDE.md           ← This file
```

---

## 🎯 For Your Interview

### **Demo the Dashboard**

1. **Share your screen**
2. **Run**: `streamlit run streamlit_app.py`
3. **Upload** the Excel file
4. **Show** the analytics

### **Talking Points**

> "I built an interactive Streamlit dashboard because:
> 
> 1. **User Experience** - Analysts prefer visual interfaces over scripts
> 2. **Stakeholder Demos** - Easy to show results to non-technical users
> 3. **Modern Stack** - Streamlit is standard for data apps in 2025
> 4. **Production Ready** - Can be deployed to Streamlit Cloud instantly
> 
> The dashboard includes:
> - File upload with validation
> - Real-time processing
> - Interactive Plotly charts
> - Export to CSV/Excel
> - Search and filter capabilities"

---

## 🏆 Why This Stands Out

### **Most candidates submit:**
- ❌ Just a Python script
- ❌ No visualization
- ❌ Command-line only

### **You're submitting:**
- ✅ Python script (core functionality)
- ✅ Interactive web dashboard (UX)
- ✅ Visual analytics (charts)
- ✅ Professional UI (polished)

---

## 📊 Dashboard Metrics

- **Loading time**: ~2 seconds
- **Processing time**: ~10 seconds for 84 schemes
- **File size**: 15 KB (Python code)
- **Dependencies**: 4 packages

---

## 🚀 Advanced: Deploy to Cloud

### **Option 1: Streamlit Cloud (Free)**

```bash
# 1. Push to GitHub
git add streamlit_app.py requirements_streamlit.txt
git commit -m "Add Streamlit dashboard"
git push

# 2. Visit streamlit.io/cloud
# 3. Click "New app"
# 4. Select your repo
# 5. Deploy!
```

Your app will be live at:
```
https://your-app-name.streamlit.app
```

### **Option 2: Heroku**

```bash
# Create Procfile
echo "web: streamlit run streamlit_app.py" > Procfile

# Deploy
heroku create
git push heroku main
```

---

## ✅ Pre-Demo Checklist

Before showing to anyone:

- [ ] Dashboard runs without errors
- [ ] All charts display correctly
- [ ] File upload works
- [ ] Download buttons work
- [ ] Search/filter works
- [ ] Colors look professional
- [ ] No console errors

---

## 🎬 Ready to Impress!

Your dashboard is **production-ready** and **demo-ready**!

**To run:**
```bash
streamlit run streamlit_app.py
```

**Then:**
1. Upload Excel file
2. Click Process
3. Explore analytics
4. Download CSV

**Enjoy! 🎉**
