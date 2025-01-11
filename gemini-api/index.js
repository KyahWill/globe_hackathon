const express = require("express");
const app = express();
const PORT = 3000;

require("dotenv").config();

//Gemini
const { GoogleGenerativeAI } = require("@google/generative-ai");
const genAI = new GoogleGenerativeAI(process.env.API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
const axios = require("axios");

// Middleware to parse JSON bodies
app.use(express.json());

// Create a post endpoint that will accept a json content and generate a response
app.post("/api/generate", async (req, res) => {
  try {
    const prompt =
      "Analyze this data, and provide the following: Platform, Category, Date, Location, Content, Author, Sentiment, Priority.";
    const promp2 = "Should be in json structure, with snake case keys";
    const result = await model.generateContent([
      prompt,
      promp2,
      JSON.stringify(req.body),
    ]);
    console.log(result.response.candidates[0].content.parts[0].text);
    res.json(JSON.parse(result.response.candidates[0].content.parts[0].text.replace('```json', "").replace('```', "")));
  } catch (error) {
    res.status(500).json({ message: error.message, content: req.body });
  }
});

// Create an enpoint that will call dummy api using axios
app.get("/api/dummy", async (req, res) => {
  try {
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/todos/1"
    );
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
