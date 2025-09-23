# Single Page Report Generator using Google Gemini API | CodeAuris
- Single-page web app (React + Express) that uses Google Gemini API to generate structured reports.
- Requires a valid Gemini API key from Google AI Studio.

**Links:**
- [Video link]()
- [Blog link]()

**How to run this example**
- Clone this repo 
- Navigate to downloaded folder

**Environment variables - Google Gemini API Key**
- Create .env file in the server folder
- Add GEMINI_API_KEY and GEMINI_API_MODEL in the .env file

**Build Docker Image**
- This will use the Dockerfile in the application folder
```bash
docker build -t single-page-report-app:latest .
docker run -p 3000:3000 single-page-report-app:latest
```
Then visit [http://localhost:3000](http://localhost:3000).
