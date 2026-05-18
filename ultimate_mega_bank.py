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
            <h1>🚀 البنك الشامل - جميع أقسام الـ OOP 🚀</h1>
            <p>مقسّم حرفياً زي المنهج: شامل الـ MCQs، الأكواد، الـ Tracing، ومسائل הـ UML بالأكشن في الـ main</p>
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
                        "ans": """#include <iostream>
using namespace std;

class Rectangle {
private:
    float width;
    float height;
public:
    void setWidth(float w) { width = w; }
    void setHeight(float h) { height = h; }
    
    float getArea() {
        return width * height;
    }
};

int main() {
    // Action in main!
    Rectangle rect;
    rect.setWidth(5.5);
    rect.setHeight(10.0);
    cout << "Area of rectangle is: " << rect.getArea() << endl;
    return 0;
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
                        "ans": """#include <iostream>
using namespace std;

class Bank {
private:
    double balance;
public:
    Bank(double initial) {
        balance = initial;
    }
    bool withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            cout << "Withdrawal successful. New balance: " << balance << endl;
            return true;
        } else {
            cout << "Insufficient funds!" << endl;
            return false;
        }
    }
};

int main() {
    Bank myBank(1000.0);
    myBank.withdraw(400.0); // Should succeed
    myBank.withdraw(800.0); // Should fail
    return 0;
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
                "name": "Constructors (Default, Parameterized, Copy) & Destructor",
                "questions": [
                    {"type": "tf", "q": "If you define a parameterized constructor, the compiler still generates a default constructor for you automatically.", "a": "False", "eng": "Once you define ANY constructor, the compiler stops generating the default one.", "ar": "غلط. بمجرد ما بتعمل Constructor بتاعك (حتى لو بـ parameters)، الكومبايلر بيبطل يساعدك ولازم تكتب الـ Default بنفسك لو عاوزه."},
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
#include <string>
using namespace std;

class Student {
private:
    int id;
    string name;
public:
    // 1. Default Constructor
    Student() {
        id = 0; name = "Unknown";
        cout << "Default Constructor Called\\n";
    }
    
    // 2. Parameterized Constructor
    Student(int i, string n) {
        id = i; name = n;
        cout << "Parameterized Constructor Called\\n";
    }
    
    // 3. Copy Constructor
    Student(const Student& s) {
        id = s.id;
        name = s.name;
        cout << "Copy Constructor Called\\n";
    }
    
    // Destructor
    ~Student() {
        cout << "Destructor Called for " << name << "\\n";
    }
    
    void print() { cout << "ID: " << id << " Name: " << name << endl; }
};

int main() {
    Student s1;                  // Calls Default
    Student s2(101, "Ahmed");    // Calls Parameterized
    Student s3 = s2;             // Calls Copy Constructor
    
    s3.print();
    return 0; // Destructors called in reverse order (s3, then s2, then s1)
}""",
                        "eng": "Demonstrates the complete lifecycle of objects. Notice the Copy constructor must take a reference.",
                        "ar": "المسألة دي بتلم كل أنواع الـ Constructors. في الـ main جربنا نعمل أوبجيكت فاضي (Default)، وأوبجيكت ببيانات (Parameterized)، وأوبجيكت بينسخ من واحد تاني (Copy). وفي النهاية הـ Destructor هيمسحهم بالعكس."
                    }
                ]
            },
            {
                "name": "Returning Objects, Inline Functions & Const Methods",
                "questions": [
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

class Point {
private:
    int x, y;
public:
    Point(int xVal, int yVal) {
        x = xVal; y = yVal;
    }
    
    // Inline & Const function
    inline void print() const {
        cout << "(" << x << ", " << y << ")\\n";
    }
    
    // Function taking objects and returning an object
    Point addPoints(Point p1, Point p2) {
        Point temp(p1.x + p2.x, p1.y + p2.y);
        return temp;
    }
};

int main() {
    Point p1(3, 4);
    Point p2(1, 2);
    
    // Note: Calling via object since it's a member function
    Point p3 = p1.addPoints(p1, p2); 
    
    cout << "Result: ";
    p3.print();
    
    return 0;
}""",
                        "eng": "Objects can be passed exactly like normal variables, and returned identically. Const methods guarantee the object's data won't change.",
                        "ar": "في الـ main بعتنا اتنين أوبجيكتس للدالة `addPoints`، الدالة جمعت الـ X والـ Y وعملت أوبجيكت جديد (temp) ورجعته، واستقبلناه في `p3`. واستخدمنا `inline` عشان نسرع أداء الطباعة."
                    }
                ]
            },
            {
                "name": "Static Members & Array of Objects",
                "questions": [
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

class Car {
private:
    string model;
    static int totalCars; // Declaration only
public:
    Car() {
        model = "Default";
        totalCars++;
    }
    Car(string m) {
        model = m;
        totalCars++;
    }
    
    static int getTotalCars() {
        return totalCars;
    }
    
    ~Car() {
        totalCars--;
    }
};

// Static Initialization MUST be outside the class!
int Car::totalCars = 0;

int main() {
    cout << "Initial Cars: " << Car::getTotalCars() << endl;
    
    // Array of Objects calls Default Constructor 3 times
    Car showroom[3]; 
    
    cout << "Cars after array creation: " << Car::getTotalCars() << endl;
    
    {
        Car temp("BMW"); // Local block scope
        cout << "Cars inside block: " << Car::getTotalCars() << endl;
    } // temp is destroyed here
    
    cout << "Cars after block: " << Car::getTotalCars() << endl;
    
    return 0;
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
                "name": "Dynamic Allocation (Stack/Heap) & Memory Leaks",
                "questions": [
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

class DynamicArray {
private:
    int size;
    int* arr;
public:
    DynamicArray(int s) {
        size = s;
        arr = new int[size]; // Heap allocation
        cout << "Array of size " << size << " created in Heap.\\n";
    }
    
    void fillData() {
        for(int i=0; i<size; i++) {
            arr[i] = i * 10;
        }
        cout << "First element: " << arr[0] << ", Last: " << arr[size-1] << endl;
    }
    
    ~DynamicArray() {
        delete[] arr; // Crucial for preventing memory leak!
        cout << "Array memory freed.\\n";
    }
};

int main() {
    // Dynamically allocating the OBJECT itself in the Heap!
    DynamicArray* myArr = new DynamicArray(50);
    
    myArr->fillData();
    
    // If we don't call delete, the destructor is NEVER called!
    delete myArr; 
    
    return 0;
}""",
                        "eng": "A dynamic object must be explicitly deleted. When `delete myArr` is called, the object's destructor runs, which in turn deletes the inner dynamic array.",
                        "ar": "هنا إحنا حجزنا (أوبجيكت) كامل في الـ Heap باستخدام new. الأوبجيكت ده جواه Constructor بيحجز (مصفوفة) في الـ Heap بردو! لو معملناش `delete myArr` في الـ main، الهدّام مش هيشتغل والمصفوفة مش هتتمسح والدنيا هتبوظ."
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

class Person {
protected:
    string name;
public:
    Person(string n) { name = n; }
};

class Employee : public Person {
protected:
    int id;
public:
    // Pass 'n' up to Person
    Employee(string n, int i) : Person(n) {
        id = i;
    }
};

class Manager : public Employee {
private:
    double bonus;
public:
    // Pass 'n' and 'i' up to Employee
    Manager(string n, int i, double b) : Employee(n, i) {
        bonus = b;
    }
    
    void display() {
        // Can access protected members from grandparents directly!
        cout << "Manager: " << name << ", ID: " << id << ", Bonus: $" << bonus << endl;
    }
};

int main() {
    Manager boss("Ahmed", 101, 5000.0);
    boss.display();
    return 0;
}""",
                        "eng": "Constructor chaining is required in multi-level inheritance to pass arguments up the hierarchy.",
                        "ar": "الوراثة المتعددة المستويات (جد -> أب -> ابن). كل كلاس لازم يسلم المتغيرات للي فوقه في الـ Initialization List. ولأن المتغيرات `protected`، الحفيد قدر يستخدم `name` بتاع الجد مباشرة من غير Getter."
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

// Abstract Class
class Animal {
public:
    virtual void sound() = 0; // Pure Virtual Function
    virtual ~Animal() {} // Virtual Destructor
};

class Dog : public Animal {
public:
    void sound() override { cout << "Dog says: Woof!\\n"; }
};

class Cat : public Animal {
public:
    void sound() override { cout << "Cat says: Meow!\\n"; }
};

int main() {
    // Array of Base Class Pointers (Polymorphism Magic!)
    Animal* zoo[2];
    zoo[0] = new Dog();
    zoo[1] = new Cat();
    
    cout << "--- Zoo Sounds ---\\n";
    for(int i = 0; i < 2; i++) {
        // Late Binding happens here based on the actual object!
        zoo[i]->sound(); 
    }
    
    // Cleanup
    for(int i = 0; i < 2; i++) {
        delete zoo[i]; 
    }
    
    return 0;
}""",
                        "eng": "An array of base pointers iterating over derived objects is the classic, most powerful use-case of Polymorphism.",
                        "ar": "ده أعظم مثال يوضح الـ Polymorphism (تعدد الأوجه). عملنا مصفوفة بوينترات من نوع الأب Animal، وحطينا جواها كلب وقطة. ولما عملنا Loop نادينا دالة `sound()` واحدة بس، بس كل حيوان طلع الصوت بتاعه حسب نوعه الحقيقي (Late Binding)."
                    }
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
                    code_html = f'<pre class="code-box" dir="ltr"><code>{q["code"]}</code></pre>'
                
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
                    <pre class="code-box" dir="ltr"><code>{q['ans']}</code></pre>
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

print("Ultimate Mega Bank Generated with RTL Arabic fix and main() UML actions.")
