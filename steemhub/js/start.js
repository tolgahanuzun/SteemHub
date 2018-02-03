var core = new momentum.Core();
var usurname = 'tolgahanuzun';
core.start();
	// I want to run the time update and rendering every second
setInterval(function() {
	core.updateTime();
	core.render();
},1000*30);

	// I only want to fetch and update the weather once every ten minutes
setInterval(function() {
	core.updateWeather();
	core.render();
}, 1000*60*10);



$("#save").click(function(){
var obj = {}; 
var account = document.getElementById('git-account').value+";";   
var surname = document.getElementById('surname').value+";";   
    
chrome.storage.sync.set({'names': account});
chrome.storage.sync.set({'surname': surname});
        
});


chrome.storage.sync.get('names', function(val){
    
var xmlHttp = new XMLHttpRequest();
username = val['names'].split(';').reverse()[1];
xmlHttp.open( "GET", 'http://127.0.0.1:8000/user_details?name='+username , false ); // false for synchronous request
xmlHttp.send( null );

data = JSON.parse(xmlHttp.responseText)
div = document.getElementById("slide-out")

text_res = '';

for(i = 0; i < data['result'].length; i++){
div.insertAdjacentHTML('beforeend', 
'<li>'+ data['result'][i] + '</li><hr>')}

})
$(".button-collapse").sideNav();

$(document).ready(function(){
$('.modal').modal({
    dismissible: false, // Modal can be dismissed by clicking outside of the modal
    opacity: 0.1, // Opacity of modal background
    inDuration: 300, // Transition in duration
    outDuration: 200, // Transition out duration
    startingTop: '2 %', // Starting top style attribute
    endingTop: '2%', // Ending top style attribute
    
    }
  );
});

$("#save").click(function(){
$('.modal').modal('close');
location.reload();
});

$("#close").click(function(){
$('.modal').modal('close');
});