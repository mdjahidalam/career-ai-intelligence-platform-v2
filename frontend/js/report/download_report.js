// ==========================================
// Download AI Report
// ==========================================

document.addEventListener(

    "DOMContentLoaded",

    function () {

        const button =

            document.getElementById(

                "downloadReportButton"

            );

        if (button) {

            button.addEventListener(

                "click",

                downloadReport

            );

        }

    }

);

async function downloadReport() {

    const { jsPDF } = window.jspdf;

    const pdf = new jsPDF();

    const resumeName =
        document.getElementById(
            "reportResumeName"
        ).innerText;

    const ats =
        document.getElementById(
            "reportATS"
        ).innerText;

    const placement =
        document.getElementById(
            "reportPlacement"
        ).innerText;

    const salary =
        document.getElementById(
            "reportSalary"
        ).innerText;

    const career =
        document.getElementById(
            "reportCareer"
        ).innerText;

    pdf.setFontSize(20);

    pdf.text(

        "Career AI Resume Report",

        20,

        20

    );

    pdf.setFontSize(12);

    pdf.text(

        "Resume : " + resumeName,

        20,

        35

    );

    pdf.text(

        "ATS Score : " + ats,

        20,

        50

    );

    pdf.text(

        "Placement : " + placement,

        20,

        60

    );

    pdf.text(

        "Salary : " + salary,

        20,

        70

    );

    pdf.text(

        "Career : " + career,

        20,

        80

    );

    let y = 100;

    pdf.text(

        "Skills",

        20,

        y

    );

    y += 10;

    document

        .querySelectorAll(

            "#reportSkills .skill-badge"

        )

        .forEach(

            skill => {

                pdf.text(

                    "- " + skill.innerText,

                    25,

                    y

                );

                y += 8;

            }

        );

    y += 8;

    pdf.text(

        "Strengths",

        20,

        y

    );

    y += 10;

    document

        .querySelectorAll(

            "#reportStrengths li"

        )

        .forEach(

            item => {

                pdf.text(

                    "- " + item.innerText,

                    25,

                    y

                );

                y += 8;

            }

        );

    y += 8;

    pdf.text(

        "Weaknesses",

        20,

        y

    );

    y += 10;

    document

        .querySelectorAll(

            "#reportWeaknesses li"

        )

        .forEach(

            item => {

                pdf.text(

                    "- " + item.innerText,

                    25,

                    y

                );

                y += 8;

            }

        );

    y += 8;

    pdf.text(

        "Recommendations",

        20,

        y

    );

    y += 10;

    document

        .querySelectorAll(

            "#reportRecommendations li"

        )

        .forEach(

            item => {

                pdf.text(

                    "- " + item.innerText,

                    25,

                    y

                );

                y += 8;

            }

        );

    pdf.save(

        resumeName + "_AI_Report.pdf"

    );

}