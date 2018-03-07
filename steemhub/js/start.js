var core = new momentum.Core();
var usurname = 'tolgahanuzun';
var server_url = 'http://159.65.21.161:2001'


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
var surname = document.getElementById('steemit').value
var vote = document.getElementById('vote').checked
var follow = document.getElementById('follow').checked
var post = document.getElementById('post').checked
var transfer = document.getElementById('transfer').checked

    

chrome.storage.sync.set({'surname': surname});
        
chrome.storage.sync.set({
  'surname': surname,
  'vote': vote,
  'follow': follow,
  'post': post,
  'transfer': transfer
});

})

chrome.storage.sync.get(['surname','vote','follow','post','transfer'], function(val){
var xmlHttp = new XMLHttpRequest();
text = '/user_details?name=' + val['surname'] + '&vote=' + val['vote'] + '&follow=' + val['follow']
text = text + '&post=' + val['post'] + '&transfer=' +val['transfer']

get_url = server_url + text
console.log(get_url)
xmlHttp.open( "GET", get_url , false ); // false for synchronous request
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