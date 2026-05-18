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
        .container { position: relative; z-index: 1; max-width: 1000px; margin: auto; padding: 0 20px; }
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
            width: fit-content;
            margin: 15px auto;
            border: 2px solid #334155;
            text-align: left;
            font-size: 1.1rem;
            line-height: 1.5;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
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
            <p>أكبر تجميعة أسئلة تغطي كل سطر في المنهج (Choose, True/False, UML)</p>
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
        "topic": "1. Introduction to OOP",
        "subtopics": [
            {
                "name": "Why do we use OOP and what is OOP",
                "questions": [
                    {"type": "tf", "q": "OOP is mainly used to write code line-by-line without organizing it into structures.", "a": "False", "eng": "Procedural programming does this. OOP organizes code into objects representing real-world entities.", "ar": "البرمجة الإجرائية هي اللي بتكتب سطر سطر، لكن الـ OOP معمولة عشان ننظم الكود في شكل كائنات (Objects) تشبه العالم الحقيقي."},
                    {"type": "mcq", "q": "Which of the following best describes an Object in OOP?", "opts": ["A) A simple variable", "B) A function", "C) An instance of a class", "D) A data type"], "a": "C) An instance of a class", "eng": "A class is a blueprint, and an object is a specific instance created from that blueprint.", "ar": "الأوبجيكت هو نسخة حقيقية (Instance) مبنية من التصميم اللي اسمه Class."},
                    {"type": "mcq", "q": "What problem did OOP primarily solve compared to Procedural Programming?", "opts": ["A) Slow execution speed", "B) Spaghetti code and lack of reusability in large systems", "C) Hardware limitations", "D) Inability to write math functions"], "a": "B) Spaghetti code and lack of reusability in large systems", "eng": "OOP was introduced to manage large, complex software by promoting modularity and reuse, preventing 'spaghetti code'.", "ar": "الـ OOP حلت مشكلة الكود المعقد اللي داخل في بعضه (Spaghetti code) في البرامج الكبيرة، وخليتنا نقدر نعيد استخدام الكود بسهولة."},
                    {"type": "tf", "q": "OOP makes it difficult to map software models to real-world objects.", "a": "False", "eng": "OOP is literally designed to map software structures to real-world objects using concepts like classes, attributes, and methods.", "ar": "بالعكس تماماً! الـ OOP معمولة مخصوص عشان تخلينا نبرمج الحاجات كأنها حقيقية (عربية ليها لون وسرعة، وبتمشي وتقف)."}
                ]
            },
            {
                "name": "OOP Principles",
                "questions": [
                    {"type": "mcq", "q": "Which OOP principle focuses on hiding internal details and showing only essential features?", "opts": ["A) Encapsulation", "B) Abstraction", "C) Inheritance", "D) Polymorphism"], "a": "B) Abstraction", "eng": "Abstraction hides complex implementation details and exposes only the necessary interface.", "ar": "التجريد (Abstraction) هو إنك تخفي التفاصيل المعقدة وتظهر بس الحاجات اللي اليوزر محتاجها (زي سواقة العربية من غير ما تعرف الموتور شغال إزاي)."},
                    {"type": "mcq", "q": "Wrapping data and functions into a single unit (class) is known as:", "opts": ["A) Polymorphism", "B) Inheritance", "C) Encapsulation", "D) Modularity"], "a": "C) Encapsulation", "eng": "Encapsulation binds data and the methods that manipulate that data together, preventing outside interference.", "ar": "الكبسلة (Encapsulation) هي إننا نجمع البيانات والدوال اللي بتتعامل معاها جوه كبسولة واحدة (Class) ونحميها من التعديل العشوائي."},
                    {"type": "tf", "q": "Polymorphism allows a single function to behave differently based on the object that calls it.", "a": "True", "eng": "This is the essence of polymorphism (many forms), commonly achieved via virtual functions (method overriding).", "ar": "صح. البولي مورفيزم (تعدد الأوجه) بيخلي نفس الدالة تعمل حاجات مختلفة على حسب الأوبجيكت اللي بيناديها."},
                    {"type": "mcq", "q": "Which principle is primarily associated with 'IS-A' relationship?", "opts": ["A) Inheritance", "B) Encapsulation", "C) Polymorphism", "D) Abstraction"], "a": "A) Inheritance", "eng": "Inheritance defines an 'is-a' relationship (e.g., A Dog IS-A Animal).", "ar": "الوراثة بتمثل علاقة (هو عبارة عن)، يعني الكلب (هو عبارة عن) حيوان فبيورث منه الخصائص."},
                    {"type": "tf", "q": "Encapsulation is achieved in C++ primarily through access modifiers like private and protected.", "a": "True", "eng": "By making data members private, we restrict direct access and enforce encapsulation.", "ar": "صح. الكبسلة بنعملها عن طريق إننا نخلي المتغيرات private، ومحدش يقدر يعدل فيها إلا من خلال الـ Setter و الـ Getter."}
                ]
            },
            {
                "name": "Benefits of OOP",
                "questions": [
                    {"type": "mcq", "q": "Which of the following is a direct advantage of Inheritance?", "opts": ["A) Data hiding", "B) Code Reusability", "C) Faster execution", "D) Memory optimization"], "a": "B) Code Reusability", "eng": "Inheritance allows a new class to reuse properties and methods of an existing class, reducing duplicate code.", "ar": "الوراثة (Inheritance) ميزتها الأساسية إنها بتمنع تكرار الكود، يعني بنعيد استخدام كود الأب في الابن (Code Reusability)."},
                    {"type": "tf", "q": "OOP makes software maintenance and troubleshooting harder because of its complex structure.", "a": "False", "eng": "OOP actually makes maintenance easier because objects are self-contained and modular. Bugs are easier to isolate.", "ar": "غلط تماماً. الـ OOP بتسهل الصيانة جداً لإن كل حاجة متقسمة لـ Objects، فلو فيه مشكلة في حاجة معينة بنروح للـ Class بتاعها ونصلحها من غير ما نأثر على باقي الكود."},
                    {"type": "mcq", "q": "How does Encapsulation benefit the security of an application?", "opts": ["A) It encrypts the source code.", "B) It prevents unauthorized components from modifying internal object data.", "C) It stops hackers from downloading the program.", "D) It makes the program password protected."], "a": "B) It prevents unauthorized components from modifying internal object data.", "eng": "By hiding data behind private access modifiers, it prevents accidental or malicious corruption of the object's state from outside the class.", "ar": "الكبسلة بتحمي البيانات الداخلية من إن أي جزء تاني في الكود يبوظها بالغلط أو يغيرها بدون قصد، وده بيخلي الكود آمن وقوي."}
                ]
            },
            {
                "name": "UML Design",
                "questions": [
                    {"type": "mcq", "q": "In a UML Class Diagram, the three main compartments of a class box represent:", "opts": ["A) Class Name, Methods, Subclasses", "B) Class Name, Attributes, Operations (Methods)", "C) Attributes, Methods, Access Modifiers", "D) Class Name, Variables, Data Types"], "a": "B) Class Name, Attributes, Operations (Methods)", "eng": "A standard UML class box has three parts: Top (Name), Middle (Attributes/Variables), Bottom (Operations/Methods).", "ar": "صندوق الـ UML بيتقسم لـ 3 أجزاء: فوق اسم الكلاس، في النص المتغيرات (Attributes)، وتحت الدوال (Operations)."},
                    {"type": "uml", "q": "Convert this simple UML to a class outline.", "uml": "Student\\n-------------------\\n- id: int\\n- gpa: double\\n-------------------\\n+ printDetails(): void", "ans": "class Student {\\nprivate:\\n    int id;\\n    double gpa;\\npublic:\\n    void printDetails();\\n};", "eng": "Minus (-) means private, plus (+) means public.", "ar": "الناقص معناه private والزائد معناه public، وبنعكس ترتيب الاسم والنوع في الـ C++."},
                    {"type": "uml", "q": "Convert this UML containing a constructor and a static member.", "uml": "Bank\\n-------------------\\n- balance: float\\n- static totalAccounts: int\\n-------------------\\n+ Bank(b: float)\\n+ getTotal(): int", "ans": "class Bank {\\nprivate:\\n    float balance;\\n    static int totalAccounts;\\npublic:\\n    Bank(float b);\\n    int getTotal();\\n};", "eng": "Static variables are simply prefixed with the `static` keyword in C++.", "ar": "الكلمة static بتنزل زي ما هي قبل نوع المتغير، والـ Constructor بيكون دالة ليها نفس اسم الكلاس من غير Return type."}
                ]
            }
        ]
    },
    {
        "topic": "2. Objects & Classes",
        "subtopics": [
            {
                "name": "Access Modifiers (Visibility Mode)",
                "questions": [
                    {"type": "mcq", "q": "Which access modifier allows members to be accessed by derived classes but NOT by external code?", "opts": ["A) public", "B) private", "C) protected", "D) default"], "a": "C) protected", "eng": "Protected members are hidden from the outside world but fully accessible to child classes.", "ar": "الـ protected بيقفل الباب قدام أي حد من بره (زي الـ private)، بس بيسمح للأبناء (الورثة) إنهم يستخدموا البيانات دي."},
                    {"type": "tf", "q": "If no access modifier is specified in a `class`, members are public by default.", "a": "False", "eng": "In C++, `class` members are `private` by default, whereas `struct` members are `public` by default.", "ar": "غلط. في الكلاس لو مكتبتش حاجة الكومبايلر بيعتبر كل حاجة private، لكن في الـ struct بيعتبرها public."}
                ]
            },
            {
                "name": "Constructor (Default vs. Parameterized vs. Copy)",
                "questions": [
                    {"type": "mcq", "q": "When is a Copy Constructor called?", "opts": ["A) When an object is passed by reference.", "B) When an object is returned by reference.", "C) When a new object is initialized with an existing object.", "D) When an object goes out of scope."], "a": "C) When a new object is initialized with an existing object.", "eng": "It is invoked in cases like: `MyClass obj2 = obj1;` or when passing by value.", "ar": "الـ Copy Constructor بيشتغل لما تيجي تعمل أوبجيكت جديد وتنسخ فيه داتا بتاعت أوبجيكت قديم (عشان كده اسمه Copy)."},
                    {"type": "tf", "q": "A class must always explicitly define a default constructor, otherwise you cannot create any objects.", "a": "False", "eng": "If you define NO constructors at all, the compiler automatically provides a default one.", "ar": "غلط. لو مكتبتش أي Constructor خالص، الكومبايلر طيب وبيعملك واحد Default ببلاش. لكن لو كتبت واحد بـ Parameters، هنا الكومبايلر بيسحب إيده ولازم أنت تكتب الـ Default بنفسك لو محتاجه."},
                    {"type": "mcq", "q": "Which of the following is the correct signature for a Copy Constructor in class `Test`?", "opts": ["A) Test(Test obj);", "B) Test(const Test& obj);", "C) Test(Test* obj);", "D) void Test(Test& obj);"], "a": "B) Test(const Test& obj);", "eng": "It must take a reference (usually const) to an object of the same class. If passed by value, it would cause an infinite recursive loop.", "ar": "لازم الـ Copy Constructor ياخد Parameter من نوع Reference (&)، لإن لو أخد Object عادي هيحتاج ينسخه، وعشان ينسخه هينادي الـ Copy Constructor تاني، وندخل في Loop مبيخلصش (Infinite Recursion)."},
                    {"type": "tf", "q": "If you define a Parameterized constructor, the compiler will still provide a free Default constructor.", "a": "False", "eng": "Once you define ANY constructor, the compiler steps back and assumes you are fully controlling the object creation.", "ar": "غلط. بمجرد ما بتكتب أي Constructor بإيدك (حتى لو بـ parameters)، الكومبايلر بيبطل يساعدك ومبيعملش الـ Default، لازم إنت تكتبه بنفسك لو عاوزه."}
                ]
            },
            {
                "name": "Destructor",
                "questions": [
                    {"type": "mcq", "q": "Which of the following is true regarding destructors?", "opts": ["A) They can take arguments.", "B) They can be overloaded.", "C) They are called automatically when an object goes out of scope.", "D) They return a boolean value indicating success."], "a": "C) They are called automatically when an object goes out of scope.", "eng": "Destructors cannot take arguments, cannot be overloaded, return nothing, and execute automatically upon object destruction.", "ar": "الـ Destructor بيشتغل أوتوماتيك أول ما الأوبجيكت يموت (يخرج بره الأقواس بتاعته). ومينفعش ياخد Parameters ولا يتعمله Overload."},
                    {"type": "tf", "q": "You must manually call the destructor like `obj.~MyClass();` to free memory.", "a": "False", "eng": "You almost never call a destructor manually. For stack objects, it's automatic. For heap objects, calling `delete obj;` automatically calls the destructor.", "ar": "غلط. إنت مبتناديش الـ Destructor بإيدك خالص. لو الأوبجيكت في الـ Stack بيتمسح لوحده، ولو في الـ Heap بتعمل delete وهو بينادي الـ Destructor لوحده."},
                    {"type": "tf", "q": "A class can have multiple destructors if they have different parameter lists.", "a": "False", "eng": "A destructor takes no parameters, so it is impossible to overload it. A class can only have one destructor.", "ar": "غلط تماماً. الـ Destructor مبياخدش أي parameters أصلاً، فمستحيل نعمله Overload، وكل كلاس ليه Destructor واحد بس."}
                ]
            },
            {
                "name": "Setter & Getter (Mutators & Accessors)",
                "questions": [
                    {"type": "tf", "q": "Setters are typically `void` functions, while Getters return the data type of the member variable.", "a": "True", "eng": "Setters update a value and don't return anything. Getters retrieve a value, so they must return it.", "ar": "صح. الـ Setter وظيفته يغير القيمة فغالباً بيكون void، لكن الـ Getter وظيفته يرجع القيمة فلازم يكون ليه Return Type زي نوع المتغير."},
                    {"type": "mcq", "q": "Why do we use Setters instead of making variables public?", "opts": ["A) To make the code run faster.", "B) To validate data before assigning it to the variable.", "C) Because the compiler forces us to.", "D) To increase the file size."], "a": "B) To validate data before assigning it to the variable.", "eng": "Setters allow you to add validation logic (like ensuring age > 0) before modifying the private variable.", "ar": "عشان الـ Setter بيخلينا نحط شروط على البيانات قبل ما تتسجل (زي إن العمر ميكونش بالسالب)، وده بيحمي الأوبجيكت من القيم الغلط."}
                ]
            },
            {
                "name": "Inline vs. Regular member functions",
                "questions": [
                    {"type": "mcq", "q": "What is the primary trade-off when using `inline` functions?", "opts": ["A) Faster execution but larger executable size.", "B) Slower execution but smaller executable size.", "C) Memory leaks.", "D) Inability to access private members."], "a": "A) Faster execution but larger executable size.", "eng": "Inline functions avoid function call overhead (faster) by replacing the call with the actual code (which increases the overall code size).", "ar": "الـ inline بيخلي البرنامج أسرع لإنه بيلغي وقت استدعاء الدالة، بس في المقابل بيكبر حجم ملف البرنامج النهائي (Executable) لإنه بيكرر كود الدالة في كل مكان اتنادت فيه."},
                    {"type": "tf", "q": "A member function defined completely inside the class declaration is automatically treated as inline.", "a": "True", "eng": "Implicit inline: Any method defined within the class body is treated by the compiler as an inline request.", "ar": "صح. لو كتبت الكود بتاع الدالة كله جوه الكلاس، الكومبايلر بيعتبرها inline من غير ما إنت تكتب الكلمة دي أصلاً."},
                    {"type": "tf", "q": "If you write the `inline` keyword, the compiler is FORCED to make the function inline regardless of its size.", "a": "False", "eng": "The `inline` keyword is only a REQUEST to the compiler. If the function is too large or contains loops/recursion, the compiler will ignore it.", "ar": "غلط. كلمة inline دي مجرد (طلب) للكومبايلر مش (أمر). لو الدالة كانت كبيرة أو فيها Loops أو Recursion، الكومبايلر هيرفض الطلب وهيعتبرها دالة عادية."}
                ]
            },
            {
                "name": "Objects as arguments & Returning objects",
                "questions": [
                    {"type": "mcq", "q": "To prevent an object from being copied when passed to a function, but also ensure the function cannot modify it, how should it be passed?", "opts": ["A) Pass by value", "B) Pass by reference", "C) Pass by const reference (`const ClassName& obj`)", "D) Pass by pointer"], "a": "C) Pass by const reference (`const ClassName& obj`)", "eng": "Passing by reference avoids the copy overhead. Adding `const` guarantees the function won't alter the object.", "ar": "عشان نوفر وقت الميموري ومنعملش نسخة، بنبعته بـ Reference (&)، وعشان نأمن الأوبجيكت الأصلي إن الدالة متعدلش فيه، بنحط كلمة const."},
                    {"type": "tf", "q": "When a function returns an object by value, a temporary object is created to hold the return value.", "a": "True", "eng": "A temporary copy is made using the Copy Constructor to transfer the local object out of the function scope safely.", "ar": "صح. الكومبايلر بيعمل نسخة مؤقتة من الأوبجيكت اللي الدالة هترجعه عشان يبعته للمكان اللي نادى الدالة، وبعدين بيمسح الأوبجيكت الداخلي."},
                    {"type": "mcq", "q": "If you pass an object by value to a function, which constructor is called?", "opts": ["A) Default Constructor", "B) Parameterized Constructor", "C) Copy Constructor", "D) No constructor is called"], "a": "C) Copy Constructor", "eng": "Passing by value means making a copy. The Copy Constructor is responsible for creating this new copy.", "ar": "طالما بعتناه By Value يبقى الكومبايلر هياخد منه نسخة، والمسئول عن أخد النسخ هو الـ Copy Constructor."}
                ]
            },
            {
                "name": "Static class data & Constant members",
                "questions": [
                    {"type": "mcq", "q": "A static data member belongs to:", "opts": ["A) The object that modified it first.", "B) The class itself, shared by all objects.", "C) The global namespace.", "D) The main function."], "a": "B) The class itself, shared by all objects.", "eng": "Static members are class-level variables. There is only one copy of them regardless of how many objects are instantiated.", "ar": "المتغير الـ Static مِلك للكلاس كله مش بتاع أوبجيكت معين. يعني هو نسخة واحدة بس مشتركة، لو أوبجيكت عدله، التعديل هيسمع عند الباقيين كلهم."},
                    {"type": "mcq", "q": "Can a constant member function modify a static data member?", "opts": ["A) Yes, always.", "B) No, it cannot modify any variables.", "C) Only if the static variable is also const.", "D) It causes a syntax error."], "a": "A) Yes, always.", "eng": "A `const` member function guarantees not to modify the *instance* variables. Static variables belong to the class, not the instance.", "ar": "المعلومة دي خبيثة شوية! الدالة الـ const بتوعد الكومبايلر إنها مش هتغير بيانات الأوبجيكت، لكن المتغير الـ Static مش بتاع الأوبجيكت أصلاً، فتقدر تغيره عادي جداً."},
                    {"type": "tf", "q": "A const object can call non-const member functions as long as they don't actually change any variables.", "a": "False", "eng": "The compiler does not analyze the body of the function. It strictly prohibits a const object from calling ANY function not explicitly marked with `const`.", "ar": "غلط. الكومبايلر مبيقرأش النوايا! طالما الأوبجيكت const، مش هيسمحلك تنادي أي دالة إلا لو كان مكتوب جنبها صراحةً كلمة const."},
                    {"type": "tf", "q": "Static member variables must be initialized inside the class declaration.", "a": "False", "eng": "Static members must be defined and initialized OUTSIDE the class declaration (e.g., `int MyClass::count = 0;`).", "ar": "غلط. المتغير الـ static لازم ياخد قيمته المبدئية (Initialize) بره الكلاس خالص، مينفعش تديله قيمة جواه."}
                ]
            },
            {
                "name": "Arrays of objects",
                "questions": [
                    {"type": "mcq", "q": "When declaring `Point p[5];`, what is strictly required in the `Point` class?", "opts": ["A) A copy constructor", "B) A parameterized constructor", "C) A default constructor", "D) A destructor"], "a": "C) A default constructor", "eng": "Array instantiation without explicit initializers requires the default constructor to construct each element.", "ar": "عشان تعمل مصفوفة أوبجيكتس فاضية، الكومبايلر بيحتاج Default Constructor عشان يناديه لكل عنصر يبنيه. لو مش موجود هيطلع error."},
                    {"type": "tf", "q": "If you create an array of 10 objects, the destructor will be called exactly once when the array goes out of scope.", "a": "False", "eng": "The destructor is called once for EACH object in the array (so 10 times in total).", "ar": "غلط. زي ما الـ Constructor اشتغل لكل عنصر لوحده عشان يتبني، الـ Destructor هيشتغل 10 مرات بردو عشان يمسح كل عنصر لوحده."}
                ]
            }
        ]
    },
    {
        "topic": "3. Memory Management",
        "subtopics": [
            {
                "name": "Dynamic vs Static Memory & Stack vs Heap",
                "questions": [
                    {"type": "mcq", "q": "Dynamic memory allocation occurs at:", "opts": ["A) Compile-time on the Stack", "B) Compile-time on the Heap", "C) Run-time on the Stack", "D) Run-time on the Heap"], "a": "D) Run-time on the Heap", "eng": "Dynamic allocation (using `new` or `malloc`) happens while the program is running, and the memory comes from the Heap.", "ar": "الحجز الديناميكي (بكلمة new) بيحصل والبرنامج شغال (Run-time) وبيحجز المساحة في منطقة الـ Heap."},
                    {"type": "tf", "q": "Local variables declared inside a function are stored on the Heap.", "a": "False", "eng": "Local variables are stored on the Stack, and they are automatically destroyed when the function exits.", "ar": "غلط. المتغيرات المحلية بتتحط في الـ Stack، وبتتمسح لوحدها أول ما الدالة تخلص."},
                    {"type": "mcq", "q": "Which memory region is manually managed by the programmer?", "opts": ["A) Stack", "B) Heap", "C) Data Segment", "D) Code Segment"], "a": "B) Heap", "eng": "The Heap requires the programmer to explicitly allocate (`new`) and deallocate (`delete`) memory.", "ar": "الـ Heap هو المكان الوحيد اللي إنت كـ مبرمج مسؤول عنه، تحجز بـ new وتمسح بـ delete بإيدك."}
                ]
            },
            {
                "name": "Dynamic Arrays & Deletion",
                "questions": [
                    {"type": "tf", "q": "Using `delete arr;` instead of `delete[] arr;` for a dynamic array causes a syntax error at compile time.", "a": "False", "eng": "It will compile fine, but at run-time, it will only destruct the first element, causing a Memory Leak (undefined behavior).", "ar": "غلط. الكومبايلر مش هيطلع إيرور وهيشغل البرنامج عادي، بس المشكلة هتحصل وقت التشغيل إن أول عنصر بس اللي هيتمسح والباقي هيعمل Memory Leak."},
                    {"type": "mcq", "q": "Which code correctly creates a dynamic array of 10 integers?", "opts": ["A) int arr = new int(10);", "B) int* arr = new int[10];", "C) int arr[10] = new int;", "D) int* arr = new int(10);"], "a": "B) int* arr = new int[10];", "eng": "Dynamic arrays are created using a pointer and the `new` operator followed by the type and square brackets.", "ar": "بنعمل بوينتر ونساويه بـ new واسم النوع وبعده الأقواس المربعة [ ] اللي جواها الحجم."}
                ]
            },
            {
                "name": "Memory Problems (Stack Overflow/Dangling Pointers)",
                "questions": [
                    {"type": "mcq", "q": "A dangling pointer occurs when:", "opts": ["A) A pointer points to NULL.", "B) A pointer is not initialized.", "C) A pointer points to memory that has been deallocated.", "D) Memory is allocated but never freed."], "a": "C) A pointer points to memory that has been deallocated.", "eng": "If you `delete p;`, `p` still holds the old address. It becomes a dangling pointer. (Memory allocated but never freed is a Memory Leak).", "ar": "الـ Dangling pointer هو بوينتر بيشاور على مكان إحنا خلاص عملناله delete. (أما إنك تحجز ميموري ومتمسحهاش ده اسمه Memory Leak)."},
                    {"type": "mcq", "q": "Which of the following causes a Stack Overflow?", "opts": ["A) Forgetting to delete dynamic memory.", "B) Creating a massive object on the Heap.", "C) Infinite or extremely deep recursion.", "D) Using uninitialized pointers."], "a": "C) Infinite or extremely deep recursion.", "eng": "The stack stores function call frames. Infinite recursion fills the stack up until it overflows.", "ar": "الـ Stack بتمتلي لما دالة تفضل تنادي نفسها لمالانهاية (Recursion)، فيحصل Stack Overflow والبرنامج يقفل."},
                    {"type": "tf", "q": "Setting a pointer to `nullptr` after deleting it is a good practice to prevent Dangling Pointers.", "a": "True", "eng": "Assigning `nullptr` ensures you don't accidentally access or double-delete the deallocated memory.", "ar": "صح جداً. أحسن طريقة عشان تتجنب الـ Dangling Pointer إنك بعد ما تعمل delete، تخلي البوينتر يساوي nullptr عشان تضمن إنه مبيشاورش على الهوا."}
                ]
            }
        ]
    },
    {
        "topic": "4. Inheritance",
        "subtopics": [
            {
                "name": "Types of Inheritance",
                "questions": [
                    {"type": "mcq", "q": "Which type of inheritance suffers from the 'Diamond Problem'?", "opts": ["A) Single", "B) Multi-level", "C) Multiple", "D) Hierarchical"], "a": "C) Multiple", "eng": "When a class inherits from two classes, and both of those inherit from a common base class, ambiguity arises (the Diamond Problem). C++ fixes this with `virtual` inheritance.", "ar": "مشكلة الـ Diamond Problem بتظهر في الوراثة المتعددة (Multiple) لما كلاس يورث من كلاسين، والاتنين الكلاسين دول بيورثوا من نفس الجد، فالكومبايلر بيحتار يجيب البيانات من أي طريق."},
                    {"type": "tf", "q": "Hierarchical inheritance is when multiple base classes are inherited by a single derived class.", "a": "False", "eng": "That describes Multiple Inheritance. Hierarchical inheritance is when ONE base class is inherited by MULTIPLE derived classes.", "ar": "غلط. الوراثة الهرمية هي إن أب واحد يورث لكذا ابن (زي الكلاس Shape يورث لـ Circle و Rectangle)."}
                ]
            },
            {
                "name": "Class access specification",
                "questions": [
                    {"type": "mcq", "q": "In `class Child : protected Parent`, what happens to the `public` members of `Parent`?", "opts": ["A) They remain public in Child.", "B) They become protected in Child.", "C) They become private in Child.", "D) They are inaccessible."], "a": "B) They become protected in Child.", "eng": "In protected inheritance, both public and protected members of the base class become protected in the derived class.", "ar": "في الوراثة الـ protected، أي حاجة public في الأب بتتحول وتبقى protected في الابن، وطبعاً الـ private بتاع الأب بيفضل مقفول."},
                    {"type": "mcq", "q": "What is the default inheritance mode if not specified?", "opts": ["A) public", "B) protected", "C) private", "D) internal"], "a": "C) private", "eng": "If you just write `class Child : Parent`, C++ makes it private inheritance by default.", "ar": "لو مكتبتش نوع الوراثة، الكومبايلر بيعتبرها Private Inheritance أوتوماتيك."},
                    {"type": "tf", "q": "A derived class can directly access the private members of its base class if it uses public inheritance.", "a": "False", "eng": "Private members of a base class are NEVER directly accessible by ANY derived class, regardless of the inheritance mode.", "ar": "غلط. الـ private بتاع الأب محرم على أي حد، حتى الابن ميقدرش يقرأه ولا يعدل فيه مباشرة، لازم يستخدم Getter و Setter."}
                ]
            },
            {
                "name": "Order of Inheritance (Constructors & Destructors)",
                "questions": [
                    {"type": "tf", "q": "When a derived class object is created, the derived class constructor executes its body BEFORE the base class constructor executes.", "a": "False", "eng": "Base class constructor always executes FIRST, then the derived class constructor. You must lay the foundation before building the roof.", "ar": "غلط. الأب بيتبني الأول وبعدين الابن (الأساس قبل الدور اللي فوقه). فجسم الـ Constructor بتاع الأب بيتنفذ الأول."},
                    {"type": "mcq", "q": "If C inherits from B, and B inherits from A. What is the order of Destructors when an object of C is destroyed?", "opts": ["A) A -> B -> C", "B) C -> B -> A", "C) A -> C -> B", "D) Destructors run concurrently"], "a": "B) C -> B -> A", "eng": "Destruction is always the exact reverse of construction. Construction is A->B->C, so destruction is C->B->A.", "ar": "الهدد عكس البناء. إحنا بنينا الأب وبعدين الابن، يبقى في الهدد بنشيل الحفيد الأول C، وبعدين الأب B، وبعدين الجد A."}
                ]
            }
        ]
    },
    {
        "topic": "5. Polymorphism",
        "subtopics": [
            {
                "name": "Virtual functions vs. non-virtual functions",
                "questions": [
                    {"type": "tf", "q": "Without the `virtual` keyword, a base class pointer pointing to a derived object will call the derived class's overridden method.", "a": "False", "eng": "Without `virtual`, the compiler uses Early Binding and calls the method based on the pointer's type (Base), not the actual object type (Derived).", "ar": "غلط. لو مكتبتش virtual، الكومبايلر هيبص على نوع البوينتر (اللي هو الأب) وهينادي دالة الأب. الـ virtual هي اللي بتخليه يستنى للـ Run-time وينادي دالة الابن."},
                    {"type": "mcq", "q": "What is Late Binding?", "opts": ["A) Linking functions at compile time.", "B) Determining which virtual function to call during program execution (run-time).", "C) Forgetting to link external libraries.", "D) Declaring variables at the end of the file."], "a": "B) Determining which virtual function to call during program execution (run-time).", "eng": "Late binding (or dynamic binding) happens at run-time, which is how virtual functions achieve polymorphism.", "ar": "الـ Late Binding هو إن الكومبايلر يأجل قراره لحد ما البرنامج يشتغل عشان يشوف البوينتر بيشاور على أنهي أوبجيكت بالضبط وينادي الدالة بتاعته."}
                ]
            },
            {
                "name": "Abstract class",
                "questions": [
                    {"type": "mcq", "q": "A class with at least one Pure Virtual Function is called:", "opts": ["A) A concrete class", "B) An abstract class", "C) A static class", "D) A polymorphic class"], "a": "B) An abstract class", "eng": "A pure virtual function (`virtual void f() = 0;`) makes the class abstract, meaning you cannot create objects of it.", "ar": "مجرد ما الكلاس يكون جواه دالة واحدة Pure Virtual (بتساوي صفر)، بيتحول لـ Abstract Class ومتقدرش تعمل منه أوبجيكت."},
                    {"type": "tf", "q": "You can instantiate (create objects of) an Abstract Class as long as you use a pointer.", "a": "False", "eng": "You can create POINTERS of an Abstract Class (like `Shape* s`), but you cannot instantiate it (no `new Shape()` or `Shape s;`).", "ar": "غلط. مستحيل تعمل أوبجيكت من Abstract Class. إنت تقدر تعمل بوينتر منه بس عشان تخليه يشاور على الأبناء."}
                ]
            },
            {
                "name": "Function Overloading & Overriding",
                "questions": [
                    {"type": "tf", "q": "Function overloading is an example of Run-time Polymorphism.", "a": "False", "eng": "Function overloading is Compile-time (Static) Polymorphism. The compiler knows exactly which function to call based on the arguments.", "ar": "غلط. الـ Overloading بيتحل وقت الـ Compile-time لأن الكومبايلر بيعرف الدالة المطلوبة من عدد وأنواع الـ Parameters."},
                    {"type": "mcq", "q": "Which of the following is NOT valid for function overloading?", "opts": ["A) Changing the number of parameters.", "B) Changing the data types of parameters.", "C) Changing the order of parameters.", "D) Only changing the return type."], "a": "D) Only changing the return type.", "eng": "To overload a function, the parameter list MUST be different. Changing only the return type causes a compilation error.", "ar": "عشان تعمل Overload لازم تغير الـ Parameters (العدد أو النوع). لو غيرت الـ Return Type بس الكومبايلر هيعتبره إيرور ومش هيقبله."},
                    {"type": "mcq", "q": "What is the key difference between Overloading and Overriding?", "opts": ["A) Overriding happens in the same class, overloading happens in derived classes.", "B) Overloading happens in the same class, overriding requires inheritance.", "C) There is no difference.", "D) Overriding changes the return type only."], "a": "B) Overloading happens in the same class, overriding requires inheritance.", "eng": "Overloading uses the same function name with different parameters in the same scope. Overriding redefines a base class virtual function in a derived class with the EXACT same signature.", "ar": "الـ Overloading بيحصل في نفس الكلاس (نفس اسم الدالة بس parameters مختلفة)، أما الـ Overriding بيحصل في الوراثة (الابن بيعدل على دالة الأب بنفس شكلها بالضبط)."}
                ]
            }
        ]
    }
]

