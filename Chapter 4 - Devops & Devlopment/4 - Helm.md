# Container Orchestration Foundations: Kubernetes & Helm

Before deploying production-grade services, it is important to understand how container orchestration works.

This module introduces Kubernetes and Helm as the standard tools for managing containerized applications at scale.

The goal is to understand *how systems are deployed, configured, and managed*, and to gain hands-on experience using real-world labs.

---

### ⏳ Timeline  
Estimated Duration: 2 Days  

**Day 1 – Theory & Concepts**  
- Kubernetes core architecture  
- Workloads and networking  
- Helm fundamentals and packaging  

**Day 2 – Hands-On Labs**  
- Kubernetes practical labs  
- Helm chart deployment  
- Debugging and inspection  

---

### 📚 Resources  
Use the resources below as your primary reference:

- [Kubernetes Documentation](https://kubernetes.io/docs/)  
- [Helm Documentation](https://helm.sh/docs/)  
- [OpenShift Documentation](https://docs.openshift.com/)  

---

# Day 1 – Kubernetes & Helm Concepts

### ❓ Guide Questions

1. What is Kubernetes, and what problems does it solve compared to running containers manually on vm?  
קוברנטיס זו מערכת לפריסה, הרחבה ולניהול של קוטיינרים.
 קוברנטיס מקלה יותר על המשתמש בכך שהיא:
- מאפשרת למנהלים לקבץ קונטיינרים יחד למקום אחד ומרוכז, דבר המקל על ניהולם.
- קוברנטיס דוראג לשרידות הקונטיינרים בכך שהוא מרים כמה קונטיינרים וכל קונטיינר הוא מציב בשרת שונה.
- כאשר יש עומסי עבודה קוברנטיס ידאג להריץ עוד עותקים של הקונטיינרים ולאחר שהעומס יפחת הוא יוריד את מספר העותקים בהתאם.
- כאשר קונטיינר קורס קוברנטיס מחליף אותובקונטינר חדש ותקין באופן אוטומטי.
- קוברנטיס מאפשר לקונטיינרים יותר יעילות בניצול משאבי החומרה מאשר ממכונות וירטואליות.

2. Describe the main Kubernetes components and architecture.  
   Include: cluster, nodes, control plane, kubelet, API server, etcd.
   קוברנטיס קלסטר- קלאסטר הוא קבוצה של מכונות הנקראות נודים (קלאסטר מכיל נוד אחד לפחות), המשמשים להרצת הקונטיינרים שמנוהלים על ידי הקוברנטיס.
   קונטרול פלן- הקונטרולר פלן מנהל את הנודים והפודים בכל הקלאסטר בצורה כזו שזמינותו תהיה גבוהה, הוא אחראי לתזמון הרצת הקונטיינרים ולהגדרת מדיניות הקלסטר.
    הקונטרולר פלן מורכב מהרכיבים: Kubernetes API - רכיב שמתווך בין כלל הרכיבים השונים בקלסטר והוא מספק Rest API אשר מאפשר לתקשר עם הקלסטר , המתזמן של קוברנטיס- רכיב שמחפש פודים שלא מקושרים לנודים, ומקצה כל פוד לנוד מתאים בהתאם למדיניות הקלסטר ולכמות משאבים הפנויים, ו הetcd - רכיב שהוא מאגר נתונים מבוזר המבוסס על מפתחות וערכים המאחסן את כל הנתונים והמצב הנוכחי של הקוברנטיס קלסטר.
   נוד- נוד הוא מכונה וירטואלית או פיזית אשר חלק מקלסטר הקוברנטיס, בתוך הנודס הקונטיינרים בפועל רצים.
   כל נוד מורכב מkubelet- רכיב שמוודא שהפודים והקונטיינרים שבתוכם רצים, ומ-Container runtime- רכיב תוכנה שאחראי להפעיל את הקונטיינרים שבתוך הנוד .

3. What are the core Kubernetes resources?  
    Explain Pods, Stateful sets, daemon sets , limit ranges, pv and PVC, namespaces, cronjobs, jobs, roles, rolebindings  Deployments, Services, ConfigMaps, and Secrets, and how they interact.
   -ה Pod : הפוד הוא יחידת הניהול הקטנה ביותר בקוברנטיס והוא אובייקט שמאפשר להריץ קונטיינר אחד או יותר בצורה מנוהלת.
   -ה deployment : אובייקט שמייצג ישות של אפליקציה אשר אחראי להגדיר לקוברנטיס באיזה אופן ליצור ולשנות את הפודים של אותה האפליקציה.
   ה-service :  הסרוויס הוא אובייקט המייצג שירות מסוים אשר מאפשר גישה למספר פודים בקלסטר ומאפשר להם לתקשר זה עם זה (הסרוויס הדיפולטי לא מאפשר לגשת לפודים מחוץ לקלסטר).
במקום לגשת לפוד מסוים בקלאסטר באמצעות כתובת הIP שלו, אפשר לפנות לסרוויס של קוברנטיס והוא ידע להפנות את הבקשה לפוד הרלוונטי.
למעשה השימוש בסרוויס חושף את הפודים בקלסטר בצורה קבועה, מה שמאפשר לקלסטרלתפקד באופן יציב גם כאשר חל שינוי בפודים (מה שקורה מספר רב של פעמים מכיוון שפודים הם רכיבים זמניים אשר עלולים להיווצר ולהימחק פעמים רבות).
   -הStateful sets: אובייקט שעושה שימוש באחסון פרסיסתנתי כדי להבטיח את השמירה על הstate של האפליקציה ושל כל הפודים בה.
   בשונה מdeployment הפודים לא יכולים פשוט להיות מוחלפים באחרים לאחר שהם נופלים, בסטטפול סט לכל פוד יש מזהה יחודי שנשמר בצורה פרסיתנתית והוא משתמש לשמירה על המצב של כלל המערכת, לאחר שפוד בסטטפול סט נופל יחליף אותו פוד בעל מזהה יחודי הזהה לו בשונה מדיפלוימנט.   
   -הnamspaces- רכיב שמאפשר להפריד בין סביבות שונות בתוך הקלסטר, בקוברנטיס עבור כל namespace אפשר לנהל הרשאות ולהקצות משאבים.
   ה- ConfigMaps : אובייקט שמאפשר "להזריק" קונפיגורציה לפוד מבלי לשנות את כל  הimage .
   ה-Secret : זהו configmap שהתוכן של קובץ הקונפיגורציה שלו מקודד בbase64  כדי שהתוכן  יראה הרבה פחות קריא לעין האנושית, נעשה שימוש בסיקרט כאשר נרצה לשמור מידע רגיש.
   ה-PV: אובייקט שמהווה מקור אחסון.
   הPVC: אובייקט שמהווה בקשה של המשתמש לקבל מקור לאחסון (PV), אשר ממופה כווליום לפוד.
   
   
6. How does networking work in Kubernetes?  
   Explain Service types (ClusterIP, NodePort,Ingress,Internal or external network) and basic communication between pods.

7. What is Helm, and why is it used?  
   Explain charts, values.yaml, templating, and how Helm simplifies deployments.

---

# Day 2 – Hands-On Labs (Kubernetes & Helm)

### ⚠️ Important

There are **two versions of this exercise**:

- Internal lab (provided by the team)  
- External lab (public platforms)  

👉 **You must ask your mentor which version you are required to complete before starting.**

---

## 🧪 Lab Tasks (External Option)

### Kubernetes Core Practice

👉 Start here:  
- [KillerCoda Kubernetes Labs](https://killercoda.com/kubernetes)

**You must complete the following scenarios:**

- Kubernetes Basics  
- Kubernetes Pods  
- Kubernetes Deployments  

---

### 🎯 Required Skills (Must Demonstrate)

During the labs, you must perform:

- Deploy an application (nginx or similar)  
- Expose it using a Service  
- **Scale the deployment (replicas up/down)**  
- **Perform a Rolling Update (change image/version)**  
- Inspect logs and running pods  

---

### Helm Hands-On Lab

👉 Helm practice:  
- [KillerCoda Helm Labs](https://killercoda.com/helm)

Tasks:

- Install a Helm chart  
- Modify values.yaml  
- Perform upgrade  
- Uninstall release  

---

## 🔄 Alternatives

Assignment: Compare two Kubernetes deployment approaches:

- Helm Charts vs Raw Kubernetes YAML manifests

Deliverable:
- 1–2 sentences comparison  
- Include a real-world use case for each  

Goal:
Understand the trade-offs between templated/package-based deployments and manual resource definitions.

---

## 🎯 User Story & Scenario

Assignment: Describe a real-world Kubernetes deployment using Helm.

Deliverable (2 paragraphs):

- Describe a service (e.g., API) deployed to Kubernetes  
- Explain how deployment is managed using Helm (chart, values.yaml, releases)  
- Describe how Helm helps manage environments (dev/staging/prod) and simplifies updates (e.g., rolling upgrades)  

---

## 🎯 Deliverable

By the end of this module, you should have:

- Completed the assigned labs (internal or external, per mentor decision)  
- Successfully deployed and exposed an application in Kubernetes  
- Demonstrated scaling and rolling updates  
- Used Helm to install and manage an application  
- Demonstrated ability to inspect and debug workloads 
