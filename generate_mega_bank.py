import re
import os
import copy

# 1. Clean up final_exam.html in both locations
file_paths = [
    r"c:\Users\HP\OneDrive\Desktop\namoly\final_exam.html",
    r"c:\Users\HP\OneDrive\Desktop\oop-portal-test\final_exam.html"
]
for path in file_paths:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Remove the section starting with <!-- القسم السادس:
        # and ending before </script> but wait, the section was injected inside the container.
        # Let's find <!-- القسم السادس: and remove until the last </div> before <script src="app.js">
        match = re.search(r'<!-- القسم السادس:.*?</div>\s*</div>', content, flags=re.DOTALL)
        if match:
            # wait, the regex might be greedy or not greedy enough.
            # let's just do a string split
            start_marker = "<!-- القسم السادس:"
            if start_marker in content:
                start_idx = content.find(start_marker)
                # Find the next closing div of the container which is followed by script
                script_idx = content.find('<script src="app.js"></script>', start_idx)
                if script_idx != -1:
                    last_div_idx = content.rfind('</div>', start_idx, script_idx)
                    if last_div_idx != -1:
                        content = content[:start_idx] + "\n    " + content[last_div_idx:]
                        with open(path, "w", encoding="utf-8") as f:
                            f.write(content)

# Now, generate mega_bank.html
html_template = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بنك الأسئلة الشامل الشامل - موسوعة الـ OOP</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <style>
        .exam-header {
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.05));
            border-bottom: 1px solid rgba(16, 185, 129, 0.2);
            margin-bottom: 2rem;
            border-radius: 0 0 20px 20px;
        }
        .exam-header h1 {
            color: #10b981;
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        .exam-header p {
            color: #d1d5db;
            font-size: 1.2rem;
        }
        #particles-js {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: 0;
        }
        .container { position: relative; z-index: 1; }
        .header-nav { position: sticky; z-index: 100; }
        .topic-title {
            color: #60a5fa;
            border-bottom: 2px solid #3b82f6;
            padding-bottom: 10px;
            margin-top: 4rem;
            font-size: 1.8rem;
        }
        .subtopic-title {
            color: #a78bfa;
            margin-top: 2rem;
            font-size: 1.4rem;
        }
        .code-analysis-section {
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        .code-analysis-section h3 {
            color: #fcd34d;
            margin-bottom: 1rem;
        }
        .essay-answer { margin-top: 1rem; }
    </style>
</head>
<body>
    <div id="particles-js"></div>
    <header class="header-nav">
        <a href="final_exam.html" class="back-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
            الرجوع للامتحان الشامل (Back to Exam)
        </a>
        <h2 style="margin:0; font-size: 1.2rem;">Mega Question Bank</h2>
    </header>

    <div class="container">
        <div class="exam-header">
            <h1>🚀 بنك الأسئلة المكثف للفاينال 🚀</h1>
            <p>مئات الأسئلة المتدرجة (Choose, True/False, UML) تغطي كل حرف في المنهج</p>
        </div>
        
        {content}

    </div>

    <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            particlesJS('particles-js', {
              "particles": {
                "number": { "value": 80, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#10b981" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.5 },
                "size": { "value": 3 },
                "line_linked": { "enable": true, "distance": 150, "color": "#10b981", "opacity": 0.4, "width": 1 },
                "move": { "enable": true, "speed": 2 }
              }
            });
        });
    </script>
