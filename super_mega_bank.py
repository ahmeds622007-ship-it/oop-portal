import os

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
            font-size: 1.1rem;
            line-height: 1.5;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .code-box {
            background: #0f172a;
            color: #a7f3d0;
            padding: 15px;
            border-left: 4px solid #10b981;
            border-radius: 6px;
            font-family: 'JetBrains Mono', monospace;
            margin-top: 10px;
            margin-bottom: 15px;
            overflow-x: auto;
        }
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
            <h1>🚀 بنك الأسئلة المكثف للفاينال 🚀</h1>
            <p>أكبر تجميعة أسئلة UML و Code Tracing تغطي كل حرف في المنهج</p>
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

# Massively expanded question database
db = [
    {
        "topic": "🔥 1. Advanced UML To Code (أهم قسم)",
        "subtopics": [
            {
                "name": "Standard Classes & Static Members",
                "questions": [
                    {
                        "type": "uml", 
                        "q": "Convert the following UML into C++ Code. Pay attention to Static Variables and Member initialization.", 
                        "uml": """Employee
-------------------
- empId: int
- salary: float
- static companyName: string
- static empCount: int
-------------------
+ Employee(id: int, s: float)
+ getSalary(): float
+ static getCount(): int
+ ~Employee()""", 
                        "ans": """#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
    int empId;
    float salary;
    static string companyName;
    static int empCount;

public:
    Employee(int id, float s) {
        empId = id;
        salary = s;
        empCount++;
    }
    
    float getSalary() {
        return salary;
    }
    
    static int getCount() {
        return empCount;
    }
    
    ~Employee() {
        empCount--;
    }
};

// Static Initialization MUST be outside
string Employee::companyName = "TechCorp";
int Employee::empCount = 0;""", 
                        "eng": "Static variables must be declared inside the class but initialized globally outside of it. Static methods can only access static variables.", 
                        "ar": "ركز إن أي متغير static لازم ياخد قيمته المبدئية برا الكلاس خالص! ومسحنا الموظف في الـ Destructor فلازم ننقص الـ empCount."
                    },
                    {
                        "type": "uml", 
                        "q": "Convert the following UML containing constant methods and pointers.", 
                        "uml": """Book
-------------------
- title: string
- pages: int*
- price: const float
-------------------
+ Book(t: string, p: int, pr: float)
+ getTitle() const: string
+ print() const: void
+ ~Book()""", 
                        "ans": """#include <iostream>
#include <string>
using namespace std;

class Book {
private:
    string title;
    int* pages;
    const float price;

public:
    // Const members MUST be initialized using an Initialization List
    Book(string t, int p, float pr) : price(pr) {
        title = t;
        pages = new int(p);
    }
    
    string getTitle() const {
        return title;
    }
    
    void print() const {
        cout << "Title: " << title << " Price: " << price << endl;
    }
    
    ~Book() {
        delete pages;
    }
};""", 
                        "eng": "A `const` member variable must be initialized using a member initializer list in the constructor. Dynamic pointers must be cleaned up in the destructor.", 
                        "ar": "التريكة هنا إن الـ price ده const! المتغير الثابت مينفعش ياخد قيمته جوه أقواس الـ Constructor، لازم ياخدها بطريقة الـ Initialization List (النقطتين اللي قبل الأقواس). وطبعاً البوينتر لازم نعمله delete في الهدام."
                    }
                ]
            },
            {
                "name": "Inheritance & Polymorphism UML",
                "questions": [
                    {
                        "type": "uml", 
                        "q": "Implement the following Inheritance Hierarchy with Polymorphism (Virtual Functions).", 
                        "uml": """Vehicle (Abstract)
-------------------
# speed: int
-------------------
+ Vehicle(s: int)
+ virtual start() = 0: void
+ virtual ~Vehicle()
         ^
         |
    Car (Derived)
-------------------
- doors: int
-------------------
+ Car(s: int, d: int)
+ start(): void""", 
                        "ans": """#include <iostream>
using namespace std;

class Vehicle {
protected:
    int speed;
public:
    Vehicle(int s) {
        speed = s;
    }
    
    // Pure Virtual Function
    virtual void start() = 0;
    
    // Virtual Destructor
    virtual ~Vehicle() {
        cout << "Vehicle Destroyed\\n";
    }
};

class Car : public Vehicle {
private:
    int doors;
public:
    // Calling Base Class Constructor
    Car(int s, int d) : Vehicle(s) {
        doors = d;
    }
    
    // Overriding the pure virtual function
    void start() override {
        cout << "Car is starting with speed " << speed << endl;
    }
    
    ~Car() {
        cout << "Car Destroyed\\n";
    }
};""", 
                        "eng": "The presence of `= 0` indicates a Pure Virtual Function, making Vehicle an Abstract Class. Car must use an initialization list to pass parameters to the Vehicle constructor.", 
                        "ar": "علامة `= 0` معناها إن الدالة دي Pure Virtual والكلاس ده أصبح Abstract. وفي الكلاس الابن لازم ننادي الـ Constructor بتاع الأب فوق عشان نبني الأساس الأول، ونعمل override للدالة."
                    },
                    {
                        "type": "uml", 
                        "q": "Multiple Inheritance with access specifiers. Implement the UML.", 
                        "uml": """Device                  Network
---------               ---------
- id: int               - ip: string
---------               ---------
+ Device(i:int)         + Network(ip: string)
+ turnOn(): void        + connect(): void

        ^               ^
        |               |
    SmartPhone (Inherits public Device, protected Network)
-------------------
- os: string
-------------------
+ SmartPhone(i:int, ip:string, o:string)
+ showInfo(): void""", 
                        "ans": """#include <iostream>
#include <string>
using namespace std;

class Device {
private:
    int id;
public:
    Device(int i) { id = i; }
    void turnOn() { cout << "Device On\\n"; }
};

class Network {
private:
    string ip;
public:
    Network(string i) { ip = i; }
    void connect() { cout << "Connected\\n"; }
};

// Multiple Inheritance
class SmartPhone : public Device, protected Network {
private:
    string os;
public:
    // Initializing both base classes
    SmartPhone(int i, string ip_addr, string o) : Device(i), Network(ip_addr) {
        os = o;
    }
    
    void showInfo() {
        turnOn(); // Accessible because public inheritance
        connect(); // Accessible because protected inheritance allows derived class access
        cout << "OS: " << os << endl;
    }
};""", 
                        "eng": "Multiple inheritance requires initializing all base classes in the derived class constructor's initialization list.", 
                        "ar": "وراثة متعددة، يعني الابن ليه اتنين أباء! في الـ Constructor بتاع الابن لازم ننده على الـ Constructors بتاعتهم هما الاتنين عشان يتبنوا."
                    }
                ]
            }
        ]
    },
    {
        "topic": "💻 2. Code Analysis & Tracing (MCQ مع أكواد)",
        "subtopics": [
            {
                "name": "Predict the Output (Constructors/Destructors)",
                "questions": [
                    {
                        "type": "mcq",
                        "q": "What is the output of the following C++ program?",
                        "code": """class Test {
public:
    Test() { cout << "1 "; }
    ~Test() { cout << "2 "; }
};
int main() {
    Test t1;
    {
        Test t2;
    }
    return 0;
}""",
                        "opts": ["A) 1 1 2 2", "B) 1 2 1 2", "C) 1 1 2", "D) 1 2 2 1"],
                        "a": "A) 1 1 2 2",
                        "eng": "t1 created (1). Enter scope. t2 created (1). Scope ends, t2 destroyed (2). main ends, t1 destroyed (2). Total: 1 1 2 2.",
                        "ar": "البرنامج بيمشي سطر سطر. الأول عملنا t1 (طبع 1)، دخلنا جوه قوسين وعملنا t2 (طبع 1). القوسين قفلوا فـ t2 مات (طبع 2). بعدين البرنامج خلص فـ t1 مات (طبع 2). الإجابة 1 1 2 2."
                    },
                    {
                        "type": "mcq",
                        "q": "What is the output of this code?",
                        "code": """class A {
public:
    A() { cout << "A"; }
    ~A() { cout << "a"; }
};
class B : public A {
public:
    B() { cout << "B"; }
    ~B() { cout << "b"; }
};
int main() {
    B obj;
    return 0;
}""",
                        "opts": ["A) ABab", "B) BAab", "C) ABba", "D) BAba"],
                        "a": "C) ABba",
                        "eng": "Construction order: Base then Derived (A -> B). Destruction order: Derived then Base (b -> a). Output: ABba.",
                        "ar": "البناء من تحت لفوق (الأب A يتبني الأول وبعدين الابن B). والهدد العكس تماماً (الابن b يتمسح وبعدين الأب a). يبقى الطباعة ABba."
                    }
                ]
            },
            {
                "name": "Predict the Output (Polymorphism & Virtual)",
                "questions": [
                    {
                        "type": "mcq",
                        "q": "What will this print?",
                        "code": """class Base {
public:
    void show() { cout << "Base"; }
};
class Derived : public Base {
public:
    void show() { cout << "Derived"; }
};
int main() {
    Base* ptr = new Derived();
    ptr->show();
    return 0;
}""",
                        "opts": ["A) Base", "B) Derived", "C) Error", "D) BaseDerived"],
                        "a": "A) Base",
                        "eng": "Because the `show` method is NOT virtual, the compiler uses early binding based on the pointer type (`Base*`). Therefore, it calls Base's show().",
                        "ar": "خبيثة جداً! إحنا معملناش الدالة virtual. فالكومبايلر بيبصميجي بيبص على نوع البوينتر (Base*) ويقوم طابع Base علطول من غير ما يشوف الأوبجيكت الفعلي نوعه إيه."
                    },
                    {
                        "type": "mcq",
                        "q": "Now consider the same code but with virtual:",
                        "code": """class Base {
public:
    virtual void show() { cout << "Base"; }
};
class Derived : public Base {
public:
    void show() override { cout << "Derived"; }
};
int main() {
    Base* ptr = new Derived();
    ptr->show();
    return 0;
}""",
                        "opts": ["A) Base", "B) Derived", "C) Error", "D) Nothing"],
                        "a": "B) Derived",
                        "eng": "Since `show()` is virtual, late binding occurs. The pointer points to a Derived object, so Derived's `show()` is executed.",
                        "ar": "لما حطينا virtual، الكومبايلر استنى وقت التشغيل، لقى إن البوينتر بيشاور على أوبجيكت حقيقي من نوع Derived، فجاب الدالة بتاعت Derived."
                    }
                ]
            },
            {
                "name": "Memory Leaks & Pointers",
                "questions": [
                    {
                        "type": "mcq",
                        "q": "Identify the issue in this code:",
                        "code": """void doSomething() {
    int* ptr = new int[100];
    // work with ptr
    ptr = new int[200];
    delete[] ptr;
}""",
                        "opts": ["A) Dangling Pointer", "B) Memory Leak", "C) Stack Overflow", "D) Syntax Error"],
                        "a": "B) Memory Leak",
                        "eng": "The original memory (`new int[100]`) is lost because the pointer `ptr` is reassigned before deleting it. The memory remains allocated but inaccessible.",
                        "ar": "اللي حصل إنك حجزت 100 مكان في الـ Heap، وبعدين خليت البوينتر يسيبهم ويروح يحجز 200 مكان تانيين! طب الـ 100 الأوليين دول مين هيمسحهم؟ ضاعوا في الميموري! ده اسمه Memory Leak."
                    }
                ]
            }
        ]
    },
    {
        "topic": "📝 3. Rapid Fire Theory Review",
        "subtopics": [
            {
                "name": "Encapsulation & Access Modifiers",
                "questions": [
                    {"type": "tf", "q": "Friend functions can access private members of a class.", "a": "True", "eng": "A friend function is explicitly granted access to all private and protected members of the class that declares it as a friend.", "ar": "صح. الـ Friend function دي الدالة صاحبة الكلاس، بنديلها تصريح إنها تشوف كل أسرار الكلاس وتتعامل مع الـ private عادي جداً."},
                    {"type": "mcq", "q": "Why would you return a value by reference from a member function?", "opts": ["A) To cause a syntax error", "B) To make the return value a constant", "C) To allow the returned variable to be used on the left side of an assignment operator (L-value)", "D) It saves hard drive space"], "a": "C) To allow the returned variable to be used on the left side of an assignment operator (L-value)", "eng": "Returning by reference allows modifying the actual member variable directly (e.g. `obj.getValue() = 5;`).", "ar": "لما الدالة بترجع Reference (&)، ده بيسمحلي أستقبل المتغير الأصلي وأقدر أغير قيمته مباشرة كأنه L-value."}
                ]
            },
            {
                "name": "Constructors Deep Dive",
                "questions": [
                    {"type": "tf", "q": "If a class has a constant member variable, you MUST define a parameterized constructor using an initialization list.", "a": "True", "eng": "Constants cannot be assigned a value inside the constructor body, they must be initialized before the body executes via the initialization list.", "ar": "صح! المتغيرات الـ const مينفعش تاخد `= القيمة` جوه جسم الـ Constructor، لازم تاخدها في الـ Initialization List قبل ما القوس يتفتح أصلاً."},
                    {"type": "tf", "q": "A copy constructor is called when we return an object by value from a function.", "a": "True", "eng": "Returning by value creates a temporary copy of the object, which invokes the copy constructor.", "ar": "صح. لما بنعمل return لـ أوبجيكت، الكومبايلر بيعمل نسخة منه عشان يبعتها، ومين اللي بيعمل نسخ؟ طبعاً الـ Copy Constructor."}
                ]
            }
        ]
    }
]

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
                    code_html = f'<pre class="code-box"><code>{q["code"]}</code></pre>'
                
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
                    <p style="color: #f8fafc; font-size: 1rem; border-right: 3px solid #38bdf8; padding-right: 10px; margin-top: 15px;"><strong>بالعامية:</strong> {q['ar']}</p>
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
                    <p style="color: #f8fafc; font-size: 1rem; border-right: 3px solid #38bdf8; padding-right: 10px; margin-top: 15px;"><strong>بالعامية:</strong> {q['ar']}</p>
                </div>
            </details>
        </div>
"""
            elif q["type"] == "uml":
                content += f"""
        <div class="code-analysis-section">
            <h4 class="question-text" dir="ltr" style="color: #c084fc;">Q{q_idx}. {q['q']}</h4>
            <pre class="uml-box"><code>{q['uml']}</code></pre>
            <details class="essay-answer">
                <summary class="reveal-answer" style="background:#a855f7;">👁️ إظهار الإجابة والتفسير</summary>
                <div class="answer-content">
                    <strong style="color:#e2e8f0;">Answer:</strong>
                    <pre class="code-box" dir="ltr"><code>{q['ans']}</code></pre>
                    <hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">
                    <strong style="color:#e2e8f0;">Explanation:</strong>
                    <p dir="ltr" style="color: #94a3b8; margin-bottom: 10px; margin-top: 5px;">{q['eng']}</p>
                    <p style="color: #f8fafc; font-size: 1rem; border-right: 3px solid #a855f7; padding-right: 10px; margin-top: 15px;"><strong>بالعامية:</strong> {q['ar']}</p>
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

print("Massive Expansion completed! Real multi-line blocks used. No literal \\n in HTML.")
