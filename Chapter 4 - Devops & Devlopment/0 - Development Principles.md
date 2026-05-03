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
   חשוב לכתוב קיום קוד נקי על מנת שהקוד יהיה מובן וקריא, וכדי שיהיה פשוט יותר לתחזק אותו.
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
קוד שמראה דוגמא למימוש:
class Circle {
    constructor(radius) {
        this.radius = radius;
    }
 
    area() {
        return Math.PI * this.radius * this.radius;
    }
}
 
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
 
    area() {
        return this.width * this.height;
    }
}
 
class AreaCalculator {
    calculate(shape) {
        return shape.area();
    }
}
בקוד למעלה נעשה שימוש בעיקרון הפולימורפיזם על מנת לאפשר את הרחבת הקוד הקיים מבלי לשנות אותו.

Liskov Substitution Principle (LSP)-
עקרון זה אומר זתתי מחלקות צריכות להיות תואמות וקשורות למחלקות האב שלהן.
כלומר, על תתי המחלקות לתמוך בכלל הפונקציונליות והתכונות של מחלקות האב שלהן.
דוגמא למימוש:
class Shape {
    getArea() {
        throw new Error("This method should be overridden!");
    }
}
 
class Rectangle extends Shape {
    constructor(width, height) {
        super();
        this.width = width;
        this.height = height;
    }
 
    getArea() {
        return this.width * this.height;
    }
}
 
class Square extends Shape {
    constructor(side) {
        super();
        this.side = side;
    }
 
    getArea() {
        return this.side * this.side;
    }
}
בקוד הזה כל מחלקת בן של המחלקה שאפ מיישמת את הפונקצייה getArea בצורה שמתאימה לה
Interface Segregation Principle (ISP)-
עקרון זה אומר שצריך להימנע ממקרים בהם מחלקות מכריחות את המשתמשים שלהם ליישם פונקציות  שהם לא זקוקים להן, במקום זאת צריך לפצל את הממשקים הגדולים לממשקים קטנים וממוקדים יותר.
דוגמא:
class Worker {
    work() {}
    eat() {}
    sleep() {}
}
הממשק הזה סותר את עיקרון מזה מכיוון שהממשקג הינו מכיל יותר מידי פונקציות, יש לפרק אותו ל3 ממשקים כאשר כל ממשק יכיל בתוכו פונקצייה אחת על מנת שהמשתמשים יכלו ליישם רק את הממשקים המכילים את הפונקציה שרלוונטית להם.
Dependency Inverted Principle (DIP)-
עקרון זה אומר שיש לתעדף שימוש בממשקים ובמחלקות אבסטרקטיות מאשר שימוש במחלקות רגילות על מנת שהקוד יהיה יותר מופשט.
דוגמה:
class Database {
    connect() {}
}
 
class UserRepository {
    constructor() {
        this.database = new Database();
    }
}
מחלקת היוזר ריפוסיטורי תלויה במחלקת הדאטה בס בקוד, לפי עקרון זה יש לעשות שימוש בממשקים כדי להפריד את התלותיות לפי הקוד הבא:
class IDatabase {
    connect() {}
}
 
class Database extends IDatabase {
    connect() {}
}
 
class UserRepository {
    constructor(database) {
        this.database = database;
    }
}




4. Explain the **KISS principle** and its importance in software design.
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
5. What are the most common **paradigms / programming** (ex. Object Orianted) styles, what are the differences and when should each be used
   מה זה פרדיגמות תכנות?
   פרדיגמות תכנות הם גישות שונות לפיתוח תוכנה, לכל גישה יש את המוסכמות והעקרונות המנחים שלה.

   מה ההבדל בין תכנות פונקציונלי לבין תכנות פרוצדורלי?
בתכנות פרוצדורלי כל משימה מפורקת לרצף של הוראות ופונקציות הנקראות פרוצדורות אשר מתבצעות אחת אחרי השנייה.
בתכנות פרוצדורלי כל משימה 
תכנות פונקציונלי מבוסס על חישוב באמצעות פונקציות מתמטיות ובו כל משימה מופרדת לפונקציה משלה.
הפרדיגמה הזו מתמקדת בפונקציות ותוצואותיהם ולא בהוראות ובסדר שבו הפונקציות מתבצעות בשונה מתכנות פרוצדורלי.
בשונה מתכנות פרוצדורלי בתכנות פונקציונלי הפונקציות צריכות לא להיות תלויות ברכיבים אחרים חיצוניים (כמו פונקציות אחרות).

