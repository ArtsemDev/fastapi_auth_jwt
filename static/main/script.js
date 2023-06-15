$('form#register-form').on('submit', function (e) {
    e.preventDefault()
    $.ajax(
        {
            url: '/api/register',
            contentType: 'application/json',
            dataType: 'json',
            method: 'post',
            data: JSON.stringify(
                {
                    email: this.email.value,
                    password: this.password.value
                }
            ),
            success: function (data) {
                document.querySelector('form#register-form').querySelector('input#email').value = ''
                document.querySelector('form#register-form').querySelector('input#password').value = ''
                document.querySelector('div.status').innerHTML = 'SUCCESS'
            },
            error: function (data) {
                document.querySelector('div.status').innerHTML = 'ERROR'
            }
        }
    )
})

$('form#login-form').on('submit', function (e) {
    e.preventDefault()
    $.ajax(
        {
            url: '/api/login',
            contentType: 'application/json',
            dataType: 'json',
            method: 'post',
            data: JSON.stringify(
                {
                    email: this.email.value,
                    password: this.password.value
                }
            ),
            success: function (data) {
                document.querySelector('form#register-form').querySelector('input#email').value = ''
                document.querySelector('form#register-form').querySelector('input#password').value = ''
                localStorage.setItem('access_token', JSON.stringify(data))
                console.log(localStorage)
            },
            error: function (data) {
                document.querySelector('div.status').innerHTML = 'ERROR'
            }
        }
    )
})

$('a#auth').click(function (e) {
    e.preventDefault()
    let token = localStorage.getItem('access_token')
    if (token) {
        token = JSON.parse(token)
        $.ajax(
            {
                url: '/api/test',
                contentType: 'application/json',
                dataType: 'json',
                method: 'get',
                headers: {
                    Authorization: `${token.token_type} ${token.access_token}`
                },
                success: function (data) {
                    console.log(data)
                },
                error: function (data) {
                    console.log(data)
                }
            }
        )
    }
})
