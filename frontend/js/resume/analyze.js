// ==========================================
// Career AI Analyze Resume
// ==========================================

// ==========================================
// Analyze Resume
// ==========================================

async function analyzeResume(resumeId) {

    const button = event.target;

    try {

        button.disabled = true;

        button.innerHTML = "Analyzing...";

        const response = await apiRequest(

            "/resume/analyze/" + resumeId,

            {

                method: "POST",

                headers: authHeaders()

            }

        );

        const result = await response.json();

        if (!response.ok) {

            throw new Error(

                result.detail ||

                "Analysis Failed"

            );

        }

        alert(

            result.message

        );

        localStorage.setItem(

            "resume_id",

            resumeId

        );

        await loadResumeList();

        await loadDashboard();

        if (

            typeof loadReport ===

            "function"

        ) {

            await loadReport();

        }

    }

    catch (error) {

        console.error(error);

        alert(

            error.message

        );

    }

    finally {

        button.disabled = false;

        button.innerHTML = "Analyze";

    }

}