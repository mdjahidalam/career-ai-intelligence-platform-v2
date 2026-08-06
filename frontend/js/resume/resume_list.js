// ==========================================
// Career AI Resume List
// ==========================================

// ==========================================
// Load Resume List
// ==========================================

async function loadResumeList() {

    try {

        const response = await apiRequest(

            "/resume/",

            {

                method: "GET",

                headers: authHeaders()

            }

        );

        const result = await response.json();

        if (!response.ok) {

            throw new Error(

                result.detail ||

                "Unable to load resumes."

            );

        }

        renderResumeTable(

            result.data

        );

    }

    catch (error) {

        console.error(error);

    }

}

// ==========================================
// Render Resume Table
// ==========================================

function renderResumeTable(resumes) {

    const tbody = document.getElementById(

        "resumeTableBody"

    );

    tbody.innerHTML = "";

    if (resumes.length === 0) {

        tbody.innerHTML = `

        <tr>

            <td colspan="4">

                No Resume Uploaded

            </td>

        </tr>

        `;

        return;

    }

    // Current Selected Resume

    const selectedResumeId = Number(

        localStorage.getItem(

            "resume_id"

        )

    );

    let currentResume = null;

    resumes.forEach((resume, index) => {

        if (

            selectedResumeId

                ? resume.id === selectedResumeId

                : index === 0

        ) {

            currentResume = resume;

        }

        tbody.innerHTML += `

        <tr>

            <td>

                ${resume.original_filename}

            </td>

            <td>

                ${resume.uploaded_at ?? "--"}

            </td>

            <td>

                ${resume.analysis_status ?? "Uploaded"}

            </td>

            <td>

                <button

                    class="action-btn view"

                    onclick="viewResume(${resume.id})">

                    View

                </button>

                <button

                    class="action-btn analyze"

                    onclick="analyzeResume(${resume.id})">

                    Analyze

                </button>

                <button

                    class="action-btn delete"

                    onclick="deleteResume(${resume.id})">

                    Delete

                </button>

            </td>

        </tr>

        `;

    });

    // Default First Resume

    if (!currentResume) {

        currentResume = resumes[0];

    }

    setCurrentResume(

        currentResume

    );

}

// ==========================================
// Current Resume Card
// ==========================================

function setCurrentResume(resume) {

    localStorage.setItem(

        "resume_id",

        resume.id

    );

    document.getElementById(

        "currentResumeName"

    ).innerHTML =

        resume.original_filename;

    document.getElementById(

        "currentResumeDate"

    ).innerHTML =

        resume.uploaded_at ?? "--";

    document.getElementById(

        "currentResumeStatus"

    ).innerHTML =

        resume.analysis_status ?? "Uploaded";

}

// ==========================================
// View Resume
// ==========================================

async function viewResume(id) {

    localStorage.setItem(
        "resume_id",
        id
    );

    await loadResumeList();

    await loadDashboard();

    if (typeof loadReport === "function") {

        await loadReport();

    }

    // Dashboard section open karo

    if (typeof showSection === "function") {

        showSection("dashboard");

    }

}