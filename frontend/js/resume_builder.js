// ==========================================
// AI Resume Builder
// ==========================================

// ------------------------------------------
// API
// ------------------------------------------

const API_BASE_URL = "http://127.0.0.1:8000";


// ------------------------------------------
// Elements
// ------------------------------------------

const backButton =
    document.getElementById("backButton");

const generateResumeButton =
    document.getElementById("generateResumeButton");

const improveResumeButton =
    document.getElementById("improveResumeButton");

const downloadDOCXButton =
    document.getElementById("downloadDOCXButton");

const resumeName =
    document.getElementById("resumeName");

const resumeStatus =
    document.getElementById("resumeStatus");

const aiStatus =
    document.getElementById("aiStatus");

const resumeLoader =
    document.getElementById("resumeLoader");


// ------------------------------------------
// Get Token
// ------------------------------------------

function getToken() {

    return localStorage.getItem(
        "access_token"
    );

}


// ------------------------------------------
// Get Resume ID
// ------------------------------------------

function getResumeId() {

    const params =
        new URLSearchParams(
            window.location.search
        );

    const urlResumeId =
        params.get("resume_id");

    if (urlResumeId) {

        return Number(urlResumeId);

    }


    const storedResumeId =
        localStorage.getItem(
            "resume_id"
        );

    if (storedResumeId) {

        return Number(
            storedResumeId
        );

    }

    return null;
}


// ------------------------------------------
// Authorization Headers
// ------------------------------------------

function authHeaders() {

    const token =
        getToken();

    return {

        "Content-Type":
            "application/json",

        "Authorization":
            `Bearer ${token}`

    };

}


// ------------------------------------------
// Show Loader
// ------------------------------------------

function showLoader(message) {

    resumeLoader.style.display =
        "block";

    aiStatus.textContent =
        message;

}


// ------------------------------------------
// Hide Loader
// ------------------------------------------

function hideLoader() {

    resumeLoader.style.display =
        "none";

}


// ------------------------------------------
// Disable Buttons
// ------------------------------------------

function setButtonsDisabled(
    disabled
) {

    generateResumeButton.disabled =
        disabled;

    improveResumeButton.disabled =
        disabled;

    downloadDOCXButton.disabled =
        disabled;

}


// ------------------------------------------
// Update Status
// ------------------------------------------

function updateStatus(
    status
) {

    resumeStatus.textContent =
        status;

}


// ------------------------------------------
// Generate Resume
// ------------------------------------------

async function generateResume() {

    const resumeId =
        getResumeId();


    if (!resumeId) {

        alert(
            "Please select a resume first."
        );

        return;

    }


    showLoader(
        "AI is generating your resume..."
    );

    setButtonsDisabled(true);

    updateStatus(
        "Generating..."
    );


    try {

        const response =
            await fetch(
                `${API_BASE_URL}/resume/generate`,
                {

                    method: "POST",

                    headers:
                        authHeaders(),

                    body:
                        JSON.stringify({

                            resume_id:
                                resumeId

                        })

                }
            );


        if (response.status === 401) {

            window.location.href =
                "login.html";

            return;

        }


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Unable to generate resume."
            );

        }


        const resumeData =
            data.data;


        renderResume(
            resumeData
        );


        updateStatus(
            "Generated"
        );

        aiStatus.textContent =
            "Resume generated successfully.";

    }

    catch (error) {

        console.error(
            "Resume generation error:",
            error
        );

        updateStatus(
            "Error"
        );

        aiStatus.textContent =
            error.message;

        alert(
            error.message
        );

    }

    finally {

        hideLoader();

        setButtonsDisabled(false);

    }

}


// ------------------------------------------
// Improve Resume
// ------------------------------------------

