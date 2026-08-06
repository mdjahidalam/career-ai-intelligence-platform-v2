// ==========================================
// Login
// ==========================================

const loginForm = document.getElementById("loginForm");

const loginButton = document.getElementById("loginButton");

// ==========================================
// Submit
// ==========================================

loginForm.addEventListener(

    "submit",

    async function (event) {

        event.preventDefault();

        loginButton.disabled = true;

        loginButton.innerHTML = "Signing In...";

        try {

            const formData = new URLSearchParams();

            formData.append(

                "username",

                document.getElementById("email").value

            );

            formData.append(

                "password",

                document.getElementById("password").value

            );

            const response = await fetch(

                API.BASE_URL + "/auth/login",

                {

                    method: "POST",

                    headers: {

                        "Content-Type":

                        "application/x-www-form-urlencoded"

                    },

                    body: formData

                }

            );

            const result = await response.json();

            if (!response.ok) {

                alert(

                    result.detail ||

                    "Login Failed"

                );

                return;

            }

            saveToken(

                result.access_token

            );

            window.location.href =

                "dashboard.html";

        }

        catch (error) {

            console.error(error);

            alert("Server Error");

        }

        finally {

            loginButton.disabled = false;

            loginButton.innerHTML = "Login";

        }

    }

);