</body>
</html>
"""

# Now we define a massive dict of topics -> subtopics -> list of questions
db = [
    {
        "topic": "1. Introduction to OOP",
        "subtopics": [
            {
                "name": "Why do we use OOP and what is OOP",
                "questions": [
                    {"type": "tf", "q": "OOP is mainly used to write code line-by-line without organizing it into structures.", "a": "False", "eng": "Procedural programming does this. OOP organizes code into objects representing real-world entities.", "ar": "البرمجة الإجرائية هي اللي بتكتب سطر سطر، لكن الـ OOP معمولة عشان ننظم الكود في شكل كائنات (Objects) تشبه العالم الحقيقي."},
                    {"type": "mcq", "q": "Which of the following best describes an Object in OOP?", "opts": ["A) A simple variable", "B) A function", "C) An instance of a class", "D) A data type"], "a": "C) An instance of a class", "eng": "A class is a blueprint, and an object is a specific instance created from that blueprint.", "ar": "الأوبجيكت هو نسخة حقيقية (Instance) مبنية من التصميم اللي اسمه Class."},
                    {"type": "mcq", "q": "What problem did OOP primarily solve compared to Procedural Programming?", "opts": ["A) Slow execution speed", "B) Spaghetti code and lack of reusability in large systems", "C) Hardware limitations", "D) Inability to write math functions"], "a": "B) Spaghetti code and lack of reusability in large systems", "eng": "OOP was introduced to manage large, complex software by promoting modularity and reuse, preventing 'spaghetti code'.", "ar": "الـ OOP حلت مشكلة الكود المعقد اللي داخل في بعضه (Spaghetti code) في البرامج الكبيرة، وخليتنا نقدر نعيد استخدام الكود بسهولة."}
                ]
            },
            {
                "name": "OOP Principles",
                "questions": [
                    {"type": "mcq", "q": "Which OOP principle focuses on hiding internal details and showing only essential features?", "opts": ["A) Encapsulation", "B) Abstraction", "C) Inheritance", "D) Polymorphism"], "a": "B) Abstraction", "eng": "Abstraction hides complex implementation details and exposes only the necessary interface.", "ar": "التجريد (Abstraction) هو إنك تخفي التفاصيل المعقدة وتظهر بس الحاجات اللي اليوزر محتاجها (زي سواقة العربية من غير ما تعرف الموتور شغال إزاي)."},
                    {"type": "mcq", "q": "Wrapping data and functions into a single unit (class) is known as:", "opts": ["A) Polymorphism", "B) Inheritance", "C) Encapsulation", "D) Modularity"], "a": "C) Encapsulation", "eng": "Encapsulation binds data and the methods that manipulate that data together, preventing outside interference.", "ar": "الكبسلة (Encapsulation) هي إننا نجمع البيانات والدوال اللي بتتعامل معاها جوه كبسولة واحدة (Class) ونحميها من التعديل العشوائي."},
                    {"type": "tf", "q": "Polymorphism allows a single function to behave differently based on the object that calls it.", "a": "True", "eng": "This is the essence of polymorphism (many forms), commonly achieved via virtual functions (method overriding).", "ar": "صح. البولي مورفيزم (تعدد الأوجه) بيخلي نفس الدالة تعمل حاجات مختلفة على حسب الأوبجيكت اللي بيناديها."}
                ]
            },
            {
                "name": "Benefits of OOP",
                "questions": [
                    {"type": "mcq", "q": "Which of the following is a direct advantage of Inheritance?", "opts": ["A) Data hiding", "B) Code Reusability", "C) Faster execution", "D) Memory optimization"], "a": "B) Code Reusability", "eng": "Inheritance allows a new class to reuse properties and methods of an existing class, reducing duplicate code.", "ar": "الوراثة (Inheritance) ميزتها الأساسية إنها بتمنع تكرار الكود، يعني بنعيد استخدام كود الأب في الابن (Code Reusability)."},
                    {"type": "tf", "q": "OOP makes software maintenance and troubleshooting harder because of its complex structure.", "a": "False", "eng": "OOP actually makes maintenance easier because objects are self-contained and modular. Bugs are easier to isolate.", "ar": "غلط تماماً. الـ OOP بتسهل الصيانة جداً لإن كل حاجة متقسمة لـ Objects، فلو فيه مشكلة في حاجة معينة بنروح للـ Class بتاعها ونصلحها من غير ما نأثر على باقي الكود."}
                ]
            },
            {
                "name": "UML Design",
                "questions": [
                    {"type": "mcq", "q": "In a UML Class Diagram, the three main compartments of a class box represent:", "opts": ["A) Class Name, Methods, Subclasses", "B) Class Name, Attributes, Operations (Methods)", "C) Attributes, Methods, Access Modifiers", "D) Class Name, Variables, Data Types"], "a": "B) Class Name, Attributes, Operations (Methods)", "eng": "A standard UML class box has three parts: Top (Name), Middle (Attributes/Variables), Bottom (Operations/Methods).", "ar": "صندوق الـ UML بيتقسم لـ 3 أجزاء: فوق اسم الكلاس، في النص المتغيرات (Attributes)، وتحت الدوال (Operations)."},
                    {"type": "uml", "q": "Convert this simple UML to a class outline.", "uml": "Student\n-------------------\n- id: int\n- gpa: double\n-------------------\n+ printDetails(): void", "ans": "class Student {\nprivate:\n    int id;\n    double gpa;\npublic:\n    void printDetails();\n};", "eng": "Minus (-) means private, plus (+) means public.", "ar": "الناقص معناه private والزائد معناه public، وبنعكس ترتيب الاسم والنوع في الـ C++."}
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
                    {"type": "mcq", "q": "Which of the following is the correct signature for a Copy Constructor in class `Test`?", "opts": ["A) Test(Test obj);", "B) Test(const Test& obj);", "C) Test(Test* obj);", "D) void Test(Test& obj);"], "a": "B) Test(const Test& obj);", "eng": "It must take a reference (usually const) to an object of the same class. If passed by value, it would cause an infinite recursive loop.", "ar": "لازم الـ Copy Constructor ياخد Parameter من نوع Reference (&)، لإن لو أخد Object عادي هيحتاج ينسخه، وعشان ينسخه هينادي الـ Copy Constructor تاني، وندخل في Loop مبيخلصش (Infinite Recursion)."}
                ]
            },
            {
                "name": "Destructor",
                "questions": [
                    {"type": "mcq", "q": "Which of the following is true regarding destructors?", "opts": ["A) They can take arguments.", "B) They can be overloaded.", "C) They are called automatically when an object goes out of scope.", "D) They return a boolean value indicating success."], "a": "C) They are called automatically when an object goes out of scope.", "eng": "Destructors cannot take arguments, cannot be overloaded, return nothing, and execute automatically upon object destruction.", "ar": "الـ Destructor بيشتغل أوتوماتيك أول ما الأوبجيكت يموت (يخرج بره الأقواس بتاعته). ومينفعش ياخد Parameters ولا يتعمله Overload."},
                    {"type": "tf", "q": "You must manually call the destructor like `obj.~MyClass();` to free memory.", "a": "False", "eng": "You almost never call a destructor manually. For stack objects, it's automatic. For heap objects, calling `delete obj;` automatically calls the destructor.", "ar": "غلط. إنت مبتناديش الـ Destructor بإيدك خالص. لو الأوبجيكت في الـ Stack بيتمسح لوحده، ولو في الـ Heap بتعمل delete وهو بينادي الـ Destructor لوحده."}
                ]
            },
            {
                "name": "Setter & Getter (Mutators & Accessors)",
                "questions": [
                    {"type": "tf", "q": "Setters are typically `void` functions, while Getters return the data type of the member variable.", "a": "True", "eng": "Setters update a value and don't return anything. Getters retrieve a value, so they must return it.", "ar": "صح. الـ Setter وظيفته يغير القيمة فغالباً بيكون void، لكن الـ Getter وظيفته يرجع القيمة فلازم يكون ليه Return Type زي نوع المتغير."}
                ]
            },
            {
                "name": "Inline vs. Regular member functions",
                "questions": [
                    {"type": "mcq", "q": "What is the primary trade-off when using `inline` functions?", "opts": ["A) Faster execution but larger executable size.", "B) Slower execution but smaller executable size.", "C) Memory leaks.", "D) Inability to access private members."], "a": "A) Faster execution but larger executable size.", "eng": "Inline functions avoid function call overhead (faster) by replacing the call with the actual code (which increases the overall code size).", "ar": "الـ inline بيخلي البرنامج أسرع لإنه بيلغي وقت استدعاء الدالة، بس في المقابل بيكبر حجم ملف البرنامج النهائي (Executable) لإنه بيكرر كود الدالة في كل مكان اتنادت فيه."},
                    {"type": "tf", "q": "A member function defined completely inside the class declaration is automatically treated as inline.", "a": "True", "eng": "Implicit inline: Any method defined within the class body is treated by the compiler as an inline request.", "ar": "صح. لو كتبت الكود بتاع الدالة كله جوه الكلاس، الكومبايلر بيعتبرها inline من غير ما إنت تكتب الكلمة دي أصلاً."}
                ]
            },
            {
                "name": "Objects as arguments",
                "questions": [
                    {"type": "mcq", "q": "To prevent an object from being copied when passed to a function, but also ensure the function cannot modify it, how should it be passed?", "opts": ["A) Pass by value", "B) Pass by reference", "C) Pass by const reference (`const ClassName& obj`)", "D) Pass by pointer"], "a": "C) Pass by const reference (`const ClassName& obj`)", "eng": "Passing by reference avoids the copy overhead. Adding `const` guarantees the function won't alter the object.", "ar": "عشان نوفر وقت الميموري ومنعملش نسخة، بنبعته بـ Reference (&)، وعشان نأمن الأوبجيكت الأصلي إن الدالة متعدلش فيه، بنحط كلمة const."}
                ]
            },
            {
                "name": "Returning objects from functions",
                "questions": [
                    {"type": "tf", "q": "When a function returns an object by value, a temporary object is created to hold the return value.", "a": "True", "eng": "A temporary copy is made using the Copy Constructor to transfer the local object out of the function scope safely.", "ar": "صح. الكومبايلر بيعمل نسخة مؤقتة من الأوبجيكت اللي الدالة هترجعه عشان يبعته للمكان اللي نادى الدالة، وبعدين بيمسح الأوبجيكت الداخلي."}
                ]
            },
            {
                "name": "Classes & Objects & Memory",
                "questions": [
                    {"type": "tf", "q": "Memory for member functions is allocated repeatedly for every new object created.", "a": "False", "eng": "Only data members take up per-object memory. Member functions are stored once in the Code Segment and shared among all objects.", "ar": "غلط. الدوال (Functions) بتتخزن في الميموري مرة واحدة بس وكل الأوبجيكتس بتشترك فيها عشان نوفر مساحة. اللي بيتكرر لكل أوبجيكت هو البيانات (Variables) بس."}
                ]
            },
            {
                "name": "Static class data",
                "questions": [
                    {"type": "mcq", "q": "A static data member belongs to:", "opts": ["A) The object that modified it first.", "B) The class itself, shared by all objects.", "C) The global namespace.", "D) The main function."], "a": "B) The class itself, shared by all objects.", "eng": "Static members are class-level variables. There is only one copy of them regardless of how many objects are instantiated.", "ar": "المتغير الـ Static مِلك للكلاس كله مش بتاع أوبجيكت معين. يعني هو نسخة واحدة بس مشتركة، لو أوبجيكت عدله، التعديل هيسمع عند الباقيين كلهم."}
                ]
            },
            {
                "name": "Constant member functions & objects",
                "questions": [
                    {"type": "mcq", "q": "Can a constant member function modify a static data member?", "opts": ["A) Yes, always.", "B) No, it cannot modify any variables.", "C) Only if the static variable is also const.", "D) It causes a syntax error."], "a": "A) Yes, always.", "eng": "A `const` member function guarantees not to modify the *instance* variables (the state of the object). Static variables belong to the class, not the instance, so `const` methods can modify them.", "ar": "المعلومة دي خبيثة شوية! الدالة الـ const بتوعد الكومبايلر إنها مش هتغير بيانات الأوبجيكت، لكن المتغير الـ Static مش بتاع الأوبجيكت أصلاً (ده بتاع الكلاس)، فتقدر تغيره عادي جداً."},
                    {"type": "tf", "q": "A const object can call non-const member functions as long as they don't actually change any variables.", "a": "False", "eng": "The compiler does not analyze the body of the function. It strictly prohibits a const object from calling ANY function not explicitly marked with `const`.", "ar": "غلط. الكومبايلر مبيقرأش النوايا! طالما الأوبجيكت const، مش هيسمحلك تنادي أي دالة إلا لو كان مكتوب جنبها صراحةً كلمة const."}
                ]
            },
            {
                "name": "Arrays of objects",
                "questions": [
                    {"type": "mcq", "q": "When declaring `Point p[5];`, what is strictly required in the `Point` class?", "opts": ["A) A copy constructor", "B) A parameterized constructor", "C) A default constructor", "D) A destructor"], "a": "C) A default constructor", "eng": "Array instantiation without explicit initializers requires the default constructor to construct each element.", "ar": "عشان تعمل مصفوفة أوبجيكتس فاضية، الكومبايلر بيحتاج Default Constructor عشان يناديه لكل عنصر يبنيه. لو مش موجود هيطلع error."}
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
                    {"type": "mcq", "q": "Dynamic memory allocation occurs at:", "opts": ["A) Compile-time on the Stack", "B) Compile-time on the Heap", "C) Run-time on the Stack", "D) Run-time on the Heap"], "a": "D) Run-time on the Heap", "eng": "Dynamic allocation (using `new` or `malloc`) happens while the program is running, and the memory comes from the Heap.", "ar": "الحجز الديناميكي (بكلمة new) بيحصل والبرنامج شغال (Run-time) وبيحجز المساحة في منطقة الـ Heap."}
                ]
            },
            {
                "name": "Dynamic Arrays & Deletion",
                "questions": [
                    {"type": "tf", "q": "Using `delete arr;` instead of `delete[] arr;` for a dynamic array causes a syntax error at compile time.", "a": "False", "eng": "It will compile fine, but at run-time, it will only destruct the first element, causing a Memory Leak (undefined behavior).", "ar": "غلط. الكومبايلر مش هيطلع إيرور وهيشغل البرنامج عادي، بس المشكلة هتحصل وقت التشغيل إن أول عنصر بس اللي هيتمسح والباقي هيعمل Memory Leak."}
                ]
            },
            {
                "name": "Memory Problems (Stack Overflow/Dangling Pointers)",
                "questions": [
                    {"type": "mcq", "q": "A dangling pointer occurs when:", "opts": ["A) A pointer points to NULL.", "B) A pointer is not initialized.", "C) A pointer points to memory that has been deallocated.", "D) Memory is allocated but never freed."], "a": "C) A pointer points to memory that has been deallocated.", "eng": "If you `delete p;`, `p` still holds the old address. It becomes a dangling pointer. (Memory allocated but never freed is a Memory Leak).", "ar": "الـ Dangling pointer هو بوينتر بيشاور على مكان إحنا خلاص عملناله delete. (أما إنك تحجز ميموري ومتمسحهاش ده اسمه Memory Leak)."}
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
                    {"type": "mcq", "q": "Which type of inheritance suffers from the 'Diamond Problem'?", "opts": ["A) Single", "B) Multi-level", "C) Multiple", "D) Hierarchical"], "a": "C) Multiple", "eng": "When a class inherits from two classes, and both of those inherit from a common base class, ambiguity arises (the Diamond Problem). C++ fixes this with `virtual` inheritance.", "ar": "مشكلة الـ Diamond Problem بتظهر في الوراثة المتعددة (Multiple) لما كلاس يورث من كلاسين، والاتنين الكلاسين دول بيورثوا من نفس الجد، فالكومبايلر بيحتار يجيب البيانات من أي طريق."}
                ]
            },
            {
                "name": "Class access specification",
                "questions": [
                    {"type": "mcq", "q": "In `class Child : protected Parent`, what happens to the `public` members of `Parent`?", "opts": ["A) They remain public in Child.", "B) They become protected in Child.", "C) They become private in Child.", "D) They are inaccessible."], "a": "B) They become protected in Child.", "eng": "In protected inheritance, both public and protected members of the base class become protected in the derived class.", "ar": "في الوراثة الـ protected، أي حاجة public في الأب بتتحول وتبقى protected في الابن، وطبعاً الـ private بتاع الأب بيفضل مقفول."}
                ]
            },
            {
                "name": "Order of Inheritance (Constructors & Destructors)",
                "questions": [
                    {"type": "tf", "q": "When a derived class object is created, the derived class constructor executes its body BEFORE the base class constructor executes.", "a": "False", "eng": "Base class constructor always executes FIRST, then the derived class constructor. You must lay the foundation before building the roof.", "ar": "غلط. الأب بيتبني الأول وبعدين الابن (الأساس قبل الدور اللي فوقه). فجسم الـ Constructor بتاع الأب بيتنفذ الأول."}
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
                    {"type": "tf", "q": "Without the `virtual` keyword, a base class pointer pointing to a derived object will call the derived class's overridden method.", "a": "False", "eng": "Without `virtual`, the compiler uses Early Binding and calls the method based on the pointer's type (Base), not the actual object type (Derived).", "ar": "غلط. لو مكتبتش virtual، الكومبايلر هيبص على نوع البوينتر (اللي هو الأب) وهينادي دالة الأب. الـ virtual هي اللي بتخليه يستنى للـ Run-time وينادي دالة الابن."}
                ]
            },
            {
                "name": "Abstract class",
                "questions": [
                    {"type": "mcq", "q": "A class with at least one Pure Virtual Function is called:", "opts": ["A) A concrete class", "B) An abstract class", "C) A static class", "D) A polymorphic class"], "a": "B) An abstract class", "eng": "A pure virtual function (`virtual void f() = 0;`) makes the class abstract, meaning you cannot create objects of it.", "ar": "مجرد ما الكلاس يكون جواه دالة واحدة Pure Virtual (بتساوي صفر)، بيتحول لـ Abstract Class ومتقدرش تعمل منه أوبجيكت."}
                ]
            },
            {
                "name": "Function Overloading",
                "questions": [
                    {"type": "tf", "q": "Function overloading is an example of Run-time Polymorphism.", "a": "False", "eng": "Function overloading is Compile-time (Static) Polymorphism. The compiler knows exactly which function to call based on the arguments.", "ar": "غلط. الـ Overloading بيتحل وقت الـ Compile-time لأن الكومبايلر بيعرف الدالة المطلوبة من عدد وأنواع الـ Parameters."}
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
            <h4 dir="ltr" style="color: #34d399; margin-bottom: 10px;">Q{q_idx}. {q['q']}</h4>
            <ol dir="ltr" style="text-align: left; margin-left: 20px; color: #e2e8f0; line-height: 1.8;">
{opts_html}
            </ol>
            <details class="essay-answer">
                <summary class="reveal-answer">👁️ إظهار الإجابة والتفسير</summary>
                <div class="answer-content">
                    <strong>Answer:</strong> <span style="color: #fbbf24;">{q['a']}</span>
                    <hr style="border-color: rgba(255,255,255,0.1); margin: 15px 0;">
                    <strong>Explanation:</strong>
                    <p dir="ltr" style="color: #d1d5db; margin-bottom: 10px;">{q['eng']}</p>
                    <p style="color: #9ca3af; font-size: 0.95rem;"><strong>بالعامية:</strong> {q['ar']}</p>
                </div>
            </details>
        </div>
"""
            elif q["type"] == "tf":
                content += f"""
        <div class="code-analysis-section">
            <h4 dir="ltr" style="color: #38bdf8; margin-bottom: 10px;">Q{q_idx}. True or False?</h4>
            <p dir="ltr" style="text-align: left; color: #e2e8f0; font-size: 1.1rem; background: rgba(0,0,0,0.2); padding: 10px; border-left: 4px solid #38bdf8; border-radius: 4px;">{q['q']}</p>
            <details class="essay-answer">
                <summary class="reveal-answer">👁️ إظهار الإجابة والتفسير</summary>
                <div class="answer-content">
                    <strong>Answer:</strong> <span style="color: #fbbf24;">{q['a']}</span>
                    <hr style="border-color: rgba(255,255,255,0.1); margin: 15px 0;">
                    <strong>Explanation:</strong>
                    <p dir="ltr" style="color: #d1d5db; margin-bottom: 10px;">{q['eng']}</p>
                    <p style="color: #9ca3af; font-size: 0.95rem;"><strong>بالعامية:</strong> {q['ar']}</p>
                </div>
            </details>
        </div>
"""
            elif q["type"] == "uml":
                content += f"""
        <div class="code-analysis-section">
            <h4 dir="ltr" style="color: #c084fc; margin-bottom: 10px;">Q{q_idx}. {q['q']}</h4>
            <div style="background: white; color: black; padding: 15px; border-radius: 8px; font-family: monospace; width: fit-content; margin: 10px auto; border: 2px solid #333; text-align: left;" dir="ltr">
                <pre style="margin: 0; white-space: pre-wrap; font-family: inherit;">{q['uml']}</pre>
            </div>
            <details class="essay-answer">
                <summary class="reveal-answer">👁️ إظهار الإجابة والتفسير</summary>
                <div class="answer-content">
                    <strong>Answer:</strong>
                    <pre class="slide-code" dir="ltr" style="border-left: 4px solid #10b981;"><code>{q['ans']}</code></pre>
                    <hr style="border-color: rgba(255,255,255,0.1); margin: 15px 0;">
                    <strong>Explanation:</strong>
                    <p dir="ltr" style="color: #d1d5db; margin-bottom: 10px;">{q['eng']}</p>
                    <p style="color: #9ca3af; font-size: 0.95rem;"><strong>بالعامية:</strong> {q['ar']}</p>
                </div>
            </details>
        </div>
"""
            q_idx += 1