async function improveResume() {

    const resumeId =
        getResumeId();


    if (!resumeId) {

        alert(
            "Please select a resume first."
        );

        return;

    }


    showLoader(
        "AI is improving your resume..."
    );

    setButtonsDisabled(true);

    updateStatus(
        "Improving..."
    );


    try {

        const response =
            await fetch(
                `${API_BASE_URL}/resume/optimize`,
                {

                    method: "POST",

                    headers:
                        authHeaders(),

                    body:
                        JSON.stringify({

                            resume_id:
                                resumeId

                        })

                }
            );


        if (response.status === 401) {

            window.location.href =
                "login.html";

            return;

        }


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Unable to improve resume."
            );

        }


        const resumeData =
            data.data;


        renderResume(
            resumeData
        );


        updateStatus(
            "Improved"
        );

        aiStatus.textContent =
            "Resume improved successfully.";

    }

    catch (error) {

        console.error(
            "Resume optimization error:",
            error
        );

        updateStatus(
            "Error"
        );

        aiStatus.textContent =
            error.message;

        alert(
            error.message
        );

    }

    finally {

        hideLoader();

        setButtonsDisabled(false);

    }

}


// ------------------------------------------
// Render Resume
// ------------------------------------------

function renderResume(
    data
) {

    if (!data) {

        return;

    }


    const candidate =
        data.candidate || {};

    const summary =
        data.professional_summary || "";


    // --------------------------------------
    // Candidate
    // --------------------------------------

    document.getElementById(
        "candidateName"
    ).textContent =
        candidate.name || "Candidate Name";


    document.getElementById(
        "candidateRole"
    ).textContent =
        candidate.role || "Professional";


    document.getElementById(
        "candidatePhone"
    ).textContent =
        candidate.phone || "";


    document.getElementById(
        "candidateLocation"
    ).textContent =
        candidate.location || "";


    // --------------------------------------
    // Email
    // --------------------------------------

    const emailElement =
        document.getElementById(
            "candidateEmail"
        );


    emailElement.textContent =
        candidate.email || "";


    if (candidate.email) {

        emailElement.href =
            `mailto:${candidate.email}`;

    }


    // --------------------------------------
    // LinkedIn
    // --------------------------------------

    setLink(
        "candidateLinkedin",
        candidate.linkedin,
        "LinkedIn"
    );


    // --------------------------------------
    // GitHub
    // --------------------------------------

    setLink(
        "candidateGithub",
        candidate.github,
        "GitHub"
    );


    // --------------------------------------
    // Portfolio
    // --------------------------------------

    setLink(
        "candidatePortfolio",
        candidate.portfolio,
        "Portfolio"
    );


    // --------------------------------------
    // Summary
    // --------------------------------------

    document.getElementById(
        "professionalSummary"
    ).textContent =
        summary;


    // --------------------------------------
    // Skills
    // --------------------------------------

    renderSkills(
        data.skills || {}
    );


    // --------------------------------------
    // Experience
    // --------------------------------------

    renderExperience(
        data.experience || []
    );


    // --------------------------------------
    // Projects
    // --------------------------------------

    renderProjects(
        data.projects || []
    );


    // --------------------------------------
    // Education
    // --------------------------------------

    renderEducation(
        data.education || []
    );


    // --------------------------------------
    // Certifications
    // --------------------------------------

    renderList(
        "certificationContainer",
        data.certifications || []
    );


    // --------------------------------------
    // Achievements
    // --------------------------------------

    renderList(
        "achievementContainer",
        data.achievements || []
    );


    // --------------------------------------
    // Languages
    // --------------------------------------

    renderLanguages(
        data.languages || []
    );

}


// ------------------------------------------
// Set Link
// ------------------------------------------

function setLink(
    elementId,
    url,
    label
) {

    const element =
        document.getElementById(
            elementId
        );


    if (!url) {

        element.textContent =
            "";

        element.removeAttribute(
            "href"
        );

        return;

    }


    let finalUrl =
        String(url).trim();


    if (
        !finalUrl.startsWith(
            "http://"
        ) &&
        !finalUrl.startsWith(
            "https://"
        )
    ) {

        finalUrl =
            `https://${finalUrl}`;

    }


    element.textContent =
        label;

    element.href =
        finalUrl;

}


