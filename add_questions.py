import re

html_content = """
        <!-- القسم السادس: التجميعة الكبرى للأسئلة -->
        <h2 style="color: #2dd4bf; border-bottom: 2px solid #14b8a6; padding-bottom: 10px; margin-top: 4rem;">القسم السادس: بنك الأسئلة المكثف (Mega Question Bank) 🚀</h2>
        <p style="text-align: center; color: #d1d5db; margin-bottom: 2rem;">هذا القسم يحتوي على كمية ضخمة من أسئلة الـ Choose والـ True/False والـ UML التي تغطي كل التفاصيل.</p>
"""

questions = [
    # True/False
    {
        "type": "tf",
        "topic": "Intro to OOP: Why OOP",
        "stmt": "Object-Oriented Programming (OOP) was primarily introduced to break down large, complex problems into smaller, manageable, and reusable components called objects.",
        "ans": "True",
        "eng": "OOP focuses on modularity, reusability, and organizing code into objects that mirror real-world entities, unlike procedural programming which focuses purely on functions.",
        "ar": "الـ OOP ظهرت عشان تحل مشكلة البرامج الكبيرة المعقدة وتكسرها لأجزاء صغيرة نقدر نعيد استخدامها اسمها Objects، وده بيسهل تعديل الكود وفهمه."
    },
    {
        "type": "mcq",
        "topic": "OOP Principles",
        "q": "Which OOP principle allows a subclass to provide a specific implementation of a method that is already provided by its parent class?",
        "opts": [
            "A) Encapsulation",
            "B) Polymorphism",
            "C) Inheritance",
            "D) Abstraction"
        ],
        "ans": "B) Polymorphism",
        "eng": "Method overriding is a form of Run-time Polymorphism where a derived class provides a specific implementation for a method declared in the base class.",
        "ar": "البولي مورفيزم (Polymorphism) هو المبدأ اللي بيسمحلك تعمل Overriding (تعديل) لدالة موجودة في الأب، وتعملها وظيفة جديدة مخصصة للابن."
    },
    {
        "type": "mcq",
        "topic": "Benefits of OOP",
        "q": "Which of the following is NOT a direct benefit of OOP?",
        "opts": [
            "A) Reusability of code",
            "B) Data hiding and security",
            "C) Slower compilation time",
            "D) Easier troubleshooting and maintenance"
        ],
        "ans": "C) Slower compilation time",
        "eng": "Slower compilation is definitely not a benefit. OOP benefits include code reusability (via inheritance), security (via encapsulation), and easier maintenance.",
        "ar": "أكيد البطء في وقت الترجمة (Compilation) مش ميزة. مميزات الـ OOP هي إننا بنعيد استخدام الكود، بنحمي البيانات، وبنصلح الأخطاء بسهولة."
    },
    {
        "type": "mcq",
        "topic": "UML Design",
        "q": "In a UML Class Diagram, what symbol is used to denote a 'protected' attribute or method?",
        "opts": [
            "A) + (plus)",
            "B) - (minus)",
            "C) # (hash)",
            "D) ~ (tilde)"
        ],
        "ans": "C) # (hash)",
        "eng": "In UML, '+' is public, '-' is private, '#' is protected, and '~' is package/default.",
        "ar": "في الـ UML، علامة الـ # بتعبر عن الـ protected. وعلامة الـ + للـ public وعلامة الـ - للـ private."
    },
    {
        "type": "tf",
        "topic": "Access Modifiers",
        "stmt": "A 'protected' member of a class is accessible from anywhere in the program, just like a 'public' member.",
        "ans": "False",
        "eng": "A protected member is accessible only within its own class and any derived (child) classes. It is not accessible from outside functions like main().",
        "ar": "الكلام ده غلط. الـ protected بيبقى متاح بس جوه الكلاس نفسه وجوه أي كلاس بيورث منه (الابن)، لكن مقدرش أستدعيه في الـ main() خالص."
    },
    {
        "type": "mcq",
        "topic": "Constructor Types",
        "q": "What happens if you provide a Parameterized Constructor in your class, but do NOT provide a Default Constructor?",
        "opts": [
            "A) The compiler will automatically generate a Default Constructor for you.",
            "B) You will not be able to create objects without passing arguments.",
            "C) The compiler will generate an error stating 'Parameterized constructor not allowed'.",
            "D) The Parameterized Constructor will act as a Default Constructor automatically."
        ],
        "ans": "B) You will not be able to create objects without passing arguments.",
        "eng": "Once you define ANY constructor (like a parameterized one), the compiler stops providing the implicit default constructor. If you try to create an object without arguments, you'll get a compilation error.",
        "ar": "لو أنت كتبت Constructor بياخد Parameters، الكومبايلر بيسحب إيده ومبيعملش Default Constructor من عنده. فلو حاولت تعمل أوبجيكت فاضي من غير ما تبعت قيم، الكود هيضرب error."
    },
    {
        "type": "tf",
        "topic": "Destructor",
        "stmt": "A class can have multiple destructors with different parameters (Destructor Overloading).",
        "ans": "False",
        "eng": "A destructor takes NO arguments and returns NO value. Therefore, it cannot be overloaded. A class can have only exactly one destructor.",
        "ar": "غلط تماماً. الـ Destructor مش بياخد أي Parameters (أقواسه دايماً فاضية)، وبالتالي مينفعش نعمله Overloading، وكل كلاس ليه Destructor واحد بس."
    },
    {
        "type": "mcq",
        "topic": "Setter & Getter",
        "q": "What is the primary purpose of Setter (Mutator) and Getter (Accessor) methods?",
        "opts": [
            "A) To run faster than direct variable access.",
            "B) To allow controlled access to private data members.",
            "C) To make public members private.",
            "D) To initialize the object at the time of creation."
        ],
        "ans": "B) To allow controlled access to private data members.",
        "eng": "Setters and getters are used in Encapsulation. They let you read (getter) or modify (setter) private variables while allowing you to add validation logic before changing the state.",
        "ar": "هدفهم الأساسي هو التحكم في قراءة وتعديل البيانات الـ private. الـ Setter بيخليك تحط شروط قبل ما تغير القيمة (زي إن العمر ميكونش بالسالب)، والـ Getter بيخليك تقرأ القيمة بس."
    },
    {
        "type": "tf",
        "topic": "Inline vs Regular Functions",
        "stmt": "Every function declared with the 'inline' keyword is strictly guaranteed to be expanded in-line by the compiler.",
        "ans": "False",
        "eng": "The 'inline' keyword is merely a request to the compiler, not a strict command. If the function is too large, recursive, or contains complex loops, the compiler may ignore the request and treat it as a regular function.",
        "ar": "غلط. كلمة inline هي مجرد 'طلب' أو 'اقتراح' للكومبايلر. لو الدالة كانت كبيرة أوي أو فيها Loops كتير، الكومبايلر هيرفض الطلب ده وهيعاملها كأنها دالة عادية جداً."
    },
    {
        "type": "mcq",
        "topic": "Objects as Arguments",
        "q": "When passing an object to a function by value, what happens?",
        "opts": [
            "A) A reference to the original object is passed.",
            "B) A copy of the object is created using the Copy Constructor.",
            "C) Any changes made inside the function affect the original object.",
            "D) The object's memory is deallocated immediately."
        ],
        "ans": "B) A copy of the object is created using the Copy Constructor.",
        "eng": "Passing by value creates a fresh copy of the object in the function's scope using the copy constructor. Modifications inside the function do not affect the original object.",
        "ar": "لما بنبعت أوبجيكت للدالة بالـ Value، بيتم استدعاء الـ Copy Constructor عشان يعمل نسخة طبق الأصل من الأوبجيكت ده جوه الدالة، وأي تغيير بيحصل في النسخة مبيأثرش على الأوبجيكت الأصلي."
    },
    {
        "type": "tf",
        "topic": "Classes & Memory",
        "stmt": "When you define a class in C++, memory is immediately allocated for its data members.",
        "ans": "False",
        "eng": "A class is just a blueprint or template. Memory is NOT allocated when a class is defined. Memory is only allocated when an OBJECT (instance) of that class is created.",
        "ar": "غلط. الكلاس ده مجرد رسمة أو تخطيط (Blueprint). الميموري مش بتتحجز غير لما تبدأ تعمل Objects (نسخ حقيقية) من الكلاس ده في البرنامج."
    },
    {
        "type": "mcq",
        "topic": "Constant Objects",
        "q": "If you have a constant object `const Point p1(5, 5);`, which of the following is true?",
        "opts": [
            "A) It can call any method in the Point class.",
            "B) It can only call static methods.",
            "C) It can only call const member functions.",
            "D) Its data members can be changed directly if they are public."
        ],
        "ans": "C) It can only call const member functions.",
        "eng": "A constant object guarantees its state won't change. Therefore, the compiler only allows it to call functions explicitly marked with the `const` keyword, assuring they are read-only.",
        "ar": "الأوبجيكت الـ const معناه إنه مقفول ومستحيل بياناته تتغير. عشان كده الكومبايلر بيمنعه إنه ينادي أي دالة إلا الدوال اللي مكتوب جنبها const (يعني دوال للقراءة فقط)."
    },
    {
        "type": "tf",
        "topic": "Arrays of Objects",
        "stmt": "To create an array of objects like `Student arr[10];`, the `Student` class must have a Default Constructor.",
        "ans": "True",
        "eng": "When creating an array of objects without explicit initialization, the compiler needs a Default Constructor to initialize each object in the array. If only a parameterized constructor exists, this line will cause a compilation error.",
        "ar": "صح. لما بتعمل مصفوفة أوبجيكتس من غير ما تديهم قيم ابتدائية، الكومبايلر بيروح ينادي الـ Default Constructor لكل عنصر فيهم. لو الكلاس مفيهوش Default Constructor، هتاخد إيرور."
    },
    {
        "type": "mcq",
        "topic": "Dynamic vs Static Memory",
        "q": "Which memory region is managed automatically by the compiler, where local variables and function call data are stored?",
        "opts": [
            "A) The Heap",
            "B) The Data Segment",
            "C) The Code Segment",
            "D) The Stack"
        ],
        "ans": "D) The Stack",
        "eng": "The Stack is used for static memory allocation (local variables, function arguments). It grows and shrinks automatically as functions are called and return.",
        "ar": "الـ Stack هي المنطقة اللي الكومبايلر بيديرها بنفسه. أي متغير بتعمله جوه دالة بيتحط في الـ Stack وبيتمسح لوحده أول ما الدالة تخلص."
    },
    {
        "type": "tf",
        "topic": "Stack Overflow",
        "stmt": "A Stack Overflow usually occurs when you dynamically allocate too much memory using the `new` operator.",
        "ans": "False",
        "eng": "Using `new` allocates memory on the Heap. Exhausting Heap memory causes a memory allocation failure (e.g., throwing bad_alloc). Stack overflow occurs due to deep/infinite recursion or allocating excessively large local variables on the Stack.",
        "ar": "غلط. كلمة new بتحجز في الـ Heap مش الـ Stack. الـ Stack Overflow بيحصل لما تعمل Recursion (دالة بتنادي نفسها لمالانهاية) أو تعمل مصفوفة عادية ضخمة جداً جوه دالة فتملى مساحة الـ Stack."
    },
    {
        "type": "mcq",
        "topic": "Array of Objects & Dynamic Allocation",
        "q": "Which code correctly creates a dynamic array of 5 `Car` objects and then frees the memory?",
        "opts": [
            "A) Car* c = new Car(5); delete c;",
            "B) Car* c = new Car[5]; delete[] c;",
            "C) Car* c = new Car[5]; delete c;",
            "D) Car c[5]; delete[] c;"
        ],
        "ans": "B) Car* c = new Car[5]; delete[] c;",
        "eng": "To allocate an array of objects dynamically, you use `new ClassName[size]`. To properly call the destructor for all elements and free the memory, you must use `delete[] pointerName;`.",
        "ar": "عشان تحجز مصفوفة في الـ Heap بتستخدم new مع أقواس مربعة []. وعشان تمسحها كلها لازم تستخدم delete []، لو استخدمت delete العادية هيمسح أول عربية بس والباقي هيفضل محجوز."
    },
    {
        "type": "tf",
        "topic": "Types of Inheritance",
        "stmt": "C++ supports Multiple Inheritance, where a single derived class can inherit from more than one base class.",
        "ans": "True",
        "eng": "Unlike Java or C#, C++ does support Multiple Inheritance (e.g., `class Child : public Parent1, public Parent2`). However, it can lead to the Diamond Problem, which is resolved using Virtual Inheritance.",
        "ar": "صح. الـ C++ بتسمح إن كلاس واحد يورث من أكتر من أب في نفس الوقت (Multiple Inheritance)، على عكس لغات تانية زي Java اللي بتمنع ده."
    },
    {
        "type": "mcq",
        "topic": "Order of Inheritance",
        "q": "If class `C` inherits from `B`, and `B` inherits from `A`. When an object of `C` is destroyed, in what order are the destructors called?",
        "opts": [
            "A) A then B then C",
            "B) C then B then A",
            "C) Random order depending on the compiler",
            "D) Only C's destructor is called"
        ],
        "ans": "B) C then B then A",
        "eng": "Constructors are called in Base-to-Derived order (A, B, C). Destructors are always called in the exact reverse order: Derived-to-Base (C, B, A).",
        "ar": "في الهدد (Destructor) بنهد اللي فوق الأول وبعدين اللي تحته. فبما إن C هو الحفيد، هيمسح C الأول، وبعدين أبوه B، وبعدين جده A."
    },
    {
        "type": "tf",
        "topic": "Virtual Functions",
        "stmt": "A virtual function is resolved at compile-time (Early Binding).",
        "ans": "False",
        "eng": "Virtual functions are resolved at run-time (Late Binding / Dynamic Binding). The exact function to call is determined based on the actual object type the pointer points to at execution time.",
        "ar": "غلط. الـ Virtual Function بتتعمل أساساً عشان الـ Run-time (وقت التشغيل)، الكومبايلر بيأجل قراره لحد ما البرنامج يشتغل ويشوف البوينتر بيشاور على مين بالظبط (Late Binding)."
    },
    {
        "type": "mcq",
        "topic": "Abstract Class",
        "q": "Which of the following makes a class an Abstract Class in C++?",
        "opts": [
            "A) Having at least one private constructor.",
            "B) Having the keyword 'abstract' in the class definition.",
            "C) Containing at least one Pure Virtual Function.",
            "D) Containing a virtual destructor."
        ],
        "ans": "C) Containing at least one Pure Virtual Function.",
        "eng": "A class becomes abstract when it has at least one pure virtual function (e.g., `virtual void fun() = 0;`). You cannot instantiate an abstract class.",
        "ar": "الكلاس بيبقى Abstract (وهمي وميتحجزلوش أوبجيكت) بمجرد ما يكون جواه دالة واحدة على الأقل من نوع Pure Virtual (يعني متساوية بـ 0 زي كدة: virtual void func() = 0)."
    },
    {
        "type": "tf",
        "topic": "Function Overloading",
        "stmt": "Function overloading requires the functions to have the exact same name and the exact same parameter list, but different return types.",
        "ans": "False",
        "eng": "Function overloading requires the SAME name but DIFFERENT parameter lists (different number, types, or order of parameters). The return type alone is NOT sufficient to distinguish overloaded functions.",
        "ar": "غلط. شرط الـ Overloading إن الدوال يكون ليها نفس الاسم، بس الـ Parameters لازم تكون مختلفة (في العدد أو النوع). اختلاف نوع الترجيع (Return type) لوحده مش كفاية والكومبايلر هيطلع error."
    },
    {
        "type": "mcq",
        "topic": "Static Class Data",
        "q": "How must a static data member of a class be initialized?",
        "opts": [
            "A) Inside the constructor of the class.",
            "B) Inside the class definition directly.",
            "C) Outside the class definition using the scope resolution operator (::).",
            "D) Inside the main function."
        ],
        "ans": "C) Outside the class definition using the scope resolution operator (::).",
        "eng": "Static data members must be defined and initialized outside the class declaration to allocate memory for them. (e.g., `int MyClass::count = 0;`).",
        "ar": "المتغير الـ Static لازم تديله قيمة ابتدائية بره الكلاس خالص باستخدام علامة الـ Scope Resolution (::). مينفعش تديله قيمة جوه الـ Constructor لإنه مشترك ومش مِلك لأوبجيكت معين."
    },
    # More MCQs
    {
        "type": "mcq",
        "topic": "Constructors",
        "q": "Can a constructor return a value?",
        "opts": [
            "A) Yes, but only an integer.",
            "B) Yes, it returns a pointer to the object.",
            "C) No, constructors do not have a return type.",
            "D) No, but it must be declared with `void`."
        ],
        "ans": "C) No, constructors do not have a return type.",
        "eng": "A constructor doesn't return anything, not even `void`. It is automatically invoked when an object is created to initialize its state.",
        "ar": "لا طبعاً. الـ Constructor ملوش أي Return Type أصلاً، ولا حتى بنكتب قبله void. هو بيتنفذ لوحده عشان يجهز الأوبجيكت."
    },
    {
        "type": "mcq",
        "topic": "UML Diagram Relationships",
        "q": "In UML, an open arrow with a dashed line (`- - - ▷`) typically represents which concept?",
        "opts": [
            "A) Generalization (Inheritance)",
            "B) Realization (Interface implementation)",
            "C) Composition",
            "D) Aggregation"
        ],
        "ans": "B) Realization (Interface implementation)",
        "eng": "A dashed line with a hollow arrow represents implementation of an interface (Realization). A solid line with a hollow arrow represents Inheritance (Generalization).",
        "ar": "السهم الفاضي المتقطع (Dashed) بيعبر عن تنفيذ Interface (Realization)، لكن السهم الفاضي المتصل (Solid) بيعبر عن الوراثة العادية (Inheritance)."
    },
    {
        "type": "tf",
        "topic": "Dynamic Allocation",
        "stmt": "If `int* p = new int;` fails to allocate memory, it returns `nullptr` by default in standard modern C++.",
        "ans": "False",
        "eng": "In modern standard C++, if `new` fails, it throws a `std::bad_alloc` exception. To make it return `nullptr` instead, you must use `new (std::nothrow) int;`.",
        "ar": "غلط. في الـ C++ الحديث، لو الـ new فشل يحجز الميموري، بيعمل Exception اسمه bad_alloc والبرنامج بيضرب. عشان تخليه يرجع nullptr في حالة الفشل لازم تستخدم (nothrow)."
    },
    
    # UML to Code Questions
    {
        "type": "uml",
        "topic": "UML to Code: Inheritance",
        "desc": "Convert the following UML into C++ Code. Focus only on the class definitions and inheritance.",
        "uml": "Vehicle\\n-------------------\\n# speed: int\\n-------------------\\n+ Vehicle(s: int)\\n+ display(): void\\n        △\\n        |\\nCar\\n-------------------\\n- model: string\\n-------------------\\n+ Car(s: int, m: string)\\n+ display(): void",
        "ans": "class Vehicle {\\nprotected:\\n    int speed;\\npublic:\\n    Vehicle(int s);\\n    virtual void display();\\n};\\n\\nclass Car : public Vehicle {\\nprivate:\\n    string model;\\npublic:\\n    Car(int s, string m);\\n    void display() override;\\n};",
        "eng": "The triangle arrow points to Vehicle, meaning Car inherits from Vehicle. The `#` indicates `protected`, and `-` indicates `private`. Since `display()` is in both, making it `virtual` in the base class is best practice.",
        "ar": "سهم الوراثة بيشاور على Vehicle، يعني Car بيورث منه وراثة public. الـ # يعني protected في الـ speed، والـ - يعني private في الـ model. وبما إن الدالة display مكررة في الاتنين، من الأفضل نخليها virtual في الأب."
    },
    {
        "type": "uml",
        "topic": "UML to Code: Abstract Class",
        "desc": "Write the C++ definition for this UML. Notice the *italicized* class and method names in UML conventions, which indicate abstraction.",
        "uml": "<<abstract>>\\nEmployee\\n-------------------\\n- name: string\\n-------------------\\n+ Employee(n: string)\\n+ getName(): string\\n+ calculatePay(): double <<abstract/pure virtual>>",
        "ans": "class Employee {\\nprivate:\\n    string name;\\npublic:\\n    Employee(string n);\\n    string getName();\\n    virtual double calculatePay() = 0; // Pure virtual function\\n};",
        "eng": "The `<<abstract>>` stereotype or italicized text means the class is abstract, which is achieved in C++ by declaring `calculatePay()` as a pure virtual function (`= 0`).",
        "ar": "كلمة abstract أو الخط المايل في الـ UML معناها إن الكلاس ده مقدرش أعمل منه أوبجيكت، وده في الـ C++ بيتعمل بإننا نخلي دالة calculatePay دالة Pure Virtual بإننا نساويها بـ صفر."
    }
]

