// GLOBAL DATA=================================================================
let tokenMenu = 0; //Variable to store the value of the last selected menu object.
let tokenHide = false; //Variable to store the bolean vaule if the extra menu is displayed or not.
let tokenFile = 0; //Variable to store the present file selected.
const img = document.createElement('img'); //Const to add the hand cursor.
img.className = 'selected';
img.src = 'https://www.dropbox.com/s/1pq4d1ksjv3tuoz/FF7Cursor.png?raw=1';
const div = document.createElement('div'); //Const to add the shadow of the hand cursor.
div.className = 'shadow';
let move = new Audio();//Variable of Audio kind to store and use move sound.
move.src ="https://www.dropbox.com/s/fiyx4q2mdwynraj/FF7CursorMove.mp3?raw=1";
let load = new Audio(); //Variable of Audio kind to store and use the load sound.
load.src = 'https://www.dropbox.com/s/v04ewrevpnnsz03/FF7CursorSaveLoad.mp3?raw=1';

// SELECTION ELEMENTS

let extras = document.querySelectorAll('.extra'); //Select all the Menus extra from the original.
let menuItems = document.querySelectorAll('#menu li'); 

// EVENT LISTENERS==================================================================

(function eventListeners(){


    //Sets the opacity of the hands icons to 1 when the initial animation ends we use this instead animation-fill-mode to control the opacity with other function later.
    document.querySelector('#right').addEventListener("animationend", function(){
        document.querySelector('#right').style.opacity = "1";
    },false);
    
    //Sets listener when a mouse is over a menu.
    document.body.addEventListener('mouseover', selectMouseOver);
    //Sets listener when a click is made in the hand icons.
    document.body.addEventListener('click', function(e){

    // Calling the changeScreen function depending of what hand icon was clicked with the file number to load.  

        if(e.target.id == "left"){

            if(tokenFile>0){
                changeScreen(--tokenFile);
            }else{
                tokenFile = 4;
                changeScreen(tokenFile);
            }
        }else if(e.target.id == "right"){
            
            if(tokenFile<4){
                changeScreen(++tokenFile);
            }else{
                tokenFile = 0;
                changeScreen(tokenFile);
    }
}
});
})();

// FUNCTIONS========================================================================



//Adds the blink effect to the semicolon in the clock.
function blink(){

let blinked = document.querySelector('#colon');
blinked.style.color = (blinked.style.color == "white" ? "grey" : "white");
setTimeout(blink , 500);
}
/////////////////////////////////////////////////////////////////////////////////
//Adds the cursor hand and play the sound when the mouse is over a menu.
function selectMouseOver(e){
    e.preventDefault();
    if(e.target.parentNode.id == 'menu'){
        tokenMenu = parseInt(e.target.getAttribute("number"));
        selection(tokenMenu);
        move.play();
    }
}

//////////////////////////////////////////////////////////////////////////////////

//Prepents the hand and shadow icons.
function selection(tokenMenu){

menuItems[tokenMenu].prepend(img); //Prepend append an element before the selected target.
menuItems[tokenMenu].prepend(div); //Using reference variables instead creating elements helps to no be removed each time.
}

//Function that calls the loadScreen and loadFile methods and manages the secuence of the screen changes.
function changeScreen(token){

let x = 0;
document.querySelector("#screen").classList.add("screenOff");
let intervalID = setInterval(function () {

    if (x === 0) {  
    loadScreen(loadFile(token));
    load.play();
    document.querySelector("#screen").classList.remove("screenOff");
    document.querySelector("#screen").classList.add("screenOn"); 
    x++;
    }else{
    document.querySelector("#screen").classList.remove("screenOn");
    window.clearInterval(intervalID);
    }
}, 3900);   
}

//Function that changes all the paramethers on the screen depends on the file loaded.
function loadScreen(file){

//Location music.
document.querySelector("#music").src = urlData(file.music);
document.querySelector("#controls").load();

//Menu Available. 
file.phsExist == "yes" ? document.querySelector("#phs").innerHTML= "PHS": document.querySelector("#phs").innerHTML= "<br>";
file.phs == "yes" ? document.querySelector("#phs").style.color= "white": document.querySelector("#phs").style.color= "grey";
file.save == "yes" ? document.querySelector("#save").style.color= "white": document.querySelector("#save").style.color= "grey";

//Restarts the hand icon position.
tokenMenu = 0;
selection(tokenMenu);

}
