// -------------------------------------------------------------------------------------- base.html

// Set a timeout to execute the code after 2500 milliseconds (2.5 seconds)
setTimeout(function () {
    // Get all elements with the class 'msg' (assuming these are Bootstrap alert elements)
    let messages = document.getElementsByClassName('msg');

    // Create a new Bootstrap Alert using the first 'msg' element
    // (assuming there may be multiple alerts and you want to close the first one)
    let alert = new bootstrap.Alert(messages[0]);

    // Close the Bootstrap Alert after it has been displayed for 2.5 seconds
    alert.close();
}, 2500);
// -------------------------------------------------------------------------------------- post_detail.html

// This code is executed when the DOM (Document Object Model) is fully loaded


// Another event listener for when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    
    // Get all elements with the class "btn-like" (comment like buttons)
    const commentLikeButtons = document.querySelectorAll(".btn-like");

    // Iterate over each comment like button and add a click event listener
    commentLikeButtons.forEach(function (commentLikeButton) {
        console.log("comment button:", commentLikeButtons);
        commentLikeButton.addEventListener("click", function () {
            // Get the comment ID and check if the button is currently liked
            const commentId = commentLikeButton.dataset.commentId;
            const likedComment = commentLikeButton.classList.contains("likedComment");

            // Perform a fetch request to like/unlike the comment
            fetch(`/like-comment/${commentId}/`, {
                method: likedComment ? "DELETE" : "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                },
            })
            .then((response) => response.json())
            .then((data) => {
                // Update the UI based on the response data
                if (data.success) {
                    if (likedComment) {
                        commentLikeButton.classList.remove("likedComment");
                    } else {
                        commentLikeButton.classList.add("likedComment");
                    }
                    // Update the likes count for the specific comment
                    const commentLikesCount = document.getElementById(`comment-likes-count-${commentId}`);
                    commentLikesCount.textContent = data.comment_likes_count;
                }
            })
            .catch((error) => console.error("Error:", error));
        });
    });

    // Function to get CSRF token from cookies
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(";").shift();
    }
});

// -------------------------------------------------------------------------------------- gallery.html

// Execute the code when the DOM (Document Object Model) is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    console.log("hello from gallery scipt.js")
    
    // Get all elements with the class 'gallery-btn-like' (like buttons in a gallery)
    const galleryLikeButtons = document.querySelectorAll(".gallery-btn-like");

    // Iterate over each gallery like button and add a click event listener
    galleryLikeButtons.forEach(function (galleryLikeButton) {
        galleryLikeButton.addEventListener("click", function () {
            
            // Get the image ID and check if the button is currently liked
            const imageId = galleryLikeButton.dataset.imageId;
            const likedImage = galleryLikeButton.classList.contains("likedImage");

            // Perform a fetch request to like/unlike the image
            fetch(`/like-image/${imageId}/`, {
                method: likedImage ? "DELETE" : "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                },
            })
            .then((response) => response.json())
            .then((data) => {
                // Update the UI based on the response data
                if (data.success) {
                    if (likedImage) {
                        galleryLikeButton.classList.remove("likedImage");
                    } else {
                        galleryLikeButton.classList.add("likedImage");
                    }
                    
                    // Update the likes count for the specific image
                    const imageLikesCount = document.getElementById(`gallery-likes-count-${imageId}`);
                    imageLikesCount.textContent = data.likes_count;
                }
            })
            .catch((error) => console.error("Error:", error));
        });
    });

    // Function to get CSRF token from cookies
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(";").shift();
    }
});
