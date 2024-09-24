const weatherDisplay = document.getElementById('weather-display');
var hours = document.querySelector('.hour');
var minutes = document.querySelector('.minutes');
var seconds = document.querySelector('.seconds');
var title = document.querySelector('.title-page');
var container = document.querySelector('.container');

navigator.geolocation.getCurrentPosition((position) => {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log('Latitude:', latitude, 'Longitude:', longitude);

    // Buscar o clima
    axios.get(`/api/weather?lat=${latitude}&lon=${longitude}`)
        .then((response) => {
            console.log('Dados do clima recebidos:', response.data);
            const weather = response.data.weather[0].description;
            const temp = response.data.main.temp;
            const city = response.data.name;
            const country = response.data.sys.country;
            const icon = response.data.weather[0].icon;

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

            // Atualizar HTML com dados e ícone
            weatherDisplay.innerHTML = `
                <h2>Clima em ${city}, ${country}</h2>
                <p>${translatedWeather}</p>
                <p>${temp}°C</p>
                <img src="http://openweathermap.org/img/wn/${icon}.png" alt="ícone do clima" />
            `;
        })
        .catch((error) => {
            console.error('Erro ao buscar dados de clima:', error);
            weatherDisplay.innerHTML = 'Erro ao buscar dados de clima';
        });

    // Buscar a localização (cidade, estado) usando geocodificação reversa
    axios.get(`/api/location?lat=${latitude}&lon=${longitude}`)
        .then((response) => {
            console.log('Dados de localização recebidos:', response.data);
            if (response.data[0]) {
                const city = response.data[0].name;
                const state = response.data[0].state;
                const country = response.data[0].country;
                
                // Atualiza com a localização correta
                weatherDisplay.innerHTML += `<p>Localização: ${city}, ${state}, ${country}</p>`;
            }
        })
        .catch((error) => {
            console.error('Erro ao buscar dados de localização:', error);
        });

}, (error) => {
    console.error('Erro ao obter localização:', error);
    weatherDisplay.innerHTML = 'Não foi possível obter a localização';
});

// Relógio
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

    if (hr < 12 && hr > 5) {
        title.innerHTML = 'Bom dia!';
        container.style.backgroundImage = "url('./images/morning.gif')"; 
        container.style.backgroundSize = "cover";
        container.style.backgroundPosition = "center";
        container.style.backgroundRepeat = "no-repeat";

    } else if (hr < 18 && hr > 12) {
        title.innerHTML = 'Boa tarde!';
        container.style.backgroundImage = "url('./images/sunset.gif')";
        container.style.backgroundSize = "cover";
        container.style.backgroundPosition = "center";
        container.style.backgroundRepeat = "no-repeat";

    } else if (hr < 24 && hr > 18) {
        title.innerHTML = 'Boa noite!';
        container.style.backgroundImage = "url('./images/night.gif')";
        container.style.backgroundSize = "cover";
        container.style.backgroundPosition = "center";
        container.style.backgroundRepeat = "no-repeat";
    }
});
