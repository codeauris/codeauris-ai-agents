from typing import Dict, Any
import sqlite3

from mcp.types import Resource

conversation_resource = Resource(
                    uri="mcp://gateway/conversations",
                    name="Conversation History",
                    description="Recent LLM conversations and responses",
                    mimeType="application/json"
                )


async def get_conversations(db_path) -> Dict[str, Any]:
    """Get recent conversations"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM conversations ORDER BY timestamp DESC LIMIT 10")
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        conn.close()

        return {
            "recent_conversations": [dict(zip(columns, row)) for row in rows],
            "total_count": len(rows)
        }
    except Exception as e:
        return {"error": str(e)}