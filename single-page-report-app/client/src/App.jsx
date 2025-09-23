import React, { useState } from 'react'


export default function App() {
    const [prompt, setPrompt] = useState('');
    const [report, setReport] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');


    async function generate() {
        setLoading(true);
        setError('');
        setReport('');
        try {
            const res = await fetch('/api/report', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt })
            });
            const data = await res.json();
            if (!res.ok) throw new Error(data.error || 'Server error');
            setReport(data.report);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }


    return (
        <div style={{ maxWidth: 800, margin: '40px auto', fontFamily: 'system-ui, Arial' }}>
            <h1>Gemini Report Generator</h1>
            <p>Type a description of the topic you want a report for and click "Generate Report".</p>


            <textarea
                rows={6}
                style={{ width: '100%', padding: 10, fontSize: 16 }}
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                placeholder="e.g. Summarize last quarter sales performance for product X"
            />


            <div style={{ marginTop: 10 }}>
                <button onClick={generate} disabled={loading || !prompt.trim()} style={{ padding: '8px 16px', fontSize: 16 }}>
                    {loading ? 'Generating…' : 'Generate Report'}
                </button>
            </div>


            {error && <pre style={{ color: 'darkred' }}>{error}</pre>}


            {report && (
                <section style={{ marginTop: 20 }}>
                    <h2>Generated Report</h2>
                    <div style={{ whiteSpace: 'pre-wrap', background: '#f6f6f6', padding: 12, borderRadius: 6 }}>{report}</div>
                </section>
            )}
        </div>
    )
}