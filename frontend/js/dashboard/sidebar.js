// ==========================================
// Career AI Sidebar Navigation
// ==========================================

const menuItems = {

    dashboard: document.getElementById("dashboardMenu"),

    resume: document.getElementById("resumeMenu"),

    report: document.getElementById("reportMenu"),

    profile: document.getElementById("profileMenu"),

    settings: document.getElementById("settingsMenu")

};

const sections = {

    dashboard: document.getElementById("dashboardSection"),

    resume: document.getElementById("resumeSection"),

    report: document.getElementById("reportSection"),

    profile: document.getElementById("profileSection"),

    settings: document.getElementById("settingsSection")

};

// ==========================================
// Hide All Sections
// ==========================================

function hideAllSections() {

    Object.values(sections).forEach(section => {

        section.style.display = "none";

    });

    Object.values(menuItems).forEach(item => {

        item.classList.remove("active");

    });

}

// ==========================================
// Show Section
// ==========================================

function showSection(name) {

    hideAllSections();

    sections[name].style.display = "block";

    menuItems[name].classList.add("active");

}

// ==========================================
// Events
// ==========================================

menuItems.dashboard.addEventListener("click", function (e) {

    e.preventDefault();

    showSection("dashboard");

});

menuItems.resume.addEventListener("click", function (e) {

    e.preventDefault();

    showSection("resume");

});

menuItems.report.addEventListener("click", function (e) {

    e.preventDefault();

    showSection("report");

});

menuItems.profile.addEventListener("click", function (e) {

    e.preventDefault();

    showSection("profile");

});

menuItems.settings.addEventListener("click", function (e) {

    e.preventDefault();

    showSection("settings");

});

// ==========================================
// Default Page
// ==========================================

showSection("dashboard");