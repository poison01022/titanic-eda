# 🚢 Titanic Dataset - Exploratory Data Analysis (EDA)

This project performs Exploratory Data Analysis (EDA) on the Titanic dataset to uncover meaningful insights using statistics and visualizations.

---

## 📁 Project Structure

```arduino
Titanic_2/
├── app.py
├── titanic.csv
├── README.md
```

---

## 📊 Objective

Understand the Titanic dataset through:

- Summary statistics
- Distribution visualizations
- Correlation analysis
- Feature-level insights

---

## 🧰 Tools & Libraries

- Python
- Pandas
- Seaborn
- Matplotlib
- (Optional) Plotly

Install requirements using:

```bash
pip install pandas matplotlib seaborn plotly
```

## 📥 Dataset

You can download the Titanic dataset from the following link:

[Click here to download dataset](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)

---

## 🧪 Key EDA Tasks Performed

1. **Load & Inspect Data**
2. **Summary Statistics**
   - `.describe()`, `.info()`, `.isnull().sum()`
3. **Missing Values Analysis**
4. **Visualizations**
   - Histograms  
   - Boxplots  
   - KDE plots  
   - Countplots  
5. **Correlation Matrix**
   - Heatmap using `df.corr()`
6. **Feature Relationships**
   - Pairplots  
   - Survival analysis by age, sex, class

---

## 📈 Sample Visualizations

- Survival count by gender  
- Correlation matrix  

> _Ensure you save these plots using `plt.savefig()` inside your script if you want them in `outputs/`._

---

## 📸 Sample Visualizations

<p align="center">
  <img src="https://github.com/user-attachments/assets/0001ffaa-676c-4219-a813-9c02cf220406" width="45%" />
  <img src="https://github.com/user-attachments/assets/b4973e24-8da5-4673-bc8a-ce9acfc88160" width="45%" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/647e49e6-4649-47f1-a5bd-3a0b4c39293e" width="45%" />
  <img src="https://github.com/user-attachments/assets/d2c5933e-3403-416c-99fc-4a30253806ec" width="45%" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/acaa7eeb-4214-4fa9-a963-66fbc9a6fc14" width="45%" />
  <img src="https://github.com/user-attachments/assets/e6df757e-763f-4226-b490-1e88c09a46be" width="45%" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/53cd30ce-3817-45b9-9320-077f819e979b" width="45%" />
</p>


## ✏️ How to Run

```bash
python app.py
```

### 💡 Make sure titanic.csv is in the same directory as app.py, or update the path in your script accordingly.

### 🧠 Insights Example

👩‍🦱 Female passengers had a significantly higher survival rate.

🎩 First-class passengers were more likely to survive.

👶 Younger passengers had better chances compared to older ones.

### 👨‍💻 Author
### Adarsh Prasad
