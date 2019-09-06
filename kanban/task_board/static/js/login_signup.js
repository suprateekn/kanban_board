$("#submit-form").on("submit", function (e) {
    e.preventDefault();
    let csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    let first_name = $("#first_name").val();
    let last_name = $("#last_name").val();
    let username = $("#username").val();
    let email = $("#email").val();
    let gender = $("input[name='gender']:checked").val();
    let password = $("#password").val();


    let data = {
        first_name: first_name,
        last_name: last_name,
        username: username,
        email: email,
        password: password,
        user_profile: {
            gender: gender,
            profile_pic: null
        },
    };

    fetch(user_api_url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        }
    })
        .then(response => {
            window.status_code = response.status;
            return response.json()
        })
        .then((result) => {
            let k = '';
            if (window.status_code === 400) {
                for (k in result) {
                    console.log(k);
                    console.log(result[k][0]);
                    $("p." + k).removeClass("d-none").html(result[k][0]);

                }
            }

            if (k === '') {
                window.location.replace(login_page_url);
            }

        })
        .catch(err => console.log(err));


});


// $("#submit-login").on("submit", function (e) {
//     e.preventDefault();
//
//
//     fetch(login_api_url, {
//
//
//         method: 'POST',
//         body: JSON.stringify(data),
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrf_token
//         }
//     })
//         .then(response => response.json())
//         .catch(err => console.log(err));
//
// });

$("#submit-form").validate({
    rules: {
        confirm_password: {
            equalTo: "#password"
        }
    },

    messages: {
        confirm_password: "Password and confirm password must be same"
    }
});

