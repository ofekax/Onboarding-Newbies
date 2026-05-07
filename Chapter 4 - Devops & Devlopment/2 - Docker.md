# Docker Foundations

Docker is a platform for running applications in isolated environments called containers.

It introduces a standardized way to package and execute software across different environments, without depending on the underlying system configuration.

Instead of installing dependencies directly on a machine, applications are bundled into portable units that can run consistently wherever Docker is available.

---

### ⏳ Timeline
Estimated Duration: 1 Day

Day 1 – Docker Core Concepts  
- Containers vs Virtual Machines  
- Images, Containers, Dockerfile  
- Networking & Storage  
- Security & Isolation  
- Build strategies (Docker, Kaniko, DinD)

---

### 📚 Resources
- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kaniko Documentation](https://github.com/GoogleContainerTools/kaniko)
- [OCI Specification](https://opencontainers.org/)

---

# Docker Core Concepts

### ❓ Guide Questions

1. **What is Docker and what problems does it solve?**  
   Explain what a container is, how it differs from a virtual machine, and why containers are useful in modern systems (portability, consistency, isolation).
דוקר זו פלטפורמה טכנולוגית המאפשרת לארוז מערכות ולהריץ אותן בסביבות מבודדות, ניידות עצמאיות ומרוחקות הנקראות קונטיינרים.
"אריזת" המערכות מתקיימת באמצעות ה- Images, הimages מכילים את כל הרכיבים שהמערכות צריכות בשביל לרוץ (ספריות, קבצי קונפיגורציה, מערכות הפעלה וכו).
הקונטינר הוא למעשה מופע של image, כאשר מריצים את פקודת הדוקר שמריצה image (הפקודה: docker run), הוא יוצר מה- image קונטיינר.
יש כמה נקודות שוני בין קונטיינר לVM וביניהם:
1.לכל מכונה וירטואלית יש מערכת הפעלה משלה ואילו הקונטיינרים חולקים את אותה מערכת ההפעלה.
2.קל לרפלק קונטיינרים על גבי סביבות עבודה שונות ואילו בVM תהליך הריפלוק הינו יותר מורכב.
3. בידוד- הקונטיינרים הינם רצים כל אחד באופן מבודד אך הם חולקים את אותה ליבת מערכת ההפעלה, המכונות הוירטואליות הינם מבודדים באופן מוחלט, לכל מכונה יש את המשאבים ומערכת ההפעלה שלה.
4. עליית המכונה הוירטואלית צורכת הרבה יותר משאבים מכיוון שהיא מריצה מערכת הפעלה שלמה, לאומת זאת הקונטיינר יריץ אך ורק את הרכיבים שאחראים לריצת האפליקציה.
5. הקונטיינרים למעשה רצים על VMים.
   סיבות למה קונטיינרים משומשים עבור מערכות מודרניות:
   1.השימוש בקונטיינרים צורך הרבה פחות משאבים מאשר VMים ובזכות כך גם למעשה הם חוסכים עלויות (כי ככל שיש צורך ביותר משאבים כך גדל הסכום שצריך לשלם עליהם בהתאם).
   2.כל קונטיינר רץ בסופו של דבר בסביבה מבודדת לו כך שהם לא תלוים זה בזה.
   3ץ הקונטיינרים נועדו לא להיות תלויים בפלטפורמה בה הם רצים,כך שכאשר רוצים להעביר את הרצת הקונטינר למקום אחר אין צורך לבצע שינויים בקוד, הם ניתנים להעברה בין מערכות בקלות.
   
   

   
   
   
2. **What are the core Docker components and how do they interact?**  
לקוח:
תפקיד הרכיב הוא לבצע התממשקות עם המשתמש, לאחר שהמשתמש מזין פקודות דוקר הרכיב שולח אותן לדמון (רכיב שעליו אני אסביר בהמשך) והוא מפעיל את הקונטיינר.
דמון:
הוא אחראי על:
   -ניהול הפקודות שהתקבלו מהלקוח ועל פיקוח ביצועם.
   -תקשורת הקונטיינרים עם רכיבים הכרחיים למערכת, ביניהם רכיבים רשתיים תשתיתיים וכו.
   -העברת המשאבים הדרושים לריצת הקונטיינר מהקרנל של מערכת ההפעלה.
   -אינטרקציה עם הרגיסטרי לאחר ביצוע פקודת פוש או פול מצד המשתמש.
רגיסטרי:
   מקום שבו מאחוחסנים אימגים וקונטיינרים שאחרים יצרו או אנחנו יצרנו.
אימגים:
כל אימג מכיל ההוראות לבניית הקונטיינר ואת כל הרכיבים ההכרחיים לריצת האפליקציה .
קונטיינרים:
הקונטיינרים הם סוג של חבילות המכילות קטע קוד מסוים ואת כל הרכיבים ההכרחיים להרצתו בצורה תקינה (ספריות, תלויות, קבצי קונפיגורציה וכו ).
כל קונטיינר הוא מופע של אימג ומנוהל על ידי הדמון.
רשת :
תפקיד הרשת הוא לאפשר לקונטיינרים לתקשר זה עם זה תוך כדי שמירה על בידודם זה מזה.


   


3. **How do networking and storage work in Docker?**  
   Explain:
   - Container networking (bridge, host, ports)  
   - Communication between containers  
   - Volumes vs bind mounts  
   - When to use persistent storage

4. **What are the security and isolation risks in Docker?**  
   Discuss:
   - Namespaces and cgroups (high-level)  
   - Running containers as root vs non-root  
   - Image vulnerabilities and best practices

5. **How are Docker images built in different environments?**  
   Compare:
   - Standard Docker build  
   - Docker-in-Docker (DinD)  
   - Kaniko  
   Explain when each approach is used (e.g., CI/CD pipelines, Kubernetes).

---

### 🔄 Alternatives
Assignment: Compare two virtualization approaches:

- Virtual Machines (VMs) vs Containers

Deliverable:
- 1–2 sentences comparison  
- Include a real-world use case for each

Goal:
Understand the trade-offs between full virtualization and container-based isolation.

---

### 🎯 User Story & Scenario

Assignment: Describe a real-world usage of Docker.

Deliverable (2 paragraphs):

- Describe a service (e.g., API) that is packaged using Docker  
- Explain how it is built (Dockerfile), stored (registry), and deployed  
- Describe briefly how containers help ensure consistency across environments
