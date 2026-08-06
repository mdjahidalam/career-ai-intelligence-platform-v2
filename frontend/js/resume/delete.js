// ==========================================
// Career AI Delete Resume
// ==========================================

async function deleteResume(resumeId) {

    const confirmDelete = confirm(
        "Are you sure you want to delete this resume?"
    );

    if (!confirmDelete) {

        return;

    }

    try {

        const response = await apiRequest(

            "/resume/" + resumeId,

            {

                method: "DELETE",

                headers: authHeaders()

            }

        );

        const result = await response.json();

        if (!response.ok) {

            throw new Error(

                result.detail ||

                "Delete Failed"

            );

        }

        alert("Resume deleted successfully.");

        localStorage.removeItem("resume_id");

        await loadResumeList();

        await loadDashboard();

    }

    catch(error){

        console.error(error);

        alert(error.message);

    }

}