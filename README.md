# 🌊 Student Tracker (v1.0.0)
**Project by: Japan (AI Engineering Student, PSU)**

Student Tracker คือเว็บแอปพลิเคชันสำหรับนักศึกษาที่ช่วยในการจัดการตารางเรียน ติดตามงาน (Task Tracking) และบันทึกไอเดีย โดยเน้นความเรียบง่ายและใช้งานได้จริง

---

## ✨ Features (คุณสมบัติเด่น)
- **Quick Notes:** ระบบบันทึกข้อความด่วน แบ่งสีตามหมวดหมู่ (Project, Exam, English, Personal)
- **Study Dashboard:** หน้าภาพรวมสำหรับติดตามสถานะการเรียน
- **Responsive Design:** รองรับการใช้งานทั้งบนคอมพิวเตอร์และมือถือ
- **Secure Logout:** ระบบออกจากระบบที่ปลอดภัยพร้อมหน้าแจ้งเตือนการ Logout

---

## 🛠 Tech Stack (เครื่องมือที่ใช้)
- **Backend:** Python (Flask Framework)
- **Frontend:** HTML5, CSS3 (Modern UI), FontAwesome Icons
- **Logic:** Session Management for Authentication

---

## 📂 โครงสร้างโฟลเดอร์ (Project Structure)
WEB/
├── static/
│   └── style.css
├── templates/
│   ├── about.html
│   ├── add_subject.html
│   ├── add.html
│   ├── assignment.html
│   ├── base.html
│   ├── calender.html
│   ├── dashboard.html
│   ├── delete_task.html
│   ├── edit_assignment.html
│   ├── forgot_password.html
│   ├── grades.html
│   ├── index.html
│   ├── login.html
│   ├── logout.html
│   ├── notes.html
│   ├── pomodoro.html
│   ├── profile.html
│   ├── register.html
│   └── subjects.html
├── app.py
└── README.md         

## 🚀 How to Run (วิธีการรันโปรเจกต์)

### 1. เตรียมความพร้อม (Prerequisites)
ตรวจสอบว่าคุณมี Python ติดตั้งอยู่ในเครื่องแล้ว:
```bash
python --version

### 2. ติดตั้ง library ที่จำเป็น
pip install flask

### 3.เริ่มต้นใช้งาน
python app.py
