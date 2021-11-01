    <script>
        $(document).ready(function () {
            showBook();
        });

        function showBook() {
            $.ajax({
                type: 'GET',
                url: '/api/list?sample_give=샘플데이터',
                data: {},
                success: function (response) {
                    let mybooks = response['books_bestsellers']
                    for (let i = 0; i < mybooks.length; i++) {
                        let title = mybooks[i]['title']
                        let image = mybooks[i]['image']
                        let author = mybooks[i]['author']
                        let url = mybooks[i]['url']

                        let temp_html = `<div class="card">
                <div class="card-content">
                    <div class="media">
                        <div class="media-left">
                            <figure class="image is-48x48">
                                <img
                                        src="${image}"
                                        alt="Placeholder image"
                                />
                            </figure>
                        </div>
                        <div class="media-content">
                            <a href="${url}" target="_blank" class="book-name title is-4">${title} </a>
                            <p class="subtitle is-6">${author}</p>
                        </div>
                    </div>
                </div>

            </div>`
                        $('#book-box').append(temp_html)
                    }
                }
            });
        }


    </script>
