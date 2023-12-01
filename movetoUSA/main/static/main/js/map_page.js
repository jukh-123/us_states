




function hoverByClass(classname, colorin, colorout="#f9f9f9"){
    var elms=document.getElementsByClassName(classname);
    for(var i=0;i<elms.length;i++){
        elms[i].onmouseover = function(){
            for(var k=0;k<elms.length;k++){
                elms[k].style="transform: scale(1.005, 1.005);";
                elms[k].style=`fill: ${colorin} !important`;//colorover;
            }
        };
        elms[i].onmouseout = function(){
            for(var k=0;k<elms.length;k++){
                elms[k].style=`fill: ${colorout} !important`;
            }
        };
    }
}
hoverByClass("West", "rgb(163, 200, 255)");
hoverByClass("South", "rgb(163, 200, 255)");
hoverByClass("Midwest", "rgb(163, 200, 255)");
hoverByClass("North-East", "rgb(163, 200, 255)");
hoverByClass("Pacific", "rgb(163, 200, 255)");


var detailsBox = document.getElementById('details-box');

document.addEventListener('mouseover', function (e) {
  if (e.target.tagName == 'path') {
    e.target.style = "fill: rgb(87, 153, 255) !important;";
    var photo_of_state = e.target.dataset.photo;
    var salary_of_state = e.target.dataset.salary;
    var jobs_of_state = e.target.dataset.jobs;
    var state_name = e.target.id;
  
    while (detailsBox.firstChild) {/* optional cleanup, faster than test.innerHTML = '' */
      detailsBox.removeChild(detailsBox.firstChild);
    }
    detailsBox.appendChild(document.createElement('h6')).innerHTML = state_name;
    detailsBox.appendChild(document.createElement('img')).src = `/media/${photo_of_state}`;
    detailsBox.appendChild(document.createElement('p')).innerHTML = "Average income: " + salary_of_state;
    detailsBox.appendChild(document.createElement('p')).innerHTML = "Main jobs: " + jobs_of_state;
    var imagemap = detailsBox.getElementsByTagName('img');
    imagemap[0].style.width = '350px';
    // imagemap.style.width = '120px';
    

    detailsBox.style.opacity = "100%";
    
  }
  else {
    detailsBox.style.opacity = "0%";
  }
});

window.onmousemove = function (e) {
  var x = e.clientX,
      y = e.clientY;
  detailsBox.style.top = (y + 20) + 'px';
  detailsBox.style.left = (x) + 'px';
};