content = ""
q_idx = 1
for topic in db:
    content += f'<h2 class="topic-title">{topic["topic"]}</h2>\\n'
    for sub in topic["subtopics"]:
        content += f'<h3 class="subtopic-title">📌 {sub["name"]}</h3>\\n'
        for q in sub["questions"]:
            if q["type"] == "mcq":
                opts_html = "\\n".join([f"                <li>{opt}</li>" for opt in q["opts"]])
                content += f"""
        <div class="code-analysis-section">
            <h4 class="question-text" dir="ltr">Q{q_idx}. {q['q']}</h4>
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
                uml_text = q['uml'].replace('\\n', '<br>')
                ans_text = q['ans'].replace('\\n', '<br>')
                content += f"""
        <div class="code-analysis-section">
            <h4 class="question-text" dir="ltr" style="color: #c084fc;">Q{q_idx}. {q['q']}</h4>
            <div class="uml-box">
                {uml_text}
            </div>
            <details class="essay-answer">
                <summary class="reveal-answer" style="background:#a855f7;">👁️ إظهار الإجابة والتفسير</summary>
                <div class="answer-content">
                    <strong style="color:#e2e8f0;">Answer:</strong>
                    <div style="background:#0f172a; padding: 15px; border-left: 4px solid #10b981; border-radius: 6px; font-family: monospace; color: #a7f3d0; margin-top:10px; margin-bottom: 15px;" dir="ltr">
                        {ans_text}
                    </div>
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

