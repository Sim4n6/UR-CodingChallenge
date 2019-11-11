

function dislike(dislike_btn) {
    // mute btn like 
    dislike_btn.disabled = true;

    // get id of current shop
    let shopId = dislike_btn.closest("div.card").id

    // send async post the shop to the api side 
    const xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/api/v1/preferred_shops/'+ shopId);
    xhr.send()
}

function like(like_btn) {
    
    // mute btn like
    like_btn.disabled = true;

    // make disappear liked shop
    like_btn.closest("div.card").style.display = 'none'; 

    // get id of current shop
    let shopId = like_btn.closest("div.card").id

    // send async post the shop to the api side 
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/v1/preferred_shops/'+shopId);
    xhr.send()

    // 4. This will be called after the response is received
    xhr.onload = function() {
        if (xhr.status != 200) { // analyze HTTP status of the response
            alert(`Error ${xhr.status}: ${xhr.statusText}`); // e.g. 404: Not Found
        } else { // show the result
            alert(`Done, got ${xhr.response.length} bytes`); // responseText is the server
        }
    };
}

function removePreferred(remove_btn) {
    // hide div of dislike_btn
    remove_btn.closest("div.card").style.display = 'none';

    // get id of current shop
    let shopId = remove_btn.closest("div.card").id

    // send async delete to the api side 
    const xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/api/v1/preferred_shops/'+ shopId);
    xhr.send()

}