מה ההבדל בין פונקציה למתודה?
מתודה היא פונקציה ששיכת למחלקה מסוימת.

   
   
Event-Driven-
 ,גישה שלפיה התקשורת בין רכיבי המערכת מתבצעת על בסיס אירועים שמתרחשים, לפי גישה זו על המערכת להגיב בהתאם לאירועים המתרחשים.
 Object oriented programming- גישה שלפיה המפתח עושה שימוש במחלקות ובאובייקטיםעב
עבור על אובייקט בגישה זו יש להגדיר את תכונותיו ואת הפונקציונליות שלו.
לOOP יש 3 עקרונות מנחים והם כימוס (היכולת לכמס את המשתנים והפעולות תחת מחלקה אחת), הורשה (היכולת של המחלקות לרשת תכונות ופעולות ממחלקת האב) ופולימורפיזם (היכולת של אובייקטים מסוגים שונים לבצע את אותה הפעולה מ"משקפיים" אחרות) .
Test Driven-
גישה שלפיה על המפתח לכתוב קודם טסטים לקוד לפני שהוא נכתב.
תכנות פונקציונלי- זוהי גישה שלפיה יש לעשות שימוש בפונקציות מטמטיות.

7. What is **Test Driven Development (TDD)**?  
   Explain the development cycle and how it improves code reliability.
   זוהי גישת תכנות שלפיה על המפתח לכתוב טסטים לקוד לפני שהוא מתחיל לכתוב את הקוד עצמו שהולך לייצור.
   תהליך העבודה עם הגישה הזו מתחיל בכך שהמפתח כותב מבחן בהתאם לפונקציונליות הרצויה אותה רוצים לממש, בהתחלה המבחן זה נכשל מכייון שהקוד עצמו עדיין לא נכתב.
   לאחר מכן המפתחים כותבים את הקוד הכי בסיסי שצריך כדי לממש את הפונקציונליות ולעבור את המבחן.
   לאחר שהקוד עבר את המבחן המפתחים יכולים לשפר אותו תוך שמירה על כך שהקוד ימשיך לעבור את המבחנים בהצלחה.
   לפי גישה זו כל רכיב קוד עוברים בדיקה יסודית על מנת לוודא שהם פועלים בהתאם למצופה וזה מקטין את הסיכוי לבאגים ותקלות במערכת .

   הגישה הזו טובה מכיוון שבה המפתח מבין באופן יותר מובהק וברור את הדרישות שעליהם עליו לענות וגם היא מסייעת לוודא שכלל רכיבי המערכת מתחברים יחדיו באופן תקין בהתאם למצופה.
   עם היתרנות לגישה זו יש חסרון, גישת התכנות הזו הינה מורכבת ולוקחת זמן רב יחסית.
   

---

# Development Workflows & Architecture Concepts

### ❓ Guide Questions

1. Explain the difference between a **Pull Request (PR)**, **Code Review (CR)**,
   and **Design Review (DR)**.  
   Why are these processes important in team development?
תפקיד הפול רקווסט הוא לאפשר למפתחים למזג לשתף את השינויים המתבצעים בבראנצים השונים בריפוסיטורי אחד עם השני.
   זה חשוב בפיתוח קבוצתי בגלל שזה מאפשר למפתחים לשתף את הקוד שהם כותבים זה עם זה.
   הCR זה הביקורת שהמפתחים מביאים זה לזה על הקוד שהם כתבו.
   זה חשוב בפיתוח קבוצתי בגלל שזה מאפשר  להם לשתף דעות אחד של השני לגבי הקוד וזה מסייע להם לקבל החלטות שקולות ומחושבות יותר במהלך הפיתוח.
   הDR זה שמפתח בונה עיצוב לאופן מימוש הקוד שאותו עליו לפתח, ועל העיצוב שהוא בנה מפתח אחר מעביר ביקורת.
   זה חשוב בפיתוח קבוצתי בגלל שזה מאפשר להם לשתף את דעותיהם לגבי העיצוב, מה שמסייע להם לקבל החלטות שקולות יותר במהלך בניית העיצוב.
 ו 

