const weatherDisplay = document.getElementById('weather-display');
var hours = document.querySelector('.hour');
var minutes = document.querySelector('.minutes');
var seconds = document.querySelector('.seconds');
var title = document.querySelector('.title-page');
var container = document.querySelector('.container');


const morningImg = new Image();
const afternoonImg = new Image();
const nightImg = new Image();
morningImg.src = './images/morning.gif';
afternoonImg.src = './images/sunset.gif';
nightImg.src = './images/night.gif';

navigator.geolocation.getCurrentPosition((position) => {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    
    Promise.all([
        axios.get(`/api/weather?lat=${latitude}&lon=${longitude}`),
        axios.get(`/api/location?lat=${latitude}&lon=${longitude}`)
    ])
    .then(([weatherResponse, locationResponse]) => {
        // Dados do clima
        const weather = weatherResponse.data.weather[0].description;
        let temp = weatherResponse.data.main.temp;
        const icon = weatherResponse.data.weather[0].icon;
        
        temp = Math.round(temp);
        // Dados de localização
        const city = locationResponse.data[0].name;
        const state = locationResponse.data[0].state;
        const country = locationResponse.data[0].country;

        // Tradução dos climas
        const translations = {
            'clear sky': 'Céu limpo',
            'few clouds': 'Poucas nuvens',
            'scattered clouds': 'Nuvens dispersas',
            'broken clouds': 'Nuvens quebradas',
            'shower rain': 'Chuva rápida',
            'rain': 'Chuva',
            'thunderstorm': 'Tempestade',
            'snow': 'Neve',
            'mist': 'Neblina'
        };

        const translatedWeather = translations[weather] || weather;

        
        weatherDisplay.innerHTML = `
            <h2>Clima em ${city}, ${country}</h2>
            <p>${translatedWeather}</p>
            <p>${temp}°C</p>
            <img src="http://openweathermap.org/img/wn/${icon}.png" alt="ícone do clima" />
            <p>Localização: ${city}, ${state}, ${country}</p>
        `;
    })
    .catch((error) => {
        console.error('Erro ao buscar dados:', error);
        weatherDisplay.innerHTML = 'Erro ao buscar dados';
    });
}, (error) => {
    console.error('Erro ao obter localização:', error);
    weatherDisplay.innerHTML = 'Não foi possível obter a localização';
});


var clock = setInterval(function time() { 
    var dateToday = new Date();
    var hr = dateToday.getHours();
    var min = dateToday.getMinutes();
    var sec = dateToday.getSeconds();

    if (hr < 10) hr = '0' + hr;
    if (min < 10) min = '0' + min;
    if (sec < 10) sec = '0' + sec;

    hours.innerHTML = hr;
    minutes.innerHTML = min;
    seconds.innerHTML = sec;

    
    if (hr >= 6 && hr < 12) {
        title.innerHTML = 'Bom dia!';
        container.style.backgroundImage = `url(${morningImg.src})`; 
    } else if (hr >= 12 && hr < 18) {
        title.innerHTML = 'Boa tarde!';
        container.style.backgroundImage = `url(${afternoonImg.src})`;
    } else {
        title.innerHTML = 'Boa noite!';
        container.style.backgroundImage = `url(${nightImg.src})`;
    }

    container.style.backgroundSize = "cover";
    container.style.backgroundPosition = "center";
    container.style.backgroundRepeat = "no-repeat";

}, 1000);
