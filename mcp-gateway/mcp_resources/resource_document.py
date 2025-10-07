from typing import Dict, Any
import sqlite3

from mcp.types import Resource

document_resource = Resource(
                    uri="mcp://gateway/documents",
                    name="Document Store",
                    description="Managed documents and knowledge base",
                    mimeType="application/json"
                )


async def get_documents(db_path) -> Dict[str, Any]:
    """Get stored documents"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM documents ORDER BY updated_at DESC")
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        conn.close()

        return {
            "documents": [dict(zip(columns, row)) for row in rows],
            "count": len(rows)
        }
    except Exception as e:
        return {"error": str(e)}