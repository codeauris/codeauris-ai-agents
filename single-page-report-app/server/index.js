import 'dotenv/config';

import express from 'express';
import cors from 'cors';
import path from 'path';
import { fileURLToPath } from 'url';
import { GoogleGenerativeAI } from '@google/generative-ai';


const app = express();
app.use(cors());
app.use(express.json());


const PORT = process.env.PORT || 3000;
const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
const GEMINI_API_MODEL = process.env.GEMINI_API_MODEL;


if (!GEMINI_API_KEY) {
    console.warn('Warning: GEMINI_API_KEY is not set.');
}


const genAI = new GoogleGenerativeAI(GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: GEMINI_API_MODEL });


async function callGemini(userPrompt) {
    const instruction = `Generate a short structured report. Include:\n- Title\n- 2-3 sentence summary\n- 3 bullet key points\n- Short recommended action.\nPrompt:\n${userPrompt}`;


    const result = await model.generateContent(instruction);
    return result.response.text();
}


app.post('/api/report', async (req, res) => {
    try {
        const { prompt } = req.body;
        if (!prompt) return res.status(400).json({ error: 'Missing prompt' });


        const report = await callGemini(prompt);
        res.json({ report });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: err.message });
    }
});


// Serve static frontend build
const __dirname = path.dirname(fileURLToPath(import.meta.url));
app.use(express.static(path.join(__dirname, '../client/dist')));
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../client/dist', 'index.html'));
});


app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});