2. Define the role of a **Pull Request (PR) / Merge Request**.
What is **squshing**? Why is it common practice to squash commits before the final merge?
Find how can you **apply specific fixes** from one branch to another without merging the entire history?
What is the process for **safely undoing** a merged PR using git revert?
תפקיד הפול רקווסט הוא לאפשר למפתחים למזג לשתף את השינויים המתבצעים בבראנצים השונים בריפוסיטורי אחד עם השני.
מעיכה בגיט זה אומר לקבץ קומיטים שהתבצעו בענף מסוים לקומיט יחיד.
נפוץ לקבץ את כל הקומיטים בבראנץ מסוים לקומיט אחד ואז לעשות אליו מרג מכיוון שזה גורם להיסטוריית הקומיטים בריפוסיטורי להיות יותר מסודרת וברורה.
באמצעות השימוש בפקודת cherry-pick אפשר לקחת שינויים שהתבצעו בקומיט ספציפי בענף ולהעתיק אותם לענף אחר.
בשביל לבטל שינויים שהתבצעו באופן בטוח באמצעות השימוש בפקודת  git revert יש לבצע את הדברים הבאים:
1-יש לבדוק את הענף שבו  התבצע הבראנץ השגוי.
   ניתן לגשת לענף באמצעות השימוש בפקודה: git checkout.
2- מוודאים שיש את הקוד הכי מעודכן באותו הבראנץ בריפוסיטורי המרוחק גם בריפוסיטורי הלוקאלי באמצעות השימוש בפקודה:git pull.
    3- מסתכלים בהיסטוריית הקומיטים הממזוגים של הבראנץ ומחפשים את המזהה של הקומיט שאותו רוצים לבטל. (הקומיטים הממוזגים דומים לקומיטים הרגילים, ההבדל היחיד הוא שלקומיט ממוזג יש לפחות 2 קומיטים בהתבצעו לפניו)
   רואים את הסיטוריית הקומיטים הממזוגים שבבראנץ באמצעות הרצת הפקודה git log.
   4-לאחר מכן מבטלים את השינויים שהתבצעו בקומיט הממוזג הרצוי באמצעות השימוש בפקודה: git revert עם מזהה הקומיט שאותו רוצים לבטל.
   לאחר מכן יש לדחוף את הקומיט על מנת שכל השינויים שהתבצעו בקומיט הזה יחולו גם בריפוסיטורי המרוחק.   
   


4. Explain the difference between **CLI (Command Line Interface)** and
   **UI (User Interface)** applications.  
   What are the benefits of each?
עם GUI המשתמש מתממשק בצורה ויזואלית ואילו עם CLI המשתמש מתממשק באופן טקסטואלי באמצעות הרצת פקודות.
היתרון של הGUI הוא שלמשתמש יותר נוח ופשוט להתממשק איתו (מכיוון שבו לא נדרש מהמשתמש לדעת פקודות וחוקי תחביר ספציפיים בשונה מCLI).
הCLI מציע למשתמש פונקציונליות גדולה יותר שבה הוא יכול לעשות שימוש וגם הוא מאפשר לו לבצע פעולות באופן יעיל יותר.
הCLI והGUI הם למעשה 2 סוגי UI שונים.

6. What is the difference between a **compiler** and an **interpreter**?  
   Provide examples of languages that use each approach.
בגישת הinterpreter האינטרפרטר ממיר ומריץ את קוד הרמה הגבוהה של המערכת שורה אחר שורה (כל שורה בקוד מומרת לשפת מכונה ואז לאחר מכן מורצת).
בגישת ה-compiler הקומפילר מקמפל (כלומר ממיר אותו לקוד שיהיה קריא עבור המכונה) את כל קוד הרמה הגבוהה של המערכת ורק לאחר מכן מאפשר את הרצתו.
שפות בהם יש שימוש ב-interpreter: פייתון, גאבה סקריפט,  באש, ועוד...
שפות בהם יש שימוש בקומפילר: גאבה, סי  שארפ ועוד..
7. What is **event-driven programming**?  
   Explain how it differs from procedural execution and where it is commonly used.
   אבנט דריבן זוהי פרדיגמת תכנות אשר בה ביצועי המערכת מבוססים על אירועים.
   לפי הפרדיגמה על המערכת להגיב לאירועים שמתקבלים באמצעות פעולות מוגדרות מראש.
   בפרדיגמת  התיכנות הפרוצדורלית, המערכת מחולקת לתתי מערכות, כאשר כל תת מארחת נקראת פרוצדורה.
   השוני בין הפרדיגמות הוא שההאבנט דריבר מבוסס על אבנטים והפרדיגמה השנייה מבוססת על פרוצדורות.
   בנוסף בתכנות פרוצדורלי על המשתמש להמתין לתגובת המערכת לאחר שהוא מבצע פעולה מסוימת ואילו בפרדיגמת אבנט דריבן המערכת תגיב באופן מיידי לפעולתו.
   נפוץ לעשות שימוש בפרדיגמת האבנט דריבן עבור מערכות שבהן יש צורך בתגובה מיידית של המערכת לשינויים ברשת או לפעולות המשתמש.
