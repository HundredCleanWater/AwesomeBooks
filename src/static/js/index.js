let submitBtn =  document.querySelector('.submitBtn')
let search = document.querySelector('.iinput').innerText

function gogo() {
    $.ajax({
        type: "GET",
        url: "/search",
        data: {search_give: search},
        success: function (response) {
            // console.log(response)
            console.log(123)
            // let json_search = JSON.parse(response['all_search_results'])
            // console.log(json_search)
        }
    })
}

submitBtn.addEventListener("click", gogo())



