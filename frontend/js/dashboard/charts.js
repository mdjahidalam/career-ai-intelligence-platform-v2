// ==========================================
// Dashboard Charts
// ==========================================

let atsChart = null;

let statusChart = null;

// ==========================================
// Create Charts
// ==========================================

function loadCharts(data){

    createATSChart(

        data.summary.ats_score

    );

    createStatusChart(

        data.status

    );

}

// ==========================================
// ATS Doughnut
// ==========================================

function createATSChart(score){

    if(atsChart){

        atsChart.destroy();

    }

    const ctx =

        document.getElementById(

            "atsChart"

        );

    atsChart =

        new Chart(

            ctx,

            {

                type:"doughnut",

                data:{

                    labels:[

                        "Score",

                        "Remaining"

                    ],

                    datasets:[{

                        data:[

                            score,

                            100-score

                        ],

                        backgroundColor:[

                            "#2563eb",

                            "#e5e7eb"

                        ],

                        borderWidth:0

                    }]

                },

                options:{

                    cutout:"70%",

                    plugins:{

                        legend:{

                            display:false

                        }

                    }

                }

            }

        );

}

// ==========================================
// Resume Status
// ==========================================

function createStatusChart(status){

    if(statusChart){

        statusChart.destroy();

    }

    const analyzed =

        status==="completed"

        ||

        status==="success"

        ||

        status==="analyzed"

        ?1:0;

    const pending =

        analyzed?0:1;

    statusChart =

        new Chart(

            document.getElementById(

                "statusChart"

            ),

            {

                type:"doughnut",

                data:{

                    labels:[

                        "Analyzed",

                        "Pending"

                    ],

                    datasets:[{

                        data:[

                            analyzed,

                            pending

                        ],

                        backgroundColor:[

                            "#22c55e",

                            "#f59e0b"

                        ]

                    }]

                },

                options:{

                    plugins:{

                        legend:{

                            position:"bottom"

                        }

                    }

                }

            }

        );

}