ר
---

# Python & API Foundations

### ❓ Guide Questions

1. What is **Python**, and what are its main characteristics compared to other
   programming languages (for example c#)?  
   Discuss readability, ecosystem, and runtime behavior.
   פייתון זו שפת תכנות מונחת עצמים ברמה גבוהה אשר בה התחביר יחסית פשוט וקל לקריאה.
   פייתון מבוססת על קוד פתוח וזה מאפשר למפתחים לשתף פעולה זה עם זה במהלך תהליך הפיתוח ולהנגיש את קוד המקור.
   פייתון עושה שימוש באינטרפרטר המכיל בתוכו קומפילר עבור המרת הקוד לשפת מכונה ועבור הרצתו.
   קוד המקור של התוכנית מוכנס לתוך האינטרפטר ולאחר מכן הקומפילר ממיר את קוד המקור לבייט קוד.
   אחר כך הקומפילר מזין את הבייט קוד למכונה הוירטואלית של פייתון ולאחר מכן התוכנית יכולה לרוץ.
   כאשר מריצים את התוכנית הפייתון האינטרפרטר ממיר את קוד המשתמש לקוד המכונה שורה אחר שורה ולאחר מכן שורת הקוד מורצת פקודה אחר פקודה.
   
   

3. What is a **REST API**?  
   Explain the core concepts such as resources, HTTP methods, and stateless communication.
רסט איפיאי הוא סוג של ממשק אי פי אי שבו מוגדרות אוסף של מתודות אשר בהם המפתחים יכולים לעשות שימוש כדי לשלוח בקשות ולקבל תגובות לישויות שונות ברשת על ידי השימוש במתודות הפרוטוקל HTTP.
הראסט אי פי אי מאפשר למפתחים לחשוף למפתחים האחרים את הממשקים שהם כותבים.
בארכיטקטורת רסט אי פי אי יש הפרדה בין הלקוח לשרת, הלקוח שולח בקשת HTTP לשרת והשרת מחזיר ללקוח תשובה בהתאם.
ארבעת סוגי הבקשות HTTP הן: GET - בקשת מידע מהשרת
, (שליחת מידע לשרת) POST
, PUT - בקשה לעדכון המידע בשרת
PEACH- בקשה לביצוע שינוי חלקי של המידע בשרת
DELETE - בקשה למחיקת המידע בשרת.
כל בקשה ברסט אי פי אי הינה עצמאית ולא תלויה בבקשות אחרות.
ברסט אי פי אי יש כתובות URL, כל כתובת כזו מייצגת שרת ברסט אי פי אי.
כאשר הלקוח רוצה לשלוח בקשת HTTP מסוימת לשרת הוא יכול לפנות אליו באמצעות הכתובת הזו.
4. **What is the Global Interpreter Lock (GIL) in Python?**  
   Explain:
   - What the GIL is and why it exists.
   - How it affects multi-threading and CPU-bound vs I/O-bound tasks  
   - Differences (if any) in how the GIL behaves across Python versions  
   - What Python 3.14 introduces regarding optionally disabling the GIL and why this is significant  
   - Common strategies to work around its limitations (e.g., multiprocessing)
בכל תוכנית שיש בה multithreading (שזה אומר שרצים על אותה יחידת העיבוד כמה תתי תהליכים בו זמנית) יש חשיבות לתזמון שבו כל אחד מתתי התהליכים יתבצע.
הגיל הוא למעשה נעילה שמתבצעת אשר מאפשרת רק לטרד אחד לבצע בייטקוד (קוד שאותו האינטרפרטר מבין) באותה נקודת זמן, ולמעשה הוא את פייתון להריץ טרד אחד בכל רגע נתון.
מכיוון שהגיל מונע מכמה טרדים לרוץ במקביל, תוכניות פייתון מרובות טרדים אינן מנוצלות במלאן את יכולתם של מעבדים מרובי ליבות, זה יכול להוות כחיסרון משמעותי עבור מפתחים שרוצים  לעשות שימוש במולטי טרדינג במערכת שלהם במטרה לשפר את ביצועיה.
עבור משימות הקשורות לקלט או פלט ההשפעה של הגיל פחות מורגשת מכיוון שנעילתו משתחררת כאשר הוא ממתין להשלמת פעולת הקלט או הפלט, וזה מאפשר לטרדים אחרים לרוץ עד שהפעולה תתבצע.
   


   **Bonus:** Compare **FastAPI** and **Flask**.
   What are the architectural differences and when would you use each framework?
   פאסט אי פי אי יותר יכול להתמודד עם עומסי עבודה, הוא יכול לטפל בטווח של 15,000-20,000 בקשות לשנייה לאומת פלאסק, שהוא יכול לטפל רק ב2,000-3,000.
   פלאסק קיים הרבה יותר זמן מאשר פאסט אי פי אי, ולכן יש יותר ניסיון פיתוחי איתו ויותר קל ללמוד אותו מאשר פאסט אי פי אי, ניתן למצוא ברשת יותר מידע מפורט ומעמיק עליו.
  בשונה מפלאסק, פאסט איפיאי מציע תמיכה מובנת באימות נתונים על ידי השימוש בספריית pydentic ובביצוע משימות באופן א- סינכורני (כלומר המשימות יכולות להתבצע באופן מקבילי ומונעות עיכוב בריצת המערכת בכך שאין צורך לחכות שמשימה תסתיים על מנת שהמשימה הבאה תרוץ).


5. What are e2e testings? What are **tests** in software development, and why are they important?  
   Explain unit tests, integration tests, and the role of automated testing.
 טסטים בפיתוח תוכנה בודיקים ומאמתים שהמערכת מתפקדת בצורה תקינה ומאובטחת בהתאם לדרישותיה.
 ה-e2e  זוהי בדיקה שמטרתה לבדוק ולאמת את כל מהלך העבודה של המערכת מתחילתה ועד סופה, בדיקות אלו למעשה מוודאות שכל רכיבי המערכת (הדאטה באיסים, הסרוויסים וכו) עובדים ביחד באופן תקין.
ישנם כמה סוגי בדיקות ובינהם:
בדיקת יחידה- בדיקה שמטרתה לבדוק ולאמת את החלקים הבודדים של המערכת, זה יכול להיות אפילו ברמת המתודה הבודדת.
בדיקת אינטגרציה- בדיקה שמטרתה לבדוק את האופן שבו רכיבים שונים במערכת עובדים יחדיו.
בדיקת אוטומציה- בדיקות אוטומציה הם בדיקות אשר מתבצעות על גבי המערכת באופן אוטומטי ומתוכנן ולא באופן ידני.
את הבדיקה הזו עושים על ידי כתיבה של קוד, לאחר סיום הבידקה מתבצעת השוואה של התוצאה שהתקבלה בבדיקה לתוצאה הרצויה.
אם במהלך הבדיקה התגלתה תקלה במערכת או שתשובת הבדיקה הייתה שונה מהצפוי המערכת תתריע על כך.

   
6. What are **mocks**, and why are they used in testing?
   מוק זה אובייקט שנוצר במטרה לחקות את התנהוגותו של אובייקט או רכיב מסוים במערכת.
   עושים שימוש באובייקט המוק  כאשר מתבצעת בדיקת מוק, בשביל לבודד ולאמת פונקציונליות מסוימת של רכיב במערכת ללא תלות בשאר הרכיבים שלה.
   Compare **pytest** with other Python testing frameworks and explain its advantages.
      הפיטאסט הינו יותר פשוט וקל לשימוש בהוושאה לכלי בדיקות אחרים, והוא תומך בביצוע בדיקות יחידה ואפילו בבדיקות מערכת.
   הפיטאסט מספק למשתמש דיווח מפרוט וברור עבור בדיקות שבהם הבדיקה נכשלה
   
   -להשוות pytest לpyunit
   הפיטאסט נחשב לספריה יותר ממוקדת וברור  מאשר הפאיוניט.
   בפאיטסט אין צורך לעשות שימוש במתודות ומחלקות של טסטים על מנת שהם יתבצעו בשונה בפאיוניט, הפאיטסט יודע לגשת לקבצי הטסטים ולפונקציות שלהם באופן אוטומטי.
בפאיטסט יש צורך להוריד את הספריה, ובווניטסט אין צורך להוריד כלום מכיוון שזה מובנה כחלק מפייתון.

   מה זה קובץPYC?
   לאחר שמריצים תוכנית בפייתון בפעם הראשונה או שמייבאים בקוד ספרייה מסוימת הקומפילר שבתוך ההאינטרפטר מקמפל את קוד המקור לבייט קוד ומאחסן את הבייט קוד בקובץ שנקרא PYC .
   
   

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