more_tf = [
    {
        "type": "tf",
        "topic": "Rapid Fire - Inheritance",
        "stmt": "A subclass can access protected members of its base class directly.",
        "ans": "True",
        "eng": "This is exactly what the protected access modifier is for: keeping members hidden from the outside world but accessible to child classes.",
        "ar": "صح جداً. الـ protected معمول مخصوص عشان يمنع الناس اللي بره الكلاس من الوصول ليه، بس يسمح للورثة (الأبناء) إنهم يستخدموه."
    },
    {
        "type": "tf",
        "topic": "Rapid Fire - Polymorphism",
        "stmt": "Pointers of a base class can point to objects of a derived class.",
        "ans": "True",
        "eng": "This is the cornerstone of Run-time Polymorphism. A Base* can point to a Derived object, and via virtual functions, execute Derived behavior.",
        "ar": "صح! دي أساس البولي مورفيزم. بوينتر الأب يقدر يشاور على أوبجيكت الابن، ولو فيه دوال virtual هيشغل الكود بتاع الابن."
    },
    {
        "type": "tf",
        "topic": "Rapid Fire - Memory",
        "stmt": "When you dynamically allocate memory using `new`, the memory is cleaned up automatically by the Garbage Collector in C++.",
        "ans": "False",
        "eng": "C++ does NOT have an automatic garbage collector. You must explicitly use `delete` or `delete[]` to free dynamically allocated memory.",
        "ar": "غلط! لغة C++ مفهاش Garbage Collector زي الـ Java. أنت اللي بتحجز بـ new وأنت اللي لازم تمسح بإيدك بـ delete، وإلا هيحصل Memory Leak."
    },
    {
        "type": "tf",
        "topic": "Rapid Fire - Destructors",
        "stmt": "A base class destructor should generally be declared as virtual if it is to be inherited.",
        "ans": "True",
        "eng": "If you delete a derived object through a base class pointer and the base class destructor is non-virtual, the derived class destructor won't be called, causing a memory leak.",
        "ar": "صح جداً! لو معملتش الـ Destructor بتاع الأب virtual، ولما تيجي تمسح الابن من خلال بوينتر الأب، هيمسح حتة من الميموري ويسيب الباقي متعلق."
    },
    {
        "type": "tf",
        "topic": "Rapid Fire - Constructors",
        "stmt": "Constructors are inherited by the derived class just like regular member functions.",
        "ans": "False",
        "eng": "Constructors are NOT inherited. A derived class must define its own constructors, which can call the base class constructor.",
        "ar": "غلط. الـ Constructors والـ Destructors مش بيورثوا. الابن لازم يعملهم بنفسه، وممكن وهو بيعملهم ينادي على بتاع الأب."
    },
    {
        "type": "tf",
        "topic": "Rapid Fire - Static Members",
        "stmt": "Static member functions can access non-static member variables of the same class.",
        "ans": "False",
        "eng": "Static functions have no `this` pointer and belong to the class itself, not to any object. Thus, they cannot access instance-specific (non-static) variables.",
        "ar": "غلط. الدوال الـ Static مش مرتبطة بأوبجيكت معين، فملهاش الحق توصل لأي متغير عادي (non-static) جوه الكلاس، بتتعامل مع المتغيرات الـ Static بس."
    },
    {
        "type": "tf",
        "topic": "Rapid Fire - Inline Functions",
        "stmt": "Writing the function definition directly inside the class declaration automatically makes it an inline function.",
        "ans": "True",
        "eng": "In C++, defining a member function completely within the class body implicitly requests the compiler to treat it as inline.",
        "ar": "صح. أي دالة بتكتب الكود بتاعها جوه الكلاس نفسه، الكومبايلر بيعتبرها inline تلقائياً من غير ما تكتب الكلمة دي."
    },
    {
        "type": "tf",
        "topic": "Rapid Fire - Returning Objects",
        "stmt": "Returning an object by reference from a function is always safe, even if it is a local variable.",
        "ans": "False",
        "eng": "Returning a reference to a local variable is extremely dangerous because the local variable is destroyed when the function ends, leaving a dangling reference.",
        "ar": "غلط جداً! لو رجعت Reference لمتغير اتعمل جوه الدالة، المتغير ده هيتمسح أول ما الدالة تخلص، وهيرجعلك Reference لسراب (Dangling Reference)."
    },
    {
        "type": "tf",
        "topic": "Rapid Fire - Encapsulation",
        "stmt": "Encapsulation can be achieved completely without using classes in C++.",
        "ans": "False",
        "eng": "While structs can also encapsulate, Encapsulation conceptually relies on objects grouping data and methods together with access specifiers, which is the core of class-based design.",
        "ar": "غلط. فكرة الكبسلة مبنية على إنك تجمع البيانات والدوال في حاجة واحدة (Class أو Struct) وتقفل على البيانات، فمستحيل تتعمل من غيرهم."
    },
    {
        "type": "tf",
        "topic": "Rapid Fire - Memory Allocation",
        "stmt": "The `new` operator in C++ not only allocates memory, but also calls the constructor of the class.",
        "ans": "True",
        "eng": "Unlike `malloc()` in C which only allocates raw memory, `new` allocates memory AND invokes the appropriate constructor to initialize the object.",
        "ar": "صح. الفرق الجوهري بين new في C++ و malloc في C، إن new مش بس بيحجز مساحة، ده كمان بيروح يشغل الـ Constructor عشان يجهز الأوبجيكت."
    }
]