# Update index.html to include the Mega Question Bank card
index_card_html = """
            <!-- MEGA QUESTION BANK SECTION -->
            <div class="lecture-card" style="margin-top: 2rem; border-color: #38bdf8; box-shadow: 0 0 25px rgba(56, 189, 248, 0.3); background: linear-gradient(180deg, #1e293b, #0f172a);" data-lecture="mega">
                <h2 style="color: #38bdf8; text-align: center; font-size: 2rem; margin-bottom: 15px; text-shadow: 0 0 10px rgba(56,189,248,0.5);">🚀 بنك الأسئلة المكثف (Mega Bank)</h2>
                <p style="text-align: center; color: #cbd5e1; margin-bottom: 25px; font-size: 1.1rem; line-height: 1.6;">تجميعة ضخمة جداً من أسئلة الـ MCQ و True/False و UML بتغطي كل تفصيلة في المنهج، مع شرح الإجابات بالعامية لتثبيت المعلومة.</p>
                <div style="display: flex; justify-content: center;">
                    <a href="mega_question_bank.html" class="btn" style="background: linear-gradient(135deg, #0284c7, #0369a1); box-shadow: 0 6px 20px rgba(2, 132, 199, 0.5); padding: 1.2rem 3.5rem; font-size: 1.3rem; border-radius: 50px;">افتح بنك الأسئلة الشامل 💡</a>
                </div>
            </div>
"""

for base in file_paths:
    index_path = os.path.join(base, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # We'll insert it right after the LAB SHEETS SECTION or FINAL EXAM SECTION.
        # Let's insert it before the closing </main> tag.
        if "mega_question_bank.html" not in content:
            main_end_idx = content.find("</main>")
            if main_end_idx != -1:
                new_content = content[:main_end_idx] + index_card_html + "\n        " + content[main_end_idx:]
                with open(index_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

print("Mega Question Bank updated and linked to index.html successfully!")
