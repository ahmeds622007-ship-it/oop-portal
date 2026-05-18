import os
import re

html_template = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بنك الأسئلة الشامل - Mega Bank - موسوعة الـ OOP</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            background-color: #0f172a;
            color: #f8fafc;
        }
        .exam-header {
            text-align: center;
            padding: 3.5rem 1rem;
            background: linear-gradient(135deg, rgba(56, 189, 248, 0.15), rgba(14, 165, 233, 0.1));
            border-bottom: 2px solid rgba(56, 189, 248, 0.3);
            margin-bottom: 2.5rem;
            border-radius: 0 0 24px 24px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        .exam-header h1 {
            color: #38bdf8;
            font-size: 2.8rem;
            margin-bottom: 15px;
            text-shadow: 0 0 15px rgba(56,189,248,0.4);
        }
        .exam-header p {
            color: #cbd5e1;
            font-size: 1.3rem;
        }
        #particles-js {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: 0;
        }
        .container { position: relative; z-index: 1; max-width: 1100px; margin: auto; padding: 0 20px; }
        .header-nav { position: sticky; z-index: 100; top: 0; background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(10px); padding: 15px; border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; justify-content: space-between; align-items: center;}
        
        .topic-title {
            color: #fcd34d;
            border-bottom: 3px solid #f59e0b;
            padding-bottom: 15px;
            margin-top: 5rem;
            font-size: 2.2rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
        }
        .subtopic-title {
            color: #c084fc;
            margin-top: 2.5rem;
            font-size: 1.6rem;
            background: rgba(192, 132, 252, 0.1);
            padding: 10px 15px;
            border-radius: 8px;
            border-right: 4px solid #c084fc;
        }
        
        .code-analysis-section {
            background: #1e293b;
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 1.8rem;
            margin-bottom: 2rem;
            box-shadow: 0 6px 12px rgba(0,0,0,0.4);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .code-analysis-section:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.6);
            border-color: rgba(56, 189, 248, 0.3);
        }
        
        .question-text {
            color: #f8fafc;
            font-size: 1.25rem;
            margin-bottom: 15px;
            font-weight: 600;
        }
        
        .options-list li {
            background: rgba(255,255,255,0.03);
            margin-bottom: 8px;
            padding: 10px 15px;
            border-radius: 6px;
            border-left: 3px solid #475569;
        }
        
        .essay-answer { margin-top: 1.5rem; }
        .reveal-answer {
            background: #0ea5e9;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            display: inline-block;
            transition: background 0.3s ease;
        }
        .reveal-answer:hover { background: #0284c7; }
        
        .answer-content {
            background: #0f172a;
            border: 1px solid rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 10px;
            margin-top: 15px;
            box-shadow: inset 0 2px 10px rgba(0,0,0,0.5);
        }
        
        .uml-box {
            background: #f8fafc;
            color: #0f172a;
            padding: 20px;
            border-radius: 8px;
            font-family: 'JetBrains Mono', monospace;
            width: 100%;
            overflow-x: auto;
            margin: 15px auto;
            border: 2px solid #334155;
            text-align: left;
            font-size: 1.2rem;
            line-height: 1.6;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .code-box {
            background: #020617; /* Even darker for true editor feel */
            color: #a7f3d0;
            padding: 20px;
            border-left: 5px solid #10b981;
            border-radius: 8px;
            font-family: 'JetBrains Mono', monospace;
            margin-top: 15px;
            margin-bottom: 15px;
            overflow-x: auto;
            font-size: 1.15rem;
            line-height: 1.6;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
        }
        /* Syntax Highlighting for Comments */
        .comment { color: #94a3b8; font-style: italic; }
    </style>
</head>
<body>
    <div id="particles-js"></div>
    <header class="header-nav">
        <a href="index.html" class="back-btn" style="color: #38bdf8; text-decoration: none; font-weight: bold;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle;"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
            الرجوع للقائمة الرئيسية (Back to Home)
        </a>
        <h2 style="margin:0; font-size: 1.2rem; color: #cbd5e1;">Mega Question Bank</h2>
    </header>

    <div class="container">
        <div class="exam-header">
            <h1>🚀 البنك الشامل - جميع أقسام الـ OOP 🚀</h1>
            <p>مقسّم حرفياً زي المنهج: شامل الـ MCQs، الأكواد، الـ Tracing، ومسائل הـ UML بالأكشن في الـ main متوثقة بالشرح العربي</p>
        </div>
        
        {content}

    </div>

    <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            particlesJS('particles-js', {
              "particles": {
                "number": { "value": 80, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#38bdf8" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.3 },
                "size": { "value": 3 },
                "line_linked": { "enable": true, "distance": 150, "color": "#38bdf8", "opacity": 0.2, "width": 1 },
                "move": { "enable": true, "speed": 1.5 }
              }
            });
        });
    </script>
</body>
</html>
"""

db = [
    {
        "topic": "1. Introduction to OOP",
        "subtopics": [
            {
                "name": "Why OOP, Principles, and Basic UML",
                "questions": [
                    {"type": "mcq", "q": "What is the main limitation of Procedural Programming that OOP aims to solve?", "opts": ["A) Slower execution time", "B) Lack of code organization leading to Spaghetti Code", "C) Inability to write mathematical formulas", "D) Poor integration with hardware"], "a": "B) Lack of code organization leading to Spaghetti Code", "eng": "Procedural programming focuses on functions rather than data, making large codebases hard to maintain.", "ar": "البرمجة الإجرائية بتركز على الدوال، ولما البرنامج بيكبر الكود بيدخل في بعضه ويبقى Spaghetti code، عشان كدا الـ OOP ظهرت لتنظيم الكود وربط البيانات بالدوال."},
                    {"type": "mcq", "q": "Which of the following describes the 'Bottom-Up' approach of OOP?", "opts": ["A) Writing the main function first", "B) Starting by designing classes and objects, then combining them to build the main program", "C) Writing functions from the bottom of the file", "D) Ignoring data and focusing on algorithms"], "a": "B) Starting by designing classes and objects, then combining them to build the main program", "eng": "OOP uses a bottom-up approach: you build the basic entities (classes) first, then use them to construct complex systems.", "ar": "الـ OOP بتبدأ من تحت لفوق (Bottom-Up). يعني بنصمم الكلاسات والأوبجيكت الأول، وبعدين نجمعهم في الـ main عشان نبني البرنامج الكبير."},
                    {"type": "mcq", "q": "Which of the following is considered a primary BENEFIT of Object-Oriented Programming?", "opts": ["A) Slower execution speed", "B) Code Reusability and Modularity", "C) Requires less memory by default", "D) Eliminates the need for compilers"], "a": "B) Code Reusability and Modularity", "eng": "Through features like inheritance and classes, OOP promotes modular design and code reusability, saving time and reducing bugs.", "ar": "أكبر فايدة للـ OOP إنها بتخلينا نعيد استخدام الكود (عن طريق الوراثة مثلاً) وإننا نقسم البرنامج لموديولات (كلاسات) منفصلة يسهل صيانتها (Modularity & Reusability)."},
                    {"type": "tf", "q": "Data Hiding (Encapsulation) makes it impossible for the user of the class to accidentally corrupt the internal state of the object.", "a": "True", "eng": "By making variables private and only exposing controlled setters/getters, the internal state cannot be modified directly.", "ar": "صح جداً. الكبسلة (Encapsulation) بتخفي البيانات (private) عشان تمنع أي حد يعدل فيها بطريقة غلط من الـ main، ولازم يستخدم دوال محددة زي الـ Setters."},
                    {
                        "type": "uml",
                        "q": "Design a UML class named 'Rectangle'. It has private width and height. Implement setters, getters, and an area method. Write the UML, then code it with a main() that uses these methods.",
                        "uml": """Rectangle
-------------------
- width: float
- height: float
-------------------
+ setWidth(w: float): void
+ setHeight(h: float): void
+ getArea(): float""",
                        "ans": """#include <iostream> // استدعاء مكتبة الإدخال والإخراج
using namespace std; // استخدام الفضاء المعياري

class Rectangle { // تعريف الكلاس
private: // البيانات الخاصة (مقفول عليها)
    float width; // الطول
    float height; // العرض
public: // الدوال العامة اللي هنستخدمها من بره
    void setWidth(float w) { width = w; } // دالة لإدخال الطول
    void setHeight(float h) { height = h; } // دالة لإدخال العرض
    
    float getArea() { // دالة لحساب المساحة
        return width * height; // ضرب الطول في العرض
    }
};

int main() { // الدالة الرئيسية
    // Action in main!
    Rectangle rect; // إنشاء أوبجيكت من نوع Rectangle
    rect.setWidth(5.5); // تحديد الطول
    rect.setHeight(10.0); // تحديد العرض
    cout << "Area of rectangle is: " << rect.getArea() << endl; // طباعة المساحة
    return 0; // إنهاء البرنامج
}""",
                        "eng": "Basic encapsulation: data is private, accessed only via public setter/getter methods.",
                        "ar": "تطبيق أساسي على الـ Encapsulation (الكبسلة). خلينا الطول والعرض private ومحدش يقدر يوصلهم في الـ main غير من خلال الدوال الـ public زي الـ set."
                    },
                    {
                        "type": "uml",
                        "q": "Design a UML for a 'Bank' system. It has a balance. Implement a constructor and a withdraw method that checks if balance is sufficient. Test this logic in main().",
                        "uml": """Bank
-------------------
- balance: double
-------------------
+ Bank(initial: double)
+ withdraw(amount: double): bool""",
                        "ans": """#include <iostream> // مكتبة الطباعة
using namespace std;

class Bank { // تعريف كلاس البنك
private: 
    double balance; // الرصيد (مخفي)
public:
    Bank(double initial) { // Constructor بيستقبل الرصيد الافتتاحي
        balance = initial; // تعيين الرصيد
    }
    bool withdraw(double amount) { // دالة السحب
        if (amount <= balance) { // لو المبلغ المطلوب أقل من أو يساوي الرصيد
            balance -= amount; // اخصم المبلغ
            cout << "Withdrawal successful. New balance: " << balance << endl; // طباعة نجاح
            return true; // السحب تم
        } else { // لو الرصيد مش مكفي
            cout << "Insufficient funds!" << endl; // طباعة رسالة فشل
            return false; // السحب اترفض
        }
    }
};

int main() {
    Bank myBank(1000.0); // فتح حساب بـ 1000
    myBank.withdraw(400.0); // سحب 400 (هينجح)
    myBank.withdraw(800.0); // سحب 800 (هيفشل لأن الباقي 600)
    return 0; // إنهاء
}""",
                        "eng": "The logic checks if the requested amount is available before deduction, demonstrating how classes protect their state.",
                        "ar": "هنا الكلاس بيحمي البيانات بتاعته، مفيش سحب بيتم إلا لو فيه رصيد كافي. جربناها في الـ main مرة سحبنا مبلغ متاح ومرة سحبنا مبلغ أكبر عشان نتأكد إن اللوجيك شغال ومفيش رصيد بالسالب."
                    }
                ]
            }
        ]
    },
    {
        "topic": "2. Objects & Classes",
        "subtopics": [
            {
                "name": "Access Modifiers, Constructors, Destructors, Setters & Getters",
                "questions": [
                    {"type": "mcq", "q": "What is the primary difference in default Access Modifiers between a `struct` and a `class` in C++?", "opts": ["A) A struct cannot have functions, a class can", "B) Default access in struct is private, in class it is public", "C) Default access in struct is public, in class it is private", "D) There is no difference"], "a": "C) Default access in struct is public, in class it is private", "eng": "If you don't write `public:` or `private:`, a struct assumes everything is public, while a class assumes everything is private.", "ar": "في الـ struct لو مكتبتش حاجة كل حاجة بتبقى مكشوفة (public). لكن الكلاس مصمم عشان يخفي البيانات فبيعتبر أي حاجة مش مكتوب قبلها modifier إنها (private)."},
                    {"type": "tf", "q": "The main reason to use Setters (Mutators) instead of making variables public is to validate data before changing it.", "a": "True", "eng": "Setters allow us to add 'if' statements to prevent bad data (like negative age or invalid passwords) from entering the object.", "ar": "صح جداً. الـ Setter مش مجرد دالة بتاخد قيمة تحطها في متغير وخلاص، فايدتها الأساسية إنك تقدر تحط شروط (if) جواها وتمنع المستخدم إنه يدخل داتا غلط (زي عمر بالسالب مثلاً)."},
                    {"type": "tf", "q": "If you define a parameterized constructor, the compiler still generates a default constructor for you automatically.", "a": "False", "eng": "Once you define ANY constructor, the compiler stops generating the default one.", "ar": "غلط. بمجرد ما بتعمل Constructor بتاعك (حتى لو بـ parameters)، الكومبايلر بيبطل يساعدك ولازم تكتب الـ Default بنفسك لو عاوزه."},
                    {"type": "mcq", "q": "When is the Copy Constructor invoked?", "opts": ["A) When returning an object by value", "B) When passing an object by value as an argument", "C) When explicitly initializing one object with another of the same type", "D) All of the above"], "a": "D) All of the above", "eng": "A copy constructor is triggered whenever a completely new object is created from an existing object.", "ar": "الـ Copy Constructor بيشتغل في كل الحالات دي: لو رجعت أوبجيكت By Value من دالة، أو بعته لدالة By Value، أو لو ساويت أوبجيكت جديد بواحد قديم وقت تعريفه (زي Student s2 = s1)."},
                    {"type": "mcq", "code": """class Test {
public:
    Test() { cout << "D "; }
    Test(int x) { cout << "P "; }
};
int main() {
    Test t1;
    Test t2(5);
    Test t3(); 
    return 0;
}""", "q": "What will be printed to the screen?", "opts": ["A) D P D", "B) D P", "C) P D", "D) Compiler Error"], "a": "B) D P", "eng": "Test t3() is a function declaration (returning a Test object), NOT an object instantiation! It is known as the Most Vexing Parse in C++.", "ar": "خبيثة جداً جداً! السطر الأول بيطبع D، التاني بيطبع P. السطر التالت `Test t3()` ده مش بيعمل أوبجيكت! الكومبايلر بيفتكره دالة عادية اسمها t3 بترجع أوبجيكت من نوع Test، فمش بيستدعي الـ Constructor خالص."},
                    {
                        "type": "uml",
                        "q": "Implement all 3 constructors (Default, Parameterized, Copy) and a Destructor for a 'Student' class with an ID and Name. Create objects using all 3 in main().",
                        "uml": """Student
-------------------
- id: int
- name: string
-------------------
+ Student()
+ Student(i: int, n: string)
+ Student(const s: Student&)
+ ~Student()
+ print(): void""",
                        "ans": """#include <iostream>
#include <string> // مكتبة النصوص
using namespace std;

class Student { // كلاس الطالب
private:
    int id; // رقم الطالب
    string name; // اسم الطالب
public:
    // 1. Default Constructor
    Student() { // الـ Constructor الافتراضي (فاضي)
        id = 0; name = "Unknown"; // قيم ابتدائية
        cout << "Default Constructor Called\\n"; // للتأكيد
    }
    
    // 2. Parameterized Constructor
    Student(int i, string n) { // بياخد بارامترز
        id = i; name = n; // تعيين القيم
        cout << "Parameterized Constructor Called\\n";
    }
    
    // 3. Copy Constructor
    Student(const Student& s) { // بياخد Reference من أوبجيكت تاني
        id = s.id; // نسخ الـ ID
        name = s.name; // نسخ الاسم
        cout << "Copy Constructor Called\\n";
    }
    
    // Destructor
    ~Student() { // الهدّام (بيشتغل لما الأوبجيكت يموت)
        cout << "Destructor Called for " << name << "\\n";
    }
    
    void print() { cout << "ID: " << id << " Name: " << name << endl; } // دالة الطباعة
};

int main() {
    Student s1;                  // أوبجيكت فاضي (ينادي Default)
    Student s2(101, "Ahmed");    // أوبجيكت ببيانات (ينادي Parameterized)
    Student s3 = s2;             // أوبجيكت جديد بينسخ من s2 (ينادي Copy)
    
    s3.print(); // طباعة بيانات s3
    return 0; // البرنامج بيقفل والهدام بيشتغل بالعكس (s3 ثم s2 ثم s1)
}""",
                        "eng": "Demonstrates the complete lifecycle of objects. Notice the Copy constructor must take a reference.",
                        "ar": "المسألة دي بتلم كل أنواع الـ Constructors. في الـ main جربنا نعمل أوبجيكت فاضي (Default)، وأوبجيكت ببيانات (Parameterized)، وأوبجيكت بينسخ من واحد تاني (Copy). وفي النهاية הـ Destructor هيمسحهم بالعكس."
                    }
                ]
            },
            {
                "name": "Objects as Arguments, Memory & Const/Static Members",
                "questions": [
                    {"type": "tf", "q": "Memory is allocated for a Class when it is defined in the code.", "a": "False", "eng": "A class is just a blueprint. NO memory is allocated until an object of that class is created.", "ar": "غلط! الكلاس مجرد تصميم على ورق (Blueprint) مابياخدش أي ميموري خالص. الميموري بتتحجز أول ما تصنع منه أوبجيكت (Object Creation) في الـ main."},
                    {"type": "mcq", "q": "Why is it highly recommended to pass objects to functions 'By Reference' (e.g., `void func(const Object& obj)`) rather than 'By Value'?", "opts": ["A) It prevents the use of public methods", "B) It avoids the overhead of invoking the copy constructor and copying all data", "C) It deletes the object automatically", "D) It turns the object into a static variable"], "a": "B) It avoids the overhead of invoking the copy constructor and copying all data", "eng": "Passing by value makes a full copy of the object which is slow and consumes memory. Passing by reference just passes the memory address.", "ar": "تمرير الـ Object للدوال (By Value) بيخلي الكومبايلر يشغل הـ Copy Constructor ويعمل نسخة كاملة من الأوبجيكت بكل اللي فيه وده بيبطئ البرنامج. عشان كده دايماً بنبعته (By Reference &) عشان نبعت مساره بس، وبنحط const لو مش عايزين الدالة تغير فيه."},
                    {"type": "tf", "q": "An inline function guarantees that the compiler will expand it at the call site.", "a": "False", "eng": "Inline is only a REQUEST to the compiler. If the function is too complex, contains loops, or is recursive, the compiler ignores the inline request.", "ar": "غلط. كلمة Inline دي (طلب) بنطلبه من الكومبايلر، بس لو الدالة كانت معقدة أوي أو فيها Loops الكومبايلر هيرفض الطلب ويعتبرها دالة عادية جداً."},
                    {"type": "mcq", "code": """class Number {
    int val;
public:
    Number(int v) { val = v; }
    int getVal() { return val; } // NOT const
};
int main() {
    const Number n(10);
    cout << n.getVal();
    return 0;
}""", "q": "What happens when this code is compiled?", "opts": ["A) Prints 10", "B) Compilation Error", "C) Runtime Error", "D) Prints garbage value"], "a": "B) Compilation Error", "eng": "A constant object (`const Number n`) CANNOT call non-const methods. Since `getVal` is not marked as const, the compiler blocks it to protect the object.", "ar": "عشان الأوبجيكت `n` متعرف إنه ثابت (const)، الكومبايلر بيمنعه إنه يستدعي أي دالة مش متأمنة بكلمة const، عشان خايف إنها تغير قيمته. فلازم نكتب `int getVal() const` عشان يشتغل."},
                    {"type": "mcq", "q": "Which of the following is TRUE about Static Member Functions?", "opts": ["A) They can access non-static member variables", "B) They have a 'this' pointer", "C) They can only access static member variables and static functions", "D) They must be called using an object"], "a": "C) They can only access static member variables and static functions", "eng": "Static methods belong to the class level. They do not know about specific objects, so they have no 'this' pointer and can only interact with static variables.", "ar": "الدوال הـ Static دي بتاعة الكلاس ككل مش بتاعة أوبجيكت معين. فمتقدرش توصل لمتغيرات عادية (لأن مفيش this pointer يعرّفها الأوبجيكت فين)، وتتعامل بس مع الحاجات הـ static زيها."},
                    {
                        "type": "uml",
                        "q": "Create a 'Point' class with X and Y. Make an inline function to print it. Create a function 'addPoints' that takes two objects and RETURNS a new Point object. Test in main().",
                        "uml": """Point
-------------------
- x: int
- y: int
-------------------
+ Point(x: int, y: int)
+ inline print() const: void
+ addPoints(p1: Point, p2: Point): Point""",
                        "ans": """#include <iostream>
using namespace std;

class Point { // كلاس النقطة
private:
    int x, y; // الإحداثيات
public:
    Point(int xVal, int yVal) { // Constructor
        x = xVal; y = yVal;
    }
    
    // Inline & Const function
    inline void print() const { // دالة Inline وسريعة وكمان Const
        cout << "(" << x << ", " << y << ")\\n"; // طباعة النقطة
    }
    
    // Function taking objects and returning an object
    Point addPoints(Point p1, Point p2) { // دالة بتاخد 2 أوبجيكتس
        Point temp(p1.x + p2.x, p1.y + p2.y); // بنجمعهم ونحطهم في أوبجيكت جديد
        return temp; // بنرجع الأوبجيكت الجديد
    }
};

int main() {
    Point p1(3, 4); // النقطة الأولى
    Point p2(1, 2); // النقطة التانية
    
    // Note: Calling via object since it's a member function
    Point p3 = p1.addPoints(p1, p2); // بننادي الدالة عشان تجمعهم
    
    cout << "Result: ";
    p3.print(); // بنطبع النتيجة
    
    return 0; // إنهاء
}""",
                        "eng": "Objects can be passed exactly like normal variables, and returned identically. Const methods guarantee the object's data won't change.",
                        "ar": "في الـ main بعتنا اتنين أوبجيكتس للدالة `addPoints`، الدالة جمعت الـ X والـ Y وعملت أوبجيكت جديد (temp) ورجعته، واستقبلناه في `p3`. واستخدمنا `inline` عشان نسرع أداء الطباعة."
                    },
                    {
                        "type": "uml",
                        "q": "Design a 'Car' class. It has a static variable 'totalCars' to track how many cars are created. In main(), create an array of 3 Cars and print the static variable using a static method.",
                        "uml": """Car
-------------------
- model: string
- static totalCars: int
-------------------
+ Car()
+ Car(m: string)
+ static getTotalCars(): int
+ ~Car()""",
                        "ans": """#include <iostream>
#include <string>
using namespace std;

class Car { // كلاس العربية
private:
    string model; // موديل العربية
    static int totalCars; // متغير Static (مُشترك بين كل العربيات)
public:
    Car() { // Default Constructor
        model = "Default";
        totalCars++; // بنزود عدد العربيات
    }
    Car(string m) { // Parameterized Constructor
        model = m;
        totalCars++; // بنزود عدد العربيات
    }
    
    static int getTotalCars() { // دالة Static عشان ترجع العدد
        return totalCars; // هترجع المتغير الـ static
    }
    
    ~Car() { // Destructor
        totalCars--; // لما عربية تتمسح، ننقص العدد
    }
};

// Static Initialization MUST be outside the class!
int Car::totalCars = 0; // تعريف المتغير הـ Static بره الكلاس ونديله صفر

int main() {
    cout << "Initial Cars: " << Car::getTotalCars() << endl; // بنشوف العدد قبل أي حاجة
    
    // Array of Objects calls Default Constructor 3 times
    Car showroom[3]; // حجزنا مصفوفة فيها 3 عربيات
    
    cout << "Cars after array creation: " << Car::getTotalCars() << endl; // العدد بقى 3
    
    {
        Car temp("BMW"); // عملنا عربية جديدة جوه قوسين Scope
        cout << "Cars inside block: " << Car::getTotalCars() << endl; // العدد بقى 4
    } // الـ Scope خلص، عربية BMW اتمسحت، الهدام نقص العدد
    
    cout << "Cars after block: " << Car::getTotalCars() << endl; // العدد رجع 3 تاني
    
    return 0; // إنهاء
}""",
                        "eng": "Static variables are shared among all instances. They must be initialized globally outside the class.",
                        "ar": "المتغير الـ static مشترك بين كل العربيات. أول ما عملنا Array فيها 3 عربيات، الـ Constructor اشتغل 3 مرات وزود العدد. ولما الأوبجيكت اللي جوه القوسين مات، الـ Destructor اشتغل ونقص العدد. وطبعنا العدد بدون ما نحتاج أوبجيكت عن طريق `Car::getTotalCars()`."
                    }
                ]
            }
        ]
    },
    {
        "topic": "3. Memory Management",
        "subtopics": [
            {
                "name": "Stack vs Heap & Memory Problems",
                "questions": [
                    {"type": "mcq", "q": "What is the difference between `new` in C++ and `malloc()` in C?", "opts": ["A) They are exactly the same", "B) `malloc` calls constructors, `new` does not", "C) `new` allocates memory AND calls the constructor, `malloc` only allocates raw memory", "D) `new` is used for the stack, `malloc` for the heap"], "a": "C) `new` allocates memory AND calls the constructor, `malloc` only allocates raw memory", "eng": "In OOP, objects must be initialized. `new` ensures the constructor is called automatically after memory is allocated.", "ar": "دي حتة مهمة جداً! `new` في الـ C++ مش بس بتحجز مكان في الـ Heap، دي كمان بتشغل الـ Constructor عشان تبني الأوبجيكت صح. لكن `malloc` بتاعة الـ C كانت بتحجز ميموري فاضية (زبالة) ومش بتشغل حاجة."},
                    {"type": "mcq", "q": "Which of the following scenarios is the most common cause of a 'Stack Overflow' error?", "opts": ["A) Forgetting to write 'delete' after 'new'", "B) Infinite or excessively deep recursion without a base case", "C) Reassigning a pointer to a new location", "D) Accessing private variables from main"], "a": "B) Infinite or excessively deep recursion without a base case", "eng": "The stack has limited size. If a function calls itself infinitely, it fills up the stack memory until it overflows.", "ar": "الـ Stack مساحته صغيرة نسبياً. لو عملت دالة بتنادي نفسها إلى ما لا نهاية (Recursion بدون شرط توقف) أو عملت مصفوفة حجمها ضخم جداً جوه دالة عادية، الـ Stack بيتملي ويضرب ويديك Error."},
                    {"type": "tf", "q": "A Memory Leak happens when a pointer pointing to dynamically allocated memory goes out of scope without calling `delete`.", "a": "True", "eng": "If the pointer disappears, the memory it was pointing to is orphaned and can never be freed.", "ar": "صح تماماً. لو البوينتر اتمسح من الـ Stack لأنه خلص الـ Scope، الميموري اللي حجزها في הـ Heap هتفضل محجوزة على الفاضي ومفيش أي طريقة نوصلها بيها. وده هو الـ Memory Leak."},
                    {
                        "type": "mcq",
                        "code": """void process() {
    int* data = new int[500];
    // processing ...
    data = new int[1000];
    delete[] data;
}""",
                        "q": "What critical memory error occurs in this code?",
                        "opts": ["A) Dangling Pointer", "B) Memory Leak of 500 integers", "C) Stack Overflow", "D) Double Free Error"],
                        "a": "B) Memory Leak of 500 integers",
                        "eng": "The pointer `data` originally pointed to 500 ints. By reassigning it without `delete[]` first, those 500 ints are lost in the Heap forever.",
                        "ar": "حجزنا 500 مكان، وبعدين البوينتر سابهم ومسك في 1000 مكان تانيين! طب الـ 500 الأوليين دول هيمسحهم إزاي ومفيش بوينتر بيشاور عليهم؟ ضاعوا في الميموري (Memory Leak)."
                    },
                    {
                        "type": "uml",
                        "q": "Create a 'DynamicArray' class that allocates a dynamic int array in its constructor and deletes it in its destructor. Test in main() by dynamically allocating the class object itself.",
                        "uml": """DynamicArray
-------------------
- size: int
- arr: int*
-------------------
+ DynamicArray(s: int)
+ fillData(): void
+ ~DynamicArray()""",
                        "ans": """#include <iostream>
using namespace std;

class DynamicArray { // الكلاس
private:
    int size; // حجم المصفوفة
    int* arr; // بوينتر هيشاور على المصفوفة في الـ Heap
public:
    DynamicArray(int s) { // Constructor
        size = s; // نسجل الحجم
        arr = new int[size]; // بنحجز الميموري في הـ Heap
        cout << "Array of size " << size << " created in Heap.\\n";
    }
    
    void fillData() { // دالة تعبئة البيانات
        for(int i=0; i<size; i++) { // Loop لملء الأرقام
            arr[i] = i * 10; // بنملا المصفوفة
        }
        cout << "First element: " << arr[0] << ", Last: " << arr[size-1] << endl;
    }
    
    ~DynamicArray() { // Destructor الأهم
        delete[] arr; // لازم نمسح المصفوفة عشان نمنع الـ Memory Leak!
        cout << "Array memory freed.\\n";
    }
};

int main() {
    // Dynamically allocating the OBJECT itself in the Heap!
    DynamicArray* myArr = new DynamicArray(50); // بنحجز الأوبجيكت نفسه في الـ Heap بـ new
    
    myArr->fillData(); // بننادي دالة التعبئة
    
    // If we don't call delete, the destructor is NEVER called!
    delete myArr; // خطوة قاتلة: لازم نعمل delete عشان הـ Destructor يشتغل والمصفوفة تتمسح
    
    return 0; // إنهاء
}""",
                        "eng": "A dynamic object must be explicitly deleted. When `delete myArr` is called, the object's destructor runs, which in turn deletes the inner dynamic array.",
                        "ar": "هنا إحنا حجزنا (أوبجيكت) كامل في الـ Heap باستخدام new. الأوبجيكت ده جواه Constructor بيحجز (مصفوفة) في الـ Heap بردو! لو معملناش `delete myArr` في الـ main، الهدّام مش هيشتغل والمصفوفة مش هتتمسح والدنيا هتبوظ."
                    },
                    {
                        "type": "uml",
                        "q": "Implement Deep Copy vs Shallow Copy. Create a 'StringBox' class holding a dynamic char pointer. Implement a Custom Copy Constructor to avoid dangling pointers. Test it in main().",
                        "uml": """StringBox
-------------------
- text: char*
-------------------
+ StringBox(t: const char*)
+ StringBox(const other: StringBox&)  << Deep Copy
+ ~StringBox()
+ print(): void""",
                        "ans": """#include <iostream>
#include <cstring> // مكتبة التعامل مع الحروف
using namespace std;

class StringBox { // كلاس الصندوق
private:
    char* text; // بوينتر لكلمة
public:
    // Regular Constructor
    StringBox(const char* t) {
        text = new char[strlen(t) + 1]; // بنحجز مكان على قد الكلمة بالضبط في הـ Heap
        strcpy(text, t); // بننسخ الكلمة في الميموري
    }
    
    // Deep Copy Constructor!
    StringBox(const StringBox& other) { // الـ Copy Constructor الحقيقي عشان يحل مشكلة الـ Shallow
        text = new char[strlen(other.text) + 1]; // بنحجز مكان جديد خالص (NEW memory)
        strcpy(text, other.text); // بننسخ الداتا نفسها مش مجرد الـ Address
        cout << "Deep copy performed.\\n";
    }
    
    ~StringBox() { // الهدام
        delete[] text; // بيمسح الميموري بتاعته بس (بدون تدخل في الميموري بتاعة الأوبجيكتس التانية)
    }
    
    void print() { cout << "Text: " << text << endl; } // الطباعة
};

int main() {
    StringBox box1("Hello OOP"); // الأوبجيكت الأول
    // This calls the copy constructor. If it was shallow, both would point to same memory!
    StringBox box2 = box1; // الأوبجيكت التاني بيعمل Deep Copy من الأول
    
    box1.print();
    box2.print();
    // لما الـ main يخلص، الاتنين Destructors هيشتغلوا ويمسحوا أماكن منفصلة بسلام.
    return 0;
}""",
                        "eng": "Without a deep copy constructor, both objects' pointers would hold the same memory address. Deleting one would make the other a dangling pointer, crashing the program when it's deleted twice.",
                        "ar": "لو معملناش Copy Constructor بـ Deep Copy، الكومبايلر هينسخ عنوان البوينتر بس! ولما البرنامج يخلص، الاتنين Destructors هيحاولوا يمسحوا نفس العنوان من الـ Heap والبرنامج هيضرب (Double Free). هنا إحنا حجزنا مكان جديد خالص للنسخة ونقلنا فيه الداتا."
                    }
                ]
            }
        ]
    },
    {
        "topic": "4. Inheritance",
        "subtopics": [
            {
                "name": "Types, Access Specifiers & Order",
                "questions": [
                    {"type": "tf", "q": "Hybrid Inheritance is a combination of more than one type of inheritance (e.g., combining Multilevel and Multiple inheritance).", "a": "True", "eng": "Yes, whenever a class structure mixes different inheritance models (like a diamond shape), it is termed hybrid inheritance.", "ar": "صح. الوراثة الهجينة (Hybrid) هي لما البرنامج بتاعنا يبقى فيه خلطة من الوراثة، يعني مثلاً فيه جزء Multi-level شغال وجزء Multiple، فبنسميها مهجنة."},
                    {"type": "mcq", "q": "What happens in 'private inheritance'?", "opts": ["A) Public and protected members of Base become private in Derived", "B) Public members of Base remain public", "C) Base class cannot be inherited", "D) Everything in Base becomes protected"], "a": "A) Public and protected members of Base become private in Derived", "eng": "In private inheritance, the derived class can use the base methods internally, but they are completely hidden from the outside world (the main).", "ar": "لما الكلاس الابن يورث بشكل `private`، بياخد كل حاجة `public` و `protected` من الأب يحبسها جواه ويخليها `private` عنده هو، وبالتالي محدش في הـ main بيقدر يشوفها."},
                    {"type": "tf", "q": "In inheritance, the derived class constructor runs BEFORE the base class constructor.", "a": "False", "eng": "The Base class (the foundation) is always constructed BEFORE the Derived class.", "ar": "غلط تماماً. البناء بيبدأ من الأب (الأساس) وبعدين الابن بيكمل عليه. الهدد بس هو اللي بيبدأ بالابن الأول."},
                    {
                        "type": "mcq",
                        "code": """class A {
public: A() { cout << "1"; } ~A() { cout << "2"; }
};
class B : public A {
public: B() { cout << "3"; } ~B() { cout << "4"; }
};
int main() { B obj; }""",
                        "q": "Trace the exact output sequence:",
                        "opts": ["A) 1 3 4 2", "B) 3 1 2 4", "C) 1 2 3 4", "D) 3 4 1 2"],
                        "a": "A) 1 3 4 2",
                        "eng": "Constructors: Base(1) -> Derived(3). Destructors: Derived(4) -> Base(2).",
                        "ar": "الأساس بيتبني الأول (A هيطبع 1)، بعدين الابن (B هيطبع 3). الهدد بيبقى العكس، نهدم الدور الأخير (B هيطبع 4)، وبعدين الأساس (A هيطبع 2). يبقى الناتج 1 3 4 2."
                    },
                    {
                        "type": "uml",
                        "q": "Implement Multiple Inheritance. Class 'Engine' and Class 'Wheels' are base classes. Class 'Car' inherits BOTH. Show how to initialize them in Car's constructor. Test in main().",
                        "uml": """Engine                 Wheels
-------                -------
- hp: int              - size: int
-------                -------
+ Engine(h: int)       + Wheels(s: int)
+ showHp()             + showSize()

          \\           /
           \\         /
            \\       /
               Car (public Engine, public Wheels)
-------------------
- brand: string
-------------------
+ Car(h: int, s: int, b: string)
+ displayInfo(): void""",
                        "ans": """#include <iostream>
#include <string>
using namespace std;

class Engine { // الأب الأول (المحرك)
protected:
    int hp; // قوة الحصان
public:
    Engine(int h) { hp = h; } // Constructor بتاع المحرك
    void showHp() { cout << "Engine HP: " << hp << endl; } // طباعة القوة
};

class Wheels { // الأب التاني (العجلات)
protected:
    int size; // مقاس العجلة
public:
    Wheels(int s) { size = s; } // Constructor بتاع العجل
    void showSize() { cout << "Wheel Size: " << size << " inches" << endl; } // طباعة المقاس
};

// Multiple Inheritance! Car inherits from BOTH Engine and Wheels
class Car : public Engine, public Wheels { // وراثة متعددة، العربية بتورثهم الاتنين
private:
    string brand; // ماركة العربية
public:
    // MUST call both base constructors in the initialization list!
    Car(int h, int s, string b) : Engine(h), Wheels(s) { // بندي الآباء القيم بتاعتهم هنا قبل أي حاجة
        brand = b; // بنخزن המاركة
    }
    
    void displayInfo() { // دالة بنجمع فيها الداتا
        cout << "Brand: " << brand << endl; // بنطبع الماركة
        showHp();   // الدالة دي جيالنا من الأب الأول (المحرك)
        showSize(); // الدالة دي جيالنا من الأب التاني (العجل)
    }
};

int main() {
    Car myCar(500, 19, "Ferrari"); // بنعمل عربية فيراري بقوة 500 وعجل 19
    myCar.displayInfo(); // بنعرض كل الداتا اللي اتجمعت من الوراثة
    return 0; // إنهاء
}""",
                        "eng": "In Multiple Inheritance, the child has multiple parents. It must initialize all of them in its constructor's initializer list.",
                        "ar": "ده تطبيق على الوراثة المتعددة (Multiple Inheritance). العربية بتورث من محرك ومن عجلات. ففي Constructor بتاع العربية، لازم ننادي على Constructor الأب الأول والأب التاني في הـ Initialization List عشان يتملوا بيانات."
                    },
                    {
                        "type": "uml",
                        "q": "Implement Multi-level Inheritance. Base class 'Person', child 'Employee', grandchild 'Manager'. Chain the constructors correctly and test in main().",
                        "uml": """Person
-------------------
# name: string
-------------------
+ Person(n: string)
        ^
        |
    Employee
-------------------
# id: int
-------------------
+ Employee(n: string, i: int)
        ^
        |
    Manager
-------------------
- bonus: double
-------------------
+ Manager(n: string, i: int, b: double)
+ display(): void""",
                        "ans": """#include <iostream>
#include <string>
using namespace std;

class Person { // الجد
protected:
    string name; // اسم الشخص
public:
    Person(string n) { name = n; } // الجد بياخد الاسم
};

class Employee : public Person { // الأب بيورث الجد
protected:
    int id; // رقم الموظف
public:
    // Pass 'n' up to Person
    Employee(string n, int i) : Person(n) { // بنسلم הـ name للجد في الأقواس بتاعت الـ Initialization
        id = i; // بنسجل הـ id
    }
};

class Manager : public Employee { // الابن بيورث الأب (كده بقى عندنا 3 مستويات)
private:
    double bonus; // البونص
public:
    // Pass 'n' and 'i' up to Employee
    Manager(string n, int i, double b) : Employee(n, i) { // بنسلم الداتا للأب
        bonus = b; // بنسجل الـ bonus
    }
    
    void display() {
        // Can access protected members from grandparents directly!
        cout << "Manager: " << name << ", ID: " << id << ", Bonus: $" << bonus << endl; // الـ name ده جاي من الجد مباشرة!
    }
};

int main() {
    Manager boss("Ahmed", 101, 5000.0); // عملنا المدير وبعتناله بيانات الـ 3 مستويات
    boss.display(); // طبعنا البيانات الموروثة
    return 0; // إنهاء
}""",
                        "eng": "Constructor chaining is required in multi-level inheritance to pass arguments up the hierarchy.",
                        "ar": "الوراثة المتعددة المستويات (جد -> أب -> ابن). كل كلاس لازم يسلم المتغيرات للي فوقه في الـ Initialization List. ولأن المتغيرات `protected`، الحفيد قدر يستخدم `name` بتاع الجد مباشرة من غير Getter."
                    },
                    {
                        "type": "uml",
                        "q": "Design Hierarchical Inheritance. 'Vehicle' is base. 'Car' and 'Truck' both inherit from Vehicle. Demonstrate this structure in main() creating objects for both.",
                        "uml": """        Vehicle
       # speed: int
       + Vehicle(s)
          /    \\
         /      \\
     Car        Truck
- doors: int   - loadCapacity: int
+ Car(s, d)    + Truck(s, l)
+ show()       + show()""",
                        "ans": """#include <iostream>
using namespace std;

class Vehicle { // الأب
protected:
    int speed; // السرعة (موروثة للأبناء)
public:
    Vehicle(int s) { speed = s; } // Constructor الأب
};

class Car : public Vehicle { // الابن الأول (عربية)
private:
    int doors; // الأبواب
public:
    Car(int s, int d) : Vehicle(s) { doors = d; } // بياخد السرعة يديها للأب
    void show() { cout << "Car Speed: " << speed << ", Doors: " << doors << endl; } // طباعة الداتا
};

class Truck : public Vehicle { // الابن التاني (شاحنة)
private:
    int loadCapacity; // الحمولة
public:
    Truck(int s, int l) : Vehicle(s) { loadCapacity = l; } // بياخد السرعة يديها للأب
    void show() { cout << "Truck Speed: " << speed << ", Load: " << loadCapacity << " Tons" << endl; } // طباعة الداتا
};

int main() {
    Car c(120, 4); // عملنا عربية
    Truck t(80, 10); // عملنا شاحنة
    
    c.show(); // طبعنا العربية اللي ورثت الـ speed من الأب
    t.show(); // طبعنا الشاحنة اللي كمان ورثت الـ speed من الأب
    
    return 0; // إنهاء
}""",
                        "eng": "In hierarchical inheritance, multiple distinct child classes inherit from one single parent class.",
                        "ar": "الوراثة الهرمية، أب واحد (Vehicle) طالع منه كذا ابن (Car و Truck). كل ابن بيبعت الـ speed للأب عشان يتسجل عنده ويكمل بناء نفسه ببياناته الخاصة."
                    }
                ]
            }
        ]
    },
    {
        "topic": "5. Polymorphism",
        "subtopics": [
            {
                "name": "Virtual Functions, Early/Late Binding & Abstract Classes",
                "questions": [
                    {"type": "mcq", "q": "What makes a class an 'Abstract Class' in C++?", "opts": ["A) The class has no member variables", "B) The class contains at least one pure virtual function (e.g. = 0)", "C) The class inherits from multiple parents", "D) The class has a private constructor"], "a": "B) The class contains at least one pure virtual function (e.g. = 0)", "eng": "A pure virtual function explicitly marks the class as a base-only concept, preventing instantiation.", "ar": "عشان الكلاس يبقى Abstract ومحدش يقدر يعمل منه Object خالص، لازم يكون جواه دالة `virtual` ومكتوب جنبها `= 0` (Pure Virtual)."},
                    {"type": "tf", "q": "A virtual destructor is important when you delete a derived object through a base class pointer.", "a": "True", "eng": "If the base destructor is not virtual, deleting via a base pointer will only call the base destructor, leaking derived class memory.", "ar": "صح جداً ومهمة جداً. لو البوينتر نوعه (أب) وبيشاور على (ابن)، ولما تيجي تمسحه بـ delete لو الهدّام مش virtual، الكومبايلر هيمسح الأب بس ويسيب الابن يعمل Memory Leak!"},
                    {
                        "type": "mcq",
                        "code": """class Base {
public: virtual void print() { cout << "Base"; }
};
class Derived : public Base {
public: void print() { cout << "Derived"; }
};
int main() {
    Base* ptr = new Derived();
    ptr->print();
}""",
                        "q": "What happens here and why?",
                        "opts": ["A) Prints 'Base' because of Early Binding", "B) Prints 'Derived' because of Late Binding", "C) Syntax Error", "D) Prints both"],
                        "a": "B) Prints 'Derived' because of Late Binding",
                        "eng": "The `virtual` keyword tells the compiler to check the actual object type at run-time (Late Binding), resolving to Derived.",
                        "ar": "بسبب كلمة `virtual` اللي في دالة الأب، الكومبايلر بيعمل Late Binding وبيستنى وقت التشغيل يشوف البوينتر بيشاور على أوبجيكت إيه بالظبط (بيشاور على Derived)، فبيطبع Derived."
                    },
                    {
                        "type": "uml",
                        "q": "Implement an Abstract Class 'Animal' with a pure virtual method 'sound()'. Create 'Dog' and 'Cat' derived classes. In main(), create an array of Animal pointers and loop through them to trigger Polymorphism.",
                        "uml": """Animal (Abstract)
-------------------
-------------------
+ virtual sound() = 0: void

        ^
   _____|_____
   |         |
  Dog       Cat
-------   -------
-------   -------
+ sound() + sound()""",
                        "ans": """#include <iostream>
using namespace std;

// Abstract Class (عشان فيه Pure Virtual)
class Animal {
public:
    virtual void sound() = 0; // Pure Virtual Function (مفيش جسم للدالة)
    virtual ~Animal() {} // Virtual Destructor (أساسي عشان الـ Memory)
};

class Dog : public Animal { // الكلب بيورث من الحيوان
public:
    void sound() override { cout << "Dog says: Woof!\\n"; } // لازم يطبق الدالة بتاعة الصوت
};

class Cat : public Animal { // القطة بتورث من الحيوان
public:
    void sound() override { cout << "Cat says: Meow!\\n"; } // لازم تطبق الدالة بردو
};

int main() {
    // Array of Base Class Pointers (Polymorphism Magic!)
    Animal* zoo[2]; // مصفوفة بوينترات من نوع الأب
    zoo[0] = new Dog(); // الأول بيشاور على كلب
    zoo[1] = new Cat(); // التاني بيشاور على قطة
    
    cout << "--- Zoo Sounds ---\\n";
    for(int i = 0; i < 2; i++) { // Loop للتشغيل
        // Late Binding happens here based on the actual object!
        zoo[i]->sound(); // الكومبايلر بيستنى وقت التشغيل وينادي الصوت الصح حسب الأوبجيكت الحقيقي!
    }
    
    // Cleanup
    for(int i = 0; i < 2; i++) { // بنلف عليهم نمسحهم
        delete zoo[i]; // بنمسحهم عشان الـ Memory Leak، وهنا الـ Virtual Destructor هيشتغل
    }
    
    return 0; // إنهاء
}""",
                        "eng": "An array of base pointers iterating over derived objects is the classic, most powerful use-case of Polymorphism.",
                        "ar": "ده أعظم مثال يوضح الـ Polymorphism (تعدد الأوجه). عملنا مصفوفة بوينترات من نوع الأب Animal، وحطينا جواها كلب وقطة. ولما عملنا Loop نادينا دالة `sound()` واحدة بس، بس كل حيوان طلع الصوت بتاعه حسب نوعه الحقيقي (Late Binding)."
                    },
                    {
                        "type": "uml",
                        "q": "Implement Function Overloading vs Overriding. Create a class MathBase with a virtual method 'compute(int)' and overloaded method 'compute(double)'. Inherit MathDerived and override 'compute(int)'. Test in main().",
                        "uml": """MathBase
-------------------
-------------------
+ virtual compute(x: int): void
+ compute(x: double): void

        ^
        |
   MathDerived
-------------------
-------------------
+ compute(x: int) override: void""",
                        "ans": """#include <iostream>
using namespace std;

class MathBase { // الأب
public:
    // Virtual function ready for Overriding
    virtual void compute(int x) { // دالة بتاخد رقم صحيح
        cout << "Base compute(int): " << x * 2 << endl;
    }
    
    // Overloaded function (same name, different parameter)
    void compute(double x) { // نفس الاسم بس بتاخد كسر (ده اسمه Overloading جوه الكلاس)
        cout << "Base compute(double): " << x * 3.14 << endl;
    }
};

class MathDerived : public MathBase { // الابن
public:
    // Overriding the exact same signature
    void compute(int x) override { // كتبنا نفس الدالة بالظبط تاني عشان نعدلها (ده الـ Overriding مع الوراثة)
        cout << "Derived compute(int) overridden!: " << x * x << endl;
    }
    
    // Note: C++ hides overloaded base functions if a derived class overrides one of them
    // To unhide them, we use: using MathBase::compute;
    using MathBase::compute; // حيلة مهمة جداً عشان الدالة التانية بتاعة الكسر متستخباش
};

int main() {
    MathDerived obj; // عملنا الأوبجيكت من نوع الابن
    
    // Calls overridden Derived method
    obj.compute(5); // بينادي الدالة اللي تعدلت
    
    // Calls overloaded Base method (only works because of 'using' keyword)
    obj.compute(5.5); // بينادي دالة الكسر اللي جايالنا من الأب
    
    // Polymorphism test
    MathBase* ptr = &obj; // بوينتر من نوع الأب بيشاور عالابن
    ptr->compute(10); // Late binding -> calls Derived (بينادي الابن عشان virtual)
    
    return 0; // إنهاء
}""",
                        "eng": "Demonstrates the subtle difference: Overloading is within the same scope with different parameters. Overriding is across inheritance scopes with the EXACT same parameters.",
                        "ar": "هنا بنشرح الفرق بين الـ Overloading (نفس الاسم بس بياخد داتا مختلفة جوه نفس الكلاس) والـ Overriding (الابن بيورث دالة من الأب وبيكتبها تاني بنفس كل حاجة عشان يعدلها). وفي הـ main جربنا الاتنين وجربنا הـ Polymorphism."
                    }
                ]
            }
        ]
    }
]


# Add syntax highlighting logic for comments in C++ code
def highlight_comments(code):
    # Regex to find // comments and wrap them in a span
    # Using multi-line regex
    highlighted = re.sub(r'(//.*)', r'<span class="comment">\1</span>', code)
    return highlighted

content = ""
q_idx = 1
for topic in db:
    content += f'<h2 class="topic-title">{topic["topic"]}</h2>\n'
    for sub in topic["subtopics"]:
        content += f'<h3 class="subtopic-title">📌 {sub["name"]}</h3>\n'
        for q in sub["questions"]:
            if q["type"] == "mcq":
                opts_html = "\n".join([f"                <li>{opt}</li>" for opt in q["opts"]])
                
                # Check if it has code block
                code_html = ""
                if "code" in q:
                    code_html = f'<pre class="code-box" dir="ltr"><code>{highlight_comments(q["code"])}</code></pre>'
                
                content += f"""
        <div class="code-analysis-section">
            <h4 class="question-text" dir="ltr">Q{q_idx}. {q['q']}</h4>
            {code_html}
            <ul class="options-list" dir="ltr" style="text-align: left; margin-left: 10px; color: #cbd5e1; list-style-type: none; padding-left: 0;">
{opts_html}
            </ul>
            <details class="essay-answer">
                <summary class="reveal-answer">👁️ إظهار الإجابة والتفسير</summary>
                <div class="answer-content">
                    <strong style="color:#e2e8f0;">Answer:</strong> <span style="color: #34d399; font-weight: bold; font-size:1.1rem;">{q['a']}</span>
                    <hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">
                    <strong style="color:#e2e8f0;">Explanation:</strong>
                    <p dir="ltr" style="color: #94a3b8; margin-bottom: 10px; margin-top: 5px;">{q['eng']}</p>
                    <p dir="rtl" style="text-align: right; color: #f8fafc; font-size: 1.05rem; border-right: 3px solid #38bdf8; padding-right: 15px; margin-top: 15px; line-height: 1.8;"><strong>بالعامية: </strong>{q['ar']}</p>
                </div>
            </details>
        </div>
"""
            elif q["type"] == "tf":
                content += f"""
        <div class="code-analysis-section">
            <h4 dir="ltr" style="color: #38bdf8; margin-bottom: 10px; font-size:1.3rem;">Q{q_idx}. True or False?</h4>
            <p dir="ltr" style="text-align: left; color: #f8fafc; font-size: 1.15rem; background: rgba(56, 189, 248, 0.1); padding: 15px; border-left: 4px solid #38bdf8; border-radius: 6px;">{q['q']}</p>
            <details class="essay-answer">
                <summary class="reveal-answer">👁️ إظهار الإجابة والتفسير</summary>
                <div class="answer-content">
                    <strong style="color:#e2e8f0;">Answer:</strong> <span style="color: #f59e0b; font-weight: bold; font-size:1.1rem;">{q['a']}</span>
                    <hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">
                    <strong style="color:#e2e8f0;">Explanation:</strong>
                    <p dir="ltr" style="color: #94a3b8; margin-bottom: 10px; margin-top: 5px;">{q['eng']}</p>
                    <p dir="rtl" style="text-align: right; color: #f8fafc; font-size: 1.05rem; border-right: 3px solid #f59e0b; padding-right: 15px; margin-top: 15px; line-height: 1.8;"><strong>بالعامية: </strong>{q['ar']}</p>
                </div>
            </details>
        </div>
"""
            elif q["type"] == "uml":
                content += f"""
        <div class="code-analysis-section">
            <h4 class="question-text" dir="ltr" style="color: #c084fc;">Q{q_idx}. {q['q']}</h4>
            <pre class="uml-box" dir="ltr"><code>{q['uml']}</code></pre>
            <details class="essay-answer">
                <summary class="reveal-answer" style="background:#a855f7;">👁️ إظهار الإجابة والتفسير</summary>
                <div class="answer-content">
                    <strong style="color:#e2e8f0;">Answer:</strong>
                    <pre class="code-box" dir="ltr"><code>{highlight_comments(q['ans'])}</code></pre>
                    <hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">
                    <strong style="color:#e2e8f0;">Explanation:</strong>
                    <p dir="ltr" style="color: #94a3b8; margin-bottom: 10px; margin-top: 5px;">{q['eng']}</p>
                    <p dir="rtl" style="text-align: right; color: #f8fafc; font-size: 1.05rem; border-right: 3px solid #a855f7; padding-right: 15px; margin-top: 15px; line-height: 1.8;"><strong>بالعامية: </strong>{q['ar']}</p>
                </div>
            </details>
        </div>
"""
            q_idx += 1


final_html = html_template.replace("{content}", content)

file_paths = [
    r"c:\Users\HP\OneDrive\Desktop\namoly",
    r"c:\Users\HP\OneDrive\Desktop\oop-portal-test"
]

for base in file_paths:
    mega_path = os.path.join(base, "mega_question_bank.html")
    with open(mega_path, "w", encoding="utf-8") as f:
        f.write(final_html)

print("Ultimate Mega Bank V4 Generated. Formatted code nicely with Arabic comments on EVERY line.")