// ------------------------------------------
// Render Skills
// ------------------------------------------

function renderSkills(
    skills
) {

    const container =
        document.getElementById(
            "skillsContainer"
        );

    container.innerHTML =
        "";


    Object.entries(
        skills
    ).forEach(
        ([category, values]) => {

            if (!values) {
                return;
            }


            if (!Array.isArray(values)) {

                values = [
                    values
                ];

            }


            values =
                values.filter(
                    item =>
                        item !== null &&
                        String(item).trim()
                );


            if (!values.length) {
                return;
            }


            const paragraph =
                document.createElement(
                    "p"
                );

            paragraph.className =
                "skill-category";


            const strong =
                document.createElement(
                    "strong"
                );

            strong.textContent =
                `${category}: `;


            paragraph.appendChild(
                strong
            );


            paragraph.appendChild(
                document.createTextNode(
                    values.join(", ")
                )
            );


            container.appendChild(
                paragraph
            );

        }
    );

}


// ------------------------------------------
// Render Experience
// ------------------------------------------

function renderExperience(
    experience
) {

    const container =
        document.getElementById(
            "experienceContainer"
        );

    container.innerHTML =
        "";


    experience.forEach(
        item => {

            const wrapper =
                document.createElement(
                    "div"
                );

            wrapper.className =
                "experience-item";


            const title =
                document.createElement(
                    "div"
                );

            title.className =
                "experience-role";

            title.textContent =
                item.role ||
                item.title ||
                "";


            const company =
                document.createElement(
                    "div"
                );

            company.className =
                "experience-company";

            company.textContent =
                item.company ||
                "";


            wrapper.appendChild(
                title
            );

            wrapper.appendChild(
                company
            );


            const bullets =
                item.bullets ||
                item.description ||
                [];


            addBullets(
                wrapper,
                bullets
            );


            container.appendChild(
                wrapper
            );

        }
    );

}


// ------------------------------------------
// Render Projects
// ------------------------------------------

function renderProjects(
    projects
) {

    const container =
        document.getElementById(
            "projectsContainer"
        );

    container.innerHTML =
        "";


    projects.forEach(
        project => {

            const wrapper =
                document.createElement(
                    "div"
                );

            wrapper.className =
                "project-item";


            const title =
                document.createElement(
                    "div"
                );

            title.className =
                "project-title";

            title.textContent =
                project.title ||
                project.name ||
                "";


            wrapper.appendChild(
                title
            );


            const bullets =
                project.bullets ||
                project.description ||
                [];


            addBullets(
                wrapper,
                bullets
            );


            if (
                project.technologies
            ) {

                const technologies =
                    document.createElement(
                        "div"
                    );

                technologies.className =
                    "project-technologies";

                technologies.textContent =
                    `Technologies: ${
                        Array.isArray(
                            project.technologies
                        )
                            ? project.technologies.join(
                                ", "
                            )
                            : project.technologies
                    }`;


                wrapper.appendChild(
                    technologies
                );

            }


            container.appendChild(
                wrapper
            );

        }
    );

}


// ------------------------------------------
// Add Bullets
// ------------------------------------------

function addBullets(
    parent,
    bullets
) {

    if (!bullets) {
        return;
    }


    if (!Array.isArray(bullets)) {

        bullets = [
            bullets
        ];

    }


    if (!bullets.length) {
        return;
    }


    const list =
        document.createElement(
            "ul"
        );


    bullets.forEach(
        bullet => {

            const li =
                document.createElement(
                    "li"
                );

            li.textContent =
                String(bullet);

            list.appendChild(
                li
            );

        }
    );


    parent.appendChild(
        list
    );

}


// ------------------------------------------
// Render Education
// ------------------------------------------

