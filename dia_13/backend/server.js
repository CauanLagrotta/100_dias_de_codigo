require('dotenv').config({path: '../../.env'});
const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(express.static('../frontend'));
app.use(cors());

// Rota para obter o clima
app.get('/api/weather', async (req, res) => {
    const apiKey = process.env.API_KEY;
    const latitude = req.query.lat;
    const longitude = req.query.lon;

    try {
        const response = await axios.get(`https://api.openweathermap.org/data/2.5/weather`, {
            params: {
                lat: latitude,
                lon: longitude,
                appid: apiKey,
                units: 'metric'
            }
        });

        res.json(response.data);

    } catch (error) {
        console.error('Erro ao buscar dados de clima:', error);
        res.status(500).json({ error: 'Erro ao buscar dados de clima' });
    }
});

// Rota para obter a cidade e estado (geocodificação reversa)
app.get('/api/location', async (req, res) => {
    const apiKey = process.env.API_KEY;
    const latitude = req.query.lat;
    const longitude = req.query.lon;

    try {
        const response = await axios.get(`http://api.openweathermap.org/geo/1.0/reverse`, {
            params: {
                lat: latitude,
                lon: longitude,
                limit: 1,
                appid: apiKey
            }
        });

        res.json(response.data);

    } catch (error) {
        console.error('Erro ao buscar dados de localização:', error);
        res.status(500).json({ error: 'Erro ao buscar dados de localização' });
    }
});

app.listen(PORT, () => {
    console.log(`Servidor rodando em: http://localhost:${PORT}`);
});
