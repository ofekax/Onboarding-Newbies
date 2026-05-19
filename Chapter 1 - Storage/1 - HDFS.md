# Hadoop Distributed File System (HDFS) :elephant:

## Overview
This session focuses on the core concepts of HDFS, the distributed storage layer of the Hadoop ecosystem. Understanding its architecture will help you appreciate how big data clusters store and manage massive datasets across many machines.

**Study the key components, design decisions, and how they work together to provide fault-tolerant, scalable storage.**

## Goals
- Learn the architecture and roles of HDFS components (NameNode, DataNode, etc.).
- Understand how HDFS handles storage, replication, and availability.
- Practice planning a self-study day and managing your time.

:warning: **Note:**
- This is a self-study day; independence and time management matter.
- Focus on grasping the full picture of each concept; if you can’t explain it, you haven’t learned it.
- When in doubt, consult your mentor about what to study.

### ⏳ Timeline
Estimated Duration: 3 Days
- Day 1-3: Learn the concepts of HDFS; spent time on what is it? on fault tolernce, on failover process and on how reads and writes are being done?
    - Have a Q&A session at the third day and in between sessions each day

## Core Concepts

Consider the following five questions to cover the major HDFS topics:

1. **Architecture & Roles:**  Describe HDFS’s overall architecture, including NameNode(s), DataNodes, blocks, and how the namespace and metadata are managed. Don’t forget the role of ZooKeeper in coordinating HA and keeping track of leases.
   בלוקס- בHDFS הקבצים מחולקים לבלוקים אשר מכילים את נתוני הקבצים ומאוחסנים כיחידות אצמעיות, באופן דיפולטי גודל כל בלוק הוא 128 MB בHDFS.
   הNamenoodes : נוד שמנהל את הnamespace של מערכת הקבצים ואחראי לשמור על המבנה ההירכי של מערכת הקבצים ועל המטא דאטה של כל הקבצים\התיקיות שנמצאים במערכת הקבצים.
   הnamenoode יודע עבור כל קובץ באיזה datanoodes הבלוקים שלו מאוחסנים.
   הDatanoodes : הנודים שבהם בסופו של דבר דבר התונים מאוחסנים. הנודים הללו מאחסנים ומחזירים בלוקים בהתאם להוראת הnamennode.
   כל datanoode מדווח לאחר כל פרק זמן מסוים לnamenood רשימv של הבלוקים שמאוכסנים אצלו כדי שהוא יהיה עקבי ומעודכן כמה שיותר.
   בHADDOP HA קלסטר 2 מכונות שונות או יותר מוגדרות כnamenoodes ובכל רגע רק namenoode אחר יהיה פעיל, והשאר יהיו במצב stand by ויספקו גיבוי באופן מהיר כאשר הnamenood הפעיל יקרוס.
   כאשר מתבצע שינוי מסוים בnamespace על ידי הnamenoode הפעיל, יתווסיף תיעוד על השינוי שבוצע בקובץ edit log (קובץ שבו מתועדים השינויים שבוצעו) אשר מאוסחן בספריה המאוחסנת במקור אחסון משותף לכל הnamenoodes.
   הstand by נודס עוקבים כל הזמן אחר הספרייה המשותפת וכאשר הם מבחינים בתיעוד לשינוי שבוצע הם מיישמים אותו בnamespace שלהם.
   הHDFS HA קלסטר עושה שימוש בזוקיפר עבור בחירת הnamenood הפעיל ועבור סנכרון הנתונים.

   
2. **Storage & Fault Tolerance:**  Explain how HDFS divides files into blocks, uses replication (default factor three), and how it detects and recovers from node failures.
   כל קובץ בHDFS מחולק לבלוקים בגודל מסוים (באופן דיפולטי גודל כל בלוק הינו 128MB ) ולאחר מכן הבלוקים הללו מאוחסנים בדאטה נודס שונים.
   עבור כל קובץ בHDFS כאשר הנתונים שבו מחולקים לבלוקים, הרפליקישן פאקטור יוצר באופן אוטומתי העתקים של הבלוקים שמרכיבים את הקובץ.
   באופן דיפולטי נוצרים 3 העתקים (המשתמש יכול לשנות זאת) וכל העתק יאוחסן בדאטה נוד אחר.
   שכפול הבלוקים של הקבצים למעשה תורם רבות לשרידות המידע של שלהם.
   כאשר מכונה מסוימת קורסת, יהיה עדיין ניתן לגשת לנתוני הקובץ.
   מכיוון יהיה אפשר לגשת לבלוקים של אותו הקובץ אשר שוכפלו למכונה אחרת.
   בנוסף הוספת הרפליקות מסייעת עבור שיפועי ביצועי הקריאה בקלסטר (מכיוון שיש יותר datanoodes, ולכן ביזור בקשות הקריאה גדל).
   
   
   
4. **Topology Awareness & Performance:**  What is rack awareness and why does HDFS replicate across racks? Discuss how block placement, snapshots, and checksums contribute to performance and data integrity.
   בקלסטר של HDFS כפי שאמרתי הנתונים מחולקים לבלוקים אשר מאוחסנים על גבי מכונות שונות אשר נקראות DATANODES, הדאטה נודס הינם מקובצים לקבוצות של racks (כל ראק למעשה מכיל בתוכו קבוצה של דאטה נודס).
   הדופ עושה שימוש בRack Awareness כדי לאפשר לnamenood לדעת באיזה rack כל datanoode מאוחסן.
    דבר המסייע לnamenoode להחליט באיזה racks לאחסן את הנתונים ואת העותקים שלהם.
