/**
 * OOP Study Portal - Core Logic v2
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Setup Quiz Functionality
    setupQuizzes();
    
    // 2. Setup scroll progress bar
    setupScrollProgress();
    
    // 3. Add entrance animations
    setupAnimations();
});

/**
 * Quiz System - Button-based MCQ
 */
function setupQuizzes() {
    // This is handled by the global checkAnswer function below
}

/**
 * Global checkAnswer - called from onclick on option buttons
 * @param {HTMLElement} btn - The clicked button element
 * @param {number} selectedIndex - The index of the selected option (0-based)
 */
window.checkAnswer = function(btn, selectedIndex) {
    const question = btn.closest('.question');
    if (!question) return;
    
    // Prevent re-answering
    if (question.classList.contains('answered')) return;
    question.classList.add('answered');
    
    const correctIndex = parseInt(question.dataset.answer);
    const allBtns = question.querySelectorAll('.option-btn');
    const feedback = question.querySelector('.feedback');
    
    // Disable all buttons
    allBtns.forEach(b => {
        b.style.pointerEvents = 'none';
    });
    
    if (selectedIndex === correctIndex) {
        // Correct answer
        btn.classList.add('correct');
        btn.innerHTML = '✅ ' + btn.innerHTML;
    } else {
        // Wrong answer - mark selected as wrong
        btn.classList.add('wrong');
        btn.innerHTML = '❌ ' + btn.innerHTML;
        
        // Highlight the correct answer
        allBtns[correctIndex].classList.add('correct');
        allBtns[correctIndex].innerHTML = '✅ ' + allBtns[correctIndex].innerHTML;
    }
    
    // Show feedback
    if (feedback) {
        feedback.classList.add('show');
        if (selectedIndex === correctIndex) {
            feedback.style.background = 'rgba(16, 185, 129, 0.15)';
            feedback.style.borderLeft = '4px solid #10b981';
            feedback.style.color = '#a7f3d0';
        } else {
            feedback.style.background = 'rgba(239, 68, 68, 0.15)';
            feedback.style.borderLeft = '4px solid #ef4444';
            feedback.style.color = '#fca5a5';
        }
    }
};

/**
 * Scroll Progress Bar
 */
function setupScrollProgress() {
    const progressBar = document.getElementById('progressBar');
    if (!progressBar) return;
    
    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        progressBar.style.width = scrollPercent + '%';
    });
}

/**
 * Entrance Animations using Intersection Observer
 */
function setupAnimations() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe all slide containers and quiz sections
    document.querySelectorAll('.slide-container, .quiz-section, .summary-section, .essay-section, .output-question-section, .write-code-section, .code-analysis-section').forEach(el => {
        el.classList.add('animate-target');
        observer.observe(el);
    });
}

/**
 * Progress Tracking
 */
window.markLectureCompleted = function(btn, lecId) {
    if (btn.classList.contains('completed')) return;
    
    // Save to localStorage
    localStorage.setItem('namoly_' + lecId + '_completed', 'true');
    
    // Update button UI
    btn.classList.add('completed');
    btn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> مكتملة ✅';
    btn.style.pointerEvents = 'none';
};

// Check for completed lectures on page load
document.addEventListener('DOMContentLoaded', () => {
    // 1. On index page: update cards
    const cards = document.querySelectorAll('.lecture-card');
    cards.forEach(card => {
        const lecId = card.getAttribute('data-lecture');
        if (localStorage.getItem('namoly_' + lecId + '_completed') === 'true') {
            card.classList.add('completed-card');
            const badge = card.querySelector('.badge');
            if(badge) badge.innerText = '✅ مكتملة';
            const progressFill = card.querySelector('.progress-fill');
            if(progressFill) progressFill.style.width = '100%';
            const progressText = card.querySelector('.progress-text');
            if(progressText) progressText.innerText = '100%';
        }
    });

    // 2. On lecture pages: update completion button if already completed
    const path = window.location.pathname;
    let lecId = null;
    const match = path.match(/lecture(\d+)\.html/);
    if (match) {
        lecId = 'lec' + match[1];
    }
    
    if (lecId && localStorage.getItem('namoly_' + lecId + '_completed') === 'true') {
        const compBtn = document.querySelector('.completion-btn');
        if (compBtn) {
            compBtn.classList.add('completed');
            compBtn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> مكتملة ✅';
            compBtn.style.pointerEvents = 'none';
        }
    }
});
