function createCookie(string) {
    document.cookie = string+"= string; expires=Thu, 18 Dec 2019 12:00:00 UTC; path=/";
}

window.onload = (function(){
    document.getElementById('replyspan').innerHTML = document.cookie
    console.log(document.cookie);
})();
