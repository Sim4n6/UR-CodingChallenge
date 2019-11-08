

function dislike(dislike_btn) {
    // mute btn like 
    dislike_btn.disabled = true;

    // get id of current shop
    let shopId = dislike_btn.parentNode.parentNode.parentNode.id;

    // send async post the shop to the api side 
    const xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/api/v1/preferred_shops/'+ shopId);
    xhr.send()
}

function like(like_btn) {
    
    // mute btn like
    like_btn.disabled = true;

    // make disappear liked shop
    like_btn.parentNode.parentNode.parentNode.style.display = 'none'; 

    // get id of current shop
    let shopId = like_btn.parentNode.parentNode.parentNode.id;

    // send async post the shop to the api side 
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/v1/preferred_shops/'+shopId);
    xhr.send()
}

function removePreferred(remove_btn) {
    // hide div of dislike_btn
    remove_btn.parentNode.parentNode.parentNode.style.display = 'none';

    // get id of current shop
    let shopId = remove_btn.parentNode.parentNode.parentNode.id;

    // send async delete to the api side 
    const xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/api/v1/preferred_shops/'+ shopId);
    xhr.send()

}