באמצעות אחסון הנתונים והעתקים שלהם על גבי הrocks גם כאשר מתרחש כשל בrock, יהיה עדיין ניתן לגשת לאותם הנתונים שהוא הכיל דרך ההעתקים שנשמרו בrocks האחרים.
הHADDOP פועל לפי כללים מסוימים עבור אחסון הבלוקים והעתקים שלהם על גבי הrocks, הכללים הללו למעשה מבטיחים שלא יהיה מצב שבו יהיה אובדן למידע.
הכללים הם:
1- לא יותר מעותק אחד של בלוק יאוחסן תחת אותו הdatanoode.
2- לא יותר מ2 עותקים של אותו הבלוק יאוחסנו תחת אותו הrack.

הsnapshots:
הsnapshots ניתנים לקריאה בלבד.
כל סנאפשוט הוא למעשה העתק של מערכת הקבצים\ניתוב מסוים בה בנקודת זמן מסוימת.
קבצי הסנאפשוטס למעשה מתעדים את רשימת הבלוקים שמרכיבים את הקובץ ואת גודלו.
השימוש בסנאפשוט נעשה בין היתר גם עבור ביצוע גיבוי על נתונים.

הchecksum:
יתכן מצב שבו בלוק נתונים מגיע פגום עקב תקלות רשת, שגיאות IO וכו...
כדי לטפל בכך, כאשר לקוח יוצר קובץ בHDFS, הHDFS מפעיל אלגוריתם checksum עבור כל אחד מהבלוקים שמרכיבים את הקובץ ואת התוצאה המתקבלת עבור כל בלוק הוא שומר בתוך קובץ מוסתר בnamespace של אותה מערכת הקבצים.
כשאר לקוח רוצה לגשת לקובץ קיים במHDFS, עבור כל datanoode שבו מאוחסן בלוק נתונים שחלק מה-קובץ הרצוי מופעל האלגוריתם checksum ומתבצע אימות בין התוצאה המתקבלת לבין התוצאה הצפויה כדי להבטיח שהבלוק אינו פגום.
אם האימות לא הוצלח הלקוח יכול לאחזר את הבלוק הפגום מdatanoode אחר אשר מהווה העתק לאותו הבלוק הפגום.

4. **High Availability :**  Outline HDFS High Availability (Active/Standby NameNode, JournalNodes). How do these features improve scalability and uptime?
    בHADDOP HA קלסטר 2 מכונות שונות או יותר מוגדרות כnamenoodes ובכל רגע רק namenoode אחר יהיה פעיל, והשאר יהיו במצב stand by ויספקו גיבוי באופן מהיר כאשר הnamenood הפעיל יקרוס.
   כאשר מתבצע שינוי מסוים בnamespace על ידי הnamenoode הפעיל, יתווסיף תיעוד על השינוי שבוצע בקובץ edit log (קובץ שבו מתועדים השינויים שבוצעו) אשר מאוסחן בספריה המאוחסנת במקור אחסון משותף לכל הnamenoodes.
   הstand by נודס עוקבים כל הזמן אחר הספרייה המשותפת וכאשר הם מבחינים בתיעוד לשינוי שבוצע הם מיישמים אותו בnamespace שלהם כדי להיות מסונכרים עם הnamespace של הacitive namenood.
   אמצעי האחסון המשותף לnamenoodes יכול להיות NFS או QJM , מומלץ יותר לעשות שימוש בQJM מכיוון שהוא מאפשר לשתף edit logs בין כל הnamenoodes (הstand by והactive).
   כדי שהstand by namenoods ישארו מסונכרנים עם הנוד הפעיל, הנודים "המשניים" מסתכרנים באמצעות הJournalNodes.
   כאשר הactuve namenood מבצע שינוי מסויים בnamespace שלו, הactive namennod רושם תיעוד לשינוי שנעשה באמצעות קובץ הedit log בJournalNodes.
   
   


6. **Protocol & Operations:**  Describe how clients read and write data to HDFS via RPC, how they locate NameNodes and DataNodes, how DataNodes send block reports, and why these mechanisms matter for everyday operations. Cover the runtime behaviour of leases and pipeline formation.

### 🔄 Alternatives
Assignment: You are required to research and write a comparative analysis between HDFS and an industry alternative.
- Deliverable: A written summary (minimum 1 or 2 sentences).
- Focus: Compare performance, architecture, and specific "pain points" this tool solves compared to legacy systems or competitors.
- Goal: You must be able to justify why the department uses this tool for our specific environment.

### 🎯 User Story & Scenario
Assignment: Based on your research and understanding of the department's pipeline, define a concrete Use Case for this technology.
- Deliverable: A written summary example/story (two paragraphs approx.).
- Requirement: Describe a real-world scenario (e.g., a specific client requirement) where this technology is the optimal solution.
- Data Flow: Map out the data flow and explain how this tool integrates with other components in the Data Pipeline.


## Wrapping Up :trophy:
Review your answers with your mentor and discuss any unclear points. Relate these concepts back to real-world usage scenarios you might encounter.

## Action Items
- Note topics you want to investigate further.
- Prepare questions for the mentor Q&A session.
- Continue the Day 01 challenge by linking these HDFS concepts to other chapters.

## Recommended Resources
- [Official HDFS User Guide](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html)
- [Hadoop: The Definitive Guide (O'Reilly)](https://piazza-resources.s3.amazonaws.com/ist3pwd6k8p5t/iu5gqbsh8re6mj/OReilly.Hadoop.The.Definitive.Guide.4th.Edition.2015.pdf)
