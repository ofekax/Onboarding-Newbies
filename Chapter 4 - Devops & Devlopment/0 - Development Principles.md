# Software Development Foundations & Python Basics

Before building data pipelines or services, it is important to understand the
core principles of modern software development.

This module introduces the development practices, conventions, and tools that
are commonly used in professional engineering environments.

The goal is not only to learn *what the tools are*, but also *why they exist*
and how they help create maintainable, scalable, and collaborative systems.

---

### ⏳ Timeline
Estimated Duration: 2 Days

Day 1 – Software Development Foundations  
- Development principles and clean architecture
- Development workflows and collaboration
- Testing approaches and design paradigms

Day 2 – Python and API Foundations  
- Python ecosystem and development patterns
- REST APIs and Python frameworks
- Testing, mocking, and service design

---

### 📚 Resources
Use the resources below and practice researching additional information online.

- [Clean Python - Sunil Kapil](https://edu.anarcho-copy.org/Programming%20Languages/Python/Clean%20Python.pdf)
- [SOLID Principles Overview](https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
- [Python Official Documentation](https://docs.python.org/3/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/)

---

# Software Development Principles

### ❓ Guide Questions

1. What are **Clean Code principles**, and why are they important in software development?  
   Explain ideas such as readability, maintainability, and the principle of  
   **“Leave the codebase cleaner than you found it.”**
   חשוב לכתוב קיום קוד נקי על מנת שהקוד יהיה מובן וקריא, יהיה פשוט לתחזק אותו וכדי שהוא יהיה פתוח להרחבות ושינויים.
2. What are the **SOLID principles**?  
   Describe each principle and explain how they help create maintainable
   object-oriented systems.
עקרונות סוליד הינם 5 עקורנות בסיסים המנחים עבור קיום קוד נקי.
 מטרתם הינה לשפר את איכות הקוד ותחזוקתו עבור המפתחים.
העקרונות הם:
Single Responsibility Principle (SRP)-
עקרון זה מדבר על כך שלכל רכיב בקוד (מחלקה, פונקציה וכו) צריך להיות בעל אחריות אחת.
כאשר זה מתקיים הקוד הופך למופשט וברור יותר להבנה.
מורכבות הקוד נפחתת וזה מקל על התחזוקה שלו.
Open/Closed Principle (OCP)-
העקרון אומר שעל הקוד להיות פתוח להרחבות אך סגור לשינויים, כלומר על הקוד הקיים יש לאפשר הרחבות אך ללא ביצוע שינויים בו.
עקרון זה מאפשר להרחיב את פונקציונליות הקוד מבלי להפריע לאופן התפקוד של הקוד שכבר קיים ולפגוע ביציבות המערכת.
Liskov Substitution Principle (LSP)-
עקרון זה אומר זתתי מחלקות צריכות להיות תואמות וקשורות למחלקות האב שלהן.
כלומר, על תתי המחלקות לתמוך בכלל הפונקציונליות והתכונות של מחלקות האב שלהן.
Interface Segregation Principle (ISP)-
עקרון זה אומר שמחלקות לא צריכות להיות תלויות בממשקים שהן לא עושות בהם שימוש.
לפי עקרון זה כל מחלקה צריכה ליישם  רק את הממשקים שהינם הכרחיים עבורה על שהתלות והמורכסות בקוד תופחת.
Dependency Inverted Principle (DIP)-
עקרון זה אומר שיש לעשות שימוש בממשקים ובמחלקות אבסטרקטיות על מנת שהקוד יהיה יותר מופשט,גמיש וקל לתחזוקה.

3. Explain the **KISS principle** and its importance in software design.
Why does simple and intuitive software scale well?  
   Why do overly complex systems tend to fail over time?
עיקרון הקיס אומר שיש לעשות שימוש בדרך פשוטה ככל שאפשר במהלך ביצוע הפיתוח בשביל להשיג את הפונקציונליות או התוצאות הרצויות.
עקרון זה חשוב מכיוון שהוא תומך בכתיבת קוד מופשט וזה בין היתר גם מקל על הקריאות, הישום, התחזוקה, והמימוש של הקוד.
מערכות מורכבות נוטות יותר להיכשל מכיוון שהמורכבות שלהם יוצרת לעיתים יותר קרובות בלבול ושגיאות במהלך תהליך הפיתוח.
עקרון זה תומך בהתרחבויות מכיוון שהוא מעודד מפתחים להימנע ממורכבויות לא הכרחיות בקוד על מנת שהקוד יהיה כמה שיותר נקי.
הכללים המנחים למימוש העיקרון הם:
1-על כל רכיב בקוד לפתור בעיה אחת בכל פעם, יש לפשט את הקוד ככל שניתן וכתוב תוכניות קטנות.
2-יש למחוק קוד שאין בו שימוש
3-יש לייחס חשיבות לקריאות הקוד
4-יש להימנע מביצוע כפילויות קוד
5-יש לחלק את המערכת למודולים כאשר כל אחד מהם יוכל לתפקד באופן עצמאי.
4. What are the most common **paradigms / programming** (ex. Object Orianted) styles, what are the differences and when should each be used
Event-Driven- גישה שלפיה התקשורת בין רכיבי המערכת מתבצעת על בסיס אירועים שמתרחשים
 Object oriented programming- גישה שלפיה המפתח עושה שימוש במחלקות ובאובייקטיםעב
עבור על אובייקט בגישה זו יש להגדיר את תכונותיו ואת הפונקציונליות שלו.
לOOP יש 3 עקרונות מנחים והם כימוס (היכולת לכמס את המשתנים והפעולות תחת מחלקה אחת), הורשה (היכולת של המחלקות לרשת תכונות ופעולות ממחלקת האב) ופולימורפיזם (היכולת של אובייקטים מסוגים שונים לבצע את אותה הפעולה מ"משקפיים" אחרות) .
Test Driven-
גישה שלפיה על המפתח לכתוב קודם טסטים לקוד לפני שהוא נכתב.
תכנות פונקציונלי- זוהי גישה שלפיה יש לעשות שימוש בפונקציות מטמטיות.

5. What is **Test Driven Development (TDD)**?  
   Explain the development cycle and how it improves code reliability.

---

# Development Workflows & Architecture Concepts

### ❓ Guide Questions

1. Explain the difference between a **Pull Request (PR)**, **Code Review (CR)**,
   and **Design Review (DR)**.  
   Why are these processes important in team development?

2. Define the role of a **Pull Request (PR) / Merge Request**.
What is **squshing**? Why is it common practice to squash commits before the final merge?
Find how can you **apply specific fixes** from one branch to another without merging the entire history?
What is the process for **safely undoing** a merged PR using git revert?

3. Explain the difference between **CLI (Command Line Interface)** and
   **UI (User Interface)** applications.  
   What are the benefits of each?

4. What is the difference between a **compiler** and an **interpreter**?  
   Provide examples of languages that use each approach.

5. What is **event-driven programming**?  
   Explain how it differs from procedural execution and where it is commonly used.

---

# Python & API Foundations

### ❓ Guide Questions

1. What is **Python**, and what are its main characteristics compared to other
   programming languages (for example c#)?  
   Discuss readability, ecosystem, and runtime behavior.

2. What is a **REST API**?  
   Explain the core concepts such as resources, HTTP methods, and stateless communication.

3. **What is the Global Interpreter Lock (GIL) in Python?**  
   Explain:
   - What the GIL is and why it exists  
   - How it affects multi-threading and CPU-bound vs I/O-bound tasks  
   - Differences (if any) in how the GIL behaves across Python versions  
   - What Python 3.14 introduces regarding optionally disabling the GIL and why this is significant  
   - Common strategies to work around its limitations (e.g., multiprocessing)

   **Bonus:** Compare **FastAPI** and **Flask**.
   What are the architectural differences and when would you use each framework?

4. What are e2e testings? What are **tests** in software development, and why are they important?  
   Explain unit tests, integration tests, and the role of automated testing.

5. What are **mocks**, and why are they used in testing?  
   Compare **pytest** with other Python testing frameworks and explain its advantages.

---

### 🔄 Alternatives
Assignment: Research and briefly compare **two development approaches or tools** mentioned above.

Examples:
- FastAPI vs Flask
- Interpreted languages vs compiled languages

Deliverable:
- A short written comparison (1–2 sentences).
- Include a **real-life use case** for each alternative.

Goal:
Be able to explain **why a specific tool or development approach would be chosen in a real system.**

---

### 🎯 User Story & Scenario
Assignment: Based on your research, describe a small example of a **Python service or tool**.

Deliverable:
Two short paragraphs describing:

- A realistic scenario where a Python service is required.
- How testing (pytest), mocking, and clean code practices would be applied.