questions.extend(more_tf)

for i, q in enumerate(questions):
    idx = i + 27 # Starting from Q27
    if q["type"] == "mcq":
        opts_html = "\\n".join([f"                <li>{opt}</li>" for opt in q["opts"]])
        html_content += f"""
        <div class="code-analysis-section">
            <h3>Q{idx}. {q['topic']}</h3>
            <p>{q['q']}</p>
            <ol dir="ltr" style="text-align: left; margin-left: 20px;">
{opts_html}
            </ol>
            <details class="essay-answer">
                <summary class="reveal-answer">👁️ إظهار الإجابة والتفسير</summary>
                <div class="answer-content">
                    <strong>Answer:</strong> {q['ans']}
                    <hr style="border-color: rgba(255,255,255,0.1); margin: 15px 0;">
                    <strong>Explanation:</strong>
                    <p dir="ltr" style="color: #d1d5db; margin-bottom: 10px;">{q['eng']}</p>
                    <p style="color: #9ca3af; font-size: 0.95rem;"><strong>بالعامية:</strong> {q['ar']}</p>
                </div>
            </details>
        </div>
"""
    elif q["type"] == "tf":
        html_content += f"""
        <div class="code-analysis-section">
            <h3>Q{idx}. {q['topic']} (True / False)</h3>
            <p dir="ltr" style="text-align: left; margin-bottom: 15px; font-size: 1.1rem;"><strong>Statement:</strong> {q['stmt']}</p>
            <details class="essay-answer">
                <summary class="reveal-answer">👁️ إظهار الإجابة والتفسير</summary>
                <div class="answer-content">
                    <strong>Answer:</strong> {q['ans']}
                    <hr style="border-color: rgba(255,255,255,0.1); margin: 15px 0;">
                    <strong>Explanation:</strong>
                    <p dir="ltr" style="color: #d1d5db; margin-bottom: 10px;">{q['eng']}</p>
                    <p style="color: #9ca3af; font-size: 0.95rem;"><strong>بالعامية:</strong> {q['ar']}</p>
                </div>
            </details>
        </div>
"""
    elif q["type"] == "uml":
        html_content += f"""
        <div class="code-analysis-section">
            <h3>Q{idx}. {q['topic']}</h3>
            <p>{q['desc']}</p>
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

# Modify both namoly and oop-portal-test just to be absolutely sure we hit the user's active file
file_paths = [
    r"c:\Users\HP\OneDrive\Desktop\namoly\final_exam.html",
    r"c:\Users\HP\OneDrive\Desktop\oop-portal-test\final_exam.html"
]

import os

for file_path in file_paths:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            original_html = f.read()

        # Safely find the script tag to append our section right before it closes the container
        # The script tag `<script src="app.js"></script>` is right after the main container ends.
        
        target = '<script src="app.js"></script>'
        # We want to insert right before the closing </div> of the container which is right before the script tag.
        
        # Let's use regex to find the last </div> before <script src="app.js">
        match = re.search(r'(</div>\s*)(<script src="app.js">)', original_html)
        if match:
            new_html = original_html[:match.start(1)] + html_content + match.group(1) + match.group(2) + original_html[match.end(2):]
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_html)
            print(f"Questions added successfully using regex to {file_path}!")
        else:
            # Fallback string replace
            if target in original_html:
                # We inject the content AND an extra closing div, wait no, let's just insert it right before the script tag,
                # BUT wait, the questions MUST be inside the `.container` div.
                # So we must find `</div>\n\n    <script src="app.js"></script>`
                # Let's just do a reverse find for </div> before the script.
                script_idx = original_html.find(target)
                if script_idx != -1:
                    last_div_idx = original_html.rfind('</div>', 0, script_idx)
                    if last_div_idx != -1:
                        new_html = original_html[:last_div_idx] + html_content + '\\n' + original_html[last_div_idx:]
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_html)
                        print(f"Questions added successfully using fallback to {file_path}!")
                    else:
                        print(f"Could not find </div> before script in {file_path}!")
            else:
                print(f"Could not find {target} in {file_path}!")
    except Exception as e:
        print(f"Error accessing {file_path}: {e}")