function renderEducation(
    education
) {

    const container =
        document.getElementById(
            "educationContainer"
        );

    container.innerHTML =
        "";


    education.forEach(
        item => {

            const wrapper =
                document.createElement(
                    "div"
                );

            wrapper.className =
                "education-item";


            const degree =
                document.createElement(
                    "div"
                );

            degree.className =
                "education-degree";

            degree.textContent =
                item.degree ||
                item.program ||
                "";


            const details =
                document.createElement(
                    "div"
                );

            details.className =
                "education-details";

            details.textContent =
                [
                    item.institution,
                    item.location,
                    item.year,
                    item.cgpa
                ]
                .filter(Boolean)
                .join(" | ");


            wrapper.appendChild(
                degree
            );

            wrapper.appendChild(
                details
            );


            container.appendChild(
                wrapper
            );

        }
    );

}


// ------------------------------------------
// Render Simple List
// ------------------------------------------

function renderList(
    elementId,
    items
) {

    const container =
        document.getElementById(
            elementId
        );

    container.innerHTML =
        "";


    items.forEach(
        item => {

            const li =
                document.createElement(
                    "li"
                );


            if (
                typeof item ===
                "string"
            ) {

                li.textContent =
                    item;

            }

            else {

                li.textContent =
                    item.name ||
                    item.title ||
                    item.description ||
                    "";

            }


            container.appendChild(
                li
            );

        }
    );

}


// ------------------------------------------
// Render Languages
// ------------------------------------------

function renderLanguages(
    languages
) {

    const container =
        document.getElementById(
            "languagesContainer"
        );

    container.innerHTML =
        "";


    const values =
        languages.map(
            language => {

                if (
                    typeof language ===
                    "string"
                ) {

                    return language;

                }

                return [
                    language.name,
                    language.level
                ]
                .filter(Boolean)
                .join(" - ");

            }
        );


    container.textContent =
        values.join(", ");

}


// ------------------------------------------
// Download DOCX
// ------------------------------------------

async function downloadDOCX() {

    const resumeId =
        getResumeId();


    if (!resumeId) {

        alert(
            "Please select a resume first."
        );

        return;

    }


    downloadDOCXButton.disabled =
        true;

    downloadDOCXButton.textContent =
        "Preparing Word...";


    try {

        const response =
            await fetch(
                `${API_BASE_URL}/resume/download/docx`,
                {

                    method: "POST",

                    headers:
                        authHeaders(),

                    body:
                        JSON.stringify({

                            resume_id:
                                resumeId

                        })

                }
            );


        if (response.status === 401) {

            window.location.href =
                "login.html";

            return;

        }


        if (!response.ok) {

            const data =
                await response.json();

            throw new Error(
                data.detail ||
                "Unable to download resume."
            );

        }


        const blob =
            await response.blob();


        const url =
            window.URL.createObjectURL(
                blob
            );


        const link =
            document.createElement(
                "a"
            );

        link.href =
            url;

        link.download =
            "Professional_Resume.docx";


        document.body.appendChild(
            link
        );

        link.click();

        link.remove();


        window.URL.revokeObjectURL(
            url
        );

    }

    catch (error) {

        console.error(
            "DOCX download error:",
            error
        );

        alert(
            error.message
        );

    }

    finally {

        downloadDOCXButton.disabled =
            false;

        downloadDOCXButton.textContent =
            "📝 Download Word";

    }

}


// ------------------------------------------
// Back to Dashboard
// ------------------------------------------

backButton.addEventListener(
    "click",
    function () {

        window.location.href =
            "dashboard.html";

    }
);


// ------------------------------------------
// Generate
// ------------------------------------------

generateResumeButton.addEventListener(
    "click",
    generateResume
);


// ------------------------------------------
// Improve
// ------------------------------------------

improveResumeButton.addEventListener(
    "click",
    improveResume
);


// ------------------------------------------
// Download
// ------------------------------------------

downloadDOCXButton.addEventListener(
    "click",
    downloadDOCX
);


// ------------------------------------------
// Initial State
// ------------------------------------------

const resumeId =
    getResumeId();


if (!resumeId) {

    resumeName.textContent =
        "No resume selected";

    resumeStatus.textContent =
        "Select Resume";

    aiStatus.textContent =
        "Open Resume Builder from a selected resume.";

}