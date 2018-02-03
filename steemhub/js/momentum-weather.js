"use strict";

window.momentum = window.momentum || {};

// Weather

momentum.WeatherCtrl = function() {
  this.apiKey = "90c5410d2341e713ca4cc281761e3f56";
  this.apiUrl = "http://api.openweathermap.org/data/2.5/weather?APPID=" + this.apiKey;
};

momentum.WeatherCtrl.prototype = {
	// `fetchWeather(cb<Function>)` method
	// This function should fetch the current weather in Philly by performing an AJAX call. It should pass the given cb (callback) function to the success property of the call.
	// 
	// hint. look into $.ajax here: http://api.jquery.com/jquery.ajax/
	// hint. read through the documentation for the OpenWeatherAPI.
fetchWeather: function(lat, lon, cb) {
    $.ajax({
      url: this.apiUrl + "&lat=" + lat + "&lon=" + lon,
      method: "GET",
      success: cb
    });
  }
};
