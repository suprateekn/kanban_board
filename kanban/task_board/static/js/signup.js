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

    fetch(user_url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        }
    })
        .then(response => response.json())
        .catch(err => console.log(err));

});