final_html = html_template.replace("{content}", content)

for base in [r"c:\Users\HP\OneDrive\Desktop\namoly", r"c:\Users\HP\OneDrive\Desktop\oop-portal-test"]:
    mega_path = os.path.join(base, "mega_question_bank.html")
    with open(mega_path, "w", encoding="utf-8") as f:
        f.write(final_html)

# Add a button to final_exam.html to link to mega_question_bank.html
button_html = """
        <div style="text-align: center; margin: 4rem 0;">
            <a href="mega_question_bank.html" style="display: inline-block; background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 15px 30px; border-radius: 50px; font-size: 1.5rem; text-decoration: none; font-weight: bold; box-shadow: 0 10px 15px -3px rgba(16, 185, 129, 0.4); transition: transform 0.3s ease;">
                🚀 انتقل إلى بنك الأسئلة الشامل (Mega Question Bank)
            </a>
        </div>
"""

for path in file_paths:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "mega_question_bank.html" not in content:
            script_idx = content.find('<script src="app.js"></script>')
            if script_idx != -1:
                last_div_idx = content.rfind('</div>', 0, script_idx)
                if last_div_idx != -1:
                    content = content[:last_div_idx] + button_html + "\n    " + content[last_div_idx:]
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(content)

print("Created mega_question_bank.html and linked it successfully!")
