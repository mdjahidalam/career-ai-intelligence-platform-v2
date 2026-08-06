// ==========================================
// Career AI Upload Resume
// ==========================================

// ==========================================
// Upload Button
// ==========================================

const uploadButton =

    document.getElementById(

        "uploadResumeButton"

    );

if (uploadButton) {

    uploadButton.addEventListener(

        "click",

        openUploadDialog

    );

}

// ==========================================
// Upload Dialog
// ==========================================

function openUploadDialog() {

    const input =

        document.createElement(

            "input"

        );

    input.type = "file";

    input.accept = ".pdf";

    input.onchange = function () {

        uploadResume(

            input.files[0]

        );

    };

    input.click();

}

// ==========================================
// Upload Resume
// ==========================================

async function uploadResume(file) {

    if (!file) {

        return;

    }

    const formData =

        new FormData();

    formData.append(

        "file",

        file

    );

    try {

        uploadButton.disabled = true;

        uploadButton.innerHTML =

            "Uploading...";

        const response =

            await fetch(

                API.BASE_URL +

                "/resume/upload",

                {

                    method: "POST",

                    headers: {

                        Authorization:

                        "Bearer " +

                        getToken()

                    },

                    body: formData

                }

            );

        const result =

            await response.json();

        if (!response.ok) {

            throw new Error(

                result.detail ||

                "Upload Failed"

            );

        }

        alert(

            "Resume uploaded successfully."

        );

        await loadResumeList();

    }

    catch (error) {

        console.error(error);

        alert(

            error.message

        );

    }

    finally {

        uploadButton.disabled = false;

        uploadButton.innerHTML =

            "+ Upload Resume";

    }

}