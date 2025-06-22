# Affidavit Generator UI (Tkinter)

A lightweight desktop tool to generate affidavit documents from WhatsApp-style client messages.

---

## 🖥 Features

- Paste unstructured client input
- Auto-extracts name, ID, address, etc.
- Fills official `.docx` template
- Allows editing before finalizing
- One-click Windows print support

---

## 📂 Folder Structure

```
affidavit-generator/
├── main.py                  # UI App
├── affidavit_logic.py       # Message parsing & doc generation
├── requirements.txt         # Dependencies
├── Affidavit_Template.docx  # Template with placeholders
└── README.md
```

---

## 🚀 How to Run

### 🧰 Install dependencies:
```bash
pip install -r requirements.txt
```

### ▶️ Run the app:
```bash
python main.py
```

---

## 📋 Input Format
Paste messages like this:
```
Name : Kaviyarasan K
Father's name : Kathiravan K
Age : 24
Gender: Male
Current address : 2nd Floor, Eldams Road, Chennai
Pancard or aadhar card or voter I'd number : QJCPS7034B PAN
Permanent address : D/O Selvam, Ranipettai, Tamil Nadu
Mobile Number: 8056623502
```

---

## 📄 Template Placeholders
Use double curly braces in your `.docx` template:
- `{{NAME}}`
- `{{RELATION_PREFIX}}`
- `{{RELATION_NAME}}`
- `{{AGE}}`
- `{{CURRENT_ADDRESS}}`
- `{{ID_PROOF}}`
- `{{PERMANENT_ADDRESS}}`
- `{{DATE}}`

---

## 🖨️ Windows Printing
The app uses `win32api.ShellExecute()` to trigger one-click print. Available only on Windows.

---

## ✅ To Do
- [ ] Add multi-client batch support
- [ ] PDF generation
- [ ] Streamlit or Flask Web UI (Phase 2)
