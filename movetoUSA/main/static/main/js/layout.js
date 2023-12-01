
function openDropdown(){
    document.getElementById("dropdown-content").classList.toggle("show-dropdown");
}

var button = document.getElementById("search-button");

function slugify(str) {
    return String(str)
      .normalize('NFKD') // split accented characters into their base characters and diacritical marks
      .replace(/[\u0300-\u036f]/g, '') // remove all the accents, which happen to be all in the \u03xx UNICODE block.
      .trim() // trim leading or trailing whitespace
      .toLowerCase() // convert to lowercase
      .replace(/[^a-z0-9 -]/g, '') // remove non-alphanumeric characters
      .replace(/\s+/g, '-') // replace spaces with hyphens
      .replace(/-+/g, '-'); // remove consecutive hyphens
  }

button.onclick = function () {
    var text = document.getElementById("search-field").value;
    window.open("http://127.0.0.1:8000/states/" + slugify(text));
}