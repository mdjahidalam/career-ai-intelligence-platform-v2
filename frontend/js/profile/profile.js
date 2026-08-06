// ==========================================
// Career AI Profile
// ==========================================

document.addEventListener(

    "DOMContentLoaded",

    async function () {

        await loadProfile();

    }

);

// ==========================================
// Load Profile
// ==========================================

async function loadProfile() {

    try {

        // -------------------------
        // User Information
        // -------------------------

        const userResponse = await apiRequest(

            "/auth/me",

            {

                method: "GET",

                headers: authHeaders()

            }

        );

        const userResult = await userResponse.json();

        if (userResponse.ok) {

            document.getElementById(

                "profileName"

            ).innerHTML =

                userResult.data.full_name;

            document.getElementById(

                "profileEmail"

            ).innerHTML =

                userResult.data.email;

        }

        // -------------------------
        // Resume Statistics
        // -------------------------

        const resumeResponse = await apiRequest(

            "/resume/",

            {

                method: "GET",

                headers: authHeaders()

            }

        );

        const resumeResult = await resumeResponse.json();

        if (!resumeResponse.ok) {

            return;

        }

        const resumes = resumeResult.data;

        document.getElementById(

            "totalResume"

        ).innerHTML =

            resumes.length;

        let analyzed = 0;

        let pending = 0;

        resumes.forEach(

            (resume) => {

                if (

                    resume.analysis_status === "Analyzed"

                ) {

                    analyzed++;

                }

                else {

                    pending++;

                }

            }

        );

        document.getElementById(

            "analyzedResume"

        ).innerHTML =

            analyzed;

        document.getElementById(

            "pendingResume"

        ).innerHTML =

            pending;

    }

    catch (error) {

        console.error(error